#!/usr/bin/env python3
"""
Encrypting passwords for use with Python

https://www.mssqltips.com/sqlservertip/5173/encrypting-passwords-for-use-with-python-and-sql-server/

- Problem
Due to requirements in my environment I need to use SQL Server authentication
with my Python scripts instead of Windows trusted authentication. We don’t
want a clear text password stored in the Python scripts and we’re not sure how
we can secure the passwords.

- Solution
Securing passwords is always an issue when using SQL Server authentication
or any application that may store the password in clear text in a configuration
file. Windows file server permissions offer one layer of protection that can
prevent wandering eyes from coming across a password, but that may not always
be feasible. Since Python offers a number of cryptographic options we’re going
to use one popular library that will encrypt our data and make it more
difficult to steal the password.

This solution assumes Python 3.x version and users are familiar
with the Python language.
"""

from cryptography.fernet import Fernet

__author__ = "Burt King <mssqltips.com>"
__version__ = "0.1.0"


def main():
    """ Main entry point of the app """

    """ Step 1: Install Cryptography Library and Create Key
                # pip install cryptography
    """
    # key = Fernet.generate_key()
    # print(key)

    """ Step 2: Encrypt Password and Test Decrypting """
    key = b'Lp3_h5EuFS-QdZF15uGUezXoot4NVzGgjYi9uA3IYIw='
    cipher_suite = Fernet(key)
    # ciphered_text = cipher_suite.encrypt(b"SuperSecretPassword")   #required to be bytes
    # print(ciphered_text)

    ciphered_text = b'gAAAAABemMq1dUsz9WACv1Fr7pbXU6nm37JfnZCA81zxttRxixViepZOnl8BjTuDx9ufF8sFn5I6kdsi32LrzgrD8ePQo6pCPME3L_eepiSgPc4SJz32oEg='
    # unciphered_text = (cipher_suite.decrypt(ciphered_text))
    # print(unciphered_text)


    """ Step 3: Write Encrypted Password to Binary File """
    # with open('./secrets.bin', 'wb') as file_object:  file_object.write(ciphered_text)


    """ Step 4: Retrieve Encrypted Password and Decrypt """
    with open('./secrets.bin', 'rb') as file_object:
        for line in file_object:
            encryptedpwd = line
    # print(encryptedpwd)

    uncipher_text = (cipher_suite.decrypt(encryptedpwd))
    plain_text_encryptedpassword = bytes(uncipher_text).decode("utf-8") #convert to string
    print(plain_text_encryptedpassword)


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
