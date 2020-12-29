import sqlite3

MASTER_PASSWORD = "123456"

senha = input("Insira sua senha: ")
if senha != MASTER_PASSWORD:
    print("Senha inválida! Encerrando...\n")
    exit()

conn = sqlite3.connect('passwords.db')

cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    service TEXT NOT NULL,
    username TEXT NOT NULL,
    password TEXT NOT NULL
);
''')

def get_password(service):
    cursor.execute(f'''
        SELECT username, password FROM users
        WHERE service = '{service}'
    ''')

    if cursor.rowcount == 0:
        print("Serviço não cadastrado (use '2' para verificar os serviços)")
    else:
        for user in cursor.fetchall():
            print("username: " + user[0] + "\npassword: " + user[1] + "\n")

def insert_password(service, username, password):
    cursor.execute(f'''
        INSERT INTO users (service, username, password)
        VALUES ('{service}', '{username}', '{password}')
    ''')
    conn.commit()

def show_services():
    cursor.execute('''
        SELECT service FROM users;
    ''')
    for service in cursor.fetchall():
        print(service)

def menu():
    print("|-------------------------------|")
    print("|   1: Inserir nova senha:      |")
    print("|   2: Listar serviços salvos:  |")
    print("|   3: Recuperar uma senha:     |")
    print("|   4: Sair:                    |")
    print("|-------------------------------|\n")

while True:
    menu()
    op = input("O que deseja fazer? ")
    if op not in ['1', '2', '3', '4']:
        print("\nOpção inválida!")
        continue
    
    if op == '4':
        break

    if op == '1':
        service = input('Qual o nome do serviço? ')
        username = input('Qual o nome de usuario? ')
        password = input('Qual a senha? ')
        insert_password(service, username, password)
        print("\n")

    if op == '2':
        show_services()
        print("\n")

    if op == '3':
        service = input('Qual o serviço para qual quer a senha? ')
        print("\n")
        get_password(service)
        print("\n")

conn.close()