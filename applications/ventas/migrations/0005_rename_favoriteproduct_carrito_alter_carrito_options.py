# Generated by Django 4.1.6 on 2023-02-20 21:15

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ventas', '0004_product_active'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='FavoriteProduct',
            new_name='Carrito',
        ),
        migrations.AlterModelOptions(
            name='carrito',
            options={'verbose_name': 'Carrito', 'verbose_name_plural': 'Carritos'},
        ),
    ]
