print("Hi, what is your name?")
name = input()
print(f"Hello {name}!")
print("How are you today?")
feeling = input()
if 'good' in feeling:
    print("I'm feeling good too")
else:
    print("Sorry to hear that")
print("How are you today?")
feeling = input()
if 'good' in feeling.lower():
    print("I'm feeling good too")
else:
    print("Sorry to hear that")
import random

print("What's your favorite color?")
favcolor = input()
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'purple']
print(f"You like {favcolor.lower()}? My facorite color is {random.choice(colors)}”)")
