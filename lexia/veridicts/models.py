import datetime
from django.db import models

# Create your models here.


class Veridicts(models.Model):
    veridict_number = models.CharField(max_length=20)
    court_name = models.CharField(max_length=100)
    veridict_date = models.DateField(default=datetime.date.today)
    upload_date = models.DateTimeField(auto_now_add=True)
    pdf_file = models.FileField(default=None, upload_to="veridicts/")

    def __str__(self):
        return self.veridict_number + "-" + self.court_name