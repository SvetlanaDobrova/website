# Generated by Django 4.1.7 on 2023-06-08 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_contacts'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='feedbackDate',
            field=models.DateTimeField(auto_now=True),
        ),
    ]