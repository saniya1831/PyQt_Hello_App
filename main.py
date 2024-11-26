import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton,QVBoxLayout, QLabel, QGraphicsDropShadowEffect
from PyQt5.QtGui import QColor
from PyQt5 import QtGui

class HelloCore2webApp(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        hello_button = QPushButton('Say Hello', self)
        hello_button.setStyleSheet("background-color:white; width:300px;height: 30px; color:black; margin-top:100px;")


        shadow = QGraphicsDropShadowEffect()
        shadow.setColor(QColor(0, 0, 0, 150)) # Set the shadow color and opacity


        shadow.setBlurRadius(10)
        hello_button.setGraphicsEffect(shadow)

        hello_button.clicked.connect(self.say_hello)

        self.message_label = QLabel(self)


        layout = QVBoxLayout()
        layout.addWidget(hello_button)
        layout.addWidget(self.message_label)

        self.setLayout(layout)

        self.setWindowTitle('Core2web.in')
        self.setGeometry(500, 500, 500, 500)

        self.setWindowIcon(QtGui.QIcon("./images/c2w_logo.jpeg"))

    def say_hello(self):
        self.message_label.setText('Hello, Core2web!')
        self.message_label.setStyleSheet("color:red; font-size:20px;margin-left:150px")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = HelloCore2webApp()
    window.show()
    sys.exit(app.exec_())


