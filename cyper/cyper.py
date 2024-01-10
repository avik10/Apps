import os


def encrypt(text, s):
    result = ""
   # transverse the plain text
    for i in range(len(text)):
        char = text[i]
      # Encrypt uppercase characters in plain text

        if (char.isupper()):
            result += chr((ord(char) + s-65) % 26 + 65)
      # Encrypt lowercase characters in plain text
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)
    return result


def decrypt(text, s):
    result = ""
   # transverse the plain text
    for i in range(len(text)):
        char = text[i]
      # Encrypt uppercase characters in plain text

        if (char.isupper()):
            result += chr((ord(char) - s - 65) % 26 + 65)
      # Encrypt lowercase characters in plain text
        else:
            result += chr((ord(char) - s - 97) % 26 + 97)
    return result


def openFile(path, cypher, type):
    files = os.listdir(path)
    if len(files) > 0 :
        for file in files:
            temperedWordList = []
            normalWordList = []
            filepath = path+ "\\" + file
            if os.path.isfile(filepath):
                openFile = open(filepath)
                data = openFile.read()
                words = data.split()
                for i in range(len(words)):
                    normalWordList.append(words[i])
                    if type.lower() in 'en':
                        word = encrypt(words[i], cypher)
                        temperedWordList.append(word)
                    else:
                        word = decrypt(words[i], cypher)
                        temperedWordList.append(word)
                for n, i in enumerate(normalWordList):
                    normalWordList[n] = temperedWordList[n] + ' '
                openFile.close()
                openFile = open(filepath, "w+")            
                openFile.writelines(normalWordList)
            else: continue
    else:
        print("No txt file found")



if __name__ == "__main__":
    path = os.getcwd()
    parent = os.path.abspath(os.path.join(path, os.pardir))
    cypher = 5
    openFile(parent,cypher,'en')

    

