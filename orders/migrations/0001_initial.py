# Generated by Django 5.0.7 on 2024-07-29 14:12

import django.db.models.deletion
import orders.validators
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100, validators=[orders.validators.validate_unique_country_name])),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.country')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('phone', models.CharField(max_length=30)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Procesing', 'Processing'), ('Shipped', 'Shipped'), ('Delivered', 'Delivered'), ('Canceled', 'Canceled')], default='Pending', max_length=20)),
                ('address', models.CharField(max_length=50)),
                ('reference_number', models.CharField(blank=True, max_length=10, null=True, unique=True)),
                ('payment_method', models.CharField(choices=[('Paypal', 'Paypal'), ('Card', 'Card')], default='Paypal', max_length=50)),
                ('is_paid', models.BooleanField(default=False)),
                ('postal_code', models.CharField(blank=True, max_length=20, null=True)),
                ('cart', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='cart.cart')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='orders.city')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
