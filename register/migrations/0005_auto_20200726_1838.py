# Generated by Django 3.0.8 on 2020-07-26 11:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0004_auto_20200726_1835'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Users',
            new_name='AppUsers',
        ),
    ]
