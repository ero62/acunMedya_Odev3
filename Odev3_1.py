with open("odev3.txt", "w") as f:
    temp = input("lütfen metin giriniz: ")
    f.write(temp + "\n")

with open("odev3.txt", "r") as f:
    print(f.read())

with open("odev3.txt", "a") as f:
    for i in range(6):
        temp = input("lütfen metin giriniz: ")
        f.write(temp + "\n")

with open("odev3.txt", "r") as f:
    for line in f:
        print(line.strip())