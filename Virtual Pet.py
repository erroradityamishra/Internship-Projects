import random
import time

# Function to initialize a new pet
def create_pet():
    """Initialize a new pet with default attributes and custom name."""
    name = input("Enter your pet's name: ")
    return {"name": name, "happiness": 50, "hunger": 50, "health": 50}

# Function to display the main menu
def display_menu():
    """Display the user menu and get the user's choice."""
    print("\nMenu Options:")
    print("1. Feed the pet")
    print("2. Play with the pet")
    print("3. Give the pet a toy")
    print("4. Give the pet medicine")
    print("5. Check pet's status")
    print("6. Switch pet")
    print("7. Quit")
    return input("Choose an option (1-7): ")

# Function to feed the pet
def feed_pet(pet):
    """Feed the pet, decreasing hunger and slightly reducing happiness."""
    pet["hunger"] = max(pet["hunger"] - 20, 0)  # Decrease hunger by 20, min is 0
    pet["happiness"] = max(pet["happiness"] - 5, 0)  # Decrease happiness by 5
    print(f"You fed {pet['name']}! Hunger decreased.")

# Function to play with the pet
def play_with_pet(pet):
    """Play with the pet, increasing happiness and slightly increasing hunger."""
    pet["happiness"] = min(pet["happiness"] + 20, 100)  # Increase happiness by 20, max is 100
    pet["hunger"] = min(pet["hunger"] + 5, 100)  # Increase hunger by 5
    print(f"You played with {pet['name']}! Happiness increased.")

# Function to give the pet a toy
def give_pet_toy(pet):
    """Give the pet a toy, which greatly increases happiness."""
    pet["happiness"] = min(pet["happiness"] + 30, 100)  # Increase happiness by 30
    print(f"{pet['name']} loves the new toy! Happiness greatly increased.")

# Function to give the pet medicine
def give_pet_medicine(pet):
    """Give the pet medicine, which restores health and decreases hunger."""
    pet["health"] = min(pet["health"] + 20, 100)  # Increase health by 20, max is 100
    pet["hunger"] = min(pet["hunger"] + 10, 100)  # Increase hunger by 10
    print(f"{pet['name']} is feeling better after taking the medicine.")

# Function to display pet's status
def check_status(pet):
    """Display the current status of the pet."""
    print(f"\n{pet['name']}'s Status:")
    print(f"Happiness: {pet['happiness']}")
    print(f"Hunger: {pet['hunger']}")
    print(f"Health: {pet['health']}")

# Function to apply automatic changes over time
def apply_automatic_changes(pet):
    """Increase hunger and decrease happiness to simulate passage of time."""
    pet["hunger"] = min(pet["hunger"] + 5, 100)  # Increase hunger by 5
    pet["happiness"] = max(pet["happiness"] - 5, 0)  # Decrease happiness by 5

# Function to handle random events
def random_event(pet):
    """Simulate random events that can affect the pet's attributes."""
    event = random.choice(["finds_snack", "gets_sick", "no_event"])
    if event == "finds_snack":
        pet["hunger"] = max(pet["hunger"] - 10, 0)  # Decrease hunger if snack is found
        print(f"Great news! {pet['name']} found a snack and isn't as hungry now.")
    elif event == "gets_sick":
        pet["health"] = max(pet["health"] - 10, 0)  # Decrease health if pet gets sick
        pet["happiness"] = max(pet["happiness"] - 10, 0)  # Decrease happiness if sick
        print(f"Oh no! {pet['name']} got sick. Health and happiness decreased.")
    else:
        print("No random events happened this time.")

# Function to check game over conditions
def game_over(pet):
    """Check if the game is over due to extreme hunger or sadness."""
    if pet["hunger"] >= 100:
        print(f"\n{pet['name']} is too hungry! Game Over.")
        return True
    if pet["happiness"] <= 0:
        print(f"\n{pet['name']} is too sad! Game Over.")
        return True
    if pet["health"] <= 0:
        print(f"\n{pet['name']} is too unhealthy! Game Over.")
        return True
    return False

# Main function to manage the entire game
def main():
    """Main function to run the enhanced Virtual Pet Simulator."""
    pets = []  # List to store multiple pets
    number_of_pets = int(input("How many pets would you like to create? "))

    # Create multiple pets
    for _ in range(number_of_pets):
        pets.append(create_pet())

    current_pet = 0  # Start with the first pet

    while True:
        pet = pets[current_pet]  # Reference the current pet

        choice = display_menu()
        if choice == '1':
            feed_pet(pet)
        elif choice == '2':
            play_with_pet(pet)
        elif choice == '3':
            give_pet_toy(pet)
        elif choice == '4':
            give_pet_medicine(pet)
        elif choice == '5':
            check_status(pet)
        elif choice == '6':
            current_pet = (current_pet + 1) % len(pets)  # Switch to the next pet
            print(f"Switched to {pets[current_pet]['name']}!")
        elif choice == '7':
            print("Goodbye! Thank you for playing.")
            break
        else:
            print("Invalid choice! Please select from the options (1-7).")

        # Apply automatic changes and random events after each action
        apply_automatic_changes(pet)
        random_event(pet)

        # Check if the game is over for the current pet
        if game_over(pet):
            break

# Run the game
if __name__ == "__main__":
    main()
