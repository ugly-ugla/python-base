time = int(input('Введите количество секунд: '))
hours = time // 3600
minutes = (time - hours * 3600) // 60
seconds = time - (hours * 3600 + minutes * 60)

print(f"Время - {hours}:{minutes}:{seconds}")