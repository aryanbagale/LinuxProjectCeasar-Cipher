import sys

def caesar_cipher(shift, text):
    ciphertext = ""
    current_row = current_column = 1
    for char in text.upper():
        if char.isalpha():
            ascii_code = ord(char)
            new_ascii_code = ascii_code + shift
            if new_ascii_code > 90:
                remaining = new_ascii_code - 90
                new_ascii_code = 64 + remaining
            new_char = chr(new_ascii_code)
            if current_row == 5:
                ciphertext += new_char
                ciphertext += " "
                current_row = 1
                current_column += 1
            else:
                ciphertext += new_char
                current_row += 1            
            if current_column > 10:
                ciphertext += "\n"
                current_column = 1
    return ciphertext


if __name__ == '__main__':
    shift = int(sys.argv[1])
    message = input('Enter a message to encrypt: ')
    encrypted_message = caesar_cipher(shift, message)
    print(encrypted_message)
