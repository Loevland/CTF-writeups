# If you do not have pwntools installed, run the following command: python3 -m pip install --upgrade pwntools
from pwn import *
import base64
import time

morseAlphabet = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    " ": "/"
}

inverseMorseAlphabet = dict((v, k) for (k, v) in morseAlphabet.items())

# Function written by (https://gist.github.com/dcdeve/3dfba6566029f87b01aa3e38d6e1e26b)
def decodeMorse(morse, positionInString=0):
    messageSeparated = morse.split(' ')
    decodeMessage = ''
    for char in messageSeparated:
        if char in inverseMorseAlphabet:
            decodeMessage += inverseMorseAlphabet[char]
        else:
            # CNF = Character not found
            decodeMessage += '<CNF>'
    return decodeMessage


# Connect with netcat
io = connect("io.ept.gg", 30023)

# Recieve data
data = io.recvuntil("Are you ready?").decode()

# Send data
io.sendline("Yes")

# Recieve empty line then the line containing the question
io.recvline()
while(1):
    question = io.recvline().decode().strip()
    print(question)
    time.sleep(1)
    # Check if it is a morse question and if so, extract the morse code
    if "morse" in question:
        morse = question.split(": ")[1]

        decoded = decodeMorse(morse)
        print(decoded)
        io.sendline(decoded)

    elif "equation" in question:
        eq = question.split(": ")[1]
        vals = eq.split()
        decoded = 0
        if vals[1] == '+':
            decoded = int(vals[0]) + int(vals[2])

        elif vals[1] == '-':
            decoded = int(vals[0]) - int(vals[2])

        elif vals[1] == '/':
            decoded = int(int(vals[0]) / int(vals[2]))

        elif vals[1] == '*':
            decoded = int(vals[0]) * int(vals[2])

        io.sendline(str(decoded))

    elif "ascii" in question:
        val = question.split(": ")[1]
        lst = val.split()
        sum = ""
        for i in lst:
            sum = sum + chr(int(i))
        io.sendline(sum)

    elif "Base64" in question:
        base = question.split(": ")[1]
        decoded = base64.b64decode(base)
        print(decoded)
        io.sendline(decoded)

    elif "hexadecimals" in question:
        base = question.split(": ")[1]
        decoded = bytearray.fromhex(base).decode()
        print(decoded)
        io.sendline(decoded)
io.interactive()
