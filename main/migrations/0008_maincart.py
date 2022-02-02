# Generated by Django 3.2.8 on 2022-01-30 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_cart'),
    ]

    operations = [
        migrations.CreateModel(
            name='MainCart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('all_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('carts', models.ManyToManyField(to='main.Cart', verbose_name='carts')),
            ],
        ),
    ]