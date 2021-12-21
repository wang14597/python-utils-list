import os
import re
from src.main.list.util_list import UtilsList


class SplitTools:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = object.__new__(cls)
        return cls._instance

    @staticmethod
    def read_file(file_path):
        with open(file_path) as f:
            context = UtilsList(f)
        return context

    @staticmethod
    def open_file(sql_save_path):
        if os.path.exists(sql_save_path):
            os.remove(sql_save_path)
        file_obj = open(sql_save_path, 'a+')
        return file_obj


def main(**kwargs):
    tools = SplitTools()
    lines = tools.read_file(kwargs["source_file_path"])
    file = None
    for line in lines:
        search = re.search(kwargs["reg"], line)
        if search:
            if file is not None:
                file.close()
            table_ddl_file_name = f'{search.group(kwargs["group_index"])}.ddl.sql'
            table_ddl_path = os.path.join(kwargs["save_path"], table_ddl_file_name)
            file = tools.open_file(table_ddl_path)
        file.write(line)
    file.close()


if __name__ == '__main__':
    source_file_path = "../main/resource/QUANTUMDB.sql"
    save_path = "../main/resource/ddl"
    reg = r'create table \w+."(\w+)"'
    group_index = 1
    main(source_file_path=source_file_path, save_path=save_path, reg=reg, group_index=group_index)