from django.conf.urls import url
from django.contrib import admin 
#from bookflood.views import home, view_book, view_person
from bookflood import views

urlpatterns = [
    url(r'^$', views.PeopleList.as_view(), name='home'), 
    url(r'^books/$', views.BookList.as_view(), name='book'),
    url(r'^books/add/$', views.BookCreate.as_view(), name='addbook'),
    url(r'^books/(?P<pk>\d+)/$', views.BookDetail.as_view(), name='bookdetail'),
    #url(r'^person/$', view_person, name='person'),

]

