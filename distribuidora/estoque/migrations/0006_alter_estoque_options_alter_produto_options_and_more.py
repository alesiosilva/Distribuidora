# Generated by Django 4.1.6 on 2023-02-12 23:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estoque', '0005_estoque_is_entry'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='estoque',
            options={'verbose_name': 'Estoque'},
        ),
        migrations.AlterModelOptions(
            name='produto',
            options={'verbose_name': 'Produto', 'verbose_name_plural': 'Produtos'},
        ),
    ]