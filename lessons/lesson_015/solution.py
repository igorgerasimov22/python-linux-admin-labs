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

def add_empty_line():
    """
    Добавляет пустую строку
    """
    print()

def load_servers():
    """
    Открываем файл со списком серверов
    """
    servers = [{
        "name": "",
        "ip": ""
    }]
    servers = []
    with open("servers.txt", "r") as file:
        for line in file:
            line = line.strip()
            lines = line.split(',')
            if not line:
                continue
            servers.append({"name": lines[0], "ip": lines[1], "ram": lines[2], "cpu": lines[3]})
            #print(test[1])
        return servers


def print_servers(servers):
    """
    Выводим список серверов
    """
    for number, server in enumerate(servers, start=1):
        add_empty_line()
        for key,value in server.items():
            print(f"{key}: {value}")


print_header()
print_title()
servers = load_servers()
print_servers(servers)
print_header()