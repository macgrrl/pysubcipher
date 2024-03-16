import ui
from subcipher import SubCipher


# event handlers

def cipher_text_entered(sender):
    """
    Enter pressed in cipher text field
    """
    global c

    #print("Cipher text entered: ", sender.text)
    c = SubCipher(sender.text)
    sender.text = c.get_ciphertext()
    ciphertext_label.text = c.get_ciphertext()
    plaintext_label.text = c.get_plaintext()
    subs_label.text = repr(c.get_sub())
    freq_label.text = repr(c.get_sort_freq())
    #c.print_text()

def substitute_button_pressed(sender):
    """
    Substitute button is pressed
    """
    global c

    #print("Substituting...", cipher_textfield.text, "->", plain_textfield.text)
    c.substitute(cipher_textfield.text.upper(), plain_textfield.text.upper())
    #c.print_text()
    plaintext_label.text = c.get_plaintext()
    subs_label.text = repr(c.get_sub())
    cipher_textfield.begin_editing()


# main UI setup

v = ui.load_view()
v.present('sheet')

ciphertext_label = v["ciphertext_label"]
plaintext_label = v["plaintext_label"]
subs_label = v["subs_label"]
freq_label = v["freq_label"]

cipher_textfield = v["cipher_textfield"]
plain_textfield = v["plain_textfield"]

