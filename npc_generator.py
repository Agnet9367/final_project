import time; import random

print("--NPC Generator--")

names = ["Liam", "Olivia", "Noah", "Emma", "Oliver", "Ava", "Elijah", "Sophia", "William", "Isabella", "James", "Mia", "Benjamin", "Charlotte", "Lucas", "Amelia", "Henry", "Harper", "Alexander", "Evelyn", "Mason", "Abigail", "Michael", "Emily", "Daniel"]
heights_feet = [4.8, 5.0, 5.1, 5.3, 5.5, 5.6, 5.7, 5.8, 5.9, 6.0, 6.1, 6.3, 6.5]

numb_of_npc = int(input("How many NPCs do you want? "))

print(" ")

for i in range(numb_of_npc): 
        time.sleep(0.25)

        print(f"NPC #{i+1}");time.sleep(0.1)        
        print("Name: ",random.choice(names));time.sleep(0.1)
        print(f"Height: {random.choice(heights_feet)} feet");time.sleep(0.1)
        print("Has Job: ", bool(random.randint(0,2)));time.sleep(0.1)
        print("Age: ",random.randint(18, 50));print(" ");time.sleep(0.1)

        print(f"Speed:{(round(random.uniform(0.0, 1.0) * 100)) / 100} ",);time.sleep(0.1)
        print(f"Power:{(round(random.uniform(0.0, 1.0) * 100)) / 100} ",);time.sleep(0.1)
        print(f"Defense:{(round(random.uniform(0.0, 1.0) * 100)) / 100} ",);time.sleep(0.1)

        print("- - - - - - - - -");time.sleep(0.25)

print("All of your NPC's have been generated!")
