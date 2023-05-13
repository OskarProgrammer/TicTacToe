import os as system
def wyswietlenie_listy(list):
    i=0
    print(1,2,3,sep=" ")
    for x in range(len(list)):
        i+=1
        for j in range(len(list[x])):
            if list[x][j]!= "O" and list[x][j]!="X":
                print("-",end=" ")
            elif list[x][j]=="O":
                print(list[x][j],end=" ")
            elif list[x][j]=="X":
                print(list[x][j],end=" ")
            
        print(i,end="\n")
def check(list,user_1,user_2,User_1,User_2):
    global wynik
    #pionowe
    for x in range(0,3):
        if list[0][x]==list[1][x] and list[0][x]==list[2][x]:
            if list [0][x]==user_1:
                system.system("cls")
                print(f"{User_1}, who had {user_1} won")
                wynik=1
            elif list [0][x]==user_2:
                system.system("cls")
                print(f"{User_2}, who had {user_2} won")
                wynik=1
    
    #poziome
    for x in range(0,3):
        if list[x][2]==list[x][1] and list[x][2]==list[x][0]:
            if list [x][2]==user_1:
                system.system("cls")
                print(f"{User_1}, who had {user_1} won")
                wynik=1
            elif list [x][2]==user_2:
                system.system("cls")
                print(f"{User_2}, who had {user_2} won")
                wynik=1 
    if list [0][0]==list[1][1] and list[0][0]==list[2][2]:
        if list [0][0]==user_1:
                system.system("cls")
                print(f"{User_1}, who had {user_1} won")
                wynik=1
        elif list [0][0]==user_2:
                system.system("cls")
                print(f"{User_2}, who had {user_2} won")
                wynik=1

    if list [0][2]==list[1][1] and list[0][2]==list[2][0]:
        if list [0][2]==user_1:
                system.system("cls")
                print(f"{User_1}, who had {user_1} won")
                wynik=1
        elif list [0][2]==user_2:
                system.system("cls")
                print(f"{User_2}, who had {user_2} won")
                wynik =1 
    

    # 1 2 3
    # 4 5 6
    # 7 8 9
    if list [0][0]!="A" and list[0][1]!="B" and list[0][2]!="C" and list[1][0]!="D" and list[1][1]!="E" and list[1][2]!="F" and list[2][0]!="G" and list[2][1]!="H" and list[2][2]!="I":
        system.system("cls")
        print("Draw")
        wynik=1
    
    

    
            
    
while True:     
    znaki=["O","X"]
    wymogi=[1,2,3]

    i=0
    positive=["yes","YES","Yes","Tak","TAK","tak"]
    list =[["A","B","C"],["D","E","F"],["G","H","I"]]
    user_2=""
    #settings
    system.system("cls")
    #instructions
    print("Tic Tac Toe")
    print("The easy game here is what you have to do:")
    print("You have to place the circles or cross on the 3x3")
    print("board. Who first collect 3 circles or crosses in a row or in a column")
    print("Give a name of User 1:",end=" ")
    User_1=input("")
    print("Give a name of User 2:",end=" ")
    User_2=input("")
    print(f"{User_1},do you want to be circle or cross? ",end=" ")
    user_1=input("")
    while user_1!="circle" and user_1!="cross":
        print(f"{User_1},do you want to be circle or cross? ",end=" ")
        user_1=input("")
    if user_1=="circle":
        user_1="O"
        user_2="X"
    elif user_1=="cross":
        user_1="X"
        user_2="O"
    system.system("cls")
    print(f"{User_1}: {user_1}")
    print(f"{User_2}: {user_2}")
    print("Here is the board to game:")
    wyswietlenie_listy(list)
    while True:
        wynik=0
        print(f"{User_1} your turn,  please give the coordinates of the table (x-row,y-column):",end="")
        lista=input("").split(" ")
        a=int(lista[0])
        b=int(lista[1])
        while (a not in wymogi)or (b not in wymogi):
            print(f"{User_1} your turn,  please give the coordinates of the table (x-row,y-column):",end="")
            lista=input("").split(" ")
            a=int(lista[0])
            b=int(lista[1])
        while list [a-1][b-1]=="O" or list [a-1][b-1]=="X":
            print("The place already taken:")
            lista=input("").split(" ")
            a=int(lista[0])
            b=int(lista[1])
        list[a-1][b-1]=user_1
        check(list,user_1,user_2,User_1,User_2)
        if wynik==1:
            break
        system.system("cls")
        wyswietlenie_listy(list)
        print(f"{User_2} your turn,  please give the coordinates of the table (x-row,y-column):",end="")
        lista=input("").split(" ")
        a=int(lista[0])
        b=int(lista[1])
        while (a not in wymogi)or (b not in wymogi):
            print(f"{User_2} your turn,  please give the coordinates of the table (x-row,y-column):",end="")
            lista=input("").split(" ")
            a=int(lista[0])
            b=int(lista[1])
        while list [a-1][b-1]=="O" or list [a-1][b-1]=="X":
            print("The place already taken:")
            lista=input("").split(" ")
            a=int(lista[0])
            b=int(lista[1])
        list[a-1][b-1]=user_2
        print(list[a-1][b-1])
        system.system("cls")
        wyswietlenie_listy(list)
        check(list,user_1,user_2,User_1,User_2)
        if wynik==1:
            break
    print("Do you want to play again? ")
    decyzja=input()
    if decyzja in positive:
        continue
    else:
        system.system("cls")
        print("Koniec gry")
        exit()

    
