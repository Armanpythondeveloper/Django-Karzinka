# Generated by Django 4.2 on 2023-05-01 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='username',
            field=models.CharField(default='', max_length=255, unique=True, verbose_name='User Name'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.EmailField(blank=True, default='', max_length=254, verbose_name='email address'),
        ),
    ]