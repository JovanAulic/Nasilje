from django.contrib import admin
from .models import Post,Kategorija,Prijava


class PostAdmin(admin.ModelAdmin):
	list_display=('naslov','status','korisnicko_ime','tekst','autor','kategorija','vrijeme')
	list_filter=('status','korisnicko_ime','kategorija','vrijeme')
	search_fields=['naslov','tekst','kategorija']

admin.site.register(Post,PostAdmin)
admin.site.register(Kategorija)

class PrijavaAdmin(admin.ModelAdmin):
	list_display=('ime','prezime','jedinstveni_maticni_broj','pol','starost','lokacija','objekat','vrsta_nasilja','tekst')
	list_filter=('lokacija','starost','objekat')
	search_fields=['jedinstveni_maticni_broj','starost','ime','prezime','vrsta_nasilja','lokacija']

admin.site.register(Prijava, PrijavaAdmin)

