# -*- coding: utf-8 -*-
import argparse
from decimal import Clamped
import sys

from CalcRating import CalcRating
from TextDataReader import TextDataReader
from XmlDataReader import XmlDataReader
from myCalcRating import myCalcRating


def get_path_from_arguments(args) -> str:
    parser = argparse.ArgumentParser(description="Path to datafile")
    parser.add_argument("-p", dest="path", type=str, required=True,
                        help="Path to datafile")
    args = parser.parse_args(args)
    return args.path


def main():
    path = get_path_from_arguments(sys.argv[1:])

    # reader = TextDataReader()
    # students = reader.read(path)
    # print("Students: ", students, "\n")

    xmlReader = XmlDataReader()
    students2 = xmlReader.read(path)
    print("Students: ", students2, "\n")

    rating = myCalcRating(students2).calc()
    print("Rating: ", rating, "\n")


if __name__ == "__main__":
    main()
