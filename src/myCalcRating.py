# -*- coding: utf-8 -*-
from Types import DataType


class myCalcRating:

    def __init__(self, data: DataType) -> None:
        self.data: DataType = data

    def calc1(self) -> int:
        self.GoodCount = 0
        for key in self.data:
            for subject in self.data[key]:
                print(subject)
        return self.GoodCount

    def calc(self) -> int:
        goodCount = 0
        for key in self.data:
            isGood = True
            for subject in self.data[key]:
                if subject[1] < 76:
                    isGood = False
            if isGood:
                goodCount += 1
        return goodCount
