from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

print(logo)


def caeser(message, shift_by, encode_or_decode):
    cipher_text = ""
    for char in message:
        if char in alphabet:
            alpha_index = alphabet.index(char)

            if encode_or_decode == "encode":
                cipher_text += alphabet[alpha_index + shift_by]
            elif encode_or_decode == "decode":
                cipher_text += alphabet[alpha_index - shift_by]
        else:
            cipher_text += char

    print(f"The {direction}d text is {cipher_text}")


cont_encode_decode = True

while cont_encode_decode:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    shift = shift % 26

    if direction != "encode" and direction != "decode":
        print("Enter a valid input!!")
    else:
        caeser(message=text, shift_by=shift, encode_or_decode=direction)

    user_input = input("Do you want to try again [Yes/No]: ").lower()

    if user_input == "no":
        cont_encode_decode = False
        print("Good Bye!!")
