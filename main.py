import sqlite3
from datetime import datetime

# Conexão com o banco de dados SQLite
conn = sqlite3.connect('estoque_hardware.db')
cursor = conn.cursor()

# Criação da tabela de produtos
cursor.execute('''
CREATE TABLE IF NOT EXISTS produtos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    marca TEXT,
    categoria TEXT,
    preco REAL NOT NULL,
    quantidade INTEGER NOT NULL
)
''')

# Função para cadastrar um novo produto
def cadastrar_produto(nome, marca, categoria, preco, quantidade):
    cursor.execute('''
    INSERT INTO produtos (nome, marca, categoria, preco, quantidade)
    VALUES (?, ?, ?, ?, ?)
    ''', (nome, marca, categoria, preco, quantidade))
    conn.commit()
    print(f"Produto '{nome}' cadastrado com sucesso!")

# Função para registrar entrada de produtos no estoque
def registrar_entrada(produto_id, quantidade):
    cursor.execute('SELECT quantidade FROM produtos WHERE id = ?', (produto_id,))
    result = cursor.fetchone()
    if result:
        nova_quantidade = result[0] + quantidade
        cursor.execute('UPDATE produtos SET quantidade = ? WHERE id = ?', (nova_quantidade, produto_id))
        conn.commit()
        print(f"Entrada de {quantidade} unidades registrada com sucesso!")
    else:
        print("Produto não encontrado.")

# Função para registrar saída de produtos (vendas)
def registrar_saida(produto_id, quantidade):
    cursor.execute('SELECT quantidade FROM produtos WHERE id = ?', (produto_id,))
    result = cursor.fetchone()
    if result and result[0] >= quantidade:
        nova_quantidade = result[0] - quantidade
        cursor.execute('UPDATE produtos SET quantidade = ? WHERE id = ?', (nova_quantidade, produto_id))
        conn.commit()
        print(f"Venda de {quantidade} unidades registrada com sucesso!")
    else:
        print("Quantidade insuficiente ou produto não encontrado.")

# Função para gerar relatório de estoque
def gerar_relatorio():
    cursor.execute('SELECT * FROM produtos')
    produtos = cursor.fetchall()
    print("\nRelatório de Estoque:")
    for produto in produtos:
        print(f"ID: {produto[0]}, Nome: {produto[1]}, Marca: {produto[2]}, Categoria: {produto[3]}, Preço: R${produto[4]:.2f}, Quantidade: {produto[5]}")

# Função para buscar um produto pelo nome ou categoria
def buscar_produto(busca):
    cursor.execute('SELECT * FROM produtos WHERE nome LIKE ? OR categoria LIKE ?', (f'%{busca}%', f'%{busca}%'))
    resultados = cursor.fetchall()
    if resultados:
        print("\nProdutos encontrados:")
        for produto in resultados:
            print(f"ID: {produto[0]}, Nome: {produto[1]}, Marca: {produto[2]}, Categoria: {produto[3]}, Preço: R${produto[4]:.2f}, Quantidade: {produto[5]}")
    else:
        print("Nenhum produto encontrado com esses critérios.")

# Função para atualizar um produto
def atualizar_produto(produto_id, nome=None, marca=None, categoria=None, preco=None, quantidade=None):
    if nome:
        cursor.execute('UPDATE produtos SET nome = ? WHERE id = ?', (nome, produto_id))
    if marca:
        cursor.execute('UPDATE produtos SET marca = ? WHERE id = ?', (marca, produto_id))
    if categoria:
        cursor.execute('UPDATE produtos SET categoria = ? WHERE id = ?', (categoria, produto_id))
    if preco:
        cursor.execute('UPDATE produtos SET preco = ? WHERE id = ?', (preco, produto_id))
    if quantidade is not None:
        cursor.execute('UPDATE produtos SET quantidade = ? WHERE id = ?', (quantidade, produto_id))
    conn.commit()
    print("Produto atualizado com sucesso!")

# Função principal para menu de operações
def main():
    while True:
        print("\nControle de Estoque - Ferragem")
        print("1. Cadastrar Produto")
        print("2. Registrar Entrada de Produto")
        print("3. Registrar Saída de Produto")
        print("4. Gerar Relatório de Estoque")
        print("5. Buscar Produto")
        print("6. Atualizar Produto")
        print("7. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            nome = input("Nome do produto: ")
            marca = input("Marca: ")
            categoria = input("Categoria: ")
            preco = float(input("Preço: "))
            quantidade = int(input("Quantidade: "))
            cadastrar_produto(nome, marca, categoria, preco, quantidade)
        
        elif opcao == '2':
            produto_id = int(input("ID do produto: "))
            quantidade = int(input("Quantidade de entrada: "))
            registrar_entrada(produto_id, quantidade)
        
        elif opcao == '3':
            produto_id = int(input("ID do produto: "))
            quantidade = int(input("Quantidade de saída: "))
            registrar_saida(produto_id, quantidade)
        
        elif opcao == '4':
            gerar_relatorio()
        
        elif opcao == '5':
            busca = input("Nome ou categoria para buscar: ")
            buscar_produto(busca)
        
        elif opcao == '6':
            produto_id = int(input("ID do produto: "))
            nome = input("Novo nome (pressione Enter para manter): ")
            marca = input("Nova marca (pressione Enter para manter): ")
            categoria = input("Nova categoria (pressione Enter para manter): ")
            preco = input("Novo preço (pressione Enter para manter): ")
            quantidade = input("Nova quantidade (pressione Enter para manter): ")
            
            # Chamar função com valores válidos ou None
            atualizar_produto(
                produto_id, 
                nome=nome if nome else None, 
                marca=marca if marca else None, 
                categoria=categoria if categoria else None, 
                preco=float(preco) if preco else None, 
                quantidade=int(quantidade) if quantidade else None
            )
        
        elif opcao == '7':
            print("Encerrando o sistema...")
            break
        else:
            print("Opção inválida, tente novamente.")

# Executa o programa
if __name__ == "__main__":
    main()

# Fechar a conexão ao sair
conn.close()
