"""new2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from app1 import views

from django.conf.urls.static import static
from . import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('first/', views.firstpage),
    #path('', views.firstpage), #dothis and it will open by first page but chech the login function
    path('sign/', views.signup1),
    path('login/', views.login1),
    path('delete/', views.deletesession),
    path('cart/', views.cart1),
    path('prorem/',views.cartrem),
    path('order/', views.orderdone),

     path('ordershow/', views.ordershow),




    path('scnd/<str:category_id>', views.scndpage),
    path('third/<str:id>', views.thirdpage),

     path('search/', views.search1),  #for search
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)