from django.urls import path
from . import views
from .views import BaseView, NasaPricaView, KontaktView, ForumView


urlpatterns = [
	path("", views.BaseView, name="Base"),
	path("Nasa_prica/", views.NasaPricaView, name="Nasa_prica"),
	path("Kontakt/", views.KontaktView, name="Kontakt"),
	path("Forum/", views.ForumView, name="Forum"),
]