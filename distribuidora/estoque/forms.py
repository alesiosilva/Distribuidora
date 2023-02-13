from django.forms import ModelForm
from estoque.models import Produto

class ProdutoForm(ModelForm):
    class Meta:
        model = Produto
        fields = ('name', 'brand', 'flavor', 'size', 'image', 'due_date')