# Generated by Django 3.2.6 on 2021-08-19 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_rename_fullname_profile_full_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='full_name',
            field=models.CharField(max_length=300),
        ),
    ]