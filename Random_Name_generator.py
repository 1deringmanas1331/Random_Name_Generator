import random
# We enter the names in a list 
# Enter the start and ending words
syllables = ["ra", "mi", "do", "so", "la", "ti", "di", "ze", "fi", "po", "ni", "ko"]
endings = ["an", "el", "or", "ius", "ious", "ara", "ella", "inda", "oria", "ette"]

def generate_random_name():
    name_length = random.randint(2, 3)  

    name = ""
    for _ in range(name_length):
        name += random.choice(syllables)
    name += random.choice(endings)

    return name.capitalize()

if __name__ == "__main__":
    num_names = int(input("Enter the number of random names to generate: "))
    
    random_names = [generate_random_name() for _ in range(num_names)]

    print("Random Names:")
    for i, name in enumerate(random_names, 1):
        print(f"{i}. {name}")
