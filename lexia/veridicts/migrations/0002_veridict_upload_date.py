# Generated by Django 4.0.2 on 2022-02-21 22:09

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('veridicts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='veridict',
            name='upload_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
