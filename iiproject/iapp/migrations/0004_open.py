# Generated by Django 4.2.9 on 2024-02-20 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iapp', '0003_rename_bac_background'),
    ]

    operations = [
        migrations.CreateModel(
            name='Open',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='pics')),
            ],
        ),
    ]
