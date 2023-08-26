import chardet

# take input from the user
msg = input("Enter the encrypted message: ").encode()

# try decoding with multiple encoding formats
decodings = ['utf-8', 'iso-8859-1', 'cp1252']
decoded_msg = None

for encoding in decodings:
    try:
        decoded_msg = msg.decode(encoding)
        break
    except:
        pass

# check if message was decoded successfully
if decoded_msg:
    print(decoded_msg)
else:
    print("Error: Could not decode message")
