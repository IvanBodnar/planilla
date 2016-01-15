import sys
from planilla import *
from database import *
import csv


class Form(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        connect_qt()
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
        self.ui.comboBoxSexo.completer().setCompletionMode(QtGui.QCompleter.PopupCompletion)
        self.ui.comboBoxHospital.completer().setCompletionMode(QtGui.QCompleter.PopupCompletion)
        self.ui.comboBoxCausa.completer().setCompletionMode(QtGui.QCompleter.PopupCompletion)
        self.ui.dateEdit.setDate(QtCore.QDate.currentDate())
        self.ui.spinBoxAltura.clear()
        if max_id():
            self.ui.spinBoxIDVictimas.setValue(max_id())
        QtCore.QObject.connect(self.ui.pushButtonAgregar,
                               QtCore.SIGNAL('clicked()'),
                               self.confirmation)
        QtCore.QObject.connect(self.ui.pushButtonLimpiar,
                               QtCore.SIGNAL('clicked()'),
                               self.clear_form_siniestros)
        QtCore.QObject.connect(self.ui.comboBoxInspector,
                               QtCore.SIGNAL('activated(QString)'),
                               self.ui.labelStatusSiniestros.clear)
        QtCore.QObject.connect(self.ui.comboBoxSexo,
                               QtCore.SIGNAL('activated(QString)'),
                               self.ui.labelStatusVictimas.clear)
        QtCore.QObject.connect(self.ui.pushButtonMostrarTabla,
                               QtCore.SIGNAL('clicked()'),
                               self.populate_table)
        QtCore.QObject.connect(self.ui.pushButtonAgregarVictima,
                               QtCore.SIGNAL('clicked()'),
                               self.confirmation)
        QtCore.QObject.connect(self.ui.pushButtonLimpiarVictima,
                               QtCore.SIGNAL('clicked()'),
                               self.clear_form_victimas)
        self.populate_combo()
        self.clear_form_siniestros()
        self.clear_form_victimas()
        self.ui.spinBoxHomicidio.setValue(0)
        self.model = QtSql.QSqlTableModel(self)


    def insertar_siniestro(self):
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
        total_victimas = self.ui.spinBoxCantidaVictimas.value()
        homicidio = self.ui.spinBoxHomicidio.value()
        observaciones = self.ui.plainTextEditObservaciones.toPlainText()

        insert_siniestro(siniestros, inspectores=inspectores, fecha=fecha, hora_llegada=hora_llegada,
                         calle_1=calle_1, calle_2=calle_2, tipo_arteria_1=tipo_arteria_1,
                         tipo_arteria_2=tipo_arteria_2, altura=altura, v_1=v_1, v_2=v_2,
                         v_3=v_3, v_4=v_4, fuerza_seguridad=fuerza_seguridad,
                         sistema_salud=sistema_salud, total_victimas=total_victimas,
                         homicidio=homicidio, observaciones=observaciones)
        self.clear_form_siniestros()
        self.ui.labelStatusSiniestros.setText('Siniestro Agregado')
        self.ui.spinBoxIDVictimas.setValue(max_id())
        self.ui.spinBoxHomicidio.setValue(0)


        #self.ui.lineEditStatus.setText('SINIESTRO NO AGREGADO')


    def insertar_victima(self):
        siniestro_id = self.ui.spinBoxIDVictimas.value()
        sexo = self.ui.comboBoxSexo.currentText()
        edad = self.ui.spinBoxEdad.value()
        hospital_deriva = self.ui.comboBoxHospital.currentText()
        causa = self.ui.comboBoxCausa.currentText()

        insert_victima(victimas, siniestro_id=siniestro_id, sexo=sexo,
                       edad=edad, hospital_deriva=hospital_deriva, causa=causa)
        self.clear_form_victimas()
        self.ui.labelStatusVictimas.setText('Victima Agregada')



    def populate_combo(self):
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
            self.ui.comboBoxSexo.addItem(item[6])
            self.ui.comboBoxHospital.addItem(item[7])
            self.ui.comboBoxCausa.addItem(item[8])

    def clear_form_siniestros(self):
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
        self.ui.labelStatusSiniestros.clear()
        self.ui.spinBoxAltura.clear()
        self.ui.spinBoxCantidaVictimas.clear()
        self.ui.spinBoxHomicidio.clear()
        self.ui.plainTextEditObservaciones.clear()
        self.ui.labelStatusVictimas.clear()

    def clear_form_victimas(self):
        self.ui.comboBoxSexo.clearEditText()
        self.ui.spinBoxEdad.clear()
        self.ui.comboBoxHospital.clearEditText()
        self.ui.comboBoxCausa.clearEditText()
        self.ui.labelStatusVictimas.clear()

    def populate_table(self):
        if self.ui.radioButtonSiniestros.isChecked():
            table = "siniestros"
            self.model = QtSql.QSqlTableModel(self)
            self.model.setTable(table)
        elif self.ui.radioButtonVictimas.isChecked():
            table = "victimas"
            self.model = QtSql.QSqlTableModel(self)
            self.model.setTable(table)

        self.model.setEditStrategy(QtSql.QSqlTableModel.OnManualSubmit)
        self.model.select()
        self.ui.tableViewMostrar.setModel(self.model)

    def confirmation(self):
        msg = 'Agregar dato?'
        reply = QtGui.QMessageBox.question(self, 'Message', msg, QtGui.QMessageBox.Yes,
                                   QtGui.QMessageBox.No)
        sender = self.sender()

        if sender.text() == 'Agregar Siniestro':
            if reply == QtGui.QMessageBox.Yes:
                self.insertar_siniestro()
            else:
                self.ui.labelStatusSiniestros.setText('El Dato No Fue Agregado')
        elif sender.text() == 'Agregar Victima':
            if reply == QtGui.QMessageBox.Yes:
                self.insertar_victima()
            else:
                self.ui.labelStatusVictimas.setText('El Dato No Fue Agregado')


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    if not connect_qt():
        sys.exit(1)
    my_app = Form()
    my_app.show()
    sys.exit(app.exec_())

