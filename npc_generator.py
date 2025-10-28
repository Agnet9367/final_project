import time; import random; import math

print("--NPC Generator--")

attributes = ["Empathy", "Courage", "Charisma", "Honesty", "Integrity", "Patience", "Creativity", "Compassion", "Resilience", "Loyalty", "Optimism", "Humility", "Discipline", "Confidence", "Adaptability", "Assertiveness", "Determination", "Open-mindedness", "Generosity", "Humor", "Ambition", "Self-awareness", "Kindness", "Wisdom", "Tactfulness", "Diligence", "Gratitude", "Initiative", "Flexibility", "Reliability", "Altruism", "Perseverance", "Curiosity", "Forgiveness", "Modesty", "Resourcefulness", "Sensitivity", "Enthusiasm", "Focus", "Courageousness", "Thoughtfulness", "Punctuality", "Observant", "Visionary", "Respectfulness", "Tenacity", "Passion", "Self-discipline", "Fairness", "Determinedness"]
names = ["Liam", "Olivia", "Noah", "Emma", "Oliver", "Ava", "Elijah", "Sophia", "William", "Isabella", "James", "Mia", "Benjamin", "Charlotte", "Lucas", "Amelia", "Henry", "Harper", "Alexander", "Evelyn", "Mason", "Abigail", "Michael", "Emily", "Daniel"]
jobs = ["Software Engineer", "Data Scientist", "Web Developer", "Graphic Designer", "Project Manager", "Marketing Specialist", "Financial Analyst", "Mechanical Engineer", "Electrician", "Plumber", "Teacher", "Nurse", "Doctor", "Pharmacist", "Lawyer", "Architect", "Civil Engineer", "UX/UI Designer", "Cybersecurity Analyst", "Accountant", "Product Manager", "Content Writer", "Sales Representative", "Human Resources Manager", "Customer Support Specialist"]
heights_feet = [4.8, 5.0, 5.1, 5.3, 5.5, 5.6, 5.7, 5.8, 5.9, 6.0, 6.1, 6.3, 6.5]
talents = ["Singing", "Dancing", "Painting", "Writing", "Cooking", "Acting", "Public speaking", "Playing guitar", "Playing piano", "Photography", "Drawing", "Storytelling", "Problem solving", "Leadership", "Sports", "Gardening", "Designing", "Coding", "Teaching", "Negotiating", "Crafting", "Comedy", "Inventing", "Persuasion", "Memorization"]
languages = ["English", "Spanish", "French", "German", "Mandarin", "Hindi", "Arabic", "Russian", "Portuguese", "Japanese", "Korean", "Italian", "Turkish", "Swahili", "Bengali", "Urdu", "Persian", "Vietnamese", "Thai", "Dutch"]

numb_of_npc = int(input("How many NPCs do you want (1 - 10): "))

if numb_of_npc <= 10:
    for i in range(numb_of_npc): 
        time.sleep(0.2)

        print(f"NPC #{i+1}");time.sleep(0.2)
        
        print("Name: ",random.choice(names));time.sleep(0.2)

        print("Language: ",random.choice(languages));time.sleep(0.2)

        print(f"Height: {random.choice(heights_feet)} feet");time.sleep(0.2)

        print("Talent: ", random.choice(talents));time.sleep(0.2)

        print("Job: ",random.choice(jobs));time.sleep(0.2)

        print("Sigma: ",random.choice([True, False]));time.sleep(0.2)

        print("Atribute: ",random.choice(attributes));time.sleep(0.2)
        print("Atribute: ",random.choice(attributes));time.sleep(0.2)
        print("Atribute: ",random.choice(attributes));time.sleep(0.2)
        print("Atribute: ",random.choice(attributes));time.sleep(0.2)
        print("Atribute: ",random.choice(attributes));time.sleep(0.2)

        print(" ");time.sleep(1)
else:
    print("An error occured try again later")

