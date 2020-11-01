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
    length_to_add = len(input) % len(key)
    print(length_to_add)
    key_length_adjusted = key + key[0:length_to_add]
    input_hexadecimal = ""

    for i in input:
        converted_char = str(hex(ord(i)));
        print("hexadecimal value of character " + i + " is " + converted_char);
        input_hexadecimal += converted_char;
        input_hexadecimal += " ";
    key_hexadecimal = "";
    print("input as hexadecimal is : " + input_hexadecimal);
    for i in key:
        converted_char = str(hex(ord(i)));
        print("hexadecimal value of character " + i + " is " + converted_char);
        key_hexadecimal += converted_char;
        key_hexadecimal += " ";
    print("key as hexadecimal is : " + key_hexadecimal)
    print("XORed input and key is : " + str(input_hexadecimal ^ key_hexadecimal))
    output = input_hexadecimal ^ key_hexadecimal
    print(output)


xorstring("human", "input.txt", "key.txt")