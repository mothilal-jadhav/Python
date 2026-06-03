class Cat:
    def __init__(self, name, color, age):
        self.name = name
        self.color = color
        self.age = age

    def meow(self):
        print(f"{self.name} says: Meow!")

cat1 = Cat("Whiskers", "black", 3)
cat2 = Cat("Mittens", "white", 5)
cat3 = Cat("Shadow", "gray", 2)
cat4 = Cat("Luna", "orange", 4)

cat1.meow()
cat2.meow()
cat3.meow()
cat4.meow()

# function to display oldest cat
def oldest(*args):
    oldest_cat = max(args, key=lambda cat: cat.age)
    return f"The oldest cat is {oldest_cat.name} who is {oldest_cat.age} years old."

print(oldest(cat1, cat2, cat3, cat4))