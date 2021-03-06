# Generated by Django 3.0.7 on 2020-08-17 04:45

from django.db import migrations, models
import django.db.models.deletion
import phone_field.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('enterprise', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('customer_name', models.CharField(blank=True, max_length=100)),
                ('customer_email', models.EmailField(blank=True, max_length=254, null=True, unique=True)),
                ('customer_phone', phone_field.models.PhoneField(blank=True, help_text='Contact phone number', max_length=31, unique=True)),
                ('customer_address', models.CharField(max_length=200)),
                ('enterprise', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='customer', to='enterprise.Enterprise')),
            ],
            options={
                'verbose_name_plural': 'Customers',
            },
        ),
    ]
