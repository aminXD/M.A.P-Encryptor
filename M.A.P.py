import binascii
intro = """
▒█▀▄▀█ ░ ░█▀▀█ ░ ▒█▀▀█    ▒█▀▀▀ █▀▀▄ █▀▀ █▀▀█ █░░█ █▀▀█ ▀▀█▀▀ █▀▀█ █▀▀█ 
▒█▒█▒█ ▄ ▒█▄▄█ ▄ ▒█▄▄█    ▒█▀▀▀ █░░█ █░░ █▄▄▀ █▄▄█ █░░█ ░░█░░ █░░█ █▄▄▀ 
▒█░░▒█ █ ▒█░▒█ █ ▒█░░░    ▒█▄▄▄ ▀░░▀ ▀▀▀ ▀░▀▀ ▄▄▄█ █▀▀▀ ░░▀░░ ▀▀▀▀ ▀░▀▀
by aminXD.
Simple Encryptor With Hex Strings.
Important Note:
---
Dont Encrypto And Save Your Personal data (CryptoCurrencies Password, Bank Account Details, etc...) By This Encryptor!
Its Just A Simple Encryptor.
---
Anyway, I Recommend Understand How It Work (Good For People Want Make Encryptor).
What You Gonna Do??
1) Encrypt Data.
2) Decrypt Data.
3) Understand How It Work.
"""
print(intro)
try:
    def encrypt(data: str, key: int) -> str:
        data = binascii.hexlify(data.encode()).decode()
        result = ""
        for char in data:
            num = ord(char) + key
            if num > 1114111:
                while True:
                    num = (num - 1114111) - 1
                    if num <= 1114111: break
            new = chr(num)
            result += new
        return result
    def decrypt(data: set, key: int):
        result = ""
        for char in data:
            num = ord(char) - key
            if num < 0:
                num = 1114111 + num
            new = chr(num)
            result += new
        result = binascii.unhexlify(result).decode()
        return result
    def guide():
        return """Good, You Wanna Know How It Work!\nSteps Work Of This Tool:\n---\nAfter Getting Key And Text From You, It Convert Your Text To Hex String.\nNow With (For Loop) It Get Unicode Position Each Hex Letters.\nAnd Sum Unicode Position With Your Key.\nFinally Convert Unicode Position To Letter.\nAnd Return You Final Result!\n---
        """
    print("> Enter Your Choice: ",end="")
    choice = int(input())
    if choice == 1:
        print("> Enter Data: ",end="")
        data = input()
        print("> Enter Key: ",end="")
        key = int(input())
        print(encrypt(data,key))
    elif choice == 2:
        print("> Enter Data: ",end="")
        data = input()
        print("> Enter Key: ",end="")
        key = int(input())
        print(decrypt(data,key))
    elif choice == 3:
        print(guide())
except ValueError:
    print("""Please Enter Correct Data!
Reasons:
1> Invalid Data In Main Screen.
2> Can't Decrypt Your Text.""")
except Exception as err:
    raise(err)
