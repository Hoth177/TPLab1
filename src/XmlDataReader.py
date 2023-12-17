# -*- coding: utf-8 -*-
from Types import DataType
from DataReader import DataReader
import xml.etree.cElementTree as ET


class XmlDataReader(DataReader):

    def __init__(self) -> None:
        self.key: str = ''
        self.students: DataType = {}

    def read(self, path: str) -> DataType:
        self.tree = ET.ElementTree(file=path);
        self.root = self.tree.getroot();

        for child in self.root:
            self.key = child.attrib['class'];
            self.students[self.key] = []
            for child2 in child:
                self.students[self.key].append((child2.tag, int(child2.text)))
        return self.students