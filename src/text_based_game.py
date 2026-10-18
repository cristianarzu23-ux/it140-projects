"""Project Two starter for the student's text-based adventure game."""

# TODO: Add the full-name comment required by Project Two directions.
Hogwarts Heist!

def show_instructions():
    print("WELCOME TO HOGWARTS HEIST!")
    print("Objective: ")
    print("Collecte 6 horcruxes to help Harry Potter defeat Lord Voldemort.")
    print("Find the horcruxes before he finds you!")
    print("You will be able to move through Hogwarts School with the following commands: ")
    print('go north', 'go south', 'go east', 'go west')
    print("To collect items you must type: get item")
    print("If you wish to exit game type: exit.")
def show_status(current_room, inventory, rooms):
    print(f"\nYou are in: {current_room}")
    print(f"Inventory: {inventory}")
    if "item" in room in rooms[current_room]:
        print(f"You spot something glowing: {rooms[current_room]['item']}")
    print("-" * 40)
def main():
    rooms = {
        "The Great Hall": {"west": "Hogwarts Library", "south": "Gryffindor Common Room"}, 
        "Hogwarts Library": {"east": "The Great Hall", "north": "The Prefects' Bathroom", "south": "The Headmasters' Ofice", "item": "Tom Riddles' Diary"},
        "The Prefects' Bathroom": {"south": "Hogwarts Library", "item": "Helga Hufflepuff's Cup"},
        "The Headmasters' Office": {"north": "Hogwarts Library", "east": "Slytherin Common Room", "item": "Marvolo Gaunts' Ring"},
        "Gryffindor Common Room": {"north": "The Great Hall", "east": "Room of Requirement", "Item": "Rowena Ravenclaw Diadem"},
        "Slytherin Common Room": {"west": "The Headmasters' Office", "east": "Room of Requirement", "item": "Salazar Slytherins Locket"},
        "Room of Requirement": {"west": "Slytherin Common Room", "north": "Gryffindor Common Room", "south": "The Chamber of Secrets", "item": "Nagini the snake"},
        "The Chamber of Secretes": {"north": "Room of Requirement"},
        }
    
    current_room = "The Great Hall"

    inventory = []
    total_horcruxes = 6

    show_instructions()

    while true:
        show_status(current_room, inventory, rooms)

        user_input = input("What would you like to do? ").strip()
        input_parts = user_input.split(maxsplit=1)
        if not input_parts:
            print("Please enter a command.")
            continue

        action = input_parts[0].title()
        target = input_parts[1].title() if len(input_parts) > 1 else ""

        if action == "Exit":
            print("\nThanks for playing Hogwarts Heist!")
            break
        elif action == "Go":
            if target in rooms[current_room]:
                current_room = rooms[current_room][target]

                if current_room == "The Chamber of Secrets":
                    if len(inventory) == 6:
                        print("You collected all the horcruxes and helped Harry defeat Lord Voldemort...")
                        print("You Win!!!")
                    else:
                        print("AVADA KEDAVRA! Voldemort has defeated you!")
                        print("Game Over")
                    break    
            else:
                print(f"You Can't go {target} from here.")
        elif action == "get":
            if ("item" in rooms[current_room] and target == rooms[current_room] ["item"].title()):
                collected_item = rooms[current_room].pop("item")
                inventory.append(collected_item)
                print(f"Succesfully collected {collected_item}!")
            else:
                print(f"Can't get '{target}' here.")
        else:
            print("Invaid input. Type 'go [direction]' or 'get [item]'.")
if __name__ == "__main__":
    main()
