# Generated by Django 3.0.3 on 2020-02-09 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cooking', '0005_auto_20200209_1732'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='relationships',
        ),
        migrations.AddField(
            model_name='customuser',
            name='friends',
            field=models.ManyToManyField(related_name='_customuser_friends_+', to='cooking.CustomUser'),
        ),
        migrations.DeleteModel(
            name='Relationship',
        ),
    ]
