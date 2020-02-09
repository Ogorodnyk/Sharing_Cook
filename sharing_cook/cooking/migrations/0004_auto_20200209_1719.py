# Generated by Django 3.0.3 on 2020-02-09 17:19

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cooking', '0003_auto_20200125_2221'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='languages',
        ),
        migrations.AddField(
            model_name='customuser',
            name='country',
            field=django_countries.fields.CountryField(default='', max_length=2),
        ),
        migrations.AddField(
            model_name='customuser',
            name='language_1',
            field=models.CharField(default='', max_length=32),
        ),
        migrations.AddField(
            model_name='customuser',
            name='language_2',
            field=models.CharField(default='', max_length=32),
        ),
        migrations.AddField(
            model_name='customuser',
            name='language_3',
            field=models.CharField(default='', max_length=32),
        ),
    ]
