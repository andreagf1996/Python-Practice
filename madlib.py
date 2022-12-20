# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


name = input("What's your name? ")
print(f"Hello, {name}. It's so exciting to meet you!")

mood = input("How're you today? ")

if mood.lower() == "good" or mood.lower() == "great" or mood.lower() == "happy" or mood.lower() == "fine" or mood.lower() == "terrific":
    print("Oh good! I'm so glad to hear that! Let's do a madlib to keep the good times rolling.")
else:
    print("Oh no! I'm sorry to hear that! Maybe a madlib will help. :)")

print("Ok, I'll ask you for a noun, verb, or adjective, and together we'll make a fun story.")

noun = input("Noun: ")
adj = input("Adjective: ")
adj2 = input("Adjective: ")
verb = input("Verb: ")
location = input("Location: ")
verb2 = input("Verb: ")

print(f"Once upon a time there lived a {noun}. They were very {adj}, but also very {adj2}. In the morning, {noun} decided to {verb} to the nearest {location}. Once there they {verb2} and {noun} lived happily ever after.")


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
