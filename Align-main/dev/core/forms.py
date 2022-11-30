from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Project, Action

class NewUserForm(UserCreationForm):
	email = forms.EmailField() # default required is True

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user
    
# More on overriding default widget
# https://docs.djangoproject.com/en/4.1/topics/forms/modelforms/#overriding-the-default-fields
class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ('description', 'visibility', 'status', 'users', 'files', 'tags')

class ActionForm(ModelForm):
    class Meta:
        model = Action
        fields = ('description', 'visibility', 'status', 'start_date', 'start_time', 'end_date', 'end_time', 'p_project', 'p_action', 'files', 'tags')

