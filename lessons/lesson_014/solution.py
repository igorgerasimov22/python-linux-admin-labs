def print_header():
    """
    Функция печатает заголовок и подвал
    """
    print("=" * 30)

def print_title():
    """
    Функция выводит заголовок
    """
    print("\nИНВЕНТОРИЗАЦИЯ\n")

def add_empty_line():
    """
    Функция добавляет пустую строку
    """

def create_servers():
    """
    Функция запрашивает количество серверов и на основании количество запрашивает информацию о самих серверах
    Имя
    IP
    RAM
    CPU
    """
    servers_count = int(input("Введите количество серверов: "))
    servers = []
    for number in range(servers_count):
        servers.append({
            "Имя": input("Введите имя сервера: "),
            "IP": input("Введите ip адрес: "),
            "RAM": input("Введите объём ОЗУ (GB): "),
            "CPU": input("Введите кол-во ядер CPU: ")
        })
    return servers

def print_servers(servers):
    """
    Функция выводит список серверов
    """
    for number, server in enumerate(servers, start=1):
        for key, value in server.items():
            print(f"{key}: {value}")
        add_empty_line()
        

print_header()
servers = create_servers()
print_title()
print_servers(servers)
print_header()