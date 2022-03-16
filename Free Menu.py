# Free menu coded by fastcode


def menu3():
    print("This is menu 3.")
    while True:
        input("Press any key to exit.")
        input()
        menu()




def menu2():
    print("This is menu 2.")
    while True:
        input("Press any key to exit.")
        input()
        menu()




def menu1():
    print("This is menu 1.")
    while True:
        input("Press any key to exit")
        input()
        menu()









def menu():
    print("Menu Name Here")
    print("""
    
    1 - Menu 1
    2 - Menu 2
    3 - Menu 3
    
    """)
    menu_options = input("> ")
    if menu_options == "1":
        menu1()
    elif menu_options == "2":
        menu2()
    elif menu_options == "3":
        menu3()
print(menu())