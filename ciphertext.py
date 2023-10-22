logo = """
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8
8b         ,adPPPPP88 8PP"""""""  `"Y8BA,  ,ADPPPPP88 88
"8A,   ,AA 88,    ,88 "8B,   ,AA AA    ]8I 88,    ,88 88
 `"YBBD8"' `"8BBDP"Y8  `"YBBD8"' `"YBBDP"' `"8BBDP"Y8 88
            88             88
           ""             88
                          88
 ,ADPPYBA, 88 8B,DPPYBA,  88,DPPYBA,   ,ADPPYBA, 8B,DPPYBA,
A8"     "" 88 88P'    "8A 88P'    "8A A8P_____88 88P'   "Y8
8B         88 88       D8 88       88 8PP""""""" 88
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88
              88
              88
"""
print(logo)

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','o','p','q','r','s','t','u','v','w','x','y','z']


def caesar(start_text,shift_number,cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_number *= -1
    for letter in start_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = position + shift_number
            end_text += alphabet[new_position]
        else:
            end_text += letter
    print(f"Here's the {cipher_direction} result: {end_text}")

should_end = False
while not should_end:
    direction = input("Type encode for encryption and decode for decryption\n")
    text = input("Type the text message\n").lower()
    shift = int(input("Type shift number\n"))
    shift = shift%26
    caesar(start_text=text,shift_number=shift,cipher_direction=direction) ;
    restart = input("Do you wanna encode and decode again")
    if restart == "no":
        should_end = True
        print("Goodbye !")


