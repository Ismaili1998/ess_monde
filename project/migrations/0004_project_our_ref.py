# Generated by Django 4.1.7 on 2023-04-15 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0003_remove_project_our_ref'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='our_ref',
            field=models.CharField(default='zdzred', max_length=255),
            preserve_default=False,
        ),
    ]
