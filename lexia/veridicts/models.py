import datetime
from django.db import models

# Create your models here.

class Veridict(models.Model):
  court_name = models.CharField(max_length=100)
  veridict_date = models.DateField(default=datetime.date.today)
  upload_date = models.DateTimeField(auto_now_add=True)
  pdf_file = models.FileField(default=None)