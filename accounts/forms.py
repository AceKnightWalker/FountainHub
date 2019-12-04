from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm


# add email 

#class UserForm(forms.ModelForm):
    #password = forms.CharField(widget=forms.PasswordInput)
   # email address= forms.EmailField(widget=forms.EmailInput)

   # class Meta:
    #    model = User
    #    fields = ['username', 'email address', 'password']

class UserCreationForm(UserCreationForm):
	email = forms.EmailField(required=True, label ='Email', widget=forms.EmailInput)
	first_name = forms.CharField(required=True, label ='first_name', widget=forms.TextInput)
	last_name = forms.CharField(required=True, label ='last_name', widget=forms.TextInput)

	class Meta(object):
		model = User
		fields = ('first_name', 'last_name', 'username', 'email')
			
	def save(self, commit=True):
		user = super(UserCreationForm, self).save(commit=False)
		user.first_name = self.cleaned_data['first_name']
		user.first_name = self.cleaned_data['first_name']
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user
		