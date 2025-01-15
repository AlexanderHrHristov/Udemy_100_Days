

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""

    # Промяна на посоката на шифроване/дешифроване
    if encode_or_decode == "decode":
        shift_amount *= -1

    # Обработка на всяка буква
    for letter in original_text:
        if letter in alphabet:
            shifted_position = (alphabet.index(letter) + shift_amount) % len(alphabet)
            output_text += alphabet[shifted_position]
        else:
            output_text += letter  # Добавяне на символи извън азбуката без промяна

    print(f"Here is the {encode_or_decode}d result: {output_text}")

# Извикване на функцията
caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)
