from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_LoginWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.setEnabled(True)
        MainWindow.resize(300, 335)
        MainWindow.setMinimumSize(QtCore.QSize(300, 300))
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        MainWindow.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setMinimumSize(QtCore.QSize(291, 171))
        self.frame.setMaximumSize(QtCore.QSize(291, 171))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.LoginButton = QtWidgets.QPushButton(self.frame)
        self.LoginButton.setGeometry(QtCore.QRect(160, 145, 75, 23))
        self.LoginButton.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.LoginButton.setStyleSheet("QPushButton {\n"
"color: \'black\';\n"
"background: #E1E1E1;\n"
"border: 1px solid #ADADAD;\n"
"border-radius: 10px\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"border-color: blue\n"
"}\n"
"")
        self.LoginButton.setObjectName("LoginButton")
        self.UsernameLine = QtWidgets.QLineEdit(self.frame)
        self.UsernameLine.setGeometry(QtCore.QRect(90, 30, 113, 20))
        self.UsernameLine.setInputMask("")
        self.UsernameLine.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.UsernameLine.setPlaceholderText("")
        self.UsernameLine.setObjectName("UsernameLine")
        self.UsernameLabel = QtWidgets.QLabel(self.frame)
        self.UsernameLabel.setGeometry(QtCore.QRect(90, 10, 47, 13))
        self.UsernameLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.UsernameLabel.setObjectName("UsernameLabel")
        self.PasswordLine = QtWidgets.QLineEdit(self.frame)
        self.PasswordLine.setGeometry(QtCore.QRect(90, 80, 113, 20))
        self.PasswordLine.setInputMask("")
        self.PasswordLine.setText("")
        self.PasswordLine.setEchoMode(QtWidgets.QLineEdit.Password)
        self.PasswordLine.setPlaceholderText("")
        self.PasswordLine.setObjectName("PasswordLine")
        self.RegisterButton = QtWidgets.QPushButton(self.frame)
        self.RegisterButton.setGeometry(QtCore.QRect(60, 145, 75, 23))
        self.RegisterButton.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.RegisterButton.setStyleSheet("QPushButton {\n"
"color: \'black\';\n"
"background: #E1E1E1;\n"
"border: 1px solid #ADADAD;\n"
"border-radius: 10px\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"border-color: blue\n"
"}\n"
"")
        self.RegisterButton.setObjectName("RegisterButton")
        self.PasswordLabel = QtWidgets.QLabel(self.frame)
        self.PasswordLabel.setGeometry(QtCore.QRect(90, 60, 47, 13))
        self.PasswordLabel.setObjectName("PasswordLabel")
        self.InformationLabel = QtWidgets.QLabel(self.frame)
        self.InformationLabel.setGeometry(QtCore.QRect(10, 110, 281, 31))
        self.InformationLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.InformationLabel.setText("")
        self.InformationLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.InformationLabel.setWordWrap(True)
        self.InformationLabel.setIndent(-1)
        self.InformationLabel.setObjectName("InformationLabel")
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 300, 21))
        self.menubar.setObjectName("menubar")
        self.menuOptions = QtWidgets.QMenu(self.menubar)
        self.menuOptions.setGeometry(QtCore.QRect(239, 125, 135, 94))
        self.menuOptions.setObjectName("menuOptions")
        self.menuThemes = QtWidgets.QMenu(self.menuOptions)
        self.menuThemes.setObjectName("menuThemes")
        MainWindow.setMenuBar(self.menubar)
        self.actionTing = QtWidgets.QAction(MainWindow)
        self.actionTing.setObjectName("actionTing")
        self.actionthing = QtWidgets.QAction(MainWindow)
        self.actionthing.setObjectName("actionthing")
        self.actionSettings_2 = QtWidgets.QAction(MainWindow)
        self.actionSettings_2.setMenuRole(QtWidgets.QAction.TextHeuristicRole)
        self.actionSettings_2.setObjectName("actionSettings_2")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setMenuRole(QtWidgets.QAction.TextHeuristicRole)
        self.actionExit.setObjectName("actionExit")
        self.actionDark_Mode = QtWidgets.QAction(MainWindow)
        self.actionDark_Mode.setObjectName("actionDark_Mode")
        self.actionLight_Mode = QtWidgets.QAction(MainWindow)
        self.actionLight_Mode.setObjectName("actionLight_Mode")
        self.menuThemes.addAction(self.actionDark_Mode)
        self.menuThemes.addAction(self.actionLight_Mode)
        self.menuOptions.addAction(self.menuThemes.menuAction())
        self.menuOptions.addAction(self.actionExit)
        self.menubar.addAction(self.menuOptions.menuAction())
        self.UsernameLabel.setBuddy(self.UsernameLine)
        self.PasswordLabel.setBuddy(self.PasswordLine)

        self.retranslateUi(MainWindow)
        self.UsernameLine.returnPressed.connect(self.LoginButton.click)
        self.PasswordLine.returnPressed.connect(self.LoginButton.click)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.UsernameLine, self.PasswordLine)
        MainWindow.setTabOrder(self.PasswordLine, self.LoginButton)
        MainWindow.setTabOrder(self.LoginButton, self.RegisterButton)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Klient"))
        self.LoginButton.setText(_translate("MainWindow", "Login"))
        self.UsernameLabel.setText(_translate("MainWindow", "Username"))
        self.RegisterButton.setText(_translate("MainWindow", "Register"))
        self.PasswordLabel.setText(_translate("MainWindow", "Password"))
        self.menuOptions.setTitle(_translate("MainWindow", "Options"))
        self.menuThemes.setTitle(_translate("MainWindow", "Themes"))
        self.actionTing.setText(_translate("MainWindow", "Ting"))
        self.actionthing.setText(_translate("MainWindow", "thing"))
        self.actionSettings_2.setText(_translate("MainWindow", "Settings"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionDark_Mode.setText(_translate("MainWindow", "Dark Theme"))
        self.actionLight_Mode.setText(_translate("MainWindow", "Light Theme"))