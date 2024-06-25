from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from post.models import Post


class HomeView(View):

    def get(self, request):
        posts = Post.objects.all()
        return render(request, 'home/index.html', {'posts': posts})

    def post(self, request):
        pass
