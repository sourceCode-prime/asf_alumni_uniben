# Generated by Django 3.2.6 on 2021-08-30 09:18

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, unique=True)),
                ('caption', ckeditor.fields.RichTextField()),
                ('thumbnail', models.ImageField(default='blog.png', upload_to='blog_images%Y%M%d')),
                ('content', ckeditor.fields.RichTextField(help_text='this is the main writeup of the blog')),
                ('timestamp', models.DateField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
