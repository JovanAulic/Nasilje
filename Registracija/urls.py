from django.urls import path
from . import views
from .views import KorisnickaRegistracijaView

urlpatterns = [
	path('Singup', KorisnickaRegistracijaView.as_view(), name="Registracija"),
]