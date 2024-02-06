from import_this import RACE_DATA 

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


 
def print_racer_info(RACE_DATA, i):
    for place, racer_info in RACE_DATA.items():
        if racer_info['FinishedPlace'] == i:
            if i == 1:
                sek = racer_info["FinishedTimeSeconds"]
                winner = f"Выиграл {racer_info['RacerName']}!!! Поздравляем"
                print(winner)
                print("_" * len(winner)) 
                print("")
            print(f"Гонщик на {racer_info['FinishedPlace']} месте:")
            print(f"Имя: {racer_info['RacerName']}")
            print(f"Команда: {racer_info['RacerTeam']}")
            print(f"Время: {convert_seconds_to_time(racer_info['FinishedTimeSeconds'])}")

         
for i in range(1, 3+ 1):
    print_racer_info(RACE_DATA, i) 
    print("")

           