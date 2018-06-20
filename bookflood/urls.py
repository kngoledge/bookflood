from django.conf.urls import url
from django.contrib import admin 
from bookflood.views import home, view_book, view_person

urlpatterns = [
    url('', view_person),

]

