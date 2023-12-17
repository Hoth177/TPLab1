# -*- coding: utf-8 -*-
from Types import DataType
from DataReader import DataReader
import xml.etree.cElementTree as ET

key: str = '';
students: DataType = {};
path = '.\data\data.xml';

tree = ET.ElementTree(file=path);
root = tree.getroot();

for child in root:
    key = child.attrib['class'];
    students[key] = []
    for child2 in child:
        students[key].append((child2.tag, int(child2.text)))

def calc() -> int:
    goodCount = 0
    data = students
    for key in data:
        isGood = True
        for subject in data[key]:
            if subject[1] < 76:
                isGood = False
        if isGood:
            goodCount += 1
    return goodCount

print(calc())
print('OK')
# .\data\data.xml