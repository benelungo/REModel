import os

from PySide6.QtCore import QThread

import modules.tools as mt
from queue import Queue
from PySide6.QtWidgets import QMainWindow, QSpacerItem, QSizePolicy, QVBoxLayout, QWidgetItem
from PySide6.QtGui import QIcon
from interface.Ui.ui_main_window import Ui_MainWindow
from interface.class_widget import ClassWidget
from interface.option_widgets import RangeOptionWidget, FolderOptionWidget
from interface.option_widgets import RegularOptionWidget
from interface.option_widgets import ResolutionOptionWidget
from modules.blender import load_blend_file, generate_image, get_collections
from modules.options import Options


queue = Queue()


class Worker(QThread):
    def __init__(self):
        super(Worker, self).__init__()

    def run(self):
        while True:
            mode = queue.get()
            if mode is not None:
                mode()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.folders = {}
        self.counter_id = 0
        self.path_text = None
        self.options = Options()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.additional_setup()
        self.connect_buttons_to_functions()

        self.worker = Worker()
        self.worker.start()

    def additional_setup(self):
        """Additional interface settings"""
        self.ui.PathPushButton.setIcon(QIcon(r'icons\folder.png'))
        self.ui.ProgressBar.hide()
        self.ui.ProgressBar.setFormat("%v/%m")

    def connect_buttons_to_functions(self):
        """Attaching certain functions to the corresponding buttons of the interface"""
        self.ui.FindPushButton.clicked.connect(self.process_path)
        self.ui.GeneratePushButton.clicked.connect(self.generate)
        self.ui.PathPushButton.clicked.connect(self.choose_blend_path)

    def folder_button(self, widget):
        """Append a widget to self_folders, find path to folder, and save it too"""
        name = widget.ui.OptionName.text()
        path = mt.get_folder_path(self)
        if os.path.exists(path) and os.listdir(path) != 0:
            widget.ui.label.setText("Found!")
            widget.ui.label.setStyleSheet(u"color: lightgreen;")
            self.folders[name] = path
        else:
            raise Exception("Folder not found or empty!")

    def choose_blend_path(self):
        """File path selection function for the PathLineEdit object"""
        path = mt.get_file_path()
        self.ui.PathLineEdit.setText(path)
        self.process_path()

    def process_path(self):
        """A function to try to load a blend file"""
        self.path_text = self.ui.PathLineEdit.text()
        load_blend_file(self.path_text)
        self.ui.setupUi(self)
        self.additional_setup()
        self.connect_buttons_to_functions()

        self.fill_OptionsLayout(self.options.get_options_list())
        self.fill_ClassesLayout(get_collections())

    def generate(self):
        """Dataset generation function"""
        classes_text_list, options_text_list = self.get_info_from_interface()
        save_full_path = mt.get_folder_path(self)

        # necessary paths
        filename = mt.remove_png_ext(os.path.basename(save_full_path))
        path_to_values = os.path.join(save_full_path, "images")
        path_to_targets = os.path.join(save_full_path, "masks")

        # creating directories for values and targets
        mt.create_directories(save_full_path, path_to_values, path_to_targets)

        options_values = mt.get_options_values(options_text_list)

        # show and change progress bar
        self.ui.ProgressBar.setMaximum(len(options_values))
        self.ui.ProgressBar.setValue(0)
        self.ui.ProgressBar.setFormat("%v/%m")
        if len(options_values) != 0:
            self.ui.ProgressBar.show()

        options_dict = self.options.get_options_dict()
        blend_file_path = self.path_text

        # scene rendering and save data to csv
        for value_index in range(len(options_values)):
            mt.write_to_csv(os.path.join(save_full_path, filename+'.csv'),
                            mt.reform_to_png(filename+str(value_index)),
                            list(classes_text_list.keys()),
                            list(classes_text_list.values()))
        
            generate_image(classes_text_list,
                           options_text_list,
                           save_full_path,
                           blend_file_path,
                           options_dict,
                           options_values[value_index],
                           path_to_values,
                           path_to_targets,
                           mt.reform_to_png(filename+"_"+str(value_index)))
            
            self.ui.ProgressBar.setValue(value_index + 1)

        self.ui.ProgressBar.setFormat("Done!")

        mt.open_folder(save_full_path)
        print("Done!")

    def get_info_from_interface(self):
        """A function for obtaining the necessary data from the interface"""
        classes_content_list = self.layout_content_list(self.ui.ClassesLayout)
        options_content_list = self.layout_content_list(self.ui.OptionsLayout)

        classes_text_list = {}
        for item in classes_content_list:
            if type(item) == QWidgetItem:
                classes_text_list[item.wid.ui.ClassNameLabel.text()] = item.wid.ui.ClassColorLabel.text()

        options_dict = self.options.get_options_dict()
        options_text_list = []
        for item in options_content_list:
            if type(item) == QWidgetItem and \
                    item.wid.ui.OptionName.isChecked():
                if options_dict[item.wid.ui.OptionName.text()]["type"] == "range":
                    options_text_list.append({'name': item.wid.ui.OptionName.text(),
                                              'type': options_dict[item.wid.ui.OptionName.text()]["type"],
                                              'range': {'start': int(item.wid.ui.StartLineEdit.text()),
                                                        'end': int(item.wid.ui.EndLineEdit.text()),
                                                        'step': int(item.wid.ui.StepLineEdit.text())
                                                        }})
                elif options_dict[item.wid.ui.OptionName.text()]["type"] == "resolution":
                    options_text_list.append({'name': item.wid.ui.OptionName.text(),
                                              'type': options_dict[item.wid.ui.OptionName.text()]["type"],
                                              'resolution': {'width': int(item.wid.ui.WidthLineEdit.text()),
                                                             'height': int(item.wid.ui.HeightLineEdit.text())
                                                             }})
                elif options_dict[item.wid.ui.OptionName.text()]["type"] == "folder":
                    folder_path = self.folders[item.wid.ui.OptionName.text()]
                    options_text_list.append({'name': item.wid.ui.OptionName.text(),
                                              'type': options_dict[item.wid.ui.OptionName.text()]["type"],
                                              'folder': folder_path})
                else:
                    options_text_list.append({'name': item.wid.ui.OptionName.text(),
                                              'type': options_dict[item.wid.ui.OptionName.text()]["type"]})

        return classes_text_list, options_text_list

    @staticmethod
    def layout_content_list(layout: QVBoxLayout) -> list[QWidgetItem]:
        """Returns the content of the received layout"""
        layout_objs = []
        for i in range(layout.count()):
            layout_objs.append(layout.itemAt(i))
        return layout_objs

    def fill_ClassesLayout(self, collections):
        """Function of filling ClassesScrollArea with appropriate widgets"""
        for obj in collections:
            self.add_ClassWidget(obj.name)

        # TODO: Manual appending background to classes
        self.add_ClassWidget("Scene Background")
        spacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.ui.ClassesLayout.addItem(spacer)

    def add_ClassWidget(self, name):
        """The function of adding widgets to the corresponding layout"""
        self.counter_id += 1
        widget = ClassWidget(self.counter_id)
        widget.ui.ClassNameLabel.setText(name)
        self.ui.ClassesLayout.addWidget(widget)

    def fill_OptionsLayout(self, options_list):
        """Function of filling OptionsScrollArea with appropriate widgets"""
        options_dict = self.options.get_options_dict()
        for option in options_list:
            self.add_OptionWidget(option, options_dict[option]["type"])
        spacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.ui.OptionsLayout.addItem(spacer)

    def add_OptionWidget(self, name, option_type):
        """The function of adding widgets to the corresponding layout"""
        # TODO: add option here
        self.counter_id += 1
        if option_type == "range":
            widget = RangeOptionWidget(self.counter_id)
            widget.ui.OptionName.setText(name)
            self.ui.OptionsLayout.addWidget(widget)
        elif option_type == "resolution":
            widget = ResolutionOptionWidget(self.counter_id)
            widget.ui.OptionName.setText(name)
            self.ui.OptionsLayout.addWidget(widget)
        elif option_type == "folder":
            widget = FolderOptionWidget(self.counter_id)
            widget.ui.OptionName.setText(name)
            widget.ui.FolderButton.clicked.connect(lambda: self.folder_button(widget))
            self.ui.OptionsLayout.addWidget(widget)
        else:
            widget = RegularOptionWidget(self.counter_id)
            widget.ui.OptionName.setText(name)
            self.ui.OptionsLayout.addWidget(widget)
