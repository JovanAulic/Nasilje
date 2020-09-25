from django.urls import path
from . import views
from .views import BaseView, BlogView, NewPostView, ArtikalView, DeleteArtikalView, UpdateArtikalView, KategorijaView,PrijavaView

urlpatterns = [
	#path('Početna/', views.BaseView, name="Home"),
	path('Početna_stranica/',BlogView.as_view(), name="Postovi"),
	path('NoviPost/',NewPostView.as_view(),name="NoviPost"),
	path('Artikal/<int:pk>', ArtikalView.as_view(),name="Artikal"),
	path('Artikal/<int:pk>/ObrisiPost',DeleteArtikalView.as_view(),name="Obrisi"),
	path('Artikal/Edit/<int:pk>',UpdateArtikalView.as_view(),name="Edit"),
	path('kategorija/<str:cats>/',KategorijaView, name="Kategorija"),
	path('Prijava/',PrijavaView.as_view(),name="Prijava")
]