# Generated by Django 4.1.7 on 2023-05-24 19:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_beautyservicegroup_feedback_beautyservice_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beautyservice',
            name='Group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='catalog.beautyservicegroup'),
        ),
    ]
