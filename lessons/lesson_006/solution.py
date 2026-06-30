def print_header():
    print("=" * 30)

def calculate_disk_info(total_disk_space, used_disk_space):
    free_disk_space = total_disk_space - used_disk_space
    percent_free_disk_space = used_disk_space / total_disk_space * 100
    return free_disk_space, percent_free_disk_space

total_disk_space = float(input("Введите общий объём диска (GB): "))
used_disk_space = float(input("ВВедите использованный объём (GB): "))

free_disk_space, percent_free_disk_space = calculate_disk_info(total_disk_space, used_disk_space)

print_header()
print(f"Общий объём  : {total_disk_space} GB")
print(f"Использовано : {used_disk_space} GB")
print(f"Свободно     : {free_disk_space} GB")
print(f"Использование: {percent_free_disk_space:.2f} %")
print_header()
