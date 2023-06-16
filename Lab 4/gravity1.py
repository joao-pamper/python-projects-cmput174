'''
This program should decrypt messages
ord() -> converts letters to their ASCII 
chr() -> opposite of ord()
'''
def decrypt_caesar(text: str, shift: int) -> str:
    """
    Decipher a text (Caesar cipher).
    """
    text_list = []
    for index in text:
        text_list.append(index)
    counter = -1
    for letter in text_list:
        counter += 1
        if letter.isalpha():
            newAscii = ord(letter) - shift
            if newAscii < 65 or (newAscii > 90 and newAscii < 97):
                newAscii = newAscii + 26
            new_letter = chr(newAscii)
            text_list[counter] = new_letter
    decrypted_text = ''.join(text_list)        
    return decrypted_text
    

def main() -> None:
    """
    Main program.
    """
    text = input("Enter a text to decipher: ")
    shift = 3
    # Print the deciphered text
    result = decrypt_caesar(text, shift)
    print(result)

main()