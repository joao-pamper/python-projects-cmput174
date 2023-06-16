'''
This program should decrypt messages
ord() -> converts letters to their ASCII code
chr() -> opposite of ord()
ASCII table -> http://sticksandstones.kstrom.com/appen.html 
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
        #check if it is a letter
        if letter.isalpha():
            newAscii = ord(letter) - shift
            # if outside ascii range, will adjust
            if newAscii < 65 or (newAscii > 90 and newAscii < 97): 
                newAscii = newAscii + 26
                
            new_letter = chr(newAscii)
            text_list[counter] = new_letter
    decrypted_text = ''.join(text_list)        
    return decrypted_text

def decrypt_atbash(text: str) -> str:
    """
    Decipher a text (Atbash cipher).
    """
    text_list = []
    for index in text:
        text_list.append(index)
    counter = -1
    for letter in text_list:
        counter += 1
            
        if letter.isalpha():
            Ascii = ord(letter)
            if Ascii - 65 > 26: #check if lower case
                newAscii = 123 - (Ascii - 96)
            else:
                newAscii = 91 - (Ascii - 64)
                    
            new_letter = chr(newAscii)
            text_list[counter] = new_letter
                
    decrypted_text = ''.join(text_list)        
    return decrypted_text    


def main() -> None:
    """
    Main program.
    """
    text = input("Enter a text to decipher: ")
    print("Let's try all the methods we have:")
    shift = 3
    caesar_result = decrypt_caesar(text, shift)
    atbash_result = decrypt_atbash(text)
    print('Caesar cipher: ' + str(caesar_result))
    print('Atbash cipher: ' + str(atbash_result))
    # text deciphered with both Caesar and Atbash methods
main()