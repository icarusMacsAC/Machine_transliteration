# Generated by Django 3.2.8 on 2022-04-01 08:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20220401_1322'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='pdf_decode',
            new_name='ImageCaption',
        ),
        migrations.RenameField(
            model_name='imagecaption',
            old_name='pdf',
            new_name='img',
        ),
    ]
