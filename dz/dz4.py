
def convert_seconds_to_time(seconds):
    minutes = 0
    hours = 0
    seconds_tick = 0

    for i in range(seconds + 1):
        seconds_tick += 1
        if seconds_tick == 60:
            minutes += 1
            seconds_tick = 0
        elif minutes == 60:
            minutes = 0
            hours += 1

    return f'{hours}:{minutes}:{seconds_tick-1}'

sek = int(input("Введите количество секунд: "))
result = convert_seconds_to_time(sek)
print(result)