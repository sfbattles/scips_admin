# Generated by Django 2.2.2 on 2019-06-11 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agent', '0005_auto_20190611_1955'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agentphone',
            name='phone_extension',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
