import os
import csv

from PySide6.QtWidgets import QFileDialog


def get_file_path():
    """Open a dialog so that the user can select a target file."""
    dialog = QFileDialog()
    dialog.setWindowTitle("Select a path to your file.")
    dialog.exec_()
    if dialog.selectedFiles():  # If the user closed the choice window without selecting anything.
        path_to_file = dialog.selectedFiles()[0]
        return path_to_file
    else:
        raise Exception("Aborted")


def get_folder_path(self):
    dialog = QFileDialog()
    dialog.setWindowTitle("Select a path to your folder.")
    path_to_file = str(dialog.getExistingDirectory(self, "Select Directory"))
    if path_to_file:  # If the user closed the choice window without selecting anything.
        return path_to_file
    else:
        print("Aborted")


def reform_to_png(_filename):
    """add filename ".png" ending"""
    if _filename[-4:] != ".png":
        _filename += ".png"
    return _filename


def remove_png_ext(filename: str):
    """remove ".png" file extension"""
    if filename.split(".")[-1] == "png":
        return filename[:-4]
    return filename


def create_directories(*paths):
    """create all requested directories"""
    for path in paths:
        if not os.path.exists(path):
            os.mkdir(path)


def get_options_values(options):
    """A function that returns all possible combinations of the values of the selected options"""
    result = []
    for option in options:
        if option["type"] == "range":
            start = int(option['range']['start'])
            end = int(option['range']['end'])
            step = int(option['range']['step'])
            rang = list(range(start, end+step, step))
            result.append(rang)
        elif option["type"] == "resolution":
            width = int(option['resolution']['width'])
            height = int(option['resolution']['height'])
            result.append([[width, height]])
        elif option["type"] == "folder":
            path = option['folder']
            filenames = os.listdir(path)
            filepaths = [os.path.join(path, filename) for filename in filenames
                         if os.path.isfile(os.path.join(path, filename))]
            result.append(filepaths)

    keys = [option['name'] for option in options]
    result = add_elements([[]], result)

    return [{key: value for key, value in zip(keys, values)} for values in result]


def add_elements(result, lists):
    """Add elements to 2d array"""
    if len(lists) == 0:
        return result
    else:
        new_result = []
        for i in result:
            for k in lists[0]:
                new_result.append(i + [k])
        return add_elements(new_result, lists[1:])


def write_to_csv(path, filename, classes, colors):
    """
    The function creates csv if it not exists and write data or append data if csv exists
    Example:
        In: "test.csv", "test.png", ["car", "plane"], ["red", "blue"]
        Out(test.csv): test.png;car,plane;red,blue
    """
    classes = [str(cs) for cs in classes]
    colors = [str(color) for color in colors]
    with open(path, 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow([filename, ','.join(classes), ','.join(colors)])


def open_folder(save_full_path):
    path = os.path.realpath(save_full_path)
    os.startfile(path)
