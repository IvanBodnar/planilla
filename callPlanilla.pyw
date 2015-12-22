import sys
from planilla import *
from database import *
import csv
import sqlalchemy.exc



class Form(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.comboBoxInspector.completer().setCompletionMode(QtGui.QCompleter.PopupCompletion)
        self.ui.comboBoxCalle1.completer().setCompletionMode(QtGui.QCompleter.PopupCompletion)
        self.ui.comboBoxCalle2.completer().setCompletionMode(QtGui.QCompleter.PopupCompletion)
        self.ui.dateEdit.setDate(QtCore.QDate.currentDate())
        self.ui.spinBoxAltura.clear()
        QtCore.QObject.connect(self.ui.pushButtonAgregar,
                               QtCore.SIGNAL('clicked()'),
                               self.insertar)
        QtCore.QObject.connect(self.ui.pushButtonLimpiar,
                               QtCore.SIGNAL('clicked()'),
                               self.clearForm)
        self.populateCombo()
        self.clearForm()


    def insertar(self):
        id = self.ui.spinBoxId.value()
        inspectores = self.ui.comboBoxInspector.currentText()
        fecha = self.ui.dateEdit.date().toPyDate()
        hora_llegada = self.ui.timeEditLlegada.time().toString()
        calle_1 = self.ui.comboBoxCalle1.currentText()
        calle_2 = self.ui.comboBoxCalle2.currentText()
        altura = self.ui.spinBoxAltura.value()

        try:
            insert(siniestros, inspectores=inspectores, fecha=fecha, hora_llegada=hora_llegada,
                   calle_1=calle_1, calle_2=calle_2, altura=altura)
            self.clearForm()
            self.ui.lineEditStatus.setText('Siniestro Agregado')
        except:
            self.ui.lineEditStatus.setText('SINIESTRO NO AGREGADO')




    def populateCombo(self):
        fh = open('listas.csv', 'r')
        reader = csv.reader(fh)
        listas = [x for x in reader]
        fh.close()

        for item in listas:
            self.ui.comboBoxCalle1.addItem(item[0])
            self.ui.comboBoxCalle2.addItem(item[0])
            self.ui.comboBoxInspector.addItem(item[1])

    def clearForm(self):
        self.ui.comboBoxInspector.clearEditText()
        self.ui.comboBoxCalle1.clearEditText()
        self.ui.comboBoxCalle2.clearEditText()
        self.ui.lineEditStatus.clear()
        self.ui.spinBoxAltura.clear()

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    my_app = Form()
    my_app.show()
    sys.exit(app.exec_())

