# Create your models here.
from django.db import models
import uuid

class Product(models.Model):
    name = models.CharField(max_length=48)
    price = models.IntegerField()
    description = models.CharField(max_length=255)

    @property
    def is_mood_strong(self):
        return self.mood_intensity > 5

class ProductEntry(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  # tambahkan baris ini
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    seller = models.CharField(max_length=255)
    time = models.DateField(auto_now_add=True)