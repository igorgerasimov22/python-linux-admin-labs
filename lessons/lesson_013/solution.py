def print_header():
    """
    Функция печатает заголовок и подвал
    """
    print("=" * 30)

def add_empty_line():
    """
    Функция добавляет пустую строку
    """
    print()

def create_servers():
    """
    Функция создаёт список серверов и возвращает список
    """
    servers = []
    servers.append({"name": "web01","ip": "192.168.0.1","ram": 32,"cpu": 8})
    servers.append({"name": "web02","ip": "192.168.0.2","ram": 32,"cpu": 8})
    servers.append({"name": "web03","ip": "192.168.0.3","ram": 32,"cpu": 8})
    return servers

def print_servers(servers):
    """
    Функция выводит список серверов
    """
    for number, server in enumerate(servers, start=1):
        print(f"Сервер №{number}")
        for key, value in server.items():
            print(key, value)
        add_empty_line()

print_header()
print("ИНВЕНТАРИЗАЦИЯ")
add_empty_line()
servers = create_servers()
print_servers(servers)
print_header()