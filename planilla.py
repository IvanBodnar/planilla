# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'planilla.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(694, 747)
        self.gridLayout = QtGui.QGridLayout(Dialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.tabWidget = QtGui.QTabWidget(Dialog)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab1 = QtGui.QWidget()
        self.tab1.setObjectName(_fromUtf8("tab1"))
        self.gridLayout_3 = QtGui.QGridLayout(self.tab1)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.groupBox = QtGui.QGroupBox(self.tab1)
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.horizontalLayout_6 = QtGui.QHBoxLayout(self.groupBox)
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(0, -1, 0, -1)
        self.horizontalLayout.setSpacing(20)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_7 = QtGui.QLabel(self.groupBox)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.horizontalLayout.addWidget(self.label_7)
        self.spinBoxId = QtGui.QSpinBox(self.groupBox)
        self.spinBoxId.setObjectName(_fromUtf8("spinBoxId"))
        self.horizontalLayout.addWidget(self.spinBoxId)
        self.label = QtGui.QLabel(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setSizeIncrement(QtCore.QSize(2, 0))
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.comboBoxInspector = QtGui.QComboBox(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBoxInspector.sizePolicy().hasHeightForWidth())
        self.comboBoxInspector.setSizePolicy(sizePolicy)
        self.comboBoxInspector.setEditable(True)
        self.comboBoxInspector.setMaxCount(50)
        self.comboBoxInspector.setObjectName(_fromUtf8("comboBoxInspector"))
        self.horizontalLayout.addWidget(self.comboBoxInspector)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setSizeConstraint(QtGui.QLayout.SetFixedSize)
        self.horizontalLayout_2.setSpacing(8)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_2.addWidget(self.label_2)
        self.dateEdit = QtGui.QDateEdit(self.groupBox)
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setObjectName(_fromUtf8("dateEdit"))
        self.horizontalLayout_2.addWidget(self.dateEdit)
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_2.addWidget(self.label_3)
        self.timeEditLlegada = QtGui.QTimeEdit(self.groupBox)
        self.timeEditLlegada.setObjectName(_fromUtf8("timeEditLlegada"))
        self.horizontalLayout_2.addWidget(self.timeEditLlegada)
        self.label_8 = QtGui.QLabel(self.groupBox)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.horizontalLayout_2.addWidget(self.label_8)
        self.timeEditSiniestro = QtGui.QTimeEdit(self.groupBox)
        self.timeEditSiniestro.setTime(QtCore.QTime(0, 0, 0))
        self.timeEditSiniestro.setCalendarPopup(False)
        self.timeEditSiniestro.setObjectName(_fromUtf8("timeEditSiniestro"))
        self.horizontalLayout_2.addWidget(self.timeEditSiniestro)
        self.horizontalLayout_2.setStretch(1, 1)
        self.horizontalLayout_2.setStretch(3, 1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_6.addLayout(self.verticalLayout)
        self.gridLayout_3.addWidget(self.groupBox, 0, 0, 1, 2)
        self.line = QtGui.QFrame(self.tab1)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.gridLayout_3.addWidget(self.line, 1, 0, 1, 2)
        self.groupBox_2 = QtGui.QGroupBox(self.tab1)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.comboBoxCalle1 = QtGui.QComboBox(self.groupBox_2)
        self.comboBoxCalle1.setEditable(True)
        self.comboBoxCalle1.setDuplicatesEnabled(False)
        self.comboBoxCalle1.setObjectName(_fromUtf8("comboBoxCalle1"))
        self.gridLayout_2.addWidget(self.comboBoxCalle1, 0, 1, 1, 1)
        self.label_4 = QtGui.QLabel(self.groupBox_2)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout_2.addWidget(self.label_4, 0, 0, 1, 1)
        self.comboBoxArteria2 = QtGui.QComboBox(self.groupBox_2)
        self.comboBoxArteria2.setEditable(True)
        self.comboBoxArteria2.setMaxCount(50)
        self.comboBoxArteria2.setObjectName(_fromUtf8("comboBoxArteria2"))
        self.gridLayout_2.addWidget(self.comboBoxArteria2, 1, 4, 1, 1)
        self.label_5 = QtGui.QLabel(self.groupBox_2)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout_2.addWidget(self.label_5, 1, 0, 1, 1)
        self.label_9 = QtGui.QLabel(self.groupBox_2)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.gridLayout_2.addWidget(self.label_9, 0, 3, 1, 1)
        self.comboBoxCalle2 = QtGui.QComboBox(self.groupBox_2)
        self.comboBoxCalle2.setEditable(True)
        self.comboBoxCalle2.setDuplicatesEnabled(False)
        self.comboBoxCalle2.setObjectName(_fromUtf8("comboBoxCalle2"))
        self.gridLayout_2.addWidget(self.comboBoxCalle2, 1, 1, 1, 1)
        self.comboBoxArteria1 = QtGui.QComboBox(self.groupBox_2)
        self.comboBoxArteria1.setEditable(True)
        self.comboBoxArteria1.setMaxCount(50)
        self.comboBoxArteria1.setObjectName(_fromUtf8("comboBoxArteria1"))
        self.gridLayout_2.addWidget(self.comboBoxArteria1, 0, 4, 1, 1)
        self.label_10 = QtGui.QLabel(self.groupBox_2)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.gridLayout_2.addWidget(self.label_10, 1, 3, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 0, 2, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 1, 2, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_6 = QtGui.QLabel(self.groupBox_2)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout_3.addWidget(self.label_6)
        self.spinBoxAltura = QtGui.QSpinBox(self.groupBox_2)
        self.spinBoxAltura.setSizeIncrement(QtCore.QSize(37, 0))
        self.spinBoxAltura.setBaseSize(QtCore.QSize(20, 0))
        self.spinBoxAltura.setObjectName(_fromUtf8("spinBoxAltura"))
        self.horizontalLayout_3.addWidget(self.spinBoxAltura)
        spacerItem2 = QtGui.QSpacerItem(30, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.horizontalLayout_3.setStretch(1, 1)
        self.horizontalLayout_3.setStretch(2, 1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.gridLayout_3.addWidget(self.groupBox_2, 2, 0, 1, 2)
        self.line_2 = QtGui.QFrame(self.tab1)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.gridLayout_3.addWidget(self.line_2, 3, 0, 1, 2)
        self.groupBox_4 = QtGui.QGroupBox(self.tab1)
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.gridLayout_5 = QtGui.QGridLayout(self.groupBox_4)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.gridLayout_4 = QtGui.QGridLayout()
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.label_24 = QtGui.QLabel(self.groupBox_4)
        self.label_24.setObjectName(_fromUtf8("label_24"))
        self.gridLayout_4.addWidget(self.label_24, 0, 0, 1, 1)
        self.label_25 = QtGui.QLabel(self.groupBox_4)
        self.label_25.setObjectName(_fromUtf8("label_25"))
        self.gridLayout_4.addWidget(self.label_25, 1, 0, 1, 1)
        self.comboBoxV1 = QtGui.QComboBox(self.groupBox_4)
        self.comboBoxV1.setEditable(True)
        self.comboBoxV1.setMaxCount(30)
        self.comboBoxV1.setObjectName(_fromUtf8("comboBoxV1"))
        self.gridLayout_4.addWidget(self.comboBoxV1, 0, 1, 1, 1)
        self.comboBoxV3 = QtGui.QComboBox(self.groupBox_4)
        self.comboBoxV3.setEditable(True)
        self.comboBoxV3.setMaxCount(30)
        self.comboBoxV3.setObjectName(_fromUtf8("comboBoxV3"))
        self.gridLayout_4.addWidget(self.comboBoxV3, 1, 1, 1, 1)
        self.label_26 = QtGui.QLabel(self.groupBox_4)
        self.label_26.setObjectName(_fromUtf8("label_26"))
        self.gridLayout_4.addWidget(self.label_26, 0, 2, 1, 1)
        self.label_27 = QtGui.QLabel(self.groupBox_4)
        self.label_27.setObjectName(_fromUtf8("label_27"))
        self.gridLayout_4.addWidget(self.label_27, 1, 2, 1, 1)
        self.comboBoxV2 = QtGui.QComboBox(self.groupBox_4)
        self.comboBoxV2.setEditable(True)
        self.comboBoxV2.setMaxCount(30)
        self.comboBoxV2.setObjectName(_fromUtf8("comboBoxV2"))
        self.gridLayout_4.addWidget(self.comboBoxV2, 0, 3, 1, 1)
        self.comboBoxV4 = QtGui.QComboBox(self.groupBox_4)
        self.comboBoxV4.setEditable(True)
        self.comboBoxV4.setMaxCount(30)
        self.comboBoxV4.setObjectName(_fromUtf8("comboBoxV4"))
        self.gridLayout_4.addWidget(self.comboBoxV4, 1, 3, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_4, 0, 0, 1, 1)
        self.gridLayout_3.addWidget(self.groupBox_4, 4, 0, 1, 1)
        self.groupBox_3 = QtGui.QGroupBox(self.tab1)
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_11 = QtGui.QLabel(self.groupBox_3)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.horizontalLayout_4.addWidget(self.label_11)
        self.comboBoxSeguridad = QtGui.QComboBox(self.groupBox_3)
        self.comboBoxSeguridad.setEditable(True)
        self.comboBoxSeguridad.setMaxCount(10)
        self.comboBoxSeguridad.setObjectName(_fromUtf8("comboBoxSeguridad"))
        self.horizontalLayout_4.addWidget(self.comboBoxSeguridad)
        self.label_12 = QtGui.QLabel(self.groupBox_3)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.horizontalLayout_4.addWidget(self.label_12)
        self.comboBoxSalud = QtGui.QComboBox(self.groupBox_3)
        self.comboBoxSalud.setEditable(True)
        self.comboBoxSalud.setMaxCount(10)
        self.comboBoxSalud.setObjectName(_fromUtf8("comboBoxSalud"))
        self.horizontalLayout_4.addWidget(self.comboBoxSalud)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.gridLayout_3.addWidget(self.groupBox_3, 5, 0, 1, 2)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem3)
        self.pushButtonAgregar = QtGui.QPushButton(self.tab1)
        self.pushButtonAgregar.setObjectName(_fromUtf8("pushButtonAgregar"))
        self.horizontalLayout_5.addWidget(self.pushButtonAgregar)
        self.pushButtonLimpiar = QtGui.QPushButton(self.tab1)
        self.pushButtonLimpiar.setIconSize(QtCore.QSize(20, 20))
        self.pushButtonLimpiar.setObjectName(_fromUtf8("pushButtonLimpiar"))
        self.horizontalLayout_5.addWidget(self.pushButtonLimpiar)
        self.gridLayout_3.addLayout(self.horizontalLayout_5, 6, 0, 1, 1)
        self.lineEditStatus = QtGui.QLineEdit(self.tab1)
        self.lineEditStatus.setObjectName(_fromUtf8("lineEditStatus"))
        self.gridLayout_3.addWidget(self.lineEditStatus, 7, 0, 1, 1)
        spacerItem4 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem4, 8, 1, 1, 1)
        self.line.raise_()
        self.line_2.raise_()
        self.lineEditStatus.raise_()
        self.groupBox.raise_()
        self.groupBox_2.raise_()
        self.groupBox_4.raise_()
        self.label_6.raise_()
        self.groupBox_3.raise_()
        self.tabWidget.addTab(self.tab1, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Observatorio Vial - DGSV", None))
        self.label_7.setText(_translate("Dialog", "ID:", None))
        self.label.setText(_translate("Dialog", "Inspectores:", None))
        self.label_2.setText(_translate("Dialog", "Fecha:", None))
        self.label_3.setText(_translate("Dialog", "Hora Llegada:", None))
        self.label_8.setText(_translate("Dialog", "Hora Siniestro:", None))
        self.groupBox_2.setTitle(_translate("Dialog", "Ubicacion", None))
        self.label_4.setText(_translate("Dialog", "Calle 1:", None))
        self.label_5.setText(_translate("Dialog", "Calle 2:", None))
        self.label_9.setText(_translate("Dialog", "Tipo Arteria 1:", None))
        self.label_10.setText(_translate("Dialog", "Tipo Arteria 2:", None))
        self.label_6.setText(_translate("Dialog", "Altura:", None))
        self.groupBox_4.setTitle(_translate("Dialog", "Vehiculos", None))
        self.label_24.setText(_translate("Dialog", "Vehiculo 1:", None))
        self.label_25.setText(_translate("Dialog", "Vehiculo 3:", None))
        self.label_26.setText(_translate("Dialog", "Vehiculo 2:", None))
        self.label_27.setText(_translate("Dialog", "Vehiculo 4:", None))
        self.groupBox_3.setTitle(_translate("Dialog", "Organismos Intervinientes", None))
        self.label_11.setText(_translate("Dialog", "Fuerza de Seguridad:", None))
        self.label_12.setText(_translate("Dialog", "Sistema de Salud:", None))
        self.pushButtonAgregar.setText(_translate("Dialog", "Agregar Siniestro", None))
        self.pushButtonLimpiar.setText(_translate("Dialog", "Limpiar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab1), _translate("Dialog", "Datos Siniestro", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "Tab 2", None))

