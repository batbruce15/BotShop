# Generated by Django 4.2.1 on 2023-05-13 17:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('store', '0003_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carte',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('odered', models.BooleanField(default=False)),
                ('ordered_date', models.DateField(blank=True, null=True)),
                ('orders', models.ManyToManyField(to='store.order')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
