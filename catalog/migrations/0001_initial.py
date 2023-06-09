# Generated by Django 4.1.7 on 2023-05-08 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BeautyService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Duration', models.DurationField()),
                ('Price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('Description', models.TextField()),
                ('Photo', models.ImageField(upload_to='')),
            ],
        ),
    ]
