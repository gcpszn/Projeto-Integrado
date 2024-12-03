from datetime import datetime

class Produto:
    def __init__(self, codigo, nome, quantidade, estoque_minimo, estoque_maximo, localizacao="Armazém A"):
        self.codigo = codigo
        self.nome = nome
        self.quantidade = quantidade
        self.estoque_minimo = estoque_minimo
        self.estoque_maximo = estoque_maximo
        self.localizacao = localizacao
        self.historico = []

    def atualizar_estoque(self, quantidade):
        if (self.quantidade + quantidade) < 0:
            print("Quantidade insuficiente no estoque para essa operação.")
            return False
        else:
            self.quantidade += quantidade
            movimentacao = {
                "data": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "quantidade": quantidade,
                "nova_quantidade": self.quantidade,
                "localizacao": self.localizacao
            }
            self.historico.append(movimentacao)
            return True

    def atualizar_localizacao(self):
        nova_localizacao = "Armazém B" if self.localizacao == "Armazém A" else "Armazém A"
        self.localizacao = nova_localizacao
        print(f"Localização do produto {self.codigo} alterada para: {self.localizacao}")

    def verificar_estoque(self):
        if self.quantidade < self.estoque_minimo:
            return "Estoque baixo"
        elif self.quantidade > self.estoque_maximo:
            return "Excesso de estoque"
        else:
            return "Estoque correto"

    def gerar_relatorio(self):
        print(f"Código: {self.codigo}")
        print(f"Nome: {self.nome}")
        print(f"Quantidade atual: {self.quantidade} unidades")
        print(f"Estoque mínimo: {self.estoque_minimo} unidades")
        print(f"Estoque máximo: {self.estoque_maximo} unidades")
        print(f"Estado do estoque: {self.verificar_estoque()}")
        print(f"Localização atual: {self.localizacao}")
        print("Histórico de movimentação:")
        for movimentacao in self.historico:
            print(f" - Data: {movimentacao['data']}, Quantidade alterada: {movimentacao['quantidade']}, "
                  f"Estoque atual: {movimentacao['nova_quantidade']}, Localização: {movimentacao['localizacao']}")

class SistemaGerenciamentoProdutos:
    def __init__(self):
        self.produtos = {}

    def cadastrar_produto(self, codigo, nome, quantidade, estoque_minimo, estoque_maximo, localizacao="Armazém A"):
        if estoque_minimo >= estoque_maximo:
            print("Erro: Estoque mínimo deve ser menor que o estoque máximo.")
            return
        produto = Produto(codigo, nome, quantidade, estoque_minimo, estoque_maximo, localizacao)
        self.produtos[codigo] = produto
        print("Produto cadastrado com sucesso no", localizacao)

    def atualizar_estoque(self, codigo, quantidade):
        if codigo in self.produtos:
            if self.produtos[codigo].atualizar_estoque(quantidade):
                print("Estoque atualizado com sucesso.")
            else:
                print("Erro ao atualizar estoque.")
        else:
            print("Produto não encontrado")

    def atualizar_localizacao(self, codigo):
        if codigo in self.produtos:
            self.produtos[codigo].atualizar_localizacao()
        else:
            print("Produto não encontrado")

    def gerar_relatorio(self, codigo):
        if codigo in self.produtos:
            self.produtos[codigo].gerar_relatorio()
        else:
            print("Produto não encontrado")

sistema = SistemaGerenciamentoProdutos()

while True:
    print("\n[1] Cadastrar produto")
    print("[2] Atualizar estoque")
    print("[3] Transferir entre armazéns")
    print("[4] Gerar relatório")
    print("[5] Sair")
    
    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        try:
            codigo = input("Digite o código do produto: ")
            nome = input("Digite o nome do produto: ")
            quantidade = int(input("Digite a quantidade inicial do produto: "))
            estoque_minimo = int(input("Digite o estoque mínimo do produto: "))
            estoque_maximo = int(input("Digite o estoque máximo do produto: "))
            localizacao = input("Digite a localização inicial (Armazém A ou Armazém B): ")
            if localizacao not in ["aA", "bB"]:
                print("Localização inválida. O produto será cadastrado no Armazém A por padrão.")
                localizacao = "Armazém A"
            sistema.cadastrar_produto(codigo, nome, quantidade, estoque_minimo, estoque_maximo, localizacao)
        except ValueError:
            print("Erro: Certifique-se de inserir valores numéricos válidos.")
    elif escolha == "2":
        try:
            codigo = input("Digite o código do produto: ")
            quantidade = int(input("Digite a quantidade a ser adicionada/removida: "))
            sistema.atualizar_estoque(codigo, quantidade)
        except ValueError:
            print("Erro: Certifique-se de inserir um valor numérico para a quantidade.")
    elif escolha == "3":
        codigo = input("Digite o código do produto: ")
        sistema.atualizar_localizacao(codigo)
    elif escolha == "4":
        codigo = input("Digite o código do produto: ")
        sistema.gerar_relatorio(codigo)
    elif escolha == "5":
        print("Saindo do sistema.")
        break
    else:
        print("Opção inválida. Tente novamente.")
