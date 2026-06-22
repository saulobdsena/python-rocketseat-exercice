# 📒 Contact Manager

Um gerenciador de contatos desenvolvido em **Python**, executado pelo terminal. O projeto permite cadastrar, visualizar, editar, favoritar e excluir contatos por meio de um menu interativo.

## 📌 Sobre o projeto

O **Contact Manager** foi criado para praticar conceitos fundamentais da linguagem Python, como:

* Listas;
* Dicionários;
* Funções;
* Estruturas condicionais;
* Laços de repetição;
* Tratamento de exceções;
* Uso do `match case`;
* Entrada e saída de dados pelo terminal.

Cada contato é armazenado em um dicionário com as seguintes informações:

```python
{
    "name": "Contact name",
    "number": "Contact number",
    "email": "Contact email",
    "is_fav": False
}
```

Os dicionários são adicionados à lista principal de contatos:

```python
contact_list = []
```

## ⚙️ Funcionalidades

O sistema possui as seguintes funcionalidades:

1. **Adicionar um novo contato**

   * Solicita o nome, número de telefone e e-mail.
   * Adiciona o contato à lista.

2. **Visualizar todos os contatos**

   * Exibe os contatos cadastrados.
   * Mostra a posição de cada contato na lista.
   * Indica quais contatos estão marcados como favoritos.

3. **Editar um contato**

   * Permite alterar o nome, número de telefone e e-mail de um contato existente.

4. **Favoritar ou desfavoritar um contato**

   * Alterna o status de favorito do contato selecionado.

5. **Visualizar contatos favoritos**

   * Exibe somente os contatos marcados como favoritos.

6. **Excluir um contato**

   * Remove o contato selecionado da lista.

7. **Sair do programa**

   * Encerra a execução do gerenciador.

## 🖥️ Menu do sistema

Ao executar o programa, o seguinte menu será exibido:

```text
Contact Manager Menu

1. Add New Contact
2. View Contact List
3. Edit Contact
4. Favorite/Unfavorite Contact
5. Favorite Contact List
6. Delete Contact
7. Exit
```

O usuário deve informar o número correspondente à operação que deseja realizar.

## 🚀 Como executar

### Pré-requisitos

É necessário possuir o **Python 3.10 ou superior**, pois o projeto utiliza a estrutura `match case`.

Para verificar a versão instalada:

```bash
python --version
```

ou:

```bash
python3 --version
```

### Clonando o repositório

```bash
git clone URL_DO_REPOSITORIO
```

Entre na pasta do projeto:

```bash
cd contact-manager
```

Execute o programa:

```bash
python main.py
```

Em alguns sistemas, pode ser necessário utilizar:

```bash
python3 main.py
```

## 📂 Estrutura do projeto

```text
contact-manager/
│
├── main.py
└── README.md
```

## 🔧 Funções utilizadas

### `add_contact()`

Adiciona um novo contato à lista.

```python
add_contact(contact_list, contact_name, contact_number, contact_email)
```

### `view_contacts()`

Exibe todos os contatos cadastrados.

```python
view_contacts(contact_list)
```

### `edit_contact()`

Atualiza os dados de um contato selecionado.

```python
edit_contact(contact_list, contact_index, new_name, new_number, new_email)
```

### `favorite_contact()`

Alterna o contato entre favorito e não favorito.

```python
favorite_contact(contact_list, contact_index)
```

### `view_favorite_contacts()`

Exibe somente os contatos favoritos.

```python
view_favorite_contacts(contact_list)
```

### `delete_contact()`

Remove um contato da lista.

```python
delete_contact(contact_list, contact_index)
```

## 📝 Exemplo de uso

```text
Contact Manager Menu
1. Add New Contact
2. View Contact List
3. Edit Contact
4. Favorite/Unfavorite Contact
5. Favorite Contact List
6. Delete Contact
7. Exit

Enter: 1

Contact name: John
Contact number: 99999-9999
Contact email: john@email.com

Contact John added to the contact manager
```

Ao visualizar a lista:

```text
1. | | Name: John, Number: 99999-9999, Email: john@email.com
```

Quando o contato é marcado como favorito:

```text
1. |★| Name: John, Number: 99999-9999, Email: john@email.com
```

## 🛠️ Tecnologias utilizadas

* Python 3;
* Terminal;
* Git;
* GitHub.

## 🎯 Objetivo

Este projeto tem finalidade educacional e foi desenvolvido para praticar os fundamentos da programação com Python e a organização de um programa baseado em funções.