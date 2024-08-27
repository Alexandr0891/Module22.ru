# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


##############################
#  module_2_2.py
#Операторы if, elif, else."


first=int(input('Введите первое число : '))
second=int(input('Введите второе число : '))
third=int(input('Введите третье число : '))
if first==second==third:
    print(3)
elif first!=second==third:
    print(2)
elif first==second!=third:
     print(2)
elif first==third!=second :
     print(2)
elif first!=second!=third:
    print(0)
elif first!=third!=second:
    print(0)