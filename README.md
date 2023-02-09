# Distribuidora
Aplicação WEB com Django para gestão de estoque em distribuidora de bebidas

## Model Produto
Registro de cada tipo de produto conforme características 
(id único que será relacionado com estoque)

## Model Estoque
Registro entrada/saíde com quantidade de produtos por código de barras cadastrado

## View Cadastro
Produto -> Formulário para cadastro das informações
Estoque -> Formulário para cadastro do código de barra e vínculo com o produto

## View Entrada
Acidiona 1 registro no banco por cada código de barras, se já existir, apenas atualiza incrementando quantidade

## View Baixa
Remove a quantidade infromada, ou apenas 1 unidade, de acordo a leitura do código de barras

## View Resumo
Exibe o relatório de sumarização dos tipos de produtos com quantidade e períodos de entrada/saída