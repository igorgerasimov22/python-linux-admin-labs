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
for key, value in server.items():
    print(f"{key} : {value}")
print_header()
