from django.shortcuts import render

from posts.models import Posts

from .models import AboutUs, AboutUsImage


def index(request):
    about_us = AboutUs.objects.prefetch_related('images').first()
    posts = Posts.objects.all()
    about_us_slides = AboutUsImage.objects.all()

    context = {
        'title': 'ДельтаТранс',
        'menu_items': ['Главная', 'О нас', 'Новости'],
        'about_us_slides': about_us_slides,
        'about_us': about_us,
        'posts': posts,
    }
    return render(request, 'index.html', context)
