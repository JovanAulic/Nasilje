from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from .forms import Prijava

class KorisnickaRegistracijaView(generic.CreateView):
	form_class = Prijava
	template_name = 'registration/Registracija.html'
	success_url = reverse_lazy('login')
