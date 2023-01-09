alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def ceasar(start_text, shift_amount, cipher_direction):
    end_text=""
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:
            end_text += char
    print(f"Here is the {cipher_direction}d result: {end_text}")

should_continue = False
while not should_continue:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26
    ceasar(start_text=text, shift_amount=shift, cipher_direction=direction)

    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'. \n")
    if restart == "no":
        should_continue = True
        print("Goodbye")

#def ceasar(decryption, plain_text, shift_amount):
#     cipher_text = ""
#     if decryption == "encode":
#         for letter in plain_text:
#             position = alphabet.index(letter)
#             new_position = position + shift_amount
#             new_letter = alphabet[new_position]
#             cipher_text += new_letter
#     elif decryption == "decode":
#         for letter in plain_text:
#             position = alphabet.index(letter)
#             new_position = position - shift_amount
#             new_letter = alphabet[new_position]
#             cipher_text += new_letter
#     print(f"The Message reads {cipher_text}")

# def encrypt(plain_text, shift_amount):
#     cipher_text = ""
#     for letter in plain_text:
#         position = alphabet.index(letter)
#         new_position = position + shift_amount
#         new_letter = alphabet[new_position]
#         cipher_text += new_letter
#     print(f"The encoded text is {cipher_text}")

# def decrypt(cipher_text, shift_amount):
#     plain_text = ""
#     for letter in cipher_text:
#         position = alphabet.index(letter)
#         new_position = position - shift_amount
#         new_letter = alphabet[new_position]
#         plain_text += new_letter
#     print(f"The decoded message is {plain_text}")

# if direction == "decode":
#     decrypt(cipher_text=text, shift_amount=shift)
# else:
#     encrypt(plain_text=text, shift_amount=shift)
    

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 

# for i, j in enumerate(['foo', 'bar', 'baz']):
#     if j == 'bar':
#         print(i)