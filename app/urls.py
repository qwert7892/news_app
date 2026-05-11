from django.contrib import admin
from django.urls import path
from . import views


handler404 = 'app.views.handler404_view'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('home/<int:page_id>', views.index, name='home'),
    path('news/add/', views.add_news_view, name='add'),
    path('news/success/', views.success_view, name='success'),
    path('news/<int:news_id>/', views.news_detail_view, name='detailed_news'),
    path('register', views.register_view, name='register'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('news/<int:news_id>/edit', views.news_edit_view, name='edit_news'),
    path('news/<int:news_id>/delete', views.news_delete_view, name='delete_news'),
    path('profile', views.profile_view, name='profile'),
]
