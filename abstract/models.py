from django.db import models
from django.conf import settings
# Create your models here.

class FactoryModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    comment = models.TextField()

    class Meta:
        abstract=True


class OwnedModel(FactoryModel):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        abstract=True