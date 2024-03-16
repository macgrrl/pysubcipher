import re

class SubCipher:
    """
    Substitution Cipher Assistant class
    
    Supports solving substitution ciphers
    Current language - English
    
    # Attributes
    * __ciphertext : str
        cipher text (enciphered)
    * __plaintext : str
        plain text (deciphered)
    * __sub : dict
        character substitution dictionary
        key : str
            cipher character [A-Z]
        value : str
            plaintext character corresponding to key
    * __freq : dict
        key : str
            cipher character [A-Z]
        value : int
            frequency of cipher character
    * __sort_freq : dict
        sorted in frequency order
        key : str
            cipher character [A-Z]
        value : int
            frequency of cipher character

    # Methods
    ## Overridden
    * __repr__
    
    ## Constructor
    * __init__
    
    ## Getters/Setters
    * For all attributes
    
    ## Other methods
    * reset
    * substitute1
    * substitute
    * print_text

    """


    # Special methods

    def __repr__(self):
        """
        Representation
        """
        return self.__plaintext


    def __init__(self, the_cipher_text = ""):
        """
        Constructor
        
        # Parameters
        * the_cipher_text : str
            cipher text (default: empty string)
        """
        self.__ciphertext = the_cipher_text.upper()
        self.reset()


    # Get/Set Attributes
    
    def get_ciphertext(self):
        return self.__ciphertext

    def set_ciphertext(self, p):
        self.__ciphertext = p
    
    def get_plaintext(self):
        return self.__plaintext

    def set_plaintext(self, p):
        self.__plaintext = p

    def get_sub(self):
        return self.__sub

    def set_sub(self, p):
        self.__sub = p

    def get_freq(self):
        return self.__freq

    def set_freq(self, p):
        self.__freq = p

    def get_sort_freq(self):
        return self.__sort_freq

    def set_sort_freq(self, p):
        self.__sort_freq = p


    # Methods

    def reset(self, the_cipher_text = "", reset_sub_flag = True):
        """
        Resets the plaintext string, substitutions, and computes frequencies
 
        # Parameters
        * the_cipher_text : str
            cipher text (default: empty string)
        * reset_sub_flag : bool
            True to reset the substitution dictionary (default: False)
        """
        self.__plaintext = re.sub("[A-Z]", "-", self.__ciphertext)
        self.__sub = {}
        self.__freq = {}
        for c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            self.__sub[c] = "" # no substitution
            self.__freq[c] = self.__ciphertext.count(c)

        # sort the frequencies in descending order
        self.__sort_freq = sorted(self.__freq.items(), key=lambda item: item[1], reverse=True)


    def substitute1(self, cipher, plain):
        """
        Substitutes all occurrences of the cipher character with the plain character
        """
        self.__sub[cipher] = plain
        for i in range(0, len(self.__ciphertext)):
            if self.__ciphertext[i] == cipher:
                # replace cipher character at i with plain
                self.__plaintext = self.__plaintext[:i] + plain + self.__plaintext[i+1:]


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
        print(self.__ciphertext)
        print(self.__plaintext)

