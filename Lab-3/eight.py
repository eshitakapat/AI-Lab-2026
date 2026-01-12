
# wap to check whether a key exists in a dictionary or not

my_dict = {'a': 1, 'b': 2, 'c': 3}

key_to_check = 'b'

if key_to_check in my_dict:
    print(f"Key '{key_to_check}' exists in the dictionary.")
else:
    print(f"Key '{key_to_check}' does not exist in the dictionary.")

key_to_check = 'd'

if key_to_check in my_dict:
    print(f"Key '{key_to_check}' exists in the dictionary.")
else:
    print(f"Key '{key_to_check}' does not exist in the dictionary.")
