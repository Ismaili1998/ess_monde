# Generated by Django 4.1.7 on 2023-03-17 16:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country_name', models.CharField(max_length=200)),
                ('abbreviation', models.CharField(max_length=4)),
            ],
            options={
                'db_table': 'country',
            },
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.CharField(max_length=100)),
                ('client_nbr', models.CharField(blank=True, max_length=50)),
                ('address', models.CharField(max_length=200)),
                ('postal_code', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=200)),
                ('phone_number', models.CharField(max_length=20)),
                ('fax', models.CharField(max_length=20)),
                ('mobile', models.CharField(max_length=20)),
                ('email1', models.EmailField(max_length=254)),
                ('email2', models.EmailField(max_length=254)),
                ('website', models.URLField()),
                ('internal_contact', models.CharField(max_length=200)),
                ('external_contact', models.CharField(max_length=200)),
                ('representative', models.CharField(max_length=200)),
                ('representative_1', models.CharField(max_length=200)),
                ('representative_2', models.CharField(max_length=200)),
                ('language', models.CharField(choices=[('English', 'English'), ('German', 'German'), ('French', 'French')], max_length=200)),
                ('credit_limit', models.FloatField()),
                ('remark', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client.country')),
            ],
            options={
                'db_table': 'client',
            },
        ),
    ]
