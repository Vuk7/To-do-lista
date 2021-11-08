from ToDoListUI import Ui_Dialog

from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class ToDoList(QtWidgets.QDialog):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.ui = Ui_Dialog()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    
    aplikacija = ToDoList()
    aplikacija.show()
    sys.exit(app.exec_())

