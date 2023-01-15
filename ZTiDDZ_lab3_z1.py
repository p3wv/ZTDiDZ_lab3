import base64

def toBase64():

    user_string_to_encode = input("enter a string to encode: ")

    user_string_to_encode_ascii = user_string_to_encode.encode('ascii')

    b64_bytes = base64.b64encode(user_string_to_encode_ascii)

    print("encoded text: {}".format(b64_bytes))

    print("decode now? y/n")

    if input() == "y":

        b64_bytes_to_text = base64.b64decode(b64_bytes)

        print("decoded text: {}".format(b64_bytes_to_text))
    else:
        raise(KeyboardInterrupt())

if __name__ == "__main__":
    toBase64()
