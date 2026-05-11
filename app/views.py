from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, Http404, HttpResponseForbidden
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.contrib import messages
from .models import *
from .utils import *
from .forms import *


def index(request, page_id=1):
    news = get_list_or_404(News)
    prev_page = 1
    page_id = 1
    context = {
        'title': 'Главная',
        'prev_page': prev_page,
        'page_id': page_id,
        'next_page': page_id + 1,
        'news_list': news
    }
    return render(request, template_name="home.html", context=context)


@login_required
def add_news_view(request):
    if request.method == "GET":
        context = {
            'form': NewsCreationForm()
        }
        return render(request, template_name="add_news.html", context=context)
    if request.method == "POST":
        form = NewsCreationForm(request.POST)
        if form.is_valid():
            news = form.save(commit=False)
            news.author = request.user
            news.save()
            return redirect('success')


def success_view(request):
    return render(request, template_name="success.html")


def news_detail_view(request, news_id):
    news = get_object_or_404(News, pk=news_id)
    if news.author == request.user:
        edit_rights = True
    else:
        edit_rights = False
    context = {
        'news': news,
        'edit_rights': edit_rights
    }
    return render(request, 'news_detail.html', context=context)


@login_required
def news_edit_view(request, news_id):
    news = get_object_or_404(News, pk=news_id)
    if news.author != request.user:
        return HttpResponseForbidden("Вы не можете редактировать эту новость")
    if request.method == "GET":
        form = NewsCreationForm(instance=news)
        return render(request, 'add_news.html', context={'form': form})
    if request.method == "POST":
        form = NewsCreationForm(request.POST, instance=news)
        if form.is_valid():
            form.save()
            return redirect('detailed_news', news_id)


@login_required
def news_delete_view(request, news_id):
    news = get_object_or_404(News, pk=news_id)
    if news.author != request.user:
        return HttpResponseForbidden("Вы не можете редактировать эту новость")
    news.delete()
    messages.success(request, "Новость успешно удалена.")
    return redirect('index')


def register_view(request):
    if request.method == "GET":
        form = UserCreationCustomForm()
        return render(request, "register.html", {'form': form})
    if request.method == "POST":
        form = UserCreationCustomForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        else:
            return render(request, "register.html", {'form': form})


def login_view(request):
    if request.method == "GET":
        form = UserLoginForm()
        return render(request, "login.html", {'form': form})
    if request.method == "POST":
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
        return render(request, "login.html", {'form': form})


@login_required
def logout_view(request):
    logout(request)
    return redirect('index')


@login_required
def profile_view(request):
    if request.method == "GET":
        form = ProfileUpdateForm(instance=request.user)
        return render(request, "profile.html", context={'form': form})
    if request.method == "POST":
        form = ProfileUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('index')
        return render(request, "profile.html", {'form': form})


def handler404_view(request, error_code):
    return render(request, template_name='error.html', context={'error_code': '404', 'error_message': 'error'},
                  status=404)
