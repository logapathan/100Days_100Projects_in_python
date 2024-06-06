alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
encoded_text=[]

if direction=="encode":
    
    for i in text:
        index=alphabet.index(i)
        new_index=(index+shift)%26

        encoded_text.append(alphabet[new_index])

       
    encoded_str=""
    for i in range(0,len(encoded_text)):
        encoded_str+=encoded_text[i]
    print(f"Encoded text is {encoded_str}")


    
elif direction=='decode':
    decoded_text=[]
    for i in text:
        index=alphabet.index(i)
        new_index=(index-shift)%26
        decoded_text.append(alphabet[new_index])
    decode_str=""
    for i in range(0,len(decoded_text)):
        decode_str+=decoded_text[i]
    print(f"Decoded text is {decode_str}")
