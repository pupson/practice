import caesar_art

print(caesar_art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caesar_cipher(text, shift, direction):
    
    cipher = []

    for letter in text:
        if letter not in alphabet:
            cipher += letter
        else:
            let_ind = alphabet.index(letter)

            if direction == 'encode':
                let_shift = let_ind + shift
                if let_shift > 26:
                    let_shift -= 26
                cipher += alphabet[let_shift]

            else:                
                let_shift = let_ind - shift
                if let_shift < 0:
                    let_shift += 26
                cipher += alphabet[let_shift]

    secret = ''.join(cipher)
    print(f"The {direction}d text is {secret}")


caesar_cipher(text, shift, direction)