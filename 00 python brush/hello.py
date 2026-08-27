# Hello World program in Python
print("Hello, Python")

#variables
name= "John"
number= 10
is_student= True
float_number=3.14

#comparison
print(number > 5)  # True
print(name == "John")  # True
print(is_student and (number < 20))  # True
print(float_number != 3.14)  # False

#logical operators
print(True and False)  # False
print(True or False)  # True
print(not True)  # False

#arithmetic operations
print(5/2)  # 2.5
print(5//2)  # 2
print(10 % 3)   # 1   modulus (remainder)
print(10 ** 2)  # 100 exponent (power)

#String operations
greeting = "Hello"
name = "Alice"
print(greeting + " " + name)  # Concatenation: Hello Alice
print(greeting * 3)  # Repetition: HelloHelloHello
print(greeting[0])  # Indexing: H
print(len(greeting))  # Length: 5
print(greeting[::-1])  # Slicing: olleH (reversed string)
print("   Hello   ".strip())  # Stripping whitespace: Hello
print("Hello World".split())  # Splitting: ['Hello', 'World']
print("-".join(["Hello", "World"]))  # Joining: Hello-World
print("Hello World".replace("World", "Python"))  # Replacing: Hello Python

# if statement
age= 18
if age>=18:
    print("You are an adult.")
elif age>=13:
    print("You are a teenager.")
else:
    print("You are a child.")

#loops
#for loop

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit) # Output: apple banana cherry

for i in range(5):
    print(i)  # Output: 0 1 2 3 4

for i, fruit in enumerate(fruits):
    print(i, fruits[i])  # Output: 0 apple, 1 banana, 2 cherry

#while loop
count = 0
while count < 5:
    print("Count is ",count)
    count += 1  # Increment count by 1

for n in range(10):
    if n == 5:
        break  # Exit the loop when n is 5
    if n%2==0:
        continue  # Skip even numbers
    print(n)  # Output: 1 3

#Data structures
#List
my_list = [1, 2, 3, 4, 5]
print(my_list[0])  # Accessing first element: 1
my_list.append(6)  # Adding an element: [1, 2, 3, 4, 5, 6]
my_list.remove(3)  #Removing an element: [1, 2, 4, 5, 6]
print(my_list)  # Output: [1, 2, 4, 5, 6]
print(len(my_list))  # Length of the list: 5    

#Tuple
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple[0])  # Accessing first element: 1
print(len(my_tuple))  # Length of the tuple: 5
#TO SHOW TUPLES ARE IMMUTABLE
try:
    my_tuple[0] = 10  # This will raise an error
except TypeError as e:
    print("Error:", e)  # Output: Error: 'tuple' object does not support item assignment

#Set
my_set = {1, 2, 3, 4, 5}

my_set.add(6)  # Adding an element: {1, 2, 3, 4, 5, 6}
my_set.remove(3)  # Removing an element: {1, 2, 4, 5, 6}
print(my_set)  # Output: {1, 2, 4, 5, 6}
print(len(my_set))  # Length of the set: 5

my_set2 = {4, 5, 6, 7, 8}
print(my_set.union(my_set2))  # Union: {1, 2, 3, 4, 5, 6, 7, 8}
print(my_set.intersection(my_set2))  # Intersection: {4, 5}
#set difference is the elements that are in one set but not in the other 
print(my_set.difference(my_set2))  # Difference: {1, 2, 3}
   
#dictionaries
my_dict = {"name": "Alice",
            "age": 25,
              "city": ["New York", "Los Angeles", "Chicago"]
              }

print(my_dict["name"])  # Accessing value by key: Alice
my_dict["age"] = 26  # Updating value by key
my_dict["country"] = "USA"  # Adding a new key-value pair
print(my_dict)  # Output: {'name': 'Alice', 'age': 26, 'city': 'New York', 'country': 'USA'}
print(len(my_dict))  # Length of the dictionary: 4
print(my_dict.keys())  # Getting all keys: dict_keys(['name', 'age', 'city', 'country'])
print(my_dict.values())  # Getting all values: dict_values(['Alice', 26, ['New York', 'Los Angeles', 'Chicago'], 'USA'])
print(my_dict.items())  # Getting all key-value pairs: dict_items([('name', 'Alice'), ('age', 26), ('city', ['New York', 'Los Angeles', 'Chicago']), ('country', 'USA')])

for key,value in my_dict.items():
    print(key,value)  # Output: name Alice, age 26, city ['New York', 'Los Angeles', 'Chicago'], country USA


#functions
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

print(greet("Alice"))
print(greet("Bob", "Hi"))

try:
    value = int(input("Enter a number: "))
    result = 10 / value
    print(result)
except ValueError:
    print("That wasn't a valid number.")
except ZeroDivisionError:
    print("Cannot divide by zero.")
finally:
    print("Done attempting the calculation.")


# TO DO LIST
tasks = []

while True:
    print("\n--- TO-DO LIST ---")
    print("1. View tasks")
    print("2. Add task")
    print("3. Remove task")
    print("4. Exit")
    
    choice = input("\nChoose an option (1-4): ")

    if choice == "1":
        if not tasks:
            print("\nYour list is currently empty.")
        else:
            print("\nYour Tasks:")
            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task}")

    elif choice == "2":
        new_task = input("\nEnter the task description: ").strip()
        if new_task:
            tasks.append(new_task)
            print(f"Added: '{new_task}'")
        else:
            print("Task cannot be blank!")

    elif choice == "3":
        if not tasks:
            print("\nNo tasks available to remove.")
            continue

        print("\nYour Tasks:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

        # try/except handles invalid user input safely
        try:
            task_num = int(input("\nEnter the number of the task to remove: "))
            removed_task = tasks.pop(task_num - 1)
            print(f"Removed: '{removed_task}'")
            
        except ValueError:
            print("Invalid entry! You must type a whole number.")
            
        except IndexError:
            print("That task number does not exist on your list.")
            
        finally:
            print("Removal attempt finished.")

    elif choice == "4":
        print("\nGoodbye!")
        break

    else:
        print("Invalid choice! Please choose 1, 2, 3, or 4.")



    