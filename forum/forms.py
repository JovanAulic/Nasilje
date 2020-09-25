from django import forms
from .models import Post, Kategorija, Prijava

choices = Kategorija.objects.all().values_list('ime','ime')
choice_list = []

for item in choices:
	choice_list.append(item)

class EditPostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('naslov','tekst','opis_teksta')

		widgets = {
		'naslov': forms.TextInput(attrs={'class':'form-control'}),
		'tekst': forms.Textarea(attrs={'class': 'form-control'}),
		'opis_teksta' : forms.Textarea(attrs={'class': 'form-control'}),
			}

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('naslov','autor','tekst','opis_teksta','korisnicko_ime','kategorija')

		widgets = {
		'naslov': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Napišite naslov!'}),
		'autor': forms.Select(attrs={'class': 'form-control'}),
		'tekst': forms.Textarea(attrs={'class': 'form-control'}),
		'opis_teksta' : forms.Textarea(attrs={'class': 'form-control'}),
		'kategorija': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
		'korisnicko_ime':forms.TextInput(attrs={'class':'form-control','value':'','id':'nickname','type':'hidden'}),
		}

class PrijavaForm(forms.ModelForm):
	class Meta:
		model = Prijava
		fields = ('ime','prezime','jedinstveni_maticni_broj','vrsta_nasilja','objekat','pol','lokacija','starost','tekst')

		widgets = {
		'ime': forms.TextInput(attrs={'class':'form-control','placeholder': 'Unesite Vaše ime'}),
		'prezime': forms.TextInput(attrs={'class':'form-control','placeholder': 'Unesite Vaše prezime'}),
		'jedinstveni_maticni_broj': forms.TextInput(attrs={'class':'form-control','placeholder': 'Jedinsteni matični broj'}),
		'vrsta_nasilja': forms.Select(attrs={'class':'form-control','placeholder': 'Odaberite vrstu nasilja'}),
		'objekat': forms.Select(attrs={'class':'form-control','placeholder': 'Izaberite objekat'}),
		'pol': forms.Select(attrs={'class':'form-control'}),
		'lokacija': forms.TextInput(attrs={'class':'form-control','placeholder': 'Napišite Vašu adresu prebivališta'}),
		'starost': forms.TextInput(attrs={'class':'form-control','placeholder': 'Napišite Vaš broj godina'}),
		'tekst': forms.Textarea(attrs={'class':'form-control'}),
		}
			
