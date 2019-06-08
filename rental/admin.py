from django.contrib import admin

from rental import models
# Register your models here.


all_models = [
    models.Friend,
    models.Belonging,
    models.Borrowed
]

admin.site.register(all_models)