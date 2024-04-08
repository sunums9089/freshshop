# Generated by Django 4.2.7 on 2024-02-16 04:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0001_initial'),
        ('userapp', '0002_registeration'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mycart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('total', models.IntegerField()),
                ('status', models.IntegerField(default=0)),
                ('productid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminapp.products')),
                ('userid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userapp.registeration')),
            ],
        ),
    ]
