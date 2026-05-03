from django.http import HttpResponse, Http404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
from .utils import *
from .forms import *


def index(request, page_id):
    news = load_news(page=page_id)
    for one in news:
        one['date'] = format_date(one['date'])

    prev_page = page_id - 1
    if page_id == 1:
        prev_page = 1

    context = {
        'title': 'Главная',
        'prev_page': prev_page,
        'page_id': page_id,
        'next_page': page_id + 1,
        'news_list': news
    }
    return render(request, template_name="home.html", context=context)


def add_news_view(request):
    if request.method == "GET":
        context = {
            'form': NewsForm
        }
        return render(request, template_name="add_news.html", context=context)

    if request.method == "POST":
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            add_news(
                title=data['title'],
                summary=data['summary'],
                content=data['content']
            )
            return success_view(request)
        else:
            pass


def add_news_view2(request):
    if request.method == "GET":
        context = {
            'form': NewsCreationForm
        }
        return render(request, template_name="add_news2.html", context=context)


def success_view(request):
    return render(request, template_name="success.html")


def news_detail_view(request, news_id):
    news = get_news_by_id(news_id)
    news['date'] = format_date(news['date'])
    context = {
        'news': news
    }
    return render(request, 'news_detail.html', context=context)


def register_view(request):
    if request.method == "GET":
        form = UserCreationForm()
        return render(request, "register.html", {'form': form})


def handler404_view(request, error_code):
    return render(request, template_name='error.html', context={'error_code': '404', 'error_message': 'qqww'},
                  status=404)
