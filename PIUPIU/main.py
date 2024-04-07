from PyQt5.QtCore import Qt
from PIL import Image , ImageFilter
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow , QFileDialog, QMessageBox
from PyQt5.QtGui import QPixmap
from ui import Ui_MainWindow
import os

class Widget(QMainWindow):
    def   __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.workdir = None
        self.filenames = None
        self.image = None
        self.ui.papka.clicked.connect(self.choose_folder)
        self.ui.zamitka.currentRowChanged.connect(self.show_chosen_image)
        

    def show_image_list(self):
        self.filenames = os.listdir(self.workdir)
        images = []
        for filename in self.filenames:
            if filename.endswith(".png") or filename.endswith("jpg") or filename.endswith(".jpeg"):
                images.append(filename)
        self.ui.zamitka.clear()
        self.ui.zamitka.addItems(images)

    def choose_folder(self):
        try:
            self.workdir =  QFileDialog.getExistingDirectory()
            self.show_image_list()
        except:
            massag = QMessageBox()
            massag.setText("ЗАНЯТО")
            massag.exec_()
            
    def load_image(self, imagename):
        self.image_name = imagename
        self.image_path = os.path.join(self.workdir , self.image_name)
        self.image = Image.open(self.image_path)
          
            
    def show_image(self):
        self.ui.label.hide()
        h = self.ui.label.height()
        w = self.ui.label.width()
        
        pixmap_image = QPixmap(self.image_path)
        pixmap_image = pixmap_image.scaled(w , h , Qt.KeepAspectRatio)
        self.ui.label.setPixmap(pixmap_image)
        self.ui.label.show()   
        
    def show_chosen_image(self):
        if self.ui.zamitka.currentRow()>=0:
            self.image_name = self.ui.zamitka.currentItem().text()
            self.load_image(self.image_name)
            self.show_image()
            
            
    def save_image
        

       








































app = QApplication([])
ex = Widget()
ex.show()
app.exec_()