# Generated by Django 4.1.7 on 2023-06-07 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_alter_beautyservice_group'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userContactData', models.CharField(max_length=50)),
                ('userName', models.CharField(max_length=40)),
                ('contactTimeStamp', models.DateTimeField()),
            ],
        ),
    ]