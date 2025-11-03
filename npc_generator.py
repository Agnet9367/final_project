# Import necessary modules
#'time' is used to add small delays for realism
#'random' is ysed to generate random values for NPC traits
import time; import random

print("--NPC Generator--")

# List of possible NPC names
names = [
"Liam", "Olivia", "Noah", "Emma", "Oliver", "Ava", "Elijah", "Sophia", 
"William", "Isabella", "James", "Mia", "Benjamin", "Charlotte", "Lucas", 
"Amelia", "Henry", "Harper", "Alexander", "Evelyn", "Mason", "Abigail", 
"Michael", "Emily", "Daniel"
]

# List of possible NPC heights (in feet)
heights_feet = [4.8, 5.0, 5.1, 5.3, 5.5, 5.6, 5.7, 5.8, 5.9, 6.0, 6.1, 6.3, 6.5]

# Ask the user how many NPCs to generate
numb_of_npc = int(input("How many NPCs do you want? "))

print(" ")

# Loop to generate the requested number of NPCs
for i in range(numb_of_npc): 
        time.sleep(0.25)

# Print the NPC's number 
        print(f"NPC #{i+1}");time.sleep(0.1)   

# Randomly select and print name, height, job status, and age
        print("Name: ",random.choice(names));time.sleep(0.1)
        print(f"Height: {random.choice(heights_feet)} feet");time.sleep(0.1)
        print("Has Job: ", bool(random.randint(0,2)));time.sleep(0.1)
        print("Age: ",random.randint(18, 50));time.sleep(0.1)
        print(" ")

# Randomly generate and print NPC stats: speed, power and defense
        print(f"Speed:{(round(random.uniform(0.0, 1.0) * 100)) / 100} ",);time.sleep(0.1)
        print(f"Power:{(round(random.uniform(0.0, 1.0) * 100)) / 100} ",);time.sleep(0.1)
        print(f"Defense:{(round(random.uniform(0.0, 1.0) * 100)) / 100} ",);time.sleep(0.1)

# Separator for readibility
        print("- - - - - - - - -");time.sleep(0.25)

# End message after all of the the NPCs are generated
print("All of your NPCs have been generated!")