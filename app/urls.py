from django.contrib import admin
from django.urls import path
from . import views


handler404 = 'app.views.handler404_view'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/<int:page_id>', views.index, name='home'),
    path('news/add/', views.add_news_view2, name='add'),
    path('news/success/', views.success_view, name='success'),
    path('news/<int:news_id>/', views.news_detail_view, name='detailed_news'),
    path('register', views.register_view, name='register')
]
