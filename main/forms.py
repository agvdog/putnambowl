from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .teams import TEAMS
from .models import Profile, User

class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")
		help_texts = {
            'username': None,
        }

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user

class Gameform(forms.Form):
	underdog = forms.ChoiceField(choices=TEAMS, widget=forms.Select(choices=TEAMS, attrs={'class': 'browser-default'}))
	favorite = forms.ChoiceField(choices=TEAMS, widget=forms.Select(choices=TEAMS, attrs={'class': 'browser-default'}))
	Underdog_Points = forms.FloatField(initial=0, required=False)
	Favorite_Points = forms.FloatField(initial=0, required=False)

class Announcementform(forms.Form):
	message = forms.CharField(widget=forms.Textarea)


class Pickform(forms.Form):
	def __init__(self, n, choice_list, draft,  *args, **kwargs):
		super(Pickform, self).__init__(*args, **kwargs)
		for i in range(0, n):
			default = '0'
			if draft != None:
				if len(draft) == n:
					default = draft[i]
					
			self.fields["game {}".format(i+1)] = forms.ChoiceField(
			choices=choice_list[i], 
			initial = default,
			widget=forms.Select(
				choices=choice_list[i],
				attrs={'class': 'browser-default'}
				)
			)
					          
class Preseasonform(forms.Form):
    big_loser = forms.ChoiceField(label='Big Loser',choices=TEAMS, widget=forms.Select(choices=TEAMS, attrs={'class': 'browser-default'}))
    nfc_champ = forms.ChoiceField(label='NFC Champ',choices=TEAMS[:16], widget=forms.Select(choices=TEAMS, attrs={'class': 'browser-default'}))
    afc_champ = forms.ChoiceField(label='AFC Champ',choices=TEAMS[16:], widget=forms.Select(choices=TEAMS, attrs={'class': 'browser-default'}))
    superbowl_winner = forms.ChoiceField(label='Big Winner',choices=TEAMS, widget=forms.Select(choices=TEAMS, attrs={'class': 'browser-default'}))

class Accountdashform(forms.Form):
	player_list = [(str(p.username),str(p.username)) for p in User.objects.all()]
	players = forms.ChoiceField(choices=player_list, widget=forms.Select(choices=player_list, attrs={'class': 'browser-default'}))
	add = forms.FloatField(initial = 0)