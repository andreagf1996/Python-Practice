# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


#def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    #print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
#if __name__ == '__main__':
   # print_hi('PyCharm')
 
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
val = input("Enter your height in meters: ")
height = float(val)

value = input("Enter your weight in kg: ")
weight = float(value)
def bmi(height, weight):
    wt = weight/height**2
    if wt >= 30:
        return "obese"
    elif wt >= 25 and wt < 30:
        return "overweight"
    elif wt >= 18.5 and wt < 25:
        return "normal"
    return "underweight"

print(bmi(height, weight))