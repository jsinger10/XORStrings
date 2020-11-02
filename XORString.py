import sys
import io
mode = sys.argv[1]
keyfile = sys.argv[2]
inpfile = sys.argv[3]
key = io.open(keyfile, encoding='cp1252').read()[:-1]
inp = io.open(inpfile, encoding='cp1252').read()[:-1]
debug = False

if(debug):
    print("mode:"+mode)
    print("key: "+key)
    print("inp: "+inp)

def xorstring(mode, inpfile, keyfile):
    if mode == "human":
        return humanxor(inp, key)
    else:
        return numberxor(inp, key)


def humanxor(input, key):
    output = ""
    toReturn=""
    key_length_adjusted = ""
    while len(input) - len(key_length_adjusted) > 0:
        if len(input) - len(key) > len(key):
            key_length_adjusted = key_length_adjusted + key
        elif len(input) - len(key) < len(key):
            length_to_add = len(input) % len(key)
            key_length_adjusted = key_length_adjusted + key[0:length_to_add]
    for i in range(len(input)):
        toAdd = str(hex(int(hex(ord(input[i])), 16) ^ int(hex(ord(key_length_adjusted[i])), 16)))
        if len(toAdd) < 4:
            toAdd = toAdd[0:2] + "0" + toAdd[2]
        #print(input[i] + " " + hex(int(hex(ord(input[i])), 16)) + " + " + hex(ord(key_length_adjusted[i])) + " = " +toAdd)
        output = output + toAdd
    for l in range(0, len(output), 4):
        #print(output[l + 2: l + 4])
        #print(str(output[l:l + 4]) + " = " + bytearray.fromhex(output[l + 2:l + 4]).decode(encoding='cp1252'))
        toReturn = toReturn + str(bytearray.fromhex(output[l+2:l+4]).decode(encoding='cp1252'))
    print(toReturn)
    return toReturn


def numberxor(input, key):
    output = ""
    key_length_adjusted = ""
    while len(input) - len(key_length_adjusted) > 0:
        if len(input) - len(key) > len(key):
            key_length_adjusted = key_length_adjusted + key
        elif len(input) - len(key) < len(key):
            length_to_add = len(input) % len(key)
            key_length_adjusted = key_length_adjusted + key[0:length_to_add]
    for i in range(len(input)):
        toAdd = str(hex(int(hex(ord(input[i])), 16) ^ int(hex(ord(key_length_adjusted[i])), 16)))
        if len(toAdd) < 4:
            toAdd = toAdd[0:2] + "0" + toAdd[2]
        toAdd = toAdd[2:4]
        output = output + toAdd + " "
    print(output)
    return output


xorstring(mode, inp, key)
