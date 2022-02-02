# Generated by Django 3.2.8 on 2022-01-11 07:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Nomi')),
                ('slug', models.SlugField(max_length=150, unique=True, verbose_name='*')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Nomi')),
                ('slug', models.SlugField(max_length=150, unique=True, verbose_name='*')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Nomi')),
                ('slug', models.SlugField(max_length=250, unique=True, verbose_name='*')),
                ('image', models.ImageField(upload_to='product_images/', verbose_name='Rasmi')),
                ('color', models.CharField(max_length=50, verbose_name='Rangi')),
                ('price', models.PositiveIntegerField(default=0, verbose_name='Narxi')),
                ('old_price', models.PositiveIntegerField(default=0, verbose_name='Avvalgi Narxi')),
                ('description', models.TextField(verbose_name='Tovar haqida')),
                ('instock', models.BooleanField(default=True, verbose_name='Bor / Yok')),
                ('count', models.PositiveIntegerField(default=1, verbose_name='Soni')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='main.category')),
                ('tag', models.ManyToManyField(related_name='product_tags', to='main.Tag')),
            ],
        ),
    ]
