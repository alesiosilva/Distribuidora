# Generated by Django 4.1.6 on 2023-02-09 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estoque', '0003_produto_change_date_produto_entry_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/images'),
        ),
    ]