import os
os.chdir('/Users/15087/Documents/HeadFIrstPython/ch12')

from datetime import datetime
import pprint

def convert2ampm(time24: str) -> str:
    return datetime.strptime(time24, '%H:%M').strftime('%I:%M%p')

with open('buzzers.csv') as data:             #从CSV文件中读入原始数据
    ignore = data.readline()
    flights = {}              
    for line in data:
        k, v = line.strip().split(',')
        flights[k] = v
        
pprint.pprint(flights)
print()

fts = {convert2ampm(k):v.title() for k, v in flights.items()}    #原始数据复制和转换为AM/PM格式，并改写为首字母大写
pprint.pprint(fts)
print()

when = {dest:[k for k, v in fts.items() if v == dest] for dest in set(fts.values())}   #congfts中获取每个目的地相应的飞行时间列表
pprint.pprint(when)
print()
