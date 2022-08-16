res = []
with open('199803.txt', 'r', encoding='utf-8') as file:
    for line in file :
        tmp = list(line.split())
        stops = ['，/w','。/w','？/w''！/w','、/w','；/w','：/w','“/w','（/w','）/w','——/w','《/w','》/w','-/w','~/w','●/w','一/m']
        for i in stops:
            if i in tmp:
                tmp.remove(i)
        res.append(tmp[1:])
print(res)