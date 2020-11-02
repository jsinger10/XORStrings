import sys
mode = sys.argv[1]
keyfile = sys.argv[2]
inpfile = sys.argv[3]
key = open(keyfile).read()[:-1] #removes the mandatory \n at the end of the file to support one line messages.
inp = open(inpfile).read()[:-1] #removes the mandatory \n at the end of the file to support one line messages.
debug = False

if(debug):
    print("mode:"+mode)
    print("key: "+key)
    print("inp: "+inp)

def xorstring(mode, input, key):
    if mode == "human":
        # print("do the human xor")
        humanxor(input, key)
    else:
        # print("do the hexadecimal number output")
        numberxor(input, key)


def humanxor(input, key):
    output = ""
    toReturn=""
    # print("length of input is : " + str(len(input)))
    # print("length of key is : " + str(len(key)))
    key_length_adjusted = ""
    while len(input) - len(key_length_adjusted) > 0:
        if len(input) - len(key) > len(key):
            key_length_adjusted = key_length_adjusted + key
        elif len(input) - len(key) < len(key):
            length_to_add = len(input) % len(key)
            # print(length_to_add)
            key_length_adjusted = key_length_adjusted + key[0:length_to_add]
    for i in range(len(input)):
        # print("input[i] is: " + input[i] + ", key[i] is: " + key_length_adjusted[i])
        # print(hex(ord(input[i])))
        # print(hex(ord(key_length_adjusted[i])))
        # print(hex(int(hex(ord(input[i])), 16) ^ int(hex(ord(key_length_adjusted[i])), 16)))
        toAdd = str(hex(int(hex(ord(input[i])), 16) ^ int(hex(ord(key_length_adjusted[i])), 16)))
        # print("the XOR result is : " + str(bytearray.fromhex(toAdd[2:4]).decode()))
        output = output + toAdd

    # print(output)
    for l in range(0, len(output), 4):
        # print(output[l:l+4])
        # print(bytearray.fromhex(output[l+2:l+4]).decode())
        toReturn = toReturn + str(bytearray.fromhex(output[l+2:l+4]).decode())
    # print("this is toReturn: " + toReturn)
    # print("desired output: " + " this is a test")
    return toReturn

def numberxor(input, key):
    output = ""
    toReturn=""
    # print("length of input is : " + str(len(input)))
    # print("length of key is : " + str(len(key)))
    key_length_adjusted = ""
    while len(input) - len(key_length_adjusted) > 0:
        if len(input) - len(key) > len(key):
            key_length_adjusted = key_length_adjusted + key
        elif len(input) - len(key) < len(key):
            length_to_add = len(input) % len(key)
            # print(length_to_add)
            key_length_adjusted = key_length_adjusted + key[0:length_to_add]
    for i in range(len(input)):
        # print("input[i] is: " + input[i] + ", key[i] is: " + key_length_adjusted[i])
        # print(hex(ord(input[i])))
        # print(hex(ord(key_length_adjusted[i])))
        # print(hex(int(hex(ord(input[i])), 16) ^ int(hex(ord(key_length_adjusted[i])), 16)))
        toAdd = str(hex(int(hex(ord(input[i])), 16) ^ int(hex(ord(key_length_adjusted[i])), 16)))[2:4] + " "
        # print("the XOR result is : " + str(bytearray.fromhex(toAdd[2:4]).decode()))
        output = output + toAdd

    print(output)
    # for l in range(0, len(output), 4):
    #     # print(output[l:l+4])
    #     # print(bytearray.fromhex(output[l+2:l+4]).decode())
    #     toReturn = toReturn + str(bytearray.fromhex(output[l+2:l+4]).decode())
    # print("this is toReturn: " + toReturn)
    # print("desired output: " + " 66 3d 3b 21 35 69 3a 3b 66 28 73 3c 23 3a 27")
    return toReturn


xorstring(mode, inp, key)