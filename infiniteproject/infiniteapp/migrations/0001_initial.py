# Generated by Django 3.2.16 on 2022-11-22 14:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField()),
                ('image', models.ImageField(blank=None, upload_to='category')),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField()),
                ('availability', models.BooleanField(default=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('slug', models.SlugField(unique=True)),
                ('stock', models.IntegerField()),
                ('image', models.ImageField(blank=None, upload_to='products')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='infiniteapp.category')),
            ],
            options={
                'verbose_name': 'product',
                'verbose_name_plural': 'products',
                'ordering': ['name'],
            },
        ),
    ]
