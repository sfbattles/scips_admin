# Generated by Django 2.2.2 on 2019-06-22 03:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agent', '0012_auto_20190622_0325'),
    ]

    operations = [
        migrations.RenameField(
            model_name='agentemail',
            old_name='get_portal_emails',
            new_name='get_portal_email',
        ),
    ]
