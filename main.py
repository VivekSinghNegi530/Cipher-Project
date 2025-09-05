def caesar_cipher():
    text=input("enter the message: ")
    mode=input("enter encrypt od decrypt: ")
    value=int(input("enter encrypt or decrypt value: "))
    new_text=""
    if mode=="encrypt":
        for char in text:
            asc_valuec=ord(char)
            new_asc=ord(char)+value
            new_text=new_text+chr(new_asc)
    else:
        for char in text:
            asc_value=ord(char)
            new_asc=ord(char)-value
            new_text=new_text+chr(new_asc)
    print("".join(new_text))
def force_decrypt():
    text=input("enter the message: ")
    new_text=""
    for i in range(1,27):
        for char in text:
            x=ord(char)-i
            new_text+=chr(x)
    print(f"\n{new_text}")
def atbash_cipher():
    text=input("enter the message: ")
    new_text=""
    value=int(input("enter 1 to encode message and any other number to decode: "))
    base=ord("a")
    end=ord("z")
    if value==1:
        for char in text:
            char_value=ord(char)-base
            new_char=end-char_value
            new_text+=chr(new_char)
        print(f"coded text is {new_text}")
    else:
        for char in text:
            char_value=end-ord(char)
            new_char=char_value+base
            new_text+=ord(new_char)
        print(f"decoded message is {new_text}")
def Rail_Fence_cipher():
    text=input("enter the message: ")
    new_text=""
    decrypted=""
    mode=input("enter encrypt or decrypt").lower()
    text1=""
    text2=""
    text3=""
    if mode=="encrypt":
            for i in range(0,len(text)):
                if i%2==0:
                    text1+=text[i]
                elif i%3==0:
                    text2+=text[i]
                else:
                    text3+=text[i]
            new_text=text1+text2+text3
            print(f"encoded message is {new_text}")
    else:
        length = len(text)
        text1_count = text2_count = text3_count = 0
        for i in range(length):
            if i % 2 == 0:
                text1_count += 1
            elif i % 3 == 0:
                text2_count += 1
            else:
                text3_count += 1

        text1 = text[0:text1_count]
        text2 = text[text1_count:text1_count + text2_count]
        text3 = text[text1_count + text2_count:]

        t1 = t2 = t3 = 0
        for i in range(length):
            if i % 2 == 0:
                decrypted += text1[t1]
                t1 += 1
            elif i % 3 == 0:
                decrypted += text2[t2]
                t2 += 1
            else:
                decrypted += text3[t3]
                t3 += 1

        print("Decrypted message:", decrypted)
if __name__=="__main__":
    caesar_cipher()
    force_decrypt()
    atbash_cipher()
    Rail_Fence_cipher()