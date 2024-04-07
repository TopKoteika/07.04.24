import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from ui import Ui_MainWindow
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent


class Widget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.media = QMediaPlayer()
        self.media.setVideoOutput(self.ui.video)
        self.get_date()
        self.configure()

    def configure(self):
        self.ui.Start_bnt.clicked.connect(self.madia_play)
        self.ui.Stop_Bnt.clicked.connect(self.madia_stop)
        self.ui.calendarWidget.selectionChanged.connect(self.get_date)

        

    def get_date(self):
        self.media.stop()
        day = self.ui.calendarWidget.selectedDate().day()
        day = str(day)
        vid = QMediaContent(QUrl.fromLocalFile(f'video/{day}.avi'))
        self.media.setMedia(vid)

    def media_play(self):
        self.media.play()

    def media_stop(self):
        ...


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Widget()
    ex.show()
    sys.exit(app.exec_())
