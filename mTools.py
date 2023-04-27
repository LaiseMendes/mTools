import maya.api.OpenMaya as om
import maya.mel as mel
import maya.cmds as cmds
from PySide2 import QtWidgets
from PySide2.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QLabel, QVBoxLayout, QDialog, QLineEdit, QTextEdit, QToolTip, QMessageBox
from PySide2.QtCore import Qt, QSize
from PySide2.QtGui import QColor, QFont, QPalette
from functools import partial
import sys
import json

#variaveis
path_json = r"Z:\MedScripts\Med_db.json"
path_script = r"Z:\MedScripts"
#add path to python scripts
pathList = sys.path
hasPath = False
for path in pathList:
    if 'Z:\\MedScripts' == path:
        hasPath = True
if hasPath == False:
    sys.path.append(r'Z:\MedScripts')

#add path to mel scripts
ENV = 'MAYA_SCRIPT_PATH'
paths = [os.environ.get(ENV, '')]
paths.insert(0, 'Z:/MedScripts/')
os.environ[ENV] = ';'.join(paths)

if not QtWidgets.QApplication.instance():
    app = QtWidgets.QApplication(sys.argv)
else:
    app = QtWidgets.QApplication.instance()
class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.window2 = AddWindow()
        with open(path_json) as f:
            self.dataMain = json.load(f)
        # changing the background color to blue
        self.setStyleSheet("background-color: rgb( 23, 32, 50); color: rgb(255, 255, 255);")
        # set the title
        self.setWindowTitle("mTools")
        # setting  the geometry of window
        # setGeometry(left, top, width, height)
        self.setGeometry(800, 200, 605, 436)
        self.temprow = 0
        self.tempcolumn = 0
        self.scroll = QtWidgets.QScrollArea()
        self.scroll.setWidgetResizable(True)
        self.scroll_widget = QtWidgets.QWidget()
        self.scroll_widget.setMaximumWidth(522)
        self.elementos_widget = QtWidgets.QWidget()
        vbox = QtWidgets.QGridLayout(self.scroll_widget)
        vbox.setContentsMargins(0, 0, 0, 0)
        vbox.addWidget(self.elementos_widget)
        vbox.setRowStretch(vbox.rowCount(), 1)
        self.elementos = QtWidgets.QGridLayout()
        self.elementos_widget.setLayout(self.elementos)
        self.scroll.setWidget(self.scroll_widget)
         # creating a label widget
        self.label_1 = QtWidgets.QLabel("mTools", self)
        # setting font and size
        self.label_1.setFont(QFont('Roboto', 12, QFont.DemiBold))
        # setting up background color
        self.label_1.setStyleSheet("background-color: rgb( 30, 41, 59)")
        # moving "MedRoom Tools" label position
        self.label_1.move(50, 30)
        self.label_1.setFixedSize(QSize(120, 12))
        #setToolTip
        QToolTip.setFont(QFont('Roboto', 14, QFont.Normal))
        self.label_1.setToolTip('App Top')
        # creating a label widget
        self.label_2 = QLabel("for Maya", self)
        # moving position
        self.label_2.move(50, 46)
        self.label_2.setFixedSize(QSize(60, 11))
        self.label_2.setToolTip('Muito TOP MEIXXXMO')
        # setting up background color
        self.label_2.setStyleSheet("color: rgb( 129, 143, 164)")
        # setting font and size
        self.label_2.setFont(QFont('Roboto', 8, QFont.Normal))
        self.btn_addScript = QtWidgets.QPushButton('Add Scrpit')
        self.btn_addScript.setFixedSize(78, 40)
        self.btn_addScript.setStyleSheet("QPushButton"
                                    "{"
                                    "background-color: rgb(0, 120, 98);"
                                    "border : 2px solid;"
                                    "border-color: rgb(72, 84, 102);"
                                    "border-radius : 8px;"
                                    "}"
                                    "QPushButton::hover"
                                    "{"
                                    "background-color : rgb(75, 168, 151);"
                                    "}"
                                    "QPushButton::pressed"
                                    "{"
                                    "background-color : rgb(33, 90, 80);"
                                    "}"
                                    )
        self.btn_addScript.setFont(QFont('Roboto', 9, QFont.DemiBold)) 
        #self.btn_addScript.clicked.connect(self.btn_count)
        layout = QtWidgets.QGridLayout(self)
        layout.addWidget(self.label_1, 0, 0)
        layout.addWidget(self.label_2, 1, 0)
        layout.addWidget(self.btn_addScript, 0, 4, 2, 1)
        layout.addWidget(self.scroll, 2, 0, 1, 5)
        layout.setContentsMargins(30, 22, 30, 0)
        self.btn_addScript.clicked.connect(self.clicked_addwindow)
        self.show()
        self.btn_count(self.btnNameList())
      

    def btnNameList(self):
        dataMain = {}
        with open(path_json) as f:
            dataMain = json.load(f)
        nameList = []
        for i in dataMain["scrName"]:
            nameList.append(i["btnName"])
        return(nameList)
    def clicked_button(self, name):
        for i in self.dataMain["scrName"]:
            if i["btnName"] == name:
                try:
                    tempimp = 'import ' + ((i["fName"]).split(".")[0])
                    exec(tempimp) 
                    reload(tempimp)
                except ImportError:
                    mel.eval('source' + ' ' + i["fName"])
                
                print (i["fName"])
                
    def btnHoover(self, name):
        for i in self.dataMain["scrName"]:
            if i["btnName"] == name:
                tempdesc = i["descName"]
                return(tempdesc)
    
    def clicked_addwindow(self):
        print("add scrip!")
        self.window2.show()
        self.close()
        
    def btn_count(self, dic):
        row = 0
        #count = ["UvTransfer", "compare", "rename", "other", "teste"]
        for i,a in enumerate(dic):
            self.creatBtn(i // 2, i % 2, i, a)
    def creatBtn(self, temprow,  tempcolumn, tempi, tempname):
        i = tempi
        num_row = temprow
        num_column = tempcolumn
        btn_scripts = QPushButton()
        btn_scripts.setFixedSize(253, 76)
        btn_scripts.setStyleSheet("QPushButton"
                                    "{"
                                    "background-color: rgb(51, 65, 85);"
                                    "border : 2px solid;"
                                    "border-color: rgb(72, 84, 102);"
                                    "border-radius : 8px;"
                                    "}"
                                    "QPushButton::hover"
                                    "{"
                                    "background-color : rgb(76, 96, 125);"
                                    "}"
                                    "QPushButton::pressed"
                                    "{"
                                    "background-color : rgb(17, 23, 36);"
                                    "}"
                                    )
        btn_scripts.setFont(QFont('Roboto', 11, QFont.Bold))
        btn_scripts.setText(tempname)
        btn_scripts.clicked.connect(partial(self.clicked_button,tempname))
        #btn_scripts.setToolTip(partial(self.btnHoover,tempname))
        #btn_scripts.setToolTip("Combina meshes e transfere UVs entre elas sem perder o nome dos objs. \nUso: Para dar o combine, criar um grupo (Ex: Heart.grp) que contenha as \nmeshes (Ex: Vein_1, Vein_2). Selecione o grupo e precione o combine.\n O combine irá gerar uma mesh com sufixo '_Combined' (Ex: Heart.grp_Comined). \nPara separar, selecione a mesh combinada gerada pelo combine (Ex: Heart.grp_Comined) \ne o grupo antigo (Ex: Heart.grp), e dê o separate.")
        for button in self.dataMain["scrName"]:
            if button["btnName"] == tempname:
                btn_scripts.setToolTip(button["descName"])
                break
        
        self.elementos.addWidget(btn_scripts, num_row, num_column)
        return tempname
        
class AddWindow(QDialog):
    def __init__(self):
        super(AddWindow, self).__init__()
        # changing the background color to blue
        self.setStyleSheet("background-color: rgb( 17, 23, 36); color: rgb(255, 255, 255);")
        # set the title
        self.setWindowTitle("Add Script")
        # setting  the geometry of window
        # setGeometry(left, top, width, height)
        self.setGeometry(1400, 200, 602, 387)
        self.labelName = QLabel("Add Script Name", self)
        self.labelName.setFont(QFont('Roboto', 12, QFont.DemiBold))
        self.labelName.move(34, 23)
        self.labelDesc = QLabel("Add Script Description", self)
        self.labelDesc.setFont(QFont('Roboto', 12, QFont.DemiBold))
        self.labelDesc.move(34, 129)
        self.lineName = QLineEdit(self)
        self.lineName.move(34,53)
        self.lineName.resize(250,47)
        self.lineName.setStyleSheet("background-color: rgb(51, 65, 85); border-radius : 8px;")
        self.lineName.setFont(QFont('Roboto', 11, QFont.Normal))
        self.lineName.setPlaceholderText("Add name for the script's button")
        self.lineDesc = QTextEdit(self)
        self.lineDesc.move(34,159)
        self.lineDesc.resize(536,137)
        self.lineDesc.setStyleSheet("background-color: rgb(51, 65, 85); border-radius : 8px;")
        self.lineDesc.setFont(QFont('Roboto', 11, QFont.Normal))
        self.lineDesc.setPlaceholderText('Describe: what your script does; how to use it; what is the version and last update day.(Use space between the  lines for better reading)')
        self.qlabel = QLabel(self)
        self.qlabel.move(16,64)
        self.labelScript = QLabel("Add Script File Name", self)
        self.labelScript.setFont(QFont('Roboto', 12, QFont.DemiBold))
        self.labelScript.move(314, 23)
        self.lineScript = QLineEdit(self)
        self.lineScript.move(314,53)
        self.lineScript.resize(256,47)
        self.lineScript.setStyleSheet("background-color: rgb(51, 65, 85); border-radius : 8px;")
        self.lineScript.setFont(QFont('Roboto', 11, QFont.Normal))
        self.lineScript.setPlaceholderText('Add same name as your script file name')
        #button new      
        btn_new = QPushButton("+ New", self)
        btn_new.setGeometry(473, 319, 97, 42)
        btn_new.setStyleSheet("QPushButton"
                                    "{"
                                    "background-color: rgb(59, 130, 246);"
                                    "border-radius : 8px;"
                                    "}"
                                    "QPushButton::hover"
                                    "{"
                                    "background-color : rgb(85, 150, 255);"
                                    "}"
                                    "QPushButton::pressed"
                                    "{"
                                    "background-color : rgb(43, 97, 186);"
                                    "}"
                                    )
        btn_new.setFont(QFont('Roboto', 12, QFont.Bold))
        #button cancel
        btn_cancel = QPushButton("Cancel", self)
        btn_cancel.setGeometry(349, 319, 97, 42)
        btn_cancel.setStyleSheet("QPushButton"
                                    "{"
                                    "background-color: rgb(246, 59, 70);"
                                    "border-radius : 8px;"
                                    "}"
                                    "QPushButton::hover"
                                    "{"
                                    "background-color : rgb(244, 90, 99);"
                                    "}"
                                    "QPushButton::pressed"
                                    "{"
                                    "background-color : rgb(214, 50, 60);"
                                    "}"
                                    )
        btn_cancel.setFont(QFont('Roboto', 12, QFont.Bold))
        btn_new.clicked.connect(self.clicked_new)
        btn_cancel.clicked.connect(self.cancel)
    #what happens when +New is clicked
    def clicked_new(self):
        self.cadastro()
        self.button_stored()
    #cancel button activation
    def cancel(self):
        window = MainWindow()
        self.close()
        self.window.show()
        
    #Puxa informações escritas da janela AddWindo e salva no arquivo Json 'Med_db'    
    def cadastro(self):  
        numList = [] 
        dataMain = {}
        with open(path_json) as f:
            dataMain = json.load(f)
        for j in dataMain["scrName"]:
            numList.append(j["Num"])
            numElem = len(numList) 
        self.numBtn = numElem
        self.btnLN = self.lineName.text()
        self.btnPN = self.lineDesc.toPlainText()
        self.filen = self.lineScript.text()
        self.armazena(self.btnLN,self.btnPN,self.filen,self.numBtn)
    #Alerta de script adicionado corretamente
    def button_stored(self):
        msgBox = QMessageBox()
        msgBox.setText("Script added successfully!")
        msgBox.setWindowTitle("mTools Info")
        msgBox.setGeometry(1500, 300, 200, 200)
        msgBox.setStyleSheet("background-color: rgb( 17, 23, 36); color: rgb(255, 255, 255);")
        msgBox.buttonClicked.connect(self.cancel)
        
        x = msgBox.exec_()
        
    def armazena(self,btnLN,btnDN,filen,numBtn):
        data = {}
        dataList = []       
        dataMain = {}
        with open(path_json) as f:
            dataMain = json.load(f)
        for i in dataMain["scrName"]:
            dataList.append(i)
        data["fName"] = filen
        data["btnName"] = btnLN
        data["descName"] = btnDN
        data["Num"] = numBtn
        
        dataList.append(data)
        dataMain["scrName"] = dataList
        with open(path_json, 'w') as jsonfile:
            jsonfile.write(json.dumps(dataMain, indent=4,sort_keys=True))
with open(r'Z:\MedScripts\Med_db.json') as f:
  data = json.load(f)
  #buscar lista das chaves (keys), como name, description ou text
#print(data["tag"])                               
window = MainWindow()
window.show()
app.exec_()