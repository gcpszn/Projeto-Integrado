# Projeto-Integrado
# Sistema de Gerenciamento de Estoque
Este é um sistema de gerenciamento de estoque desenvolvido em Python, utilizando Programação Orientada a Objetos (POO). Permite o cadastro de produtos, atualização de estoqus e a geração de relatórios sobre os produtos. Foi projetado para otimizar a gestão de inventário em empresas, principalmente no setor de comércio eletrônico.

Funcionalidades
Cadastro de Produto: Permite cadastrar novos produtos, definindo código, nome, quantidade inicial, estoque mínimo e máximo.
Atualização de Estoque: Permite adicionar ou remover quantidades de um produto específico.
Relatório de Produto: Gera um relatório completo sobre o produto, com informações como código, nome, quantidade atual, estoque mínimo, estoque máximo, estado do estoque e histórico de movimentações.
Como Funciona
O sistema é estruturado com duas classes principais:

Classe Produto: Representa cada produto no estoque, com atributos como código, nome, quantidade disponível, estoque mínimo e máximo. Ela também mantém um histórico de movimentações (entrada e saída de produtos).
Métodos:
atualizar_estoque(quantidade): Atualiza a quantidade do produto no estoque e armazena o histórico de movimentações.
verificar_estoque(): Verifica o status do estoque (baixo, adequado ou excesso).
gerar_relatorio(): Exibe um relatório detalhado do produto.
Classe SistemaGerenciamentoProdutos: Gerencia os produtos cadastrados, permitindo realizar as operações de cadastro, atualização e geração de relatórios.
Métodos:
cadastrar_produto(): Cadastra um novo produto.
atualizar_estoque(): Atualiza o estoque de um produto existente.
gerar_relatorio(): Gera um relatório completo de um produto específico.
Estrutura do Código
Cadastro de Produto:
O usuário é solicitado a inserir as informações do produto, como código, nome, quantidade inicial, estoque mínimo e máximo. O sistema verifica se o estoque mínimo é menor que o estoque máximo antes de cadastrar o produto.

Atualização de Estoque:
O usuário pode adicionar ou remover produtos do estoque. A função atualizar_estoque() verifica se a operação é válida (se a quantidade não ultrapassa o limite de estoque ou se não há quantidade insuficiente).

Geração de Relatório:
O usuário pode gerar um relatório detalhado de um produto, visualizando informações sobre seu estoque e histórico de movimentações.

Exemplo de Uso
python
Copiar código
# Criação do sistema
sistema = SistemaGerenciamentoProdutos()

# Cadastrar produto
sistema.cadastrar_produto("001", "Produto A", 100, 20, 200)

# Atualizar estoque
sistema.atualizar_estoque("001", -10)  # Remover 10 unidades

# Gerar relatório
sistema.gerar_relatorio("001")
Dependências
Python 3.x
Biblioteca datetime (para registrar data e hora das movimentações)
Como Rodar
Clone este repositório ou baixe o arquivo Python.
Execute o código no seu ambiente Python local.
O programa vai exibir um menu de opções para o usuário, permitindo interações contínuas (como cadastrar produtos, atualizar estoque ou gerar relatórios).
Conclusão
Esse sistema tem como objetivo facilitar a gestão de inventário de uma empresa de comércio eletrônico, com a vantagem de controlar o fluxo de produtos de maneira eficiente e simples. Ele pode ser facilmente expandido para incluir mais funcionalidades conforme necessário.
