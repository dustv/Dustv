# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainUi.ui'
#
# Created: Fri Dec 10 17:45:52 2010
#      by: PyQt4 UI code generator 4.7.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 600)
        MainWindow.setFocusPolicy(QtCore.Qt.NoFocus)
        MainWindow.setStyleSheet("     QWidget#mainCentralWidget {\n"
"         background-color: #595959;\n"
"     }\n"
"\n"
"     QTabWidget::pane { /* The tab widget frame */\n"
"         border: 1px solid #797979;\n"
"         position: absolute;\n"
"         top: -1px;\n"
"     }\n"
"\n"
"     QTabWidget::tab-bar {\n"
"         left: 0px; /* move to the right by 5px */\n"
"     }\n"
"\n"
"     /* Style the tab using the tab sub-control. Note that\n"
"         it reads QTabBar _not_ QTabWidget */\n"
"     QTabBar::tab {\n"
"         background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                     stop: 0 #595959, stop: 1.0 #494949);\n"
"       /*  background-color: #595959; */\n"
"         color: #a6a6a6;\n"
"         border: 1px solid #404040;\n"
"         border-bottom: 0px solid;\n"
"         border-bottom-color: #0070c0; /* same as the pane color */\n"
"         border-top-left-radius: 3px;\n"
"         border-top-right-radius: 3px;\n"
"         min-width: 4ex;\n"
"         padding-left: 12px;\n"
"         padding-right: 12px;\n"
"         padding-top: 1px;\n"
"         padding-bottom: 2px;\n"
"         margin-left: -1px;\n"
"         margin-right: -1px;\n"
"         font-size: 10px;\n"
"     }\n"
"\n"
"     QTabBar::tab:selected, QTabBar::tab:hover {\n"
"         background-color: #696969;\n"
"        /* background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                     stop: 0 #fafafa, stop: 0.4 #f4f4f4,\n"
"                                     stop: 0.5 #e7e7e7, stop: 1.0 #fafafa);*/\n"
"     }\n"
"\n"
"     QTabBar::tab:selected {\n"
"         border-color: #797979;\n"
"         border-bottom-color: #C2C7CB; /* same as pane color */\n"
"         color: #ffffff;\n"
"     }\n"
"\n"
"     QTabBar::tab:!selected {\n"
"         margin-top: 2px; /* make non-selected tabs look smaller */\n"
"         border-bottom: 1px solid #797979;\n"
"     }\n"
"\n"
"     /* make use of negative margins for overlapping tabs */\n"
"     QTabBar::tab:selected {\n"
"         /* expand/overlap to the left and right by 4px */\n"
"         margin-left: -4px;\n"
"         margin-right: -4px;\n"
"     }\n"
"\n"
"     QTabBar::tab:first {\n"
"         border-left: 2px solid #404040;\n"
"     }\n"
"\n"
"     QTabBar::tab:first:selected {\n"
"         margin-left: 0; /* the first selected tab has nothing to overlap with on the left */\n"
"         border-left: 1px solid #797979;\n"
"     }\n"
"\n"
"     QTabBar::tab:last:selected {\n"
"         margin-right: 0; /* the last selected tab has nothing to overlap with on the right */\n"
"         border-right: 1px solid #797979;\n"
"     }\n"
"\n"
"     QTabBar::tab:last {\n"
"         border-right: 2px solid #404040;\n"
"     }\n"
"\n"
"     QTabBar::tab:only-one {\n"
"         margin: 0; /* if there is only one tab, we don\'t want overlapping margins */\n"
"     }\n"
"\n"
"/**** MAIN TABS STYLING ****/\n"
"\n"
"     QTabWidget#mainTabsWidget::pane { /* The tab widget frame */\n"
"         border-top: 1px solid #d925ff;\n"
"         position: absolute;\n"
"         top: -1px;\n"
"     }\n"
"\n"
"     QWidget#mainTabsWidget > QTabBar::tab:!selected {\n"
"         margin-top: 2px; /* make non-selected tabs look smaller */\n"
"         border-bottom: 1px solid #d925ff;\n"
"     }\n"
"\n"
"     QWidget#mainTabsWidget > QTabBar::tab:selected {\n"
"         border-color: #d925ff;\n"
"         border-bottom-color: #C2C7CB; /* same as pane color */\n"
"         color: #ffffff;\n"
"     }\n"
"\n"
"     QWidget#productionTab, QWidget#visionTab, QWidget#soundTab, QWidget#vtTab, QWidget#replayTab, QWidget#feedsTab, QWidget#commsTab, QWidget#broadcastTab, QWidget#recordingTab, QWidget#settingsTab, QWidget#customTab {\n"
"         background-color: #292929;\n"
"     }\n"
"\n"
"/**** DOCK WIDGETS ****/\n"
"\n"
" QDockWidget {\n"
"     border: 1px solid #404040;\n"
" }\n"
"\n"
" QDockWidget::title {\n"
"     text-align: left; /* align the text to the left */\n"
"     background: #494949;\n"
"     padding-left: 5px;\n"
" }")
        self.mainCentralWidget = QtGui.QWidget(MainWindow)
        self.mainCentralWidget.setStyleSheet("None")
        self.mainCentralWidget.setObjectName("mainCentralWidget")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.mainCentralWidget)
        self.verticalLayout_3.setMargin(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.mainVerticalLayout = QtGui.QVBoxLayout()
        self.mainVerticalLayout.setSpacing(6)
        self.mainVerticalLayout.setObjectName("mainVerticalLayout")
        self.mainTabsWidget = QtGui.QTabWidget(self.mainCentralWidget)
        self.mainTabsWidget.setEnabled(True)
        self.mainTabsWidget.setFocusPolicy(QtCore.Qt.NoFocus)
        self.mainTabsWidget.setStyleSheet("None")
        self.mainTabsWidget.setTabsClosable(False)
        self.mainTabsWidget.setMovable(True)
        self.mainTabsWidget.setObjectName("mainTabsWidget")

        self.productionTab = QtGui.QMainWindow()
        self.productionTab.setObjectName("productionTab")
        self.productionTab.resize(800, 600)
        self.prodCentralWidget = QtGui.QWidget(self.productionTab)
        self.prodCentralWidget.setObjectName("prodCentralWidget")
        self.productionTab.setCentralWidget(self.prodCentralWidget)
        self.prodDockWidget = QtGui.QDockWidget(self.productionTab)
        self.prodDockWidget.setMinimumSize(QtCore.QSize(250, 300))
        self.prodDockWidget.setStyleSheet("background-color: black;")
        self.prodDockWidget.setObjectName("prodDockWidget")
        self.prodVideoWidget = QtGui.QWidget()
        self.prodVideoWidget.setObjectName("prodVideoWidget")
        self.prodDockWidget.setWidget(self.prodVideoWidget)
        self.productionTab.addDockWidget(QtCore.Qt.DockWidgetArea(4), self.prodDockWidget)
        self.prodDockWidget2 = QtGui.QDockWidget(self.productionTab)
        self.prodDockWidget2.setMinimumSize(QtCore.QSize(250, 300))
        self.prodDockWidget2.setStyleSheet("background-color: black;")
        self.prodDockWidget2.setObjectName("prodDockWidget2")
        self.prodVideoWidget2 = QtGui.QWidget()
        self.prodVideoWidget2.setObjectName("prodVideoWidget2")
        self.prodDockWidget2.setWidget(self.prodVideoWidget2)
        self.productionTab.addDockWidget(QtCore.Qt.DockWidgetArea(4), self.prodDockWidget2)
        self.prodDockWidget3 = QtGui.QDockWidget(self.productionTab)
        self.prodDockWidget3.setMinimumSize(QtCore.QSize(300, 300))
        self.prodDockWidget3.setObjectName("prodDockWidget3")
        self.prodVideoWidget_2 = QtGui.QWidget()
        self.prodVideoWidget_2.setObjectName("prodVideoWidget_2")
        self.gridLayout = QtGui.QGridLayout(self.prodVideoWidget_2)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.prodPrevBorder1 = QtGui.QWidget(self.prodVideoWidget_2)
        self.prodPrevBorder1.setObjectName("prodPrevBorder1")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.prodPrevBorder1)
        self.verticalLayout_2.setSpacing(3)
        self.verticalLayout_2.setMargin(2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.prodPrevWidget1 = QtGui.QWidget(self.prodPrevBorder1)
        self.prodPrevWidget1.setStyleSheet("background-color:black;")
        self.prodPrevWidget1.setObjectName("prodPrevWidget1")
        self.verticalLayout_2.addWidget(self.prodPrevWidget1)
        self.gridLayout.addWidget(self.prodPrevBorder1, 0, 0, 1, 1)
        self.prodPrevBorder2 = QtGui.QWidget(self.prodVideoWidget_2)
        self.prodPrevBorder2.setObjectName("prodPrevBorder2")
        self.verticalLayout_8 = QtGui.QVBoxLayout(self.prodPrevBorder2)
        self.verticalLayout_8.setMargin(2)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.prodPrevWidget2 = QtGui.QWidget(self.prodPrevBorder2)
        self.prodPrevWidget2.setStyleSheet("background-color:black;")
        self.prodPrevWidget2.setObjectName("prodPrevWidget2")
        self.verticalLayout_8.addWidget(self.prodPrevWidget2)
        self.gridLayout.addWidget(self.prodPrevBorder2, 0, 1, 1, 1)
        self.prodPrevBorder3 = QtGui.QWidget(self.prodVideoWidget_2)
        self.prodPrevBorder3.setObjectName("prodPrevBorder3")
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.prodPrevBorder3)
        self.verticalLayout_4.setMargin(2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.prodPrevWidget3 = QtGui.QWidget(self.prodPrevBorder3)
        self.prodPrevWidget3.setStyleSheet("background-color:black;")
        self.prodPrevWidget3.setObjectName("prodPrevWidget3")
        self.verticalLayout_4.addWidget(self.prodPrevWidget3)
        self.gridLayout.addWidget(self.prodPrevBorder3, 0, 2, 1, 1)
        self.prodPrevBorder4 = QtGui.QWidget(self.prodVideoWidget_2)
        self.prodPrevBorder4.setObjectName("prodPrevBorder4")
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.prodPrevBorder4)
        self.verticalLayout_5.setMargin(2)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.prodPrevWidget4 = QtGui.QWidget(self.prodPrevBorder4)
        self.prodPrevWidget4.setStyleSheet("background-color:black;")
        self.prodPrevWidget4.setObjectName("prodPrevWidget4")
        self.verticalLayout_5.addWidget(self.prodPrevWidget4)
        self.gridLayout.addWidget(self.prodPrevBorder4, 1, 0, 1, 1)
        self.prodPrevBorder5 = QtGui.QWidget(self.prodVideoWidget_2)
        self.prodPrevBorder5.setObjectName("prodPrevBorder5")
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.prodPrevBorder5)
        self.verticalLayout_6.setMargin(2)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.prodPrevWidget5 = QtGui.QWidget(self.prodPrevBorder5)
        self.prodPrevWidget5.setStyleSheet("background-color:black;")
        self.prodPrevWidget5.setObjectName("prodPrevWidget5")
        self.verticalLayout_6.addWidget(self.prodPrevWidget5)
        self.gridLayout.addWidget(self.prodPrevBorder5, 1, 1, 1, 1)
        self.prodPrevBorder6 = QtGui.QWidget(self.prodVideoWidget_2)
        self.prodPrevBorder6.setObjectName("prodPrevBorder6")
        self.verticalLayout_7 = QtGui.QVBoxLayout(self.prodPrevBorder6)
        self.verticalLayout_7.setMargin(2)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.prodPrevWidget6 = QtGui.QWidget(self.prodPrevBorder6)
        self.prodPrevWidget6.setStyleSheet("background-color:black;")
        self.prodPrevWidget6.setObjectName("prodPrevWidget6")
        self.verticalLayout_7.addWidget(self.prodPrevWidget6)
        self.gridLayout.addWidget(self.prodPrevBorder6, 1, 2, 1, 1)
        self.prodDockWidget3.setWidget(self.prodVideoWidget_2)
        self.productionTab.addDockWidget(QtCore.Qt.DockWidgetArea(8), self.prodDockWidget3)
        self.prodDockWidget4 = QtGui.QDockWidget(self.productionTab)
        self.prodDockWidget4.setObjectName("prodDockWidget4")
        self.prodControlsWidget = QtGui.QWidget()
        self.prodControlsWidget.setObjectName("prodControlsWidget")
        self.chooseFile = QtGui.QPushButton(self.prodControlsWidget)
        self.chooseFile.setGeometry(QtCore.QRect(0, 10, 87, 27))
        self.chooseFile.setObjectName("chooseFile")
        self.prodDockWidget4.setWidget(self.prodControlsWidget)
        self.productionTab.addDockWidget(QtCore.Qt.DockWidgetArea(8), self.prodDockWidget4)

        self.mainTabsWidget.addTab(self.productionTab, "")
        self.visionTab = QtGui.QWidget()
        self.visionTab.setObjectName("visionTab")
        self.mainTabsWidget.addTab(self.visionTab, "")
        self.soundTab = QtGui.QWidget()
        self.soundTab.setObjectName("soundTab")
        self.mainTabsWidget.addTab(self.soundTab, "")
        self.vtTab = QtGui.QWidget()
        self.vtTab.setObjectName("vtTab")
        self.mainTabsWidget.addTab(self.vtTab, "")
        self.replayTab = QtGui.QWidget()
        self.replayTab.setObjectName("replayTab")
        self.mainTabsWidget.addTab(self.replayTab, "")
        self.feedsTab = QtGui.QWidget()
        self.feedsTab.setObjectName("feedsTab")
        self.mainTabsWidget.addTab(self.feedsTab, "")
        self.commsTab = QtGui.QWidget()
        self.commsTab.setObjectName("commsTab")
        self.mainTabsWidget.addTab(self.commsTab, "")
        self.broadcastTab = QtGui.QWidget()
        self.broadcastTab.setObjectName("broadcastTab")
        self.mainTabsWidget.addTab(self.broadcastTab, "")
        self.recordingTab = QtGui.QWidget()
        self.recordingTab.setObjectName("recordingTab")
        self.mainTabsWidget.addTab(self.recordingTab, "")
        self.settingsTab = QtGui.QWidget()
        self.settingsTab.setObjectName("settingsTab")
        self.mainTabsWidget.addTab(self.settingsTab, "")
        self.customTab = QtGui.QWidget()
        self.customTab.setObjectName("customTab")
        self.mainTabsWidget.addTab(self.customTab, "")
        self.mainVerticalLayout.addWidget(self.mainTabsWidget)
        self.verticalLayout_3.addLayout(self.mainVerticalLayout)
        MainWindow.setCentralWidget(self.mainCentralWidget)

        self.retranslateUi(MainWindow)
        self.mainTabsWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "dust example", None, QtGui.QApplication.UnicodeUTF8))
        self.mainTabsWidget.setTabText(self.mainTabsWidget.indexOf(self.productionTab), QtGui.QApplication.translate("MainWindow", "Production", None, QtGui.QApplication.UnicodeUTF8))
        self.mainTabsWidget.setTabText(self.mainTabsWidget.indexOf(self.visionTab), QtGui.QApplication.translate("MainWindow", "Vision", None, QtGui.QApplication.UnicodeUTF8))
        self.mainTabsWidget.setTabText(self.mainTabsWidget.indexOf(self.soundTab), QtGui.QApplication.translate("MainWindow", "Sound", None, QtGui.QApplication.UnicodeUTF8))
        self.mainTabsWidget.setTabText(self.mainTabsWidget.indexOf(self.vtTab), QtGui.QApplication.translate("MainWindow", "VT", None, QtGui.QApplication.UnicodeUTF8))
        self.mainTabsWidget.setTabText(self.mainTabsWidget.indexOf(self.replayTab), QtGui.QApplication.translate("MainWindow", "Replay", None, QtGui.QApplication.UnicodeUTF8))
        self.mainTabsWidget.setTabText(self.mainTabsWidget.indexOf(self.feedsTab), QtGui.QApplication.translate("MainWindow", "Feeds", None, QtGui.QApplication.UnicodeUTF8))
        self.mainTabsWidget.setTabText(self.mainTabsWidget.indexOf(self.commsTab), QtGui.QApplication.translate("MainWindow", "Comms", None, QtGui.QApplication.UnicodeUTF8))
        self.mainTabsWidget.setTabText(self.mainTabsWidget.indexOf(self.broadcastTab), QtGui.QApplication.translate("MainWindow", "Broadcast", None, QtGui.QApplication.UnicodeUTF8))
        self.mainTabsWidget.setTabText(self.mainTabsWidget.indexOf(self.recordingTab), QtGui.QApplication.translate("MainWindow", "Recording", None, QtGui.QApplication.UnicodeUTF8))
        self.mainTabsWidget.setTabText(self.mainTabsWidget.indexOf(self.settingsTab), QtGui.QApplication.translate("MainWindow", "Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.mainTabsWidget.setTabText(self.mainTabsWidget.indexOf(self.customTab), QtGui.QApplication.translate("MainWindow", "Custom...", None, QtGui.QApplication.UnicodeUTF8))
        self.chooseFile.setText(QtGui.QApplication.translate("productionTab", "Choose File", None, QtGui.QApplication.UnicodeUTF8))

