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
        Dialog.resize(714, 844)
        self.gridLayout = QtGui.QGridLayout(Dialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.tabWidgetSiniestro = QtGui.QTabWidget(Dialog)
        self.tabWidgetSiniestro.setObjectName(_fromUtf8("tabWidgetSiniestro"))
        self.tab1 = QtGui.QWidget()
        self.tab1.setObjectName(_fromUtf8("tab1"))
        self.gridLayout_9 = QtGui.QGridLayout(self.tab1)
        self.gridLayout_9.setObjectName(_fromUtf8("gridLayout_9"))
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
        self.gridLayout_9.addWidget(self.groupBox, 0, 0, 1, 1)
        self.line = QtGui.QFrame(self.tab1)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.gridLayout_9.addWidget(self.line, 1, 0, 1, 2)
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
        self.spinBoxAltura.setMaximum(13000)
        self.spinBoxAltura.setProperty("value", 0)
        self.spinBoxAltura.setObjectName(_fromUtf8("spinBoxAltura"))
        self.horizontalLayout_3.addWidget(self.spinBoxAltura)
        spacerItem2 = QtGui.QSpacerItem(30, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.horizontalLayout_3.setStretch(1, 1)
        self.horizontalLayout_3.setStretch(2, 1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.gridLayout_9.addWidget(self.groupBox_2, 2, 0, 1, 1)
        self.line_2 = QtGui.QFrame(self.tab1)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.gridLayout_9.addWidget(self.line_2, 3, 0, 1, 2)
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
        self.gridLayout_9.addWidget(self.groupBox_4, 4, 0, 1, 1)
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
        self.gridLayout_9.addWidget(self.groupBox_3, 5, 0, 1, 1)
        self.groupBox_7 = QtGui.QGroupBox(self.tab1)
        self.groupBox_7.setObjectName(_fromUtf8("groupBox_7"))
        self.horizontalLayout_10 = QtGui.QHBoxLayout(self.groupBox_7)
        self.horizontalLayout_10.setObjectName(_fromUtf8("horizontalLayout_10"))
        self.label_16 = QtGui.QLabel(self.groupBox_7)
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.horizontalLayout_10.addWidget(self.label_16)
        self.spinBoxCantidaVictimas = QtGui.QSpinBox(self.groupBox_7)
        self.spinBoxCantidaVictimas.setObjectName(_fromUtf8("spinBoxCantidaVictimas"))
        self.horizontalLayout_10.addWidget(self.spinBoxCantidaVictimas)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem3)
        self.label_17 = QtGui.QLabel(self.groupBox_7)
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.horizontalLayout_10.addWidget(self.label_17)
        self.spinBoxHomicidio = QtGui.QSpinBox(self.groupBox_7)
        self.spinBoxHomicidio.setMaximum(1)
        self.spinBoxHomicidio.setObjectName(_fromUtf8("spinBoxHomicidio"))
        self.horizontalLayout_10.addWidget(self.spinBoxHomicidio)
        self.horizontalLayout_10.setStretch(0, 1)
        self.horizontalLayout_10.setStretch(1, 1)
        self.horizontalLayout_10.setStretch(3, 1)
        self.horizontalLayout_10.setStretch(4, 1)
        self.gridLayout_9.addWidget(self.groupBox_7, 6, 0, 1, 1)
        self.groupBox_5 = QtGui.QGroupBox(self.tab1)
        self.groupBox_5.setObjectName(_fromUtf8("groupBox_5"))
        self.gridLayout_3 = QtGui.QGridLayout(self.groupBox_5)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.plainTextEditObservaciones = QtGui.QPlainTextEdit(self.groupBox_5)
        self.plainTextEditObservaciones.setObjectName(_fromUtf8("plainTextEditObservaciones"))
        self.gridLayout_3.addWidget(self.plainTextEditObservaciones, 0, 0, 1, 1)
        self.gridLayout_9.addWidget(self.groupBox_5, 7, 0, 1, 2)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem4)
        self.pushButtonAgregar = QtGui.QPushButton(self.tab1)
        self.pushButtonAgregar.setObjectName(_fromUtf8("pushButtonAgregar"))
        self.horizontalLayout_5.addWidget(self.pushButtonAgregar)
        self.pushButtonLimpiar = QtGui.QPushButton(self.tab1)
        self.pushButtonLimpiar.setIconSize(QtCore.QSize(20, 20))
        self.pushButtonLimpiar.setObjectName(_fromUtf8("pushButtonLimpiar"))
        self.horizontalLayout_5.addWidget(self.pushButtonLimpiar)
        self.gridLayout_9.addLayout(self.horizontalLayout_5, 8, 0, 1, 1)
        self.labelStatusSiniestros = QtGui.QLabel(self.tab1)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.labelStatusSiniestros.setFont(font)
        self.labelStatusSiniestros.setText(_fromUtf8(""))
        self.labelStatusSiniestros.setObjectName(_fromUtf8("labelStatusSiniestros"))
        self.gridLayout_9.addWidget(self.labelStatusSiniestros, 9, 0, 1, 1)
        spacerItem5 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_9.addItem(spacerItem5, 9, 1, 1, 1)
        self.line.raise_()
        self.line_2.raise_()
        self.groupBox.raise_()
        self.groupBox_2.raise_()
        self.groupBox_4.raise_()
        self.groupBox_3.raise_()
        self.groupBox_5.raise_()
        self.groupBox_7.raise_()
        self.labelStatusSiniestros.raise_()
        self.tabWidgetSiniestro.addTab(self.tab1, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.gridLayout_7 = QtGui.QGridLayout(self.tab_2)
        self.gridLayout_7.setObjectName(_fromUtf8("gridLayout_7"))
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem6)
        self.pushButtonAgregarVictima = QtGui.QPushButton(self.tab_2)
        self.pushButtonAgregarVictima.setObjectName(_fromUtf8("pushButtonAgregarVictima"))
        self.horizontalLayout_9.addWidget(self.pushButtonAgregarVictima)
        self.pushButtonLimpiarVictima = QtGui.QPushButton(self.tab_2)
        self.pushButtonLimpiarVictima.setObjectName(_fromUtf8("pushButtonLimpiarVictima"))
        self.horizontalLayout_9.addWidget(self.pushButtonLimpiarVictima)
        self.gridLayout_7.addLayout(self.horizontalLayout_9, 1, 0, 1, 1)
        self.groupBox_6 = QtGui.QGroupBox(self.tab_2)
        self.groupBox_6.setTitle(_fromUtf8(""))
        self.groupBox_6.setObjectName(_fromUtf8("groupBox_6"))
        self.gridLayout_8 = QtGui.QGridLayout(self.groupBox_6)
        self.gridLayout_8.setObjectName(_fromUtf8("gridLayout_8"))
        self.comboBoxHospital = QtGui.QComboBox(self.groupBox_6)
        self.comboBoxHospital.setEditable(True)
        self.comboBoxHospital.setMaxCount(50)
        self.comboBoxHospital.setObjectName(_fromUtf8("comboBoxHospital"))
        self.gridLayout_8.addWidget(self.comboBoxHospital, 1, 3, 1, 1)
        self.spinBoxEdad = QtGui.QSpinBox(self.groupBox_6)
        self.spinBoxEdad.setMaximum(120)
        self.spinBoxEdad.setObjectName(_fromUtf8("spinBoxEdad"))
        self.gridLayout_8.addWidget(self.spinBoxEdad, 1, 1, 1, 1)
        self.label_14 = QtGui.QLabel(self.groupBox_6)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.gridLayout_8.addWidget(self.label_14, 1, 2, 1, 1)
        self.label_13 = QtGui.QLabel(self.groupBox_6)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.gridLayout_8.addWidget(self.label_13, 0, 2, 1, 1)
        self.label_7 = QtGui.QLabel(self.groupBox_6)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout_8.addWidget(self.label_7, 0, 0, 1, 1)
        self.spinBoxIDVictimas = QtGui.QSpinBox(self.groupBox_6)
        self.spinBoxIDVictimas.setMaximum(2000)
        self.spinBoxIDVictimas.setObjectName(_fromUtf8("spinBoxIDVictimas"))
        self.gridLayout_8.addWidget(self.spinBoxIDVictimas, 0, 1, 1, 1)
        self.comboBoxSexo = QtGui.QComboBox(self.groupBox_6)
        self.comboBoxSexo.setEditable(True)
        self.comboBoxSexo.setMaxCount(2)
        self.comboBoxSexo.setObjectName(_fromUtf8("comboBoxSexo"))
        self.gridLayout_8.addWidget(self.comboBoxSexo, 0, 3, 1, 1)
        self.label_15 = QtGui.QLabel(self.groupBox_6)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.gridLayout_8.addWidget(self.label_15, 1, 0, 1, 1)
        self.label_18 = QtGui.QLabel(self.groupBox_6)
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.gridLayout_8.addWidget(self.label_18, 2, 0, 1, 1)
        self.comboBoxCausa = QtGui.QComboBox(self.groupBox_6)
        self.comboBoxCausa.setEditable(True)
        self.comboBoxCausa.setMaxCount(2)
        self.comboBoxCausa.setObjectName(_fromUtf8("comboBoxCausa"))
        self.gridLayout_8.addWidget(self.comboBoxCausa, 2, 1, 1, 1)
        self.gridLayout_7.addWidget(self.groupBox_6, 0, 0, 1, 1)
        spacerItem7 = QtGui.QSpacerItem(20, 595, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_7.addItem(spacerItem7, 3, 0, 1, 1)
        self.labelStatusVictimas = QtGui.QLabel(self.tab_2)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.labelStatusVictimas.setFont(font)
        self.labelStatusVictimas.setText(_fromUtf8(""))
        self.labelStatusVictimas.setObjectName(_fromUtf8("labelStatusVictimas"))
        self.gridLayout_7.addWidget(self.labelStatusVictimas, 2, 0, 1, 1)
        self.tabWidgetSiniestro.addTab(self.tab_2, _fromUtf8(""))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.gridLayout_6 = QtGui.QGridLayout(self.tab)
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.tableViewMostrar = QtGui.QTableView(self.tab)
        self.tableViewMostrar.setObjectName(_fromUtf8("tableViewMostrar"))
        self.gridLayout_6.addWidget(self.tableViewMostrar, 0, 0, 1, 2)
        spacerItem8 = QtGui.QSpacerItem(411, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem8, 1, 0, 1, 1)
        self.widget = QtGui.QWidget(self.tab)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.horizontalLayout_8 = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.radioButtonSiniestros = QtGui.QRadioButton(self.widget)
        self.radioButtonSiniestros.setObjectName(_fromUtf8("radioButtonSiniestros"))
        self.verticalLayout_4.addWidget(self.radioButtonSiniestros)
        self.radioButtonVictimas = QtGui.QRadioButton(self.widget)
        self.radioButtonVictimas.setObjectName(_fromUtf8("radioButtonVictimas"))
        self.verticalLayout_4.addWidget(self.radioButtonVictimas)
        self.horizontalLayout_8.addLayout(self.verticalLayout_4)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.pushButtonMostrarTabla = QtGui.QPushButton(self.widget)
        self.pushButtonMostrarTabla.setObjectName(_fromUtf8("pushButtonMostrarTabla"))
        self.horizontalLayout_7.addWidget(self.pushButtonMostrarTabla)
        self.horizontalLayout_8.addLayout(self.horizontalLayout_7)
        self.gridLayout_6.addWidget(self.widget, 1, 1, 1, 1)
        self.tabWidgetSiniestro.addTab(self.tab, _fromUtf8(""))
        self.gridLayout.addWidget(self.tabWidgetSiniestro, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        self.tabWidgetSiniestro.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.tabWidgetSiniestro, self.comboBoxInspector)
        Dialog.setTabOrder(self.comboBoxInspector, self.dateEdit)
        Dialog.setTabOrder(self.dateEdit, self.timeEditLlegada)
        Dialog.setTabOrder(self.timeEditLlegada, self.timeEditSiniestro)
        Dialog.setTabOrder(self.timeEditSiniestro, self.comboBoxCalle1)
        Dialog.setTabOrder(self.comboBoxCalle1, self.comboBoxCalle2)
        Dialog.setTabOrder(self.comboBoxCalle2, self.comboBoxArteria1)
        Dialog.setTabOrder(self.comboBoxArteria1, self.comboBoxArteria2)
        Dialog.setTabOrder(self.comboBoxArteria2, self.spinBoxAltura)
        Dialog.setTabOrder(self.spinBoxAltura, self.comboBoxV1)
        Dialog.setTabOrder(self.comboBoxV1, self.comboBoxV2)
        Dialog.setTabOrder(self.comboBoxV2, self.comboBoxV3)
        Dialog.setTabOrder(self.comboBoxV3, self.comboBoxV4)
        Dialog.setTabOrder(self.comboBoxV4, self.comboBoxSeguridad)
        Dialog.setTabOrder(self.comboBoxSeguridad, self.comboBoxSalud)
        Dialog.setTabOrder(self.comboBoxSalud, self.spinBoxCantidaVictimas)
        Dialog.setTabOrder(self.spinBoxCantidaVictimas, self.plainTextEditObservaciones)
        Dialog.setTabOrder(self.plainTextEditObservaciones, self.pushButtonAgregar)
        Dialog.setTabOrder(self.pushButtonAgregar, self.pushButtonLimpiar)
        Dialog.setTabOrder(self.pushButtonLimpiar, self.spinBoxIDVictimas)
        Dialog.setTabOrder(self.spinBoxIDVictimas, self.comboBoxSexo)
        Dialog.setTabOrder(self.comboBoxSexo, self.spinBoxEdad)
        Dialog.setTabOrder(self.spinBoxEdad, self.comboBoxHospital)
        Dialog.setTabOrder(self.comboBoxHospital, self.comboBoxCausa)
        Dialog.setTabOrder(self.comboBoxCausa, self.pushButtonAgregarVictima)
        Dialog.setTabOrder(self.pushButtonAgregarVictima, self.pushButtonLimpiarVictima)
        Dialog.setTabOrder(self.pushButtonLimpiarVictima, self.tableViewMostrar)
        Dialog.setTabOrder(self.tableViewMostrar, self.radioButtonSiniestros)
        Dialog.setTabOrder(self.radioButtonSiniestros, self.radioButtonVictimas)
        Dialog.setTabOrder(self.radioButtonVictimas, self.pushButtonMostrarTabla)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Observatorio Vial - DGSV", None))
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
        self.groupBox_7.setTitle(_translate("Dialog", "Victimas", None))
        self.label_16.setText(_translate("Dialog", "Total Victimas", None))
        self.label_17.setText(_translate("Dialog", "Homicidio", None))
        self.groupBox_5.setTitle(_translate("Dialog", "Observaciones", None))
        self.pushButtonAgregar.setText(_translate("Dialog", "Agregar Siniestro", None))
        self.pushButtonLimpiar.setText(_translate("Dialog", "Limpiar", None))
        self.tabWidgetSiniestro.setTabText(self.tabWidgetSiniestro.indexOf(self.tab1), _translate("Dialog", "Datos Siniestro", None))
        self.pushButtonAgregarVictima.setText(_translate("Dialog", "Agregar Victima", None))
        self.pushButtonLimpiarVictima.setText(_translate("Dialog", "Limpiar", None))
        self.label_14.setText(_translate("Dialog", "Hospital Deriva:", None))
        self.label_13.setText(_translate("Dialog", "Sexo:", None))
        self.label_7.setText(_translate("Dialog", "ID Siniestro:", None))
        self.label_15.setText(_translate("Dialog", "Edad:", None))
        self.label_18.setText(_translate("Dialog", "Causa:", None))
        self.tabWidgetSiniestro.setTabText(self.tabWidgetSiniestro.indexOf(self.tab_2), _translate("Dialog", "Datos Victimas", None))
        self.radioButtonSiniestros.setText(_translate("Dialog", "Tabla Siniestros", None))
        self.radioButtonVictimas.setText(_translate("Dialog", "Tabla Victimas", None))
        self.pushButtonMostrarTabla.setText(_translate("Dialog", "Mostrar", None))
        self.tabWidgetSiniestro.setTabText(self.tabWidgetSiniestro.indexOf(self.tab), _translate("Dialog", "Consultas", None))

