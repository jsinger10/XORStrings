import binascii;

def xorstring(mode, input_file, key_file):
    #must take in FILE for input and key

    with open(input_file, 'r') as reader:
        input = reader.read()
    with open(key_file, 'r') as reader:
        key = reader.read()
    if mode == "human":
        print("do the human xor")
        humanxor(input, key)
    else:
        print("do the hexadecimal number output")


def humanxor(input, key):
    output = ""
    toReturn=""
    # input = input.encode()
    # print("hopefully this works : ")
    # #print(int("0x", 16))
    # print(eval(input))
    print("length of input is : " + str(len(input)))
    print("length of key is : " + str(len(key)))
    key_length_adjusted = ""
    while len(input) - len(key_length_adjusted) > 0:
        if len(input) - len(key) > len(key):
            key_length_adjusted = key_length_adjusted + key
        elif len(input) - len(key) < len(key):
            length_to_add = len(input) % len(key)
            print(length_to_add)
            key_length_adjusted = key_length_adjusted + key[0:length_to_add]
    input_hexadecimal = ""
    for i in range(len(input)):
        print("input[i] is: " + input[i] + ", key[i] is: " + key_length_adjusted[i])
        print(hex(ord(input[i])))
        print(hex(ord(key_length_adjusted[i])))
        print(hex(int(hex(ord(input[i])), 16) ^ int(hex(ord(key_length_adjusted[i])), 16)))
        output = output + str(hex(int(hex(ord(input[i])), 16) ^ int(hex(ord(key_length_adjusted[i])), 16)))
    #print("input as hexadecimal is : " + str(type(input_hexadecimal)));
    key_hexadecimal = "";

    print(output)
    # for l in range(0, len(output), 2):
    #     print(output[l:l+2])
    #     print(bytearray.fromhex(output[l:l+2]).decode())
    #     toReturn = toReturn + str(bytearray.fromhex(output[l:l+2]).decode())
    # print(toReturn)
    print(bytearray.fromhex(output).decode())


print(ord("h") ^ ord("A"))
xorstring("human", "input.txt", "key.txt")