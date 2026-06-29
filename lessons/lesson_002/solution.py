for i in range(1,6):
    print("=" * 30)
    print(f"Проверка сервера№{i}")
    server_load_cpu = int(input("Введите загрузку CPU: "))
    if server_load_cpu >=80:
        print("Загрузка CPU высокая")
    elif server_load_cpu >= 50:
        print("Загрузка CPU средняя")
    else:
        print("Загрузка CPU нормальная")
    print("=" * 30)
