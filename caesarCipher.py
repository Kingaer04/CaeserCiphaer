from string import ascii_lowercase


def  caeser(text:str, shift:int, option:str) -> str:
    current_text = ""
    if option == "decode":
            shift *= -1

    for char in text:
        if char in ascii_lowercase:
            current_position = ascii_lowercase.index(char)
            new_position  = current_position + shift
            new_character = ascii_lowercase[new_position % len(ascii_lowercase)]
            current_text += new_character
        elif char not in ascii_lowercase:
             current_text += char
    return f"The {option}d text is {current_text}"

while True:
    option = input("To 'encode' enter encode\tTo 'decode' enter decode:\n").lower()
    if (option == 'encode' or option == 'decode'):
        text = input('Type your message: \n').lower()
        shift = int(input('Type the shift number: \n'))
        print(caeser(text=text, shift=shift, option=option))
        repeat = input("\nType 'yes' if you want to go again. Otherwise type 'no':\n").lower()
        if repeat == 'no':
            print('Goodbye')
            break

    else:
        print("Wrong input") 
