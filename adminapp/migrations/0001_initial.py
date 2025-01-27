# Generated by Django 4.2.7 on 2024-02-07 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=50)),
                ('product_price', models.IntegerField(default=0)),
                ('product_image', models.ImageField(upload_to='productImage')),
            ],
        ),
    ]
