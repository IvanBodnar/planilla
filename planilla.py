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
        Dialog.resize(651, 754)
        self.gridLayout = QtGui.QGridLayout(Dialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.tabWidget = QtGui.QTabWidget(Dialog)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab1 = QtGui.QWidget()
        self.tab1.setObjectName(_fromUtf8("tab1"))
        self.gridLayout_3 = QtGui.QGridLayout(self.tab1)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.line = QtGui.QFrame(self.tab1)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.gridLayout_3.addWidget(self.line, 1, 0, 1, 1)
        self.line_2 = QtGui.QFrame(self.tab1)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.gridLayout_3.addWidget(self.line_2, 3, 0, 1, 1)
        self.listView = QtGui.QListView(self.tab1)
        self.listView.setObjectName(_fromUtf8("listView"))
        self.gridLayout_3.addWidget(self.listView, 5, 0, 1, 1)
        self.pushButton = QtGui.QPushButton(self.tab1)
        self.pushButton.setIconSize(QtCore.QSize(20, 20))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout_3.addWidget(self.pushButton, 4, 0, 1, 1)
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_4 = QtGui.QLabel(self.tab1)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_3.addWidget(self.label_4)
        self.comboBoxCalle1 = QtGui.QComboBox(self.tab1)
        self.comboBoxCalle1.setEditable(True)
        self.comboBoxCalle1.setDuplicatesEnabled(False)
        self.comboBoxCalle1.setObjectName(_fromUtf8("comboBoxCalle1"))
        self.horizontalLayout_3.addWidget(self.comboBoxCalle1)
        self.label_5 = QtGui.QLabel(self.tab1)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_3.addWidget(self.label_5)
        self.comboBoxCalle2 = QtGui.QComboBox(self.tab1)
        self.comboBoxCalle2.setEditable(True)
        self.comboBoxCalle2.setDuplicatesEnabled(False)
        self.comboBoxCalle2.setObjectName(_fromUtf8("comboBoxCalle2"))
        self.horizontalLayout_3.addWidget(self.comboBoxCalle2)
        self.horizontalLayout_3.setStretch(1, 1)
        self.horizontalLayout_3.setStretch(3, 1)
        self.gridLayout_2.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.horizontalLayout_4.setContentsMargins(1, 0, 100, -1)
        self.horizontalLayout_4.setSpacing(7)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_6 = QtGui.QLabel(self.tab1)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout_4.addWidget(self.label_6)
        self.spinBoxAltura = QtGui.QSpinBox(self.tab1)
        self.spinBoxAltura.setSizeIncrement(QtCore.QSize(37, 0))
        self.spinBoxAltura.setBaseSize(QtCore.QSize(20, 0))
        self.spinBoxAltura.setObjectName(_fromUtf8("spinBoxAltura"))
        self.horizontalLayout_4.addWidget(self.spinBoxAltura)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.horizontalLayout_4.setStretch(1, 1)
        self.horizontalLayout_4.setStretch(2, 1)
        self.gridLayout_2.addLayout(self.horizontalLayout_4, 1, 0, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 2, 0, 1, 1)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(0, -1, 0, -1)
        self.horizontalLayout.setSpacing(20)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_7 = QtGui.QLabel(self.tab1)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.horizontalLayout.addWidget(self.label_7)
        self.spinBoxId = QtGui.QSpinBox(self.tab1)
        self.spinBoxId.setObjectName(_fromUtf8("spinBoxId"))
        self.horizontalLayout.addWidget(self.spinBoxId)
        self.label = QtGui.QLabel(self.tab1)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setSizeIncrement(QtCore.QSize(2, 0))
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.comboBoxInspector = QtGui.QComboBox(self.tab1)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBoxInspector.sizePolicy().hasHeightForWidth())
        self.comboBoxInspector.setSizePolicy(sizePolicy)
        self.comboBoxInspector.setEditable(True)
        self.comboBoxInspector.setObjectName(_fromUtf8("comboBoxInspector"))
        self.horizontalLayout.addWidget(self.comboBoxInspector)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setSizeConstraint(QtGui.QLayout.SetFixedSize)
        self.horizontalLayout_2.setSpacing(8)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_2 = QtGui.QLabel(self.tab1)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_2.addWidget(self.label_2)
        self.dateEdit = QtGui.QDateEdit(self.tab1)
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setObjectName(_fromUtf8("dateEdit"))
        self.horizontalLayout_2.addWidget(self.dateEdit)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.label_3 = QtGui.QLabel(self.tab1)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_2.addWidget(self.label_3)
        self.timeEditLlegada = QtGui.QTimeEdit(self.tab1)
        self.timeEditLlegada.setObjectName(_fromUtf8("timeEditLlegada"))
        self.horizontalLayout_2.addWidget(self.timeEditLlegada)
        self.horizontalLayout_2.setStretch(1, 1)
        self.horizontalLayout_2.setStretch(4, 1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.gridLayout_3.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab1, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.gridLayout.addWidget(self.tabWidget, 0, 1, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.pushButton.setText(_translate("Dialog", "PushButton", None))
        self.label_4.setText(_translate("Dialog", "Calle 1:", None))
        self.label_5.setText(_translate("Dialog", "Calle 2:", None))
        self.label_6.setText(_translate("Dialog", "Altura:", None))
        self.label_7.setText(_translate("Dialog", "ID:", None))
        self.label.setText(_translate("Dialog", "Inspectores:", None))
        self.label_2.setText(_translate("Dialog", "Fecha:", None))
        self.label_3.setText(_translate("Dialog", "Hora Llegada:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab1), _translate("Dialog", "Datos Siniestro", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "Tab 2", None))

