"""loyaltech URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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

from django.urls import path,re_path
from .views import (
    home_view,
    search_view,
    product_detail_view,
    create_order_view,
    computers_view,
    phones_view,
    others_view,
    about_view,
    contact_view
)

app_name='store'
urlpatterns = [
    path('',home_view,name='home'),
    path('search/',search_view,name='search'),
    path('<int:id>/',product_detail_view,name='product-detail'),
    path('order/<int:id>/',create_order_view,name='create-order'),
    path('computers/',computers_view,name='computers'),
    path('phones/',phones_view,name='phones'),
    path('others/',others_view,name='others'),
    path('about/',about_view,name='about'),
    path('contact/',contact_view,name='contact'),
]

