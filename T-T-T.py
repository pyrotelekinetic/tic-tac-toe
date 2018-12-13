marks = {        #default values
    'a1': "-",
    'a2': "-",
    'a3': "-",
    'b1': "-",
    'b2': "-",
    'b3': "-",
    'c1': "-",
    'c2': "-",
    'c3': "-"
    }

def plr():
    """
        called for the player's turn
    """
    print("Your Turn!")
    print("""
   a     b     c
      |     |
1  {a1}  |  {b1}  |  {c1}
 _____|_____|_____
      |     |
2  {a2}  |  {b2}  |  {c2}
 _____|_____|_____
      |     |
3  {a3}  |  {b3}  |  {c3}
      |     |
""".format(**marks))
    turn = True
    while turn:
        where = input("Where?\n> ")
        if where in marks and marks[where] == "-":
            marks[where] = "X"
            print("""
   a     b     c
      |     |
1  {a1}  |  {b1}  |  {c1}
 _____|_____|_____
      |     |
2  {a2}  |  {b2}  |  {c2}
 _____|_____|_____
      |     |
3  {a3}  |  {b3}  |  {c3}
      |     |
""".format(**marks))
            turn = False
        elif where in ("q", "quit", "exit"):
            global done
            done = True
            turn = False
        else:
            print("Invalid coordinates.")

def bot():    #in progress - this is a placeholder
    """
        called for bot's turn
    """
    print("bot's turn!")
    for x in marks:
        if marks[x] == "-":
            marks[x] = "O"
            break

def over():
    """
        called to check whether the game has been won
    """
    print("has anybody won?")
    top = (marks['a1'], marks['b1'], marks['c1'])
    mid = (marks['a2'], marks['b2'], marks['c2'])
    low = (marks['a3'], marks['b3'], marks['c3'])
    if top == "X":
        print("You Won!")
        global done
        done = True
#    if marks['a1'] == marks['a2'] and marks['a1'] == marks['a3'] and not marks['a1'] == "-":
#        if marks['a1'] == "X":
#            print("You Won!")
#            global done
#            done = True
#        elif marks['a1'] == "O":
#            print("Bot Won!")
#            done = True

won = ""
done = False

while not done:
    plr()
    bot()
    over()
print("""
   a     b     c
      |     |
1  {a1}  |  {b1}  |  {c1}
 _____|_____|_____
      |     |
2  {a2}  |  {b2}  |  {c2}
 _____|_____|_____
      |     |
3  {a3}  |  {b3}  |  {c3}
      |     |
""".format(**marks))
