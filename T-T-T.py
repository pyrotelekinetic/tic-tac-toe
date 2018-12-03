marks = {        #default values
    'a1': "-",
    'b1': "-",
    'c1': "-",
    'a2': "-",
    'b2': "-",
    'c2': "-",
    'a3': "-",
    'b3': "-",
    'c3': "-"
    }

def plr():
    """
        called for the player's turn
    """
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
    elif where in ("q", "quit", "exit"):
        global done
        done = True
    else:
        print("Invalid coordinates.")

def bot():    #in progress - this is a placeholder
    """
        called for bot's turn
    """
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
    print("bot's turn!")

def over():    #in progress - this is a placeholder
    """
        called to calculate whether the game has been won
    """
    print("has anybody won?")
won = ""
done = False
while not done:
    plr()
    bot()
    over()
    print(won)
