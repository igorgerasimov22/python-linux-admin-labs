def print_header():
    print("=" * 30)
    """Функция выводил заголовок программы
    аргументы отсутствуют
    """

def blank_string():
    print()
    """
    Функция добавляет пустую строку
    """

servers = []
servers.append({"name": "web01", "ip": "192.168.0.1", "ram": 32, "cpu": 8})
servers.append({"name": "web02", "ip": "192.168.0.2", "ram": 32, "cpu": 8})
servers.append({"name": "web01", "ip": "192.168.0.1", "ram": 32, "cpu": 8})


print_header()
print("ИНВЕНТАРИЗАЦИЯ\n")
for number, server in enumerate(servers, start=1):
    print(f"Сервер №{number}")
    for key, value in server.items():
        print(f"{key}: {value}")
    blank_string()
print_header()
