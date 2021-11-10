import caesar_art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar_cipher():
    
    done = False

    while done != True:

        print(caesar_art.logo)

        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        
        cipher = []
        shift = shift % 26
        
        for letter in text:
            if letter not in alphabet:
                cipher += letter
            else:
                let_ind = alphabet.index(letter)

                if direction == 'encode':
                    let_shift = let_ind + shift

                else:                
                    let_shift = let_ind - shift
                
                cipher += alphabet[let_shift]

        secret = ''.join(cipher)
        print(f"The {direction}d text is {secret}")
        
        repeat = input(f"Do you want to try again? Yes/No: ").lower()
        if repeat == "no":
            done = True


caesar_cipher()