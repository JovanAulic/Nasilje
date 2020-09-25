from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Kategorija(models.Model):
	ime = models.CharField(max_length=100)

	def __str__(self):
		return self.ime

	def get_absolute_url(self):
		return reverse('Postovi')

STATUS = (
	(0,'Objavljeno'),
	(1,'Nije objavljeno')
	)


class Post(models.Model):
	naslov = models.CharField(max_length=100, unique=True)
	autor = models.ForeignKey(User, on_delete=models.CASCADE)
	korisnicko_ime = models.CharField(max_length=20)
	tekst = models.CharField(max_length=1000,default="Napiši svoju priču!")
	opis_teksta = models.CharField(max_length=300, default="Dodaj kretak tekst vašoj priči!")
	status = models.IntegerField(choices=STATUS, default=1)
	kategorija = models.CharField(max_length=200, default="Izaberite Kategoriju")
	vrijeme =models.DateTimeField(auto_now_add=True)
	
	

	def str(self):
		return self.naslov +'|'+ str(self.autor)

	def get_absolute_url(self):
		return reverse('Postovi')

class Prijava(models.Model):
	ime = models.CharField(max_length=30, default="Unesite Vaše ime")
	prezime = models.CharField(max_length=50, default="Unesite Vaše prezime")
	jedinstveni_maticni_broj = models.CharField(max_length=13, default="Unesite Vaš jedinstveni matični broj")
	vrsta_nasilja = models.CharField(max_length=20, default="Izaberite vrstu nasilju")
	objekat = models.CharField(max_length=20, default="Da li ste vi žrtva nasilja?")
	pol = models.CharField(max_length=20, default="Izaberite pol")
	lokacija = models.CharField(max_length=200, default="Unesite Vašu adresu?")
	starost = models.IntegerField()
	tekst = models.CharField(max_length=500, default="Opišite ukratko Vaš slučaj")

	def str(self):
		return self.ime +'|'+ str(self.jedinstveni_maticni_broj)

	def get_absolute_url(self):
		return reverse('Postovi')

