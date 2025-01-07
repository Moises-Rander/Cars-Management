# Carros - Projeto Fullstack Django

## Descrição
"Carros" é um sistema de gerenciamento de estoque de carros, desenvolvido com Django e hospedado na AWS. Ele permite o cadastro, edição, visualização e exclusão de veículos, além de contar com funcionalidades de autenticação e gerenciamento de usuários.

## Tecnologias Utilizadas
- **Django**: Framework de desenvolvimento web.
- **PostgreSQL**: Banco de dados relacional.
- **AWS**: Hospedagem do sistema.
  - **EC2**: Instância de servidor virtual.
  - **IP Elástico**: Endereço IP fixo para acesso.
  - **Volume de Backup**: Armazenamento adicional para emergências.
- **Git**: Controle de versão.

## Funcionalidades
- CRUD completo de cadastro de carros.
- Cadastro e verificação de usuários.
- Upload e exibição de imagens dos veículos.
- Validação de autenticação para acesso ao sistema.

## Público-Alvo
- **Vendedores**: Podem gerenciar o estoque de carros.
- **Clientes**: Podem visualizar os carros disponíveis para venda.

## Configuração Local
Para configurar e rodar o projeto localmente:
1. Clone o repositório:
   ```bash
   git clone https://github.com/usuario/projeto-carros.git
2. Entre no diretório do projeto:
   ```bash
   cd projeto-carros
3. Crie um ambiente virtual e ative-o:
   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate
4. Instale as dependências:
   ```bash
   pip install -r requirements.txt
5. Crie um arquivo ".env" na raiz do seu projeto e declare a senha do seu banco de dados:
   ```bash
   DATABASE_PASSWORD="Senha_Do_Seu_Banco_De_Dados_PostgreSQL"
   
6. Rode as migrações e inicie o servidor:
   ```bash
   python manage.py migrate
   python manage.py runserver

## Deploy da AWS
O deploy foi realizado seguindo os passos abaixo:
1. Criação de uma instância EC2 na AWS.
2. Configuração de um IP elástico para acesso fixo.
3. Configuração de firewall para acesso global.
4. Configuração de volumes de backup para emergências.
5. Linkagem do repositório GitHub ao servidor.
6. Deploy do projeto na instância EC2.

## Arquitetura
O projeto segue a arquitetura MTV (Model-Template-View), típica de aplicações Django, com as pastas estruturadas de forma organizada para facilitar a manutenção e a escalabilidade.

## Desafios e Soluções
- **Hospedagem na AWS**: Enfrentou desafios ao configurar e gerenciar a instância EC2 pela primeira vez.
- **Integração Frontend e Backend**: Trabalhou na criação de layouts de interface que se integrassem eficientemente com o backend.

## Capturas de tela
1. Tela de início do usuário logado
- <img width="1710" alt="Captura de Tela 2025-01-07 às 09 06 36" src="https://github.com/user-attachments/assets/a440ad9c-8bb8-4cb3-8963-83543c744be7" />

2. Tela de login
- <img width="1710" alt="Captura de Tela 2025-01-07 às 09 07 12" src="https://github.com/user-attachments/assets/c0c0999d-64e4-478b-80a9-ec5487e3f030" />

3. Tela de cadastro de usuários
- <img width="1710" alt="Captura de Tela 2025-01-07 às 09 07 31" src="https://github.com/user-attachments/assets/53a7643c-7dfc-43c0-bb85-5e01e994240c" />

4. Tela de cadastro de carros
- <img width="1710" alt="Captura de Tela 2025-01-07 às 09 08 00" src="https://github.com/user-attachments/assets/be42f9d3-acbb-483b-9cd1-af3badaec873" />

5. Tela de detalhes do carro
- <img width="1710" alt="Captura de Tela 2025-01-07 às 09 08 23" src="https://github.com/user-attachments/assets/f3a44e3e-3b39-4777-a547-b292690cc1d4" />

## Contato
- **Email**: moisesrander@outlook.com
- **Telefone**: +55 (98) 99123-2503

