# Distribuidora
Aplicação WEB com Django para gestão de estoque em distribuidora de bebidas

## Model Produto
* Registro de cada tipo de produto conforme características 
(id único que será relacionado com estoque)

## Model Estoque
* Registro entrada/saída com quantidade de produtos por código de barras cadastrado

## Views Produto
### produto/novo
Formulário para cadastro das informações

### produto/
* Lista com todos produtos já cadastrados com link individual direcionando para a edição do mesmo

### produto/produto_id/ 
* Template do formulário de cadastro com dados do produto consultado permitindo edição e função SALVAR

### produto/edita/produto_id/
* Template de confirmação da edição

## Views Estoque
### estoque
* Exibe o relatório de sumarização dos tipos de produtos com quantidade e períodos de entrada/saída

### entrada
* Formulário para cadastro do código de barra com quantidade e vínculo com o produto.

* Acidiona 1 registro no banco por cada código de barras, se já existir, apenas atualiza incrementando quantidade

### saida
* Remove a quantidade infromada, ou apenas 1 unidade, de acordo a leitura do código de barras