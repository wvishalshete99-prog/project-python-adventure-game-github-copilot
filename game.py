# Adventure Game Project - Text-based quest
# Using Python basics with GitHub Copilot

inventory = []  # list to store items

def start_game():
    print("\nWelcome, brave explorer!")
    name = input("What is your name? ")  # ask player name
    print(f"Hello {name}, your quest begins now...")

    choice = input("Do you want to explore the forest or enter the cave? (forest/cave): ").lower()

    if choice == "forest":
        forest_path()
    elif choice == "cave":
        cave_path()
    else:
        print("Invalid choice, try again.")
        start_game()

def forest_path():
    print("\nYou enter a dense forest. The air is thick and mysterious...")
    choice = input("Do you follow the river or climb a tree? (river/tree): ").lower()

    if choice == "river":
        print("You follow the river and discover a hidden path leading to the treasure!")
        inventory.append("golden key")
        win_game()
    elif choice == "tree":
        print("You climb the tree but slip and fall. Your adventure ends here.")
        lose_game()
    else:
        print("Invalid choice, try again.")
        forest_path()

def cave_path():
    print("\nYou step into a dark cave. It's cold and eerie...")
    choice = input("Do you light a torch or proceed in the dark? (torch/dark): ").lower()

    if choice == "torch":
        print("The torch reveals a hidden chest filled with treasure!")
        inventory.append("treasure chest")
        win_game()
    elif choice == "dark":
        print("You stumble in the dark and fall into a pit. Game over.")
        lose_game()
    else:
        print("Invalid choice, try again.")
        cave_path()

def win_game():
    print("\n🎉 Congratulations! You found the legendary treasure!")
    print(f"Your final inventory: {inventory}")

def lose_game():
    print("\n💀 You have failed your quest. Better luck next time!")

def play_game():
    while True:
        start_game()
        restart = input("\nDo you want to play again? (yes/no): ").lower()
        if restart != "yes":
            print("Thanks for playing! Goodbye.")
            break

# Run the game
if __name__ == "__main__":
    play_game()
