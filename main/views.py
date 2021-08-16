from django.contrib.auth.models import User
from django.shortcuts import render, redirect, HttpResponse
from .forms import NewUserForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from . import models, forms
from . scrape import scrape, KEY

def calulate_points(U, F):
	if U == 0 or F == 0:
		return 1

	else:
		U = float(U)/100
		F = 100/float(F)
		HP = ((1/(U*F))**0.5)-1 
		UP=(HP+1)*U
		return round(UP, 2)

def rules(request):  
	form = forms.Preseasonform(request.POST or None)
		
	if form.is_valid():
		form.save()
	return render(request=request, template_name="main/rules.html", context = {'form': form})

def pickhistory(request):
	histories = models.History.objects.all()
	weeks = [h.data for h in histories]
	return render(request=request, template_name="main/pickhistory.html", context={"weeks": weeks})

def index(request):
	return redirect("main:login")

def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			return redirect("main:homepage")
	form = NewUserForm
	if request.user.is_authenticated:
		return redirect("main:homepage")
	return render(request=request, template_name="main/register.html", context={"register_form": form})

def homepage(request):
	players = models.User.objects.all()
	leaderboard_list = [[player.profile.score, player.username, player.profile.picks] for player in players]
	leaderboard_list.sort(key=lambda x: x[0], reverse=True)
	return render(request=request, template_name="main/homepage.html", context={"lbl":leaderboard_list})


def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data["username"]
			password = form.cleaned_data["password"]
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				return redirect("main:homepage")
	form = AuthenticationForm()
	if request.user.is_authenticated:
		return redirect("main:homepage")
	return render(request=request, template_name="main/login.html", context={"login_form": form})


def logout_request(request):
    logout(request)
    return redirect("main:login")


def preseason(request):
	general = models.General.objects.all()[0]
	user = request.user
	form = forms.Preseasonform(request.POST or None)
	if form.is_valid():
		user.profile.big_loser = form.cleaned_data['big_loser']
		user.profile.nfc_champ = form.cleaned_data['nfc_champ']
		user.profile.afc_champ = form.cleaned_data['afc_champ']
		user.profile.superbowl_winner = form.cleaned_data['superbowl_winner'] 
		user.save()
		return redirect("main:homepage")
	return render(request=request, template_name="main/preseason.html", context={'form':form, 'week': general.week})


def dash(request):
	form = forms.Gameform(request.POST or None)
	if 'add' in request.POST and form.is_valid():
		team1 = form.cleaned_data['underdog']
		team2 = form.cleaned_data['favorite']
		team1p = int(form.cleaned_data['Underdog_Points'])
		team2p = int(form.cleaned_data['Favorite_Points'])
		g = models.Gamemodel(team1 = team1, team2 = team2, points = calulate_points(team1p, team2p))
		g.save()

	elif "publish" in request.POST:
		general = models.General.objects.all()[0]
		general.publish = not general.publish
		general.save()
	
	elif "delete" in request.POST:
		models.Gamemodel.objects.all().delete()

	elif "clear" in request.POST:
		general = models.General.objects.all()[0]
		players = models.User.objects.all()
		for p in players:
			p.profile.picks = None
			p.profile.score = 0
			p.save()
		general.week = 1
		general.save()
		models.Gamemodel.objects.all().delete()
		models.History.objects.all().delete()

	elif "nextweek" in request.POST:
		gamemodels = models.Gamemodel.objects.all()
		players = models.User.objects.all()
		general = models.General.objects.all()[0]
		
		th = "<td style='margin-bottom: 20px;'>game</td>"
		tb = ""

		for p in players:
			th += "<td>{}</td>".format(p.username)

		th = "<thead><tr>{}</tr></thead>".format(th)

		print(th)

		for i, g in enumerate(gamemodels):
			winner = str(int(g.winner == "true"))
			if g.winner:
				tr = "<td><p style = 'margin: 0px; color: #26a69a;'>{} (1)</p><p style = 'margin: 0px;'>{} ({})</p></td>".format(g.team1, g.team2, g.points)
			else:
				tr = "<td><p style = 'margin: 0px;'>{} (1)</p><p style = 'margin: 0px; color: #26a69a;'>{} ({})</p></td>".format(g.team1, g.team2, g.points)
			for p in players:
				if p.profile.picks != None:
					pick = p.profile.picks[i]
					if pick == winner:
						if pick == "0": 
							p.profile.score += 1
							tr += "<td style = 'color: #26a69a;'>F</td>"
						else:
							p.profile.score += g.points
							tr += "<td style = 'color: #26a69a;'>U</td>"
					else:
						if pick == "0": 
							tr += "<td>F</td>"
						else:
							tr += "<td>U</td>"
				else:
					tr += "<td>none</td>"
			tb += "<tr>{}</tr>".format(tr)
		tb = "<tbody>{}</tbody>".format(tb)
		
		pick_table = th + tb
		history = models.History(data = pick_table, week = general.week)
		history.save()

		for p in players:
			p.profile.picks = None
			p.save()
		
		general.week += 1
		general.publish = False
		general.save()

		models.Gamemodel.objects.all().delete()
	
	elif "scrape" in request.POST:
		games = scrape()
		for i in games:
			team1 = KEY[i[0]]
			team2 = KEY[i[1]]
			team1p = i[2]
			team2p = i[3]
			g = models.Gamemodel(team1 = team1, team2 = team2, points = calulate_points(team1p, team2p))
			g.save() 

	else: 
		gamemodels = models.Gamemodel.objects.all()
		b = [[[ f"{i}d" ], [ f"{i}w" ]] for i in range(len(gamemodels))]
		for i, g in enumerate(gamemodels):
			print(str(b[i][0]))
			if str(b[i][0]) in request.POST:
				g.delete()
				players = models.User.objects.all()
				for p in players:
					p.profile.picks = None
					p.save()
			elif str(b[i][1]) in request.POST:
				g.winner = not g.winner
				g.save()

	gamemodels = models.Gamemodel.objects.all()
	general = models.General.objects.all()[0]
	b = [[[str(i)+"d"],[str(i)+"w"]] for i in range(len(gamemodels))]
	game_list = zip(gamemodels, b)
	return render(request=request, template_name="main/dashboard.html", context={
		"form": form, "game_list": game_list, "publish":general.publish, "week": general.week

		}
	)

def pickform(request):
	general = models.General.objects.all()[0]
	user = request.user
	gamemodels = models.Gamemodel.objects.all()
	n = len(gamemodels)
	choice_list = []
	for g in gamemodels:
		choice_list1 = str(g.team1)+" (1)"
		choice_list2 = str(g.team2)+" ({})".format(g.points)
		choices = (
			("0", choice_list1),
			("1", choice_list2),
		)
		choice_list.append(choices)
	draft = user.profile.picks
	form = forms.Pickform(n, choice_list, draft, data=request.POST or None)
	if form.is_valid():
		cleaned_form = form.cleaned_data
		formstring = ""
		for key, value in cleaned_form.items():
			formstring += value
			
		user.profile.picks = formstring 
		user.save()
		return redirect("main:homepage")

	games = zip(form, models.Gamemodel.objects.all())
	return render(request=request, template_name="main/pickform.html", context={"games":games, 'publish':general.publish})
	