# Generated by Django 4.1.6 on 2023-02-12 23:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estoque', '0006_alter_estoque_options_alter_produto_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='due_date',
            field=models.DateField(blank=True, null=True, verbose_name='Data de vencimento'),
        ),
    ]
