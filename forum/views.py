from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView
from .models import Post,Kategorija, Prijava
from .forms import PostForm,EditPostForm, PrijavaForm
from django.urls import reverse_lazy


def BaseView(request):
	return render(request, 'Base.html',{})

class BlogView(ListView):
	model = Post
	template_name = "Post.html"
	ordering =["-id"]

class NewPostView(CreateView):
	model = Post
	form_class = PostForm
	template_name = "NewPost.html"

class ArtikalView(DetailView):
	model = Post
	form_class = PostForm
	template_name = "Artikal.html"

class DeleteArtikalView(DeleteView):
	model = Post
	template_name = "DeleteArtikal.html"
	success_url = reverse_lazy('Postovi')

class UpdateArtikalView(UpdateView):
	model = Post
	template_name = "UpdateArtikal.html"
	form_class = EditPostForm

def KategorijaView(request,cats):
	category_post = Post.objects.filter(kategorija=cats)
	return render(request, 'Kategorija.html', {'cats': cats.title(), 'category_post': category_post})

class PrijavaView(CreateView):
	model = Prijava
	template_name ="Prijava.html"
	form_class = PrijavaForm

