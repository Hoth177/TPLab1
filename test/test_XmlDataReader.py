# -*- coding: utf-8 -*-
import pytest
from src.Types import DataType
from src.XmlDataReader import XmlDataReader


class TestXmlDataReader:

    @pytest.fixture()
    def file_and_data_content(self) -> tuple[str, DataType]:
        text = '<?xml version="1.0" encoding="UTF-8" ?>\n' + \
            '<students>\n' + \
            '  <student class="Иванов Иван">\n' + \
            '       <математика>67</математика>\n' + \
            '       <литература>78</литература>\n' + \
            '       <философия>77</философия>\n' + \
            '   </student>\n' + \
            '  <student class="Крюков Дмитрий">\n' + \
            '       <математика>67</математика>\n' + \
            '       <химия>54</химия>\n' + \
            '       <социология>70</социология>\n' + \
            '   </student>\n' + \
            '  <student class="Грушин Александр">\n' + \
            '       <математика>100</математика>\n' + \
            '       <химия>100</химия>\n' + \
            '       <социология>100</социология>\n' + \
            '   </student>\n' + \
            '</students>'
        data = {
            "Иванов Иван": [
                ("математика", 67), ("литература", 78), ("философия", 77)
            ],
            "Крюков Дмитрий": [
                ("математика", 67), ("химия", 54), ("социология", 70)
            ],
            "Грушин Александр": [
                ("математика", 100), ("химия", 100), ("социология", 100)
            ]
        }
        return text, data

    @pytest.fixture()
    def filepath_and_data(self,
                          file_and_data_content: tuple[str, DataType],
                          tmpdir) -> tuple[str, DataType]:
        p = tmpdir.mkdir("datadir").join("my_data.txt")
        p.write_text(file_and_data_content[0], encoding='utf-8')
        return str(p), file_and_data_content[1]

    def test_read(self, filepath_and_data: tuple[str, DataType]) -> None:
        file_content = XmlDataReader().read(filepath_and_data[0])
        assert file_content == filepath_and_data[1]
