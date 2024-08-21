dic = {"1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0, "8": 0, "9": 0, "10": 0}
while True:
    num = input("clave: ")
    if num == "s": print(dic); break
    dic[num] = dic.get(num, 0) + 1