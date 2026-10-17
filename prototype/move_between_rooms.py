"""Module Six Milestone starter for the simplified movement prototype."""

# A dictionary for the simplified dragon text game.
# The dictionary links a room to other rooms.

rooms = {
    'Great Hall': {'South': 'Bedroom'},
    'Bedroom': {'North': 'Great Hall', 'East': 'Cellar'},
    'Cellar': {'West': 'Bedroom'}
}

current_room = "Great Hall"

while True:
    print(f"\nYou are in the {current_room}.")

    user_input = input("Enter your move: ").strip().split()

    if not user_input:
        print("Please enter a move.")
        continue
    user_move = user_input[0].lower()
    if user_move == "exit":
        print("Thank you for playing!")
        break
        
    if user_move == "go" and len(user_input) > 1:
        direction = user_input[1].title()
    elif
        direction = user_input[0].title()
        
    elif user_move == "go" and len(user_input) > 1:
        direction = user_input[1].title()
        if direction in rooms[current_room]:
            current_room = rooms[current_room][direction]
        else:
            print("You cannot go {direction}!")
    else:
         print("Invalid input! Try 'go [Direction]' or 'exit'.")

        
