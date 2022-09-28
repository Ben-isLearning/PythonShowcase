alphabet = ["a", "b", "c", "d", "e", "f", "g", "h",
            "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

msg = "xuo jxuhu!"

# print(alphabet[0])
# print(alphabet[25])

# print(alphabet[-10])
# print(msg[0])

# print("---")
# for char in range(len(msg)):
# print(msg[char])
#    for item in range(len(alphabet)):
#        if (msg[char] == alphabet[item]):
# print(char, "===", item)
# print(msg[char], "=", alphabet[item-16])
# print(alphabet[item-16])


def decode_to_characters(message, count):
    for char in range(len(msg)):
        # print(msg[char])
        for item in range(len(alphabet)):
            if (msg[char] not in alphabet):
                print(msg[char])
                break
            if (msg[char] == alphabet[item]):
                # print(char, "===", item)
                # print(msg[char], "=", alphabet[item],
                #      "index -10 =", alphabet[item-count])
                print(alphabet[item-count])


# decode_to_characters(msg, 16)

# Declare new string - x = join to string , return X at end


def decode_to_string(msg, count):
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h",
                "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    test_list = []
    for char in range(len(msg)):
        # print(msg[char])
        for item in range(len(alphabet)):
            if (msg[char] not in alphabet):
                # print(msg[char])
                test_list += msg[char]
                break
            if (msg[char] == alphabet[item]):
                # print(char, "===", item)
                # print(msg[char], "=", alphabet[item],
                #      "index -10 =", alphabet[item-count])
                # print(alphabet[item-count])
                test_list += alphabet[item-count]
    return "".join(test_list)


print(decode_to_string(msg, 16))


def encode_to_characters(msg, count):
    for char in range(len(msg)):
        # print(msg[char])
        for item in range(len(alphabet)):
            if (msg[char] not in alphabet):
                print(msg[char])
                break
            if (msg[char] == alphabet[item]):
                # print(char, "===", item)
                # print(msg[char], "=", alphabet[item],
                #      "index -10 =", alphabet[item-count])
                print(alphabet[item-23])


# print(encode_to_characters("i want to see the sunset", 13))


def encode_to_string(msg, count):
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h",
                "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    test_list = []
    for char in range(len(msg)):
        # print(msg[char])
        for item in range(len(alphabet)):
            if (msg[char] not in alphabet):
                test_list += msg[char]
                break
            if (msg[char] == alphabet[item]):
                # print(char, "===", item)
                # print(msg[char], "=", alphabet[item],
                #      "index -10 =", alphabet[item-count])
                # print(alphabet[item-23])
                test_list += alphabet[item-count]
    return "".join(test_list)


encoded = encode_to_string("i want to see the sunset", 12)
print(encoded)


print(decode_to_string(encoded, 14))


print(decode_to_string("jxu evviuj veh jxu iusedt cuiiqwu yi vekhjuud.", 16))

print(decode_to_string(
    "bqdradyuzs ygxfubxq omqemd oubtqde fa oapq kagd yqeemsqe ue qhqz yadq eqogdq!", 12))


#   First message:
#
#       jxu evviuj veh jxu iusedt cuiiqwu yi vekhjuud.
#
#   Second message:
#
#       bqdradyuzs ygxfubxq omqemd oubtqde fa oapq kagd yqeemsqe ue qhqz yadq eqogdq!

#   vhfinmxkl atox kxgwxkxw tee hy maxlx hew vbiaxkl tl hulhexmx. px'ee atox mh kxteer lmxi ni hnk ztfx by px ptgm mh dxxi hnk fxlltzxl ltyx.


def brute_force_decoder(msg):
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h",
                "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    test_list = []
    for attempt in range(len(alphabet)+1):
        count = attempt
        for char in range(len(msg)):
            # print(msg[char])
            for item in range(len(alphabet)):
                if (msg[char] not in alphabet):
                    # print(msg[char])
                    test_list += msg[char]
                    break
                if (msg[char] == alphabet[item]):
                    # print(char, "===", item)
                    # print(msg[char], "=", alphabet[item],
                    #      "index -10 =", alphabet[item-count])
                    # print(alphabet[item-count])
                    test_list += alphabet[item-count]
        print("Offset", attempt, "".join(test_list))
        test_list.clear()


#print(brute_force_decoder("vhfinmxkl atox kxgwxkxw tee hy maxlx hew vbiaxkl tl hulhexmx. px'ee atox mh kxteer lmxi ni hnk ztfx by px ptgm mh dxxi hnk fxlltzxl ltyx."))

# Offset 19 computers have rendered all of these old ciphers as obsolete. we'll have to really step up our game if we want to keep our messages safe.
