pl1,pl2=input("Ввод ").lower().split() 
def the_best_game(pl1,pl2) : 
    vvode={ 
        ("камень", "ножницы"): "Игрок 1 победил",
        ("ножницы", "бумага"): "Игрок 1 победил",
        ("бумага", "камень"): "Игрок 1 победил",
        ("ножницы", "камень"): "Игрок 2 победил",
        ("бумага", "ножницы"): "Игрок 2 победил",
        ("камень", "бумага"): "Игрок 2 победил",
    } 
     
    if pl1 == pl2 : 
        return "Ничья"  
    else : 
        return vvode.get((pl1,pl2),"Что то пошло не так ")

win= the_best_game(pl1,pl2) 
print(win) 
