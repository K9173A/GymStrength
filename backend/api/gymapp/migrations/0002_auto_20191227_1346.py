# Generated by Django 2.2.8 on 2019-12-27 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gymapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='databaseexercise',
            name='description',
            field=models.TextField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='databaseexercise',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]