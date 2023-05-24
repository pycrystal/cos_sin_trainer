import random 

tasks = ["sin 0", "sin 30", "sin 45", "sin 60", "sin 90", "cos 0", "cos 30", "cos 45", "cos 60", "cos 90", "tg 0", "tg 30", "tg 45", "tg 60", "tg 90", "ctg 0", "ctg 30", "ctg 45", "ctg 60", "ctg 90"]

mark = 0

user_repeats = int(input("Введите кол-во вопросов: "))




for i in range(user_repeats):
    task = random.choice(tasks)
    user_input = input(f"{task} -- ")

    if task == "sin 0":
        if user_input == "0":
            mark = mark + 1
            print("Верно")
        elif user_input == "ex":
            break
        elif user_input != "0":
            print("Не верно, правильный ответ - 0")
    
    if task == "sin 30":
        if user_input == "1/2":
            mark = mark + 1
            print("Верно")
        elif user_input == "ex":
            break
        elif user_input != "1/2":
            print("Не верно, правильный ответ - 1/2")

    if task == "sin 45":
        if user_input == "√2/2":
            mark = mark + 1
            print("Верно")
        elif user_input == "ex":
            break
        elif user_input != "√2/2":
            print("Не верно, правильный ответ - √2/2")     

    if task == "sin 60":
        if user_input == "√3/2":
            mark = mark + 1
            print("Верно")
        elif user_input == "ex":
            break
        elif user_input != "√3/2":
            print("Не верно, правильный ответ - √3/2")
    
    if task == "sin 90":
        if user_input == "1":
            mark = mark + 1
            print("Верно")
        elif user_input == "ex":
            break
        elif user_input != "1":
            print("Не верно, правильный ответ - 1")

    if task == "cos 0":
        if user_input == "1":
            mark = mark + 1
            print("Верно")
        elif user_input == "ex":
            break
        elif user_input != "1":
            print("Не верно, правильный ответ - 1") 

    if task == "cos 30":
        if user_input == "√3/2":
            mark = mark + 1
            print("Верно")
        elif user_input == "ex":
            break
        elif user_input != "√3/2":
            print("Не верно, правильный ответ - √3/2")
    
    if task == "cos 45":
        if user_input == "√2/2":
            mark = mark + 1
            print("Верно")
        elif user_input == "ex":
            break
        elif user_input != "√2/2":
            print("Не верно, правильный ответ - √2/2")

    if task == "cos 60":
        if user_input == "1/2":
            mark = mark + 1
            print("Верно")
        elif user_input == "ex":
            break
        elif user_input != "1/2":
            print("Не верно, правильный ответ - 1/2")     

    if task == "cos 90":
        if user_input == "0":
            mark = mark + 1
            print("Верно")
        elif user_input == "ex":
            break
        elif user_input != "0":
            print("Не верно, правильный ответ - 0")
    
    if task == "tg 0":
        if user_input == "0":
            mark = mark + 1
            print("Верно")
        elif user_input == "ex":
            break
        elif user_input != "0":
            print("Не верно, правильный ответ - 0")

    if task == "tg 30":
        if user_input == "√3/3":
            mark = mark + 1
            print("Верно")
        elif user_input == "ex":
            break
        elif user_input != "√3/3":
            print("Не верно, правильный ответ - √3/3")

    if task == "tg 45":
        if user_input == "1":
            mark = mark + 1
            print("Верно")
        elif user_input == "ex":
            break
        elif user_input != "1":
            print("Не верно, правильный ответ - 1")

    if task == "tg 60":
        if user_input == "√3":
            mark = mark + 1
            print("Верно")
        elif user_input == "ex":
            break
        elif user_input != "√3":
            print("Не верно, правильный ответ - √3")     

    if task == "tg 90":
        if user_input == "-":
            mark = mark + 1
            print("Верно")
        elif user_input == "ex":
            break
        elif user_input != "-":
            print("Не верно, правильный ответ - нет(-)")  

    if task == "ctg 0":
        if user_input == "-":
            mark = mark + 1
            print("Верно")
        elif user_input == "ex":
            break
        elif user_input != "-":
            print("Не верно, правильный ответ - нет(-)")

    if task == "ctg 30":
        if user_input == "√3":
            mark = mark + 1
            print("Верно")
        elif user_input == "ex":
            break
        elif user_input != "√3":
            print("Не верно, правильный ответ - √3")

    if task == "ctg 45":
        if user_input == "1":
            mark = mark + 1
            print("Верно")
        elif user_input == "ex":
            break    
        elif user_input != "1":
            print("Не верно, правильный ответ - 1")

    if task == "ctg 60":
        if user_input == "√3/3":
            mark = mark + 1
            print("Верно")
        elif user_input == "ex":
            break
        elif user_input != "√3/3":
            print("Не верно, правильный ответ - √3/3")     

    if task == "ctg 90":
        if user_input == "0":
            mark = mark + 1
            print("Верно")
        elif user_input == "ex":
            break    
        elif user_input != "0":
            print("Не верно, правильный ответ - 0")
        

    

    
print(f"Вы набрали {mark} из {user_repeats}")            