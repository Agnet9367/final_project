# 🤖 NPC Generator  

## 📖 Overview 
The **NPC Generator** is a simple Python script that creates a random non-player characters (NPC's) for games, projects or other situations! Each NPC is assigned a random **name**, **height**, **age**, **job status**, and thre most important stats: **speed**, **power**, and **defene**.

## 📚 Libraries Used  
- import time
- import random

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
lists of options for NPC attributes:

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



