from python_imagesearch.imagesearch import imagesearch
import pyautogui
from threading import Thread
import time
import sys

from autoclicker_gui import *



class ClickerRobot:
    def __init__(self):
        import sys
        self.app = QtWidgets.QApplication(sys.argv)
        self.app.aboutToQuit.connect(self.do_before_WindowClosing)
        self.MainWindow = QtWidgets.QMainWindow()
        self.UI = Ui_MainWindow()
        self.UI.setupUi(self.MainWindow, self)
        self.clicker_thread = Thread(target=self.start_clicking_loop)

    def showWindow(self):
        self.is_window_closed = False
        self.MainWindow.show()
        sys.exit(self.app.exec_())

    def do_before_WindowClosing(self):
        self.is_window_closed = True
        if self.clicker_thread.is_alive():
            self.clicker_thread.join()

    def start_clicker_Thread(self):
        if self.UI.imagepath_lineEdit.text() == '':
            msg = QtWidgets.QMessageBox(self.MainWindow)
            msg.setText('Please click on Browse button and select an image.')
            msg.setWindowTitle('No image selected!')
            msg.setWindowIcon(QtGui.QIcon('robot.ico'))
            msg.exec_()
            return
        self.clicker_thread = Thread(target=self.start_clicking_loop)
        self.clicker_thread.start()

    def start_clicking_loop(self):
        self.UI.start_button.setEnabled(False)
        waiting_time = self.UI.waitingTime_spinBox.value()
        image_path = self.UI.imagepath_lineEdit.text()
        click_count = 0
        self.UI.status_label.setText('Status: Clicked 0 times.')
        while True:
            posX, posY = pyautogui.position()
            if posX < 100 and posY < 100 or self.is_window_closed == True:
                self.UI.status_label.setText('Status: Stopped!')
                break
            self.UI.status_label.setText('Status: Searching image object...')
            position = imagesearch(image_path)
            if position[0] != -1:
                pyautogui.click(position)
                width, length = position
                pyautogui.moveTo(width + 150, length + 150)
                click_count += 1
                self.UI.status_label.setText('Status: Clicked ' + str(click_count) + ' times.')

            self.UI.status_label.setText('Status: Waiting for ' + str(waiting_time) + ' seconds...')
            time.sleep(waiting_time)
            #
        self.UI.start_button.setEnabled(True)


#==========

def main():
    clickerApp = ClickerRobot()
    clickerApp.showWindow()

if __name__ == '__main__':
    main()