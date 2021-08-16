from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .teams import TEAMS
from .models import Profile

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
	Underdog_Points = forms.FloatField(initial=0)
	Favorite_Points = forms.FloatField(initial=0)


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
    big_loser = forms.ChoiceField(choices=TEAMS, widget=forms.Select(choices=TEAMS, attrs={'class': 'browser-default'}))
    nfc_champ = forms.ChoiceField(choices=TEAMS[:16], widget=forms.Select(choices=TEAMS, attrs={'class': 'browser-default'}))
    afc_champ = forms.ChoiceField(choices=TEAMS[16:], widget=forms.Select(choices=TEAMS, attrs={'class': 'browser-default'}))
    superbowl_winner = forms.ChoiceField(choices=TEAMS, widget=forms.Select(choices=TEAMS, attrs={'class': 'browser-default'}))