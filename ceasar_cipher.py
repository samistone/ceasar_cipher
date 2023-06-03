
alphabets = "abcdefghijklmnopqrstuvwxyz"
choose = input("do you want to decrypt or encrypt a message: ")
# to input decrypt or encrypt option
key = int(input("Enter prefferd key for cypher: "))
# to enter shift needed in encryption or decryption 
New_message = ""
message = input("Enter your message: ")

if choose == "encrypt":
    for character in message:
# for iterating through the message 
        if character in alphabets:
            position = alphabets.find(character)
            new_position = (position + key)%26
 # for adding the index of the shift to that of the message
            New_message += alphabets[new_position]
 # for adding a new message into the empty variabe "new_message" above
        else:
            New_message += character

    print(f"Encrypted message: {New_message}")

elif choose == "decrypt":
    for character in message:
        if character in alphabets:
            position = alphabets.find(character)
            decrypt_position = (position - key)%26
# for substracting the index of the shift to that of the message
            New_message += alphabets[decrypt_position]
        else:
            New_message += character
    print(f"Decrypted message: {New_message}")

else:
    print("no response was given")
