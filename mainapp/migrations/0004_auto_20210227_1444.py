# Generated by Django 3.0 on 2021-02-27 14:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mainapp', '0003_auto_20210227_1415'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productitem',
            name='color',
        ),
        migrations.AlterField(
            model_name='cart',
            name='owner',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Владелец'),
        ),
    ]
