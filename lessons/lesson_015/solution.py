def print_header():
    """
    Выводим разделитель
    """
    print("=" * 30)

def print_title():
    """
    Вывод заголовка
    """
    print("Список серверов:\n")

def load_servers():
    """
    Открываем файл со списком серверов
    """
    with open("./servers.txt", "r") as file:
        servers = []
        for line in file:
            servers.append(line.strip())
        return servers

def print_servers(servers):
    """
    Выводим список серверов
    """
    for server in servers:
        print(server)

print_header()
print_title()
servers = load_servers()
print_servers(servers)
print_header()