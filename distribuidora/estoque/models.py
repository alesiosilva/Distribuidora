from django.db import models
import datetime as dt

# Modelagem do estoque de produtos.

class Produto(models.Model):
    name = models.CharField(max_length=200)
    brand = models.CharField(max_length=100)
    flavor = models.CharField(max_length=100)
    size = models.CharField(max_length=10)
    image = models.ImageField(blank=True, null=True, upload_to='media/images')
    entry_date = models.DateTimeField('Data cadastro', auto_created=True, default=None)
    change_date = models.DateTimeField('Data atualização', auto_now=True)
    due_date = models.DateField('Data de vencimento', null=True, blank=True)

    def __str__ (self):
        return self.name

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'

class Estoque(models.Model):
    barcode = models.CharField(max_length=100)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quant = models.IntegerField(default=0)
    is_entry = models.BooleanField(default=True)
    entry_date = models.DateTimeField('Data entrada', auto_created=True, default=None)
    change_date = models.DateTimeField('Data atualização', auto_now=True)

    class Meta:
        verbose_name = 'Estoque'

