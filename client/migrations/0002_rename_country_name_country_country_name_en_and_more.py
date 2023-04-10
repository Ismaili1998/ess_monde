# Generated by Django 4.1.7 on 2023-04-09 23:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='country',
            old_name='country_name',
            new_name='country_name_en',
        ),
        migrations.AddField(
            model_name='country',
            name='country_name_fr',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='client',
            name='client_nbr',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]