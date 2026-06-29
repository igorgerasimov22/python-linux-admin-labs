all_servers = 0
for i in range(1,6):
    print("=" * 30)
    print(f"Проверка сервера№{i}")
    all_servers += 1
    server_load_cpu = int(input("Введите загрузку CPU: "))
    if server_load_cpu >=80:
        print("Загрузка CPU высокая")
    elif server_load_cpu >= 50:
        print("Загрузка CPU средняя")
    else:
        print("Загрузка CPU нормальная")
    print("=" * 30)
print("=" * 30)
print("Проверка завершена.")
print(f"Проверено серверов: {all_servers}")
