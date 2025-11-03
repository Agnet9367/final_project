# 🤖 NPC Generator  

## 📖 Overview 
The **NPC Generator** is a simple Python script that creates a random non player characters (NPCs) for games,  projects or other situations. Each one of the NPCs is generated with a random combination of attributes, including **name**, **height**, **age**, **job status**, and three main stats: **speed**, **power** and **defense**. This script also uses the `time` module to make small delays between each printed line, giving the output a more pleasant feel as the NPCs appear one by one. This project is beginner friendly and shows important programming concepts such as lists, loops, user input and random. The NPC Generator is also really easily extendable. Users can add more features, like **genders**, **skills**, or **inventory items**, to make the generated characters even more detailed. This makes it perfect for game developers and writers who need a fast way to create a lot of different characters.

## 📚 Modules
This code uses 2 modules:
- `import time`
- `import random`

## 🌟 Code Highlights
This is a key part of the code that generates each NPC's random traits:
```python
for i in range(numb_of_npc): 
    time.sleep(0.25)
    print(f"NPC #{i+1}")
    print("Name:", random.choice(names))
    print(f"Height: {random.choice(heights_feet)} feet")
    print("Has Job:", bool(random.randint(0,2)))
    print("Age:", random.randint(18, 50))
    print(f"Speed: {(round(random.uniform(0.0, 1.0) * 100)) / 100}")
    print(f"Power: {(round(random.uniform(0.0, 1.0) * 100)) / 100}")
    print(f"Defense: {(round(random.uniform(0.0, 1.0) * 100)) / 100}")
```

## 🗃️ Variables
This project uses variables (lists of options) for NPC names and heights:
```python
names = ["Liam", "Olivia", "Noah", "Emma", "Oliver", "Ava", "Elijah", "Sophia", "William", "Isabella", "James", "Mia", "Benjamin", "Charlotte", "Lucas", "Amelia", "Henry", "Harper", "Alexander", "Evelyn", "Mason", "Abigail", "Michael", "Emily", "Daniel"]
heights_feet = [4.8, 5.0, 5.1, 5.3, 5.5, 5.6, 5.7, 5.8, 5.9, 6.0, 6.1, 6.3, 6.5]
```

## ▶️ Usage
Enter the number of NPC's you want when prompted. The program will then display each NPC's details with a short delay for readability.

## ⌨️ Example Output
```python
--NPC Generator--
How many NPCs do you want? 2

NPC #1
Name: Olivia
Height: 5.8 feet
Has Job: True
Age: 31
Speed: 0.84
Power: 0.63
Defense: 0.41
- - - - - - - - -

NPC #2
Name: Liam
Height: 6.0 feet
Has Job: False
Age: 26
Speed: 0.57
Power: 0.77
Defense: 0.69
- - - - - - - - -

All of your NPCs have been generated!
```

## 👤 Author 
**Arsen Havur**

GitHub: @Agnet9367

Email: arsenhavyr@gmail.com



