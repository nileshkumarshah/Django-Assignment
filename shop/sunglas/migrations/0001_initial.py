# Generated by Django 4.1.2 on 2022-10-24 08:12

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
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_price', models.FloatField(null=True)),
                ('ordered', models.BooleanField(null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Categary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=50)),
                ('messages', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='shoping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=90)),
                ('email', models.EmailField(max_length=100)),
                ('address', models.CharField(max_length=120)),
                ('phone', models.CharField(max_length=12)),
                ('password', models.CharField(max_length=50)),
                ('gender', models.IntegerField(choices=[(0, 'male'), (1, 'female')])),
            ],
        ),
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.IntegerField(null=True)),
                ('images', models.ImageField(upload_to='images/')),
                ('categary', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='sunglas.categary')),
            ],
        ),
        migrations.CreateModel(
            name='CartItems',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField(null=True)),
                ('quantity', models.CharField(blank=True, max_length=60)),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sunglas.cart')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sunglas.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
