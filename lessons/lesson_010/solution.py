def print_header():
    print("=" * 30)

server = {
    "name": "web01",
    "ip": "192.168.0.1",
    "ram": 32,
    "cpu": 8
}

print_header()
print("ИНФОРМАЦИЯ О СЕРВЕРЕ")
print()
print(f"Имя : {server['name']}")
print(f"IP  : {server['ip']}")
print(f"RAM : {server['ram']}")
print(f"CPU : {server['cpu']}")
print_header()
