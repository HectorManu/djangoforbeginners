# Generated by Django 4.2.5 on 2023-09-22 02:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_member_joined_date_member_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='phone',
            field=models.IntegerField(null=True),
        ),
    ]
