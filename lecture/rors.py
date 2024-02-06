def convert_ab_to_int(a,b)-> tuple[int,int]: 
    return a,b  
def devided(a): 

 
while True:  
    a,b=input("введите 2 числа   ").split()  
    try:
        a,b=convert_ab_to_int(a,b) 
    except: 
        print("ERROR")  
        print("введи числа ")

    ab_summ = a+b 
    print(f"Сумма {a} + {b} = {ab_summ}")
 
  
   
except ValueError as e -- переменной присваевываем значение ошибки , необходимо для отладки  
raise Exception - поднятие ошибки   
finally --- выполняется всегда после выполнения программы не смотря на ошибки  чаще всего используется вместе с break  

InterruptedError- ошибка отступа