def print_header():
    print("=" * 30)

servers = []
servers.append("web01")
servers.append("web02")
servers.append("db01")
servers.append("backup01")
servers.append("proxy01")

print_header()
print(f"Список серверов\n")
for i in range(len(servers)):
    print(f"{i+1}. {servers[i]}")
print_header()
