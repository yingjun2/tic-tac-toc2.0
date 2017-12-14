import sys
from PyQt5 import QtCore
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QPushButton, QApplication, QVBoxLayout, QMainWindow, QWidget, QMessageBox, \
    QLabel, QComboBox, QLineEdit
from qtpy import QtWidgets



class First(QMainWindow):
    def __init__(self, parent=None):
        super(First, self).__init__(parent)
        """
        cannot set a QLayout directly on QMainWindow
        """
        wid = QWidget(self)
        self.setCentralWidget(wid)

        self.b1 = QPushButton("battle")
        self.b1.setFixedSize(400, 200)
        self.b1.move(160, 200)
        self.b2 = QPushButton("challenge")
        self.b2.setFixedSize(400, 200)
        self.b2.move(160, 420)

        self.mainLayout = QVBoxLayout()
        wid.setLayout(self.mainLayout)
        self.setGeometry(500, 200, 420, 450)

        self.mainLayout.addWidget(self.b1)
        self.mainLayout.addWidget(self.b2)

        """
        QWidget::setLayout: Attempting to set QLayout "" on First "", which already has a layout
        """
        # self.setLayout(self.mainLayout)
        self.setWindowTitle("Welcome!")

        self.b1.clicked.connect(self.on_boardButton_clicked)
        self.b2.clicked.connect(self.on_queryButton_clicked)

    def on_boardButton_clicked(self):
        msg = QMessageBox()
        msg.setText("Please choose the game mode!")
        msg.setWindowTitle("Enjoy the game with computer :)")
        msg.addButton(QPushButton('Easy Mode'), QMessageBox.AcceptRole)
        msg.addButton(QPushButton('Hard Mode'), QMessageBox.YesRole)
        msg.addButton(QPushButton('Med Mode'), QMessageBox.NoRole)
        msg.exec_()
        result = msg.buttonRole(msg.clickedButton())
        if result == QMessageBox.YesRole:
            self.Hard_Mode()
        elif result == QMessageBox.NoRole:
            self.Med_Mode()
        else:
            self.Easy_Mode()

    def Easy_Mode(self):
        """
               avoid dependency 
               """
        from Model.Easy_MCplay import Easy_Test
        self.dialog = Easy_Test()
        self.dialog.show()

    def Hard_Mode(self):
        """

        haven't finished
        :return: 
        """
        from Model.Hard_MCplay import Hard_Test
        self.dialog1 = Hard_Test()
        self.dialog1.show()

    def Med_Mode(self):
        from Model.Med_MCplay import Med_Test
        self.dialog3 = Med_Test()
        self.dialog3.show()

    def on_queryButton_clicked(self):
        self.dialog2 = chalWindow()
        self.dialog2.show()


class BoardWindow(QMainWindow):
    def __init__(self, parent=None):
        super(BoardWindow, self).__init__(parent)
        self.setupUi(self)

    def setupUi(self, tictactoe):
        """ init tictactoe"""
        tictactoe.setObjectName("tictactoe")

        tictactoe.resize(627, 470)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHeightForWidth(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(tictactoe.sizePolicy().hasHeightForWidth())
        tictactoe.setSizePolicy(sizePolicy)

        tictactoe.setMinimumSize(QtCore.QSize(627, 470))
        tictactoe.setMaximumSize(QtCore.QSize(627, 470))
        tictactoe.setContextMenuPolicy(QtCore.Qt.NoContextMenu)

        self.centralwidget = QtWidgets.QWidget(tictactoe)
        self.centralwidget.setObjectName("centralwidget")

        """
        put the board on the frame, central widget
        """
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 0, 601, 411))
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setLineWidth(0)
        self.frame.setObjectName("frame")

        """
        tictactoe layout
        """
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")

        self.button1 = QtWidgets.QToolButton(self.frame)
        self.button1.setText("")
        self.button1.setIconSize(QtCore.QSize(128, 128))
        self.button1.setObjectName("button1")
        self.gridLayout.addWidget(self.button1, 0, 0)

        self.button2 = QtWidgets.QToolButton(self.frame)
        self.button2.setText("")
        self.button2.setIconSize(QtCore.QSize(128, 128))
        self.button2.setObjectName("button2")
        self.gridLayout.addWidget(self.button2, 0, 1)

        self.button3 = QtWidgets.QToolButton(self.frame)
        self.button3.setText("")
        self.button3.setIconSize(QtCore.QSize(128, 128))
        self.button3.setObjectName("button3")
        self.gridLayout.addWidget(self.button3, 0, 2)

        self.button4 = QtWidgets.QToolButton(self.frame)
        self.button4.setText("")
        self.button4.setIconSize(QtCore.QSize(128, 128))
        self.button4.setObjectName("button4")
        self.gridLayout.addWidget(self.button4, 1, 0)

        self.button5 = QtWidgets.QToolButton(self.frame)
        self.button5.setText("")
        self.button5.setIconSize(QtCore.QSize(128, 128))
        self.button5.setObjectName("button5")
        self.gridLayout.addWidget(self.button5, 1, 1)

        self.button6 = QtWidgets.QToolButton(self.frame)
        self.button6.setText("")
        self.button6.setIconSize(QtCore.QSize(128, 128))
        self.button6.setObjectName("button6")
        self.gridLayout.addWidget(self.button6, 1, 2)

        self.button7 = QtWidgets.QToolButton(self.frame)
        self.button7.setText("")
        self.button7.setIconSize(QtCore.QSize(128, 128))
        self.button7.setObjectName("button7")
        self.gridLayout.addWidget(self.button7, 2, 0)

        self.button8 = QtWidgets.QToolButton(self.frame)
        self.button8.setText("")
        self.button8.setIconSize(QtCore.QSize(128, 128))
        self.button8.setObjectName("button8")
        self.gridLayout.addWidget(self.button8, 2, 1)

        self.button9 = QtWidgets.QToolButton(self.frame)
        self.button9.setText("")
        self.button9.setIconSize(QtCore.QSize(128, 128))
        self.button9.setObjectName("button9")
        self.gridLayout.addWidget(self.button9, 2, 2)
        tictactoe.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(tictactoe)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 627, 22))
        self.menubar.setObjectName("menubar")
        self.menuNew = QtWidgets.QMenu(self.menubar)
        self.menuNew.setObjectName("menuNew")
        tictactoe.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(tictactoe)
        self.statusbar.setObjectName("statusbar")
        self.statusbar.showMessage("You are X AND Computer is 0. You play first")
        tictactoe.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(tictactoe)
        self.toolBar.setObjectName("toolBar")
        tictactoe.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)

        self.actionNew_Game = QtWidgets.QAction(tictactoe)
        self.actionNew_Game.setObjectName("actionNew_Game")

        self.action_Exit = QtWidgets.QAction(tictactoe)
        self.action_Exit.setObjectName("action_Exit")

        self.menuNew.addAction(self.actionNew_Game)
        self.menuNew.addSeparator()
        self.menuNew.addAction(self.action_Exit)
        self.menuNew.addSeparator()
        self.menubar.addAction(self.menuNew.menuAction())
        self.toolBar.addAction(self.actionNew_Game)

        self.retranslateUi(tictactoe)
        """
        connect with slot
        """
        QtCore.QMetaObject.connectSlotsByName(tictactoe)

    def retranslateUi(self, tictactoe):
        _translate = QtCore.QCoreApplication.translate
        tictactoe.setWindowTitle(_translate("tictactoe", "Tic Tac Toe"))
        self.menuNew.setTitle(_translate("tictactoe", "New"))
        self.toolBar.setWindowTitle(_translate("tictactoe", "toolBar"))
        self.actionNew_Game.setText(_translate("tictactoe", "New Game"))
        self.action_Exit.setText(_translate("tictactoe", "Exit"))


class chalWindow(QMainWindow):
    def __init__(self, parent=None):
        super(chalWindow, self).__init__(parent)
        self.setupUi(self)

    def setupUi(self, chalWindow):
        """ set the layout for challenge"""
        chalWindow.setObjectName("chalwindow")
        chalWindow.resize(500, 450)
        self.centralWidget = QWidget(chalWindow)
        self.centralWidget.setObjectName("centralWidget")

        self.title=QLabel(self.centralWidget)
        self.title.setGeometry(QtCore.QRect(140, 10, 200, 20))
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setFont(QFont("Roman times", 24, QFont.Bold))
        self.title.setObjectName("title")

        self.lbl1 = QLabel(self.centralWidget)
        self.lbl1.setGeometry(QtCore.QRect(30, 50, 150, 50))
        self.lbl1.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl1.setObjectName("first player")
        self.lbl2 = QLabel(self.centralWidget)
        self.lbl2.setGeometry(QtCore.QRect(180, 50, 150, 50))
        self.lbl2.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl2.setObjectName("second player")
        self.lbl3 = QLabel(self.centralWidget)
        self.lbl3.setGeometry(QtCore.QRect(330, 50, 150, 50))
        self.lbl3.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl3.setObjectName("round number")

        self.combo1 = QComboBox(self.centralWidget)
        """
        have parameter combo1 for first player mode
        """
        self.combo1.setObjectName("combo1")
        self.combo1.addItem("easy")
        self.combo1.addItem("medium")
        self.combo1.addItem("hard")
        self.combo1.setGeometry(QtCore.QRect(50, 120, 95, 50))

        self.combo2 = QComboBox(self.centralWidget)
        """
        have parameter combo2 for second player  mode 
        """
        self.combo2.setObjectName("combo2")
        self.combo2.addItem("easy")
        self.combo2.addItem("medium")
        self.combo2.addItem("hard")
        self.combo2.setGeometry(QtCore.QRect(200, 120, 95, 50))

        # input the parameter for Monte  Carlo rounds
        self.n_rounds = QLineEdit(self.centralWidget)
        self.n_rounds.setObjectName("number")
        self.n_rounds.setGeometry(360, 135, 95, 17)

        self.lb1 = QLabel(self.centralWidget)
        self.lb1.setGeometry(QtCore.QRect(30, 200, 150, 50))
        self.lb1.setAlignment(QtCore.Qt.AlignCenter)
        self.lb1.setObjectName("winningrate1")

        self.lb2 = QLabel(self.centralWidget)
        self.lb2.setGeometry(QtCore.QRect(180, 200, 150, 50))
        self.lb2.setAlignment(QtCore.Qt.AlignCenter)
        self.lb2.setObjectName("winningrate2")

        self.lb3 = QLabel(self.centralWidget)
        self.lb3.setGeometry(QtCore.QRect(330, 200, 150, 50))
        self.lb3.setAlignment(QtCore.Qt.AlignCenter)
        self.lb3.setObjectName("drawingrate")

        self.res1 = QLineEdit(self.centralWidget)
        self.res1.setGeometry(50, 300, 100, 20)
        self.res1.setObjectName("res1")
        self.res1.setStyleSheet("""QLineEdit { background-color: grey; color: white }""")

        self.res2 = QLineEdit(self.centralWidget)
        self.res2.setGeometry(200, 300, 100, 20)
        self.res2.setObjectName("res2")
        self.res2.setStyleSheet("""QLineEdit { background-color: grey; color: white }""")

        self.res3 = QLineEdit(self.centralWidget)
        self.res3.setGeometry(360, 300, 100, 20)
        self.res3.setObjectName("res3")
        self.res3.setStyleSheet("""QLineEdit { background-color: grey; color: white }""")

        self.btnrun = QtWidgets.QToolButton(self.centralWidget)
        self.btnrun.setText("Run")
        self.btnrun.setObjectName("Sure")
        self.btnrun.clicked.connect(self.on_Run_clicked)
        self.btnrun.setGeometry(QtCore.QRect(190, 400, 115, 32))

        chalWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(chalWindow)
        QtCore.QMetaObject.connectSlotsByName(chalWindow)

    def on_Run_clicked(self):
        lvl1 = self.combo1.currentText()
        lvl2 = self.combo2.currentText()
        rounds = int(self.n_rounds.text())
        from Model.PartB import partb
        self.partb = partb(lvla=lvl1, lvlb=lvl2, times=rounds)
        st_list = self.partb.MC_games()
        """

        """
        self.res1.setText("%f" % st_list[0])
        self.res2.setText("%f" % st_list[2])
        self.res3.setText("%f" % st_list[1])

    def retranslateUi(self, chalWindow):
        _translate = QtCore.QCoreApplication.translate
        chalWindow.setWindowTitle(_translate("chalWindow", ""))
        self.title.setText(_translate("chalWindow", "Monte Carlo"))
        self.lbl1.setText(_translate("chalWindow", "level of 1st player"))
        self.lbl2.setText(_translate("chalWindow", "level of 2nd player"))
        self.lbl3.setText(_translate("chalWindow", "number of MCS"))
        self.lb1.setText(_translate("resWindow", "winning rate for 1st"))
        self.lb2.setText(_translate("resWindow", "winning rate for 2nd"))
        self.lb3.setText(_translate("resWindow", "drawing rate"))
        self.btnrun.setText(_translate("chalWindow", "Run"))


def main():
    app = QApplication(sys.argv)
    main = First()
    main.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

