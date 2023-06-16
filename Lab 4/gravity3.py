'''
This program should decrypt messages
ord() -> converts letters to their ASCII code
chr() -> opposite of ord()
ASCII table -> https://www.w3schools.com/charsets/ref_html_ascii.asp 
'''
def decrypt_caesar(text: str, shift: int) -> str:
    """
    Decipher a text (Caesar cipher).
    """
    #Make an adequate list from the inputted string
    text_list = []
    for index in text:
        text_list.append(index)
    counter = -1
    #Decrypt the list
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
    #Make an adequate list from the inputted string
    text_list = []
    for index in text:
        text_list.append(index)
    counter = -1
    #Decrypt the list
    for letter in text_list:
        counter += 1
            
        if letter.isalpha():
            Ascii = ord(letter)
            if Ascii - 65 > 26: #lower case letters
                newAscii = 123 - (Ascii - 96)
            else:
                newAscii = 91 - (Ascii - 64)
                    
            new_letter = chr(newAscii)
            text_list[counter] = new_letter
                
    decrypted_text = ''.join(text_list)        
    return decrypted_text

def decrypt_a1z26(text: str) -> str:
    """
    Decipher a text (A1Z26 cipher).
    assuming all capital letters
    """
    #Make an adequate list from the inputted string
    text_list = []
    count1 = -1
    count2= -1
    for item in text:
        count1 += 1
        nextItem = '.'
        if count1 +1 <= len(text) - 1:
            nextItem = text[count1 +1]
        if count1 != count2:
            if item.isnumeric() and nextItem.isnumeric():
                count2 = count1 + 1
                text_list.append(text[count1:count1+2])
            elif item.isnumeric():
                text_list.append(text[count1])
            elif item != '-':
                text_list.append(text[count1])
    print(text_list)            
    #Decrypt the list
    count3 = -1
    for index in text_list:
        count3 += 1
        if index.isnumeric():
            Ascii = int(index) + 64
            text_list[count3] = chr(Ascii)
    
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
    a1z26_result = decrypt_a1z26(text)
    #print('Caesar cipher: ' + str(caesar_result))
    #print('Atbash cipher: ' + str(atbash_result))
    print('A1Z26 cipher: ' + str(a1z26_result))
    # text deciphered with all three methods
main()