# Generated by Django 2.0.4 on 2018-04-25 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20180425_1706'),
    ]

    operations = [
        migrations.AlterField(
            model_name='case',
            name='closed_on',
            field=models.DateField(null=True),
        ),
    ]
