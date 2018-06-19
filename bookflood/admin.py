from django.contrib import admin
from bookflood.models import Country, Genre, Language, Book, UserProfile

admin.site.register(Country)
admin.site.register(Genre)
admin.site.register(Book)
admin.site.register(Language)
admin.site.register(UserProfile)

#don't use import * for more complicated projects: list them out!

