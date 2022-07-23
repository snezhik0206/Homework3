import os


def read_sort_write():
    files_list = ["1.txt", "2.txt", "3.txt"]
    sorted_files_list = sorted(files_list, key=calculate_lines)
    data = ""
    directory = os.getcwd()
    for file_name in sorted_files_list:
        path = os.path.join(directory, file_name)
        with open(path, encoding="utf-8") as file:
            data += file_name + "\n"
            data += str(calculate_lines(file_name)) + "\n"
            data += file.read().strip() + "\n"
    with open("result_file.txt", "w", encoding="utf-8") as file:
        file.write(data)


def calculate_lines(file_name):
    directory = os.getcwd()
    path = os.path.join(directory, file_name)
    with open(path, encoding="utf-8") as file:
        lines_list = file.readlines()
    return len(lines_list)


read_sort_write()
