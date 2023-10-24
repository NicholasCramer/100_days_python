from art import logo

print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(message, shift_amount, cipher_direction):
    modified_message = ""
    if cipher_direction.lower() == "decode":
        shift_amount *= -1
    else:
        cipher_direction = "encode"
    for char in message:
        if char in alphabet:
            original_position = alphabet.index(char)
            new_position = original_position + shift_amount
            modified_message += alphabet[new_position]
        else:
            modified_message += char

    print(f"The {cipher_direction}d text is: {modified_message}\n")


should_continue = True

while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt (default function is encrypt): \n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    # Handling for shift amount greater than number of letters in alphabet
    shift = shift % 26

    caesar(message=text, shift_amount=shift, cipher_direction=direction)

    result = input("Type 'yes' if you want to go again. Otherwise type anything else. \n")
    if result.lower() == "yes":
        should_continue = True
    else:
        should_continue = False
        print("Goodbye")
