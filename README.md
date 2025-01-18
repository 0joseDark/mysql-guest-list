# mysql-guest-list
 - lista de convidados com mysql
### Passos para instalar os módulos necessários
- [English](https://github.com/0joseDark/-mysql-guest-list-0/blob/main/English-README.md) 
=======
 - [English](https://github.com/0joseDark/-mysql-guest-list-0/blob/main/English-README.md) 
1. **Instalar o Python**:
   - Certifique-se de que o Python está instalado no Windows 10. Pode ser baixado em [python.org](https://www.python.org/). Lembre-se de marcar a opção "Add Python to PATH" durante a instalação.

2. **Instalar o pip** (gestor de pacotes):
   - O pip já vem com versões recentes do Python. Para confirmar, execute no terminal:
     ```bash
     python -m ensurepip
     ```

3. **Instalar o `mysql-connector-python`**:
   - Execute o seguinte comando no terminal para instalar o conector MySQL:
     ```bash
     pip install mysql-connector-python
     ```

4. **Configurar o MySQL**:
   - Certifique-se de que o MySQL está instalado e em execução no seu sistema. Pode fazer o download em [MySQL](https://www.mysql.com/).
   - Crie uma base de dados chamada `lista_convidados`:
     ```sql
     CREATE DATABASE lista_convidados;
     ```

5. **Executar o programa**:
   - Salve o código num ficheiro chamado `lista_convidados.py` e execute com:
     ```bash
     python lista_convidados.py
     ```

Agora pode adicionar, listar e remover convidados diretamente na interface gráfica!
