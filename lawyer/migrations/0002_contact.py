# Generated by Django 4.0 on 2022-01-21 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lawyer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FirstName', models.CharField(max_length=20)),
                ('LastName', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.IntegerField()),
                ('message', models.TextField()),
            ],
        ),
    ]
