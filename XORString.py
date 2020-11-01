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

    for i in input:
        converted_char = str(hex(ord(i)));
        print("hexadecimal value of character " + i + " is " + converted_char);
        input_hexadecimal += converted_char;
        #input_hexadecimal += " ";
    print("input as hexadecimal is : " + str(type(input_hexadecimal)));
    key_hexadecimal = "";

    for i in key_length_adjusted:
        converted_char = str(hex(ord(i)));
        print("hexadecimal value of character " + i + " is " + converted_char);
        key_hexadecimal += converted_char;
        #key_hexadecimal += " ";
    #print("key as hexadecimal is : " + key_hexadecimal)
    #print("XORed input and key is : " + str(hex(int(input_hexadecimal, 16)) ^ hex(int(key_hexadecimal, 16))))
    output = hex(input_hexadecimal) ^ hex(key_hexadecimal)
    print(output)


xorstring("human", "input.txt", "key.txt")