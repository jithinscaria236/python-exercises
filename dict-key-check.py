# Program to print and check dictionary key
# Initializing dictionary for storing fruit prices
fruit_dict = {"apple": 170, "pineapple": 150, "banana": 45}
# Accessing dictionary key value
try:
    print("_________________________________________________")
    print('{:32s} {:35s} '.format("Fruit Name","Price"))
    print("_________________________________________________")
    for key, value in fruit_dict.items():
        print('{:32s} {:5d} '.format(key,value))
        print("_________________________________________________")
    print("Enter a key for checking inside the dictionary")
    input_dict_key = input()
    flag = 0
    for key, value in fruit_dict.items():
        if key == input_dict_key:
            flag = 1
            break
    if flag == 1:
        print(f"{input_dict_key} found inside the dictionary")
    else:
        print(f"{input_dict_key} not found inside the dictionary")
except Exception as error:
    print(f"Error occured inside the program\n:Please find the error details:{error}")