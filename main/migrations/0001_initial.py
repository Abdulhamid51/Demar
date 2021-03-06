# Generated by Django 3.2.8 on 2022-02-06 11:06

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mkv', models.FloatField(verbose_name='m kvadrat')),
                ('all_price', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Nomi')),
                ('slug', models.SlugField(max_length=150, unique=True, verbose_name='*')),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Ismi')),
                ('phone', models.CharField(max_length=50, verbose_name='Telefon ')),
                ('email', models.EmailField(max_length=250, verbose_name='Emaili')),
            ],
            options={
                'verbose_name': 'Aloqa',
                'verbose_name_plural': 'Aloqalar',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Ismi')),
                ('phone', models.CharField(max_length=50, verbose_name='Telefon ')),
                ('message', models.CharField(max_length=250, verbose_name='Xabari')),
            ],
            options={
                'verbose_name': 'Savol',
                'verbose_name_plural': 'Savollar',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200)),
                ('slug', models.SlugField(max_length=200)),
                ('image', models.ImageField(blank=True, upload_to='product_images/')),
                ('description', models.TextField(blank=True)),
                ('price', models.FloatField()),
                ('old_price', models.PositiveIntegerField(default=0, verbose_name='Avvalgi Narxi')),
                ('available', models.BooleanField(default=True)),
                ('instock', models.BooleanField(default=True, verbose_name='Bor / Yok')),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='main.category')),
            ],
            options={
                'ordering': ('-created',),
                'index_together': {('id', 'slug')},
            },
        ),
        migrations.CreateModel(
            name='MainCart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('all_price', models.FloatField(default=0)),
                ('carts', models.ManyToManyField(blank=True, to='main.Cart', verbose_name='carts')),
            ],
        ),
        migrations.AddField(
            model_name='cart',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.product', verbose_name='cart of product'),
        ),
    ]
