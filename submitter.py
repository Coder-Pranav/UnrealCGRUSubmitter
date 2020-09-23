import sys

from PySide2.QtWidgets import *


class Panel(QWidget):
    def __init__(self):
        super(Panel, self).__init__()
        self.setupUi()
        self.openFileManagerButton.clicked.connect(self.openFile)

    def setupUi(self):
        master_lay = QVBoxLayout()
        form_lay = QFormLayout()
        hori_lay_file = QHBoxLayout()

        self.filename = QLineEdit()
        self.resolution = QComboBox()
        self.movieFormat = QComboBox()
        self.frameRate = QComboBox()
        self.passes = QComboBox()
        self.maps = QComboBox()
        self.sequences = QComboBox()
        self.renderpathLabel = QLabel('Render Path')
        self.filepath = QLineEdit()
        self.openFileManagerButton = QPushButton('open')

        self.renderButton = QPushButton('Render')
        self.renderButton.setMinimumHeight(50)
        self.renderButton.setStyleSheet('background-color:#00b4d8')

        hori_lay_file.addWidget(self.renderpathLabel)
        hori_lay_file.addSpacerItem(QSpacerItem(19, 0))
        hori_lay_file.addWidget(self.filepath)
        hori_lay_file.addWidget(self.openFileManagerButton)

        form_lay.addRow('File Name', self.filename)
        form_lay.addRow('Resolution', self.resolution)
        form_lay.addRow('Movie Format', self.movieFormat)
        form_lay.addRow('Frame Rate', self.frameRate)
        form_lay.addRow('Render Passes', self.passes)
        form_lay.addRow('Select Map', self.maps)
        form_lay.addRow('Select Sequence', self.sequences)
        form_lay.addRow(hori_lay_file)
        master_lay.addLayout(form_lay)
        master_lay.addWidget(self.renderButton)
        self.setLayout(master_lay)
        self.setWindowTitle('Unreal Render Submitter')

    def openFile(self):
        path = QFileDialog.getOpenFileName()[0]
        self.filepath.setText(path)


app = QApplication(sys.argv)
panel = Panel()
panel.show()
app.exec_()
