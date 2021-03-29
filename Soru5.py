# Input ile girilen bir cumledeki sayilarin ve harflerin miktarini hesaplayan bir fonksiyon yaziniz.
# Ornek input: hello world! 123
# Output:
# HARFLER: 10
# SAYILAR: 3

def num_letters_and_numbers():
    string = input('Enter a anything: ')
    letters = 0
    nums = 0
    for c in string:
        # check if the char is an alpha char or a digit
        if c.isalpha():
            letters += 1
        elif c.isdigit():
            nums += 1

    return f"""Number of letters in given string is : {letters}
Number of digits in given string is : {nums}
"""


print(num_letters_and_numbers())
