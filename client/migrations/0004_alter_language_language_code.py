# Generated by Django 4.1.7 on 2023-04-26 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0003_language_language_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='language',
            name='language_code',
            field=models.CharField(max_length=4, unique=True),
        ),
    ]