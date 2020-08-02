# Generated by Django 3.0.7 on 2020-08-02 03:35

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
            name='Enterprise',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('contact_name', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=10)),
                ('shop_name', models.CharField(max_length=200)),
                ('gst_number', models.CharField(max_length=20, unique=True)),
                ('shop_address', models.CharField(max_length=400)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='enterprise', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
