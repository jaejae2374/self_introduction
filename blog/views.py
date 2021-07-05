from typing import List
from django.shortcuts import render
from .models import Post
from django.views.generic import ListView

class PostList(ListView) :
    model = Post
    ordering = '-pk'