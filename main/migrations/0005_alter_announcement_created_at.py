# Generated by Django 3.2.4 on 2021-08-19 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_announcement_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcement',
            name='created_at',
            field=models.CharField(default='08/19/21', max_length=20),
        ),
    ]
