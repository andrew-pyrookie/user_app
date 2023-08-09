import sys
from PySide6 import QtCore as qtc
from PySide6 import QtWidgets as qtw
from PySide6 import QtGui as qtg

from Application_Login.UI.w_login_ui import Ui_w_loginform


class LoginForm(qtw.QWidget,Ui_w_loginform):
    
    login_success = qtc.Signal()
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.pb_cancel.clicked.connect(self.close)
        
        self.pb_okay.clicked.connect(self.process_login)
        
    @qtc.Slot()
    def process_login(self):
        if self.le_userid.text() == "Andrew" and self.le_password.text() == "Password":
            self.login_success.emit()
            self.close()
            
        else:
            self.lb_message.setText("LogIn Incorrect!")

if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)
    
    window = LoginForm()
    window.show()
    
    sys.exit(app.exec())       