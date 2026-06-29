def print_header():
    print("=" * 30)

def calculate_free_disk(total_space_disk, used_space_disk):
    return total_space_disk - used_space_disk

total_space_disk = float(input("Введите объём диска: "))
used_space_disk = float(input("Введите использованный объём диска: "))

free_space_disk = calculate_free_disk(total_space_disk, used_space_disk)

print_header()
print(f"Объём свободного пространства GB: {free_space_disk}")
print_header()
