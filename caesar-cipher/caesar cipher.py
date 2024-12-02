# from operator import index
#
import art
print(art.logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']



# TODO-1: Create a function called 'encrypt()' that takes 'original_text' and 'shift_amount' as 2 inputs.
def encrypt(original_txt, shift_amt):
    cipher_txt = ""
    for letter in original_txt:
        if letter not in alphabet:
            cipher_txt += letter
        else:
            shift_no = alphabet.index(letter) + shift_amt
            shift_no %= len(alphabet)
            cipher_txt += alphabet[shift_no]

    print(f"here is encoded result: {cipher_txt}")

def decrypt(original_txt, shift_amt):
    real_txt = ""
    for letter in original_txt:
        if letter not in alphabet:
            real_txt += letter
        else:
            shift_no = alphabet.index(letter) - shift_amt
            shift_no %= len(alphabet)
            real_txt += alphabet[shift_no]

    print(f"here is encoded result: {real_txt}")

def caesar(original_txt, shift_amt, dirn):
    if direction == "encode":
        encrypt(original_txt=text, shift_amt=shift)
    elif direction == "decode":
        decrypt(original_txt=text, shift_amt=shift)
    else:
        print("check inputs")

should_continue = True

while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(original_txt=text, shift_amt=shift, dirn=direction)

    again = input("type 'yes' if you want to go again. Or Type 'no'.\n").lower()
    if again == "no":
        should_continue = False
        print("Goodbye")