import sys
from PySide6 import QtCore as qtc
from PySide6 import QtWidgets as qtw
from PySide6 import QtGui as qtg

from UI.add_person_window_ui import Ui_d_Person


class AddPerson(qtw.QDialog, Ui_d_Person):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)

    form = AddPerson()
    form.show()

    sys.exit(app.exec_())
