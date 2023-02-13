from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='estoque'),
    path('produto/', views.product, name='produto'),
    path('produto/<int:produto_id>/', views.detail, name='detalhe'),
    path('produto/edita/<int:produto_id>', views.edit, name='edita'),
    path('produto/novo', views.register, name='novo'),
    path('estoque/entrada/', views.entry, name='entrada'),
    path('estoque/saida/', views.output, name='saida'),
]