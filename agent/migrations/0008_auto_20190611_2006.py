# Generated by Django 2.2.2 on 2019-06-11 20:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('agent', '0007_auto_20190611_2002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agentemail',
            name='agent_no',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agent.Agent'),
        ),
    ]
