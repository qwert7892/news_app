from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/<int:page_id>', views.index, name='home'),
    path('news/add/', views.add_news_view, name='add'),
    path('news/success/', views.success_view, name='success'),
    path('news/<int:news_id>/', views.news_detail_view, name='detailed_news')
]
