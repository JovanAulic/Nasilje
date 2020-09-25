from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class Prijava(UserCreationForm):
	email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
	first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
	last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
	

	class Meta:
		model = User
		fields =('first_name','last_name','username','email','password1','password2')

	def __int__(self, *args, **kwargs):
		super(Prijava, self).__int__(*args, **kwargs)

		self.fields['username'].widget.attrs['class'] = 'form-control'
		self.fields['first_name'].widget.attrs['class'] = 'form-control'
		self.fields['name'].widget.attrs['class'] = 'form-control'
		self.fields['email'].widget.attrs['class'] = 'form-control'
		self.fields['password1'].widget.attrs['class'] = 'form-control'
		self.fields['password2'].widget.attrs['class'] = 'form-control'