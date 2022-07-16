# Generated by Django 4.0.4 on 2022-05-01 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ProductName', models.CharField(max_length=200, null=True)),
                ('ProductId', models.IntegerField(max_length=50, null=True)),
                ('Quantity', models.IntegerField(null=True)),
                ('No_of_units', models.IntegerField(null=True)),
                ('Price', models.IntegerField(null=True)),
                ('date', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('StockId', models.IntegerField(max_length=50, null=True)),
                ('StockName', models.CharField(max_length=200, null=True)),
                ('No_of_units', models.IntegerField(null=True)),
                ('CATERGORY', models.CharField(max_length=100, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]
