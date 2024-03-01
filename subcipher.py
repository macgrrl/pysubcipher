import re

class SubCipher:
    """
    Substitution Cipher Assistant
    Supports solving substitution ciphers
    Current language - English
    """

    def __repr__(self):
        """
        Representation
        """
        return self.plaintext


    def __init__(self, the_cipher_text = ""):
        """
        Class initialiser
        """
        self.ciphertext = the_cipher_text.upper()
        self.reset()
        
    
    def reset(self):
        """
        Resets the plaintext string, substitutions, and computes frequencies
        """
        self.plaintext = re.sub("[A-Z]", "-", self.ciphertext)
        self.sub = {}
        self.freq = {}
        for c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            self.sub[c] = "" # no substitution
            self.freq[c] = self.ciphertext.count(c)
        self.sort_freq = sorted(self.freq.items(), key=lambda item: item[1], reverse=True) # sort the frequencies in descending orderd


    def substitute1(self, cipher, plain):
        """
        Substitutes all occurrences of the cipher character with the plain character
        """
        self.sub[cipher] = plain
        for i in range(0, len(self.ciphertext)):
            if self.ciphertext[i] == cipher:
                # replace cipher character at i with plain
                self.plaintext = self.plaintext[:i] + plain + self.plaintext[i+1:]


    def substitute(self, cipher, plain):
        """
        Substitutes characters in cipher string with plain string
        """
        lc = len(cipher)
        lp = len(plain)
        # if plain string is shorter than cipher string then use plain string length
        for i in range(0, lp if lp < lc else lc):
            self.substitute1(cipher[i], plain[i])
            

    def print_text(self):
        """
        Prints the ciper and plain texts
        """
        print(self.ciphertext)
        print(self.plaintext)

