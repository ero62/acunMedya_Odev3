with open("odev3.txt", "w") as f:
    temp = input("lütfen metin giriniz: ")
    f.write(temp + "\n")

with open("odev3.txt", "r") as f:
    print(f.read())

with open("odev3.txt", "a+") as f:
    for i in range(5):
        while True:
            f.seek(0)
            lines = {line.strip() for line in f}
            temp = input("lütfen metin giriniz: ").strip()

            if temp in lines :
                print("farklı girini!")
            else:
                f.write(temp + "\n")
                f.flush()
                break


with open("odev3.txt", "r") as f:
    for line in f:
        print(line.strip())
