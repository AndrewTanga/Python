leaked_psw = ["123", "456", "789", 123, 456,789]
common_psw = ["abc", "def", "456", "kab", "car", 123]

def get_cracked_passwords(leaked_arr, common_arr):
    print(f'leaked ONE = ${leaked_arr}')
    print(f'common ONE = ${common_arr}')
    cracked_array = []

    for element in leaked_arr:
        print(element)
        if element in common_arr:
            print(f"Matched value = {element}")
            cracked_array.append(element)
            print(cracked_array)
    return cracked_array

cracked_psw = get_cracked_passwords(leaked_psw, common_psw)
print(f"Final array =  {cracked_psw}")