

def xorstring(mode, input, key):
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
    output = input ^ key_length_adjusted
    print(output)
    for i in input:
        input_convert_int = int(i, 16)
        converted_char = str(hex(input_convert_int)
        print("hexadecimal value of character " + i + " is " + converted_char);
        input_hexadecimal = "";



xorstring("human", "abcdefghij", "acegik")