import sys
from planilla import *
from database import *
import csv



class Form(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.comboBoxInspector.completer().setCompletionMode(QtGui.QCompleter.PopupCompletion)
        self.ui.comboBoxCalle1.completer().setCompletionMode(QtGui.QCompleter.PopupCompletion)
        self.ui.comboBoxCalle2.completer().setCompletionMode(QtGui.QCompleter.PopupCompletion)
        QtCore.QObject.connect(self.ui.pushButton,
                               QtCore.SIGNAL('clicked()'),
                               self.insertar)
        self.populateCombo()

    def insertar(self):
        id = self.ui.spinBoxId.value()
        inspectores = self.ui.comboBoxInspector.currentText()
        fecha = self.ui.dateEdit.date().toPyDate()
        hora = self.ui.timeEditLlegada.time().toString()
        calle1 = self.ui.comboBoxCalle1.currentText()
        calle2 = self.ui.comboBoxCalle2.currentText()
        insert(siniestros, id, inspectores, fecha, hora, calle1, calle2)

    def populateCombo(self):
        fh = open('listas.csv', 'r')
        reader = csv.reader(fh)
        listas = [x for x in reader]
        fh.close()

        for item in listas:
            self.ui.comboBoxCalle1.addItem(item[0])
            self.ui.comboBoxCalle2.addItem(item[0])
            self.ui.comboBoxInspector.addItem(item[1])


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    my_app = Form()
    my_app.show()
    sys.exit(app.exec_())

