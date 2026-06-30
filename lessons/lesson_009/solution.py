def print_header():
    print("=" * 30)

servers = []
for i in range(5):
    servers.append(input("Введите имя сервера: "))

print_header()
print("ИНВЕНТАРИЗАЦИЯ СЕРВЕРОВ")
for number, server in enumerate(servers, start=1):
    print(f"{number}. {server}")
print(f"Всего серверов: {len(servers)}")
print_header()
