# Generated by Django 3.0.3 on 2020-02-14 18:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cooking', '0007_auto_20200214_1649'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='relationships',
        ),
        migrations.DeleteModel(
            name='Relationship',
        ),
    ]
