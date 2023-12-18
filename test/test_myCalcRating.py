# -*- coding: utf-8 -*-
from src.Types import DataType
from src.myCalcRating import myCalcRating
import pytest


class TestmyCalcRating:

    @pytest.fixture()
    def input_dataGood0(self) -> (DataType, int):
        data: DataType = {
            "Абрамов Петр Сергеевич":
                [
                    ("математика", 75),
                    ("русский язык", 75),
                    ("программирование", 74)
                ],

            "Петров Игорь Владимирович":
                [
                    ("математика", 76),
                    ("русский язык", 80),
                    ("программирование", 78),
                    ("литература", 50)
                ]
        }
        return data, 0

    @pytest.fixture()
    def input_dataGood2(self) -> (DataType, int):
        data: DataType = {
            "Абрамов Петр Сергеевич":
                [
                    ("математика", 80),
                    ("русский язык", 76),
                    ("программирование", 100)
                ],

            "Петров Игорь Владимирович":
                [
                    ("математика", 76),
                    ("русский язык", 80),
                    ("программирование", 78),
                    ("литература", 97)
                ]
        }
        return data, 2

    def test_init_dataGood0(self, input_dataGood0: (DataType, int)) -> None:
        calc_rating = myCalcRating(input_dataGood0[0])
        assert input_dataGood0[0] == calc_rating.data

    def test_init_dataGood2(self, input_dataGood2: (DataType, int)) -> None:
        calc_rating = myCalcRating(input_dataGood2[0])
        assert input_dataGood2[0] == calc_rating.data

    def test_calcGood0(self, input_dataGood0: (DataType, int)) -> None:
        goodCount = myCalcRating(input_dataGood0[0]).calc()
        assert goodCount == input_dataGood0[1]

    def test_calcGood2(self, input_dataGood2: (DataType, int)) -> None:
        goodCount = myCalcRating(input_dataGood2[0]).calc()
        assert goodCount == input_dataGood2[1]
