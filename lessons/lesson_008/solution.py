def print_header():
    print("=" * 30)

servers = []
for i in range(0,5):
    servers.append(input(f"Введите имя сервера {i+1}: "))

print_header()
print(f"Список серверов\n")
for i in range(len(servers)):
    print(f"{i+1}. {servers[i]}")
print_header()
