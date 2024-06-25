# Generated by Django 5.0.6 on 2024-06-24 23:51

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
        ('store', '0002_category_product_id_category'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('total', models.FloatField()),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('street', models.CharField(blank=True, max_length=60, null=True)),
                ('number', models.CharField(blank=True, max_length=40, null=True)),
                ('postal_code', models.CharField(blank=True, max_length=50, null=True)),
                ('comuna', models.CharField(blank=True, max_length=50, null=True)),
                ('comentary', models.TextField(blank=True, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('id_direction', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='direcciones', to='authentication.directions')),
                ('id_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pedidos', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
