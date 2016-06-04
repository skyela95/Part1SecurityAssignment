import os
from Crypto.PublicKey import RSA


def decrypt_valuables(f):
    # TODO: For Part 2, you'll need to decrypt the contents of this file
    #open RSA 4096bit private key
    privateKey = open('keys\private.key',"r").read()
    #import key into RSA to be used for decryption
    Decypter = RSA.importKey(privateKey)
    #decode file
    decoded_text = Decypter.decrypt(f)
    print(decoded_text)


if __name__ == "__main__":
    fn = input("Which file in pastebot.net does the botnet master want to view? ")
    if not os.path.exists(os.path.join("pastebot.net", fn)):
        print("The given file doesn't exist on pastebot.net")
        os.exit(1)
    f = open(os.path.join("pastebot.net", fn), "rb").read()
    decrypt_valuables(f)
