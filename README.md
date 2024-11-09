# Controle de Estoque para Ferragem
Este é um projeto de sistema de controle de estoque para uma loja de ferragem, desenvolvido em Python, com interface de linha de comando e banco de dados SQLite. O sistema permite o cadastro, consulta, e gerenciamento de produtos no estoque, além de gerar relatórios para controle e registro de entradas e saídas.

## Funcionalidades
  1. Cadastro de Produtos: Adicione novos produtos ao estoque, incluindo nome, marca, categoria, preço e quantidade.
  2. Registro de Entrada de Produtos: Registre a entrada de novas unidades ao estoque após compras ou reposições.
  3. Registro de Saída de Produtos: Registre a saída de produtos vendidos, ajustando automaticamente a quantidade no estoque.
  4. Relatório de Estoque: Gere relatórios que mostram todos os produtos, incluindo informações detalhadas e quantidade em estoque.
  5. Busca de Produtos: Busque produtos no estoque por nome ou categoria.
  6. Atualização de Produtos: Atualize as informações de um produto específico.
  7. Exclusão de Produtos: Remova produtos que não são mais vendidos ou estão descontinuados.

   
## Tecnologias Utilizadas
  Linguagem: Python
Banco de Dados: 
  SQLite (armazenamento local)
## Pré-requisitos
  Python 3.x
  Biblioteca SQLite3 (inclusa no Python padrão)
  
## Como Executar o Projeto
1. Clone este repositório:
  bash git clone https://github.com/seuusuario/estoque-ferragem.git
  cd estoque-ferragem

2. Execute o script principal:
bash python main.py

Siga as instruções no menu para utilizar as funcionalidades do sistema.

## Estrutura do Projeto
  main.py: Script principal com a interface do usuário e o menu de opções.
  estoque_hardware.db: Banco de dados SQLite usado para armazenar informações dos produtos.
  
## Exemplo de Uso
  Controle de Estoque - Ferragem
  1. Cadastrar Produto
  2. Registrar Entrada de Produto
  3. Registrar Saída de Produto
  4. Gerar Relatório de Estoque
  5. Buscar Produto
  6. Atualizar Produto
  7. Sair

Escolha uma opção: 

## Cadastrar Produto
Para cadastrar um novo produto, escolha a opção "1" no menu e insira as informações solicitadas (nome, marca, categoria, preço e quantidade).

## Registrar Entrada ou Saída
Para registrar a entrada ou saída de produtos, escolha a opção correspondente no menu e informe o ID do produto e a quantidade.

## Gerar Relatório de Estoque
Para visualizar o relatório completo do estoque, escolha a opção "4" no menu.

## Contribuindo
Contribuições são bem-vindas! 
Sinta-se à vontade para fazer um fork deste repositório e enviar um pull request com melhorias, correções ou novas funcionalidades.
  1. Faça um fork do projeto
  2. Crie uma nova branch para suas modificações (git checkout -b minha-modificacao)
  3. Commit suas mudanças (git commit -m 'Adiciona nova funcionalidade')
  4. Faça um push para a branch (git push origin minha-modificacao)
  5. bra um pull request
Licença
Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

