# Generated by Django 4.1.6 on 2023-02-23 17:05

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicios', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicio',
            name='description',
            field=ckeditor_uploader.fields.RichTextUploadingField(default=' ', verbose_name='Descripcion'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='servicio',
            name='image_1',
            field=models.ImageField(null=True, upload_to='servicios', verbose_name='Imagen'),
        ),
        migrations.AddField(
            model_name='servicio',
            name='image_2',
            field=models.ImageField(blank=True, null=True, upload_to='servicios', verbose_name='Imagen'),
        ),
        migrations.AddField(
            model_name='servicio',
            name='image_3',
            field=models.ImageField(blank=True, null=True, upload_to='servicios', verbose_name='Imagen'),
        ),
        migrations.AddField(
            model_name='servicio',
            name='image_4',
            field=models.ImageField(blank=True, null=True, upload_to='servicios', verbose_name='Imagen'),
        ),
        migrations.AddField(
            model_name='servicio',
            name='image_5',
            field=models.ImageField(blank=True, null=True, upload_to='servicios', verbose_name='Imagen'),
        ),
    ]
