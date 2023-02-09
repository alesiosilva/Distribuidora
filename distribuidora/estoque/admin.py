from django.contrib import admin
from .models import Estoque, Produto

# Register your models here.
admin.site.register(Produto)
admin.site.register(Estoque)