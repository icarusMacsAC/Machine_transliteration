# Generated by Django 3.2.8 on 2021-10-18 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagecaption',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='static/media/uploads/image'),
        ),
    ]
