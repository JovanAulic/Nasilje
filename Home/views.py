from django.shortcuts import render


def BaseView(request):
	return render(request, "Base.html",{}) 

def NasaPricaView(request):
	return render(request, "NasaPrica.html",{})

def KontaktView(request):
	return render(request, "Kontakt.html", {})

def ForumView(request):
	return render(request, "Forum.html", {})
