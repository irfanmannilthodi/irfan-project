# Generated by Django 4.2.9 on 2024-02-21 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iapp', '0005_choose'),
    ]

    operations = [
        migrations.CreateModel(
            name='three',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('img', models.ImageField(upload_to='pics')),
                ('desc', models.TextField()),
            ],
        ),
    ]