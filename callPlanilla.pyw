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
        self.ui.comboBoxArteria1.completer().setCompletionMode(QtGui.QCompleter.PopupCompletion)
        self.ui.comboBoxArteria2.completer().setCompletionMode(QtGui.QCompleter.PopupCompletion)
        self.ui.comboBoxV1.completer().setCompletionMode(QtGui.QCompleter.PopupCompletion)
        self.ui.comboBoxV2.completer().setCompletionMode(QtGui.QCompleter.PopupCompletion)
        self.ui.comboBoxV3.completer().setCompletionMode(QtGui.QCompleter.PopupCompletion)
        self.ui.comboBoxV4.completer().setCompletionMode(QtGui.QCompleter.PopupCompletion)
        self.ui.comboBoxSeguridad.completer().setCompletionMode(QtGui.QCompleter.PopupCompletion)
        self.ui.comboBoxSalud.completer().setCompletionMode(QtGui.QCompleter.PopupCompletion)
        self.ui.dateEdit.setDate(QtCore.QDate.currentDate())
        self.ui.spinBoxAltura.clear()
        QtCore.QObject.connect(self.ui.pushButtonAgregar,
                               QtCore.SIGNAL('clicked()'),
                               self.insertar)
        QtCore.QObject.connect(self.ui.pushButtonLimpiar,
                               QtCore.SIGNAL('clicked()'),
                               self.clearForm)
        QtCore.QObject.connect(self.ui.comboBoxInspector,
                               QtCore.SIGNAL('highlighted(QString)'),
                               self.ui.lineEditStatus.clear)
        self.populateCombo()
        self.clearForm()


    def insertar(self):
        inspectores = self.ui.comboBoxInspector.currentText()
        fecha = self.ui.dateEdit.date().toPyDate()
        hora_llegada = self.ui.timeEditLlegada.time().toString()
        calle_1 = self.ui.comboBoxCalle1.currentText()
        calle_2 = self.ui.comboBoxCalle2.currentText()
        tipo_arteria_1 = self.ui.comboBoxArteria1.currentText()
        tipo_arteria_2 = self.ui.comboBoxArteria2.currentText()
        altura = self.ui.spinBoxAltura.value()
        v_1 = self.ui.comboBoxV1.currentText()
        v_2 = self.ui.comboBoxV2.currentText()
        v_3 = self.ui.comboBoxV3.currentText()
        v_4 = self.ui.comboBoxV4.currentText()
        fuerza_seguridad = self.ui.comboBoxSeguridad.currentText()
        sistema_salud = self.ui.comboBoxSalud.currentText()

        insert(siniestros, inspectores=inspectores, fecha=fecha, hora_llegada=hora_llegada,
                   calle_1=calle_1, calle_2=calle_2, tipo_arteria_1=tipo_arteria_1,
                   tipo_arteria_2=tipo_arteria_2, altura=altura, v_1=v_1, v_2=v_2,
                   v_3=v_3, v_4=v_4, fuerza_seguridad=fuerza_seguridad, sistema_salud=sistema_salud)
        self.clearForm()
        self.ui.lineEditStatus.setText('Siniestro Agregado')

        #self.ui.lineEditStatus.setText('SINIESTRO NO AGREGADO')




    def populateCombo(self):
        fh = open('listas.csv', 'r')
        reader = csv.reader(fh)
        listas = [x for x in reader]
        fh.close()

        for item in listas:
            self.ui.comboBoxCalle1.addItem(item[0])
            self.ui.comboBoxCalle2.addItem(item[0])
            self.ui.comboBoxInspector.addItem(item[1])
            self.ui.comboBoxArteria1.addItem(item[2])
            self.ui.comboBoxArteria2.addItem(item[2])
            self.ui.comboBoxV1.addItem(item[3])
            self.ui.comboBoxV2.addItem(item[3])
            self.ui.comboBoxV3.addItem(item[3])
            self.ui.comboBoxV4.addItem(item[3])
            self.ui.comboBoxSeguridad.addItem(item[4])
            self.ui.comboBoxSalud.addItem(item[5])

    def clearForm(self):
        self.ui.comboBoxInspector.clearEditText()
        self.ui.comboBoxCalle1.clearEditText()
        self.ui.comboBoxCalle2.clearEditText()
        self.ui.comboBoxArteria1.clearEditText()
        self.ui.comboBoxArteria2.clearEditText()
        self.ui.comboBoxV1.clearEditText()
        self.ui.comboBoxV2.clearEditText()
        self.ui.comboBoxV3.clearEditText()
        self.ui.comboBoxV4.clearEditText()
        self.ui.comboBoxSeguridad.clearEditText()
        self.ui.comboBoxSalud.clearEditText()
        self.ui.lineEditStatus.clear()
        self.ui.spinBoxAltura.clear()


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    my_app = Form()
    my_app.show()
    sys.exit(app.exec_())

