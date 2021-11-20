import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QDialog
from PyQt5 import QtGui
import sqlite3
from pochta_pr import Ui_Dialog1
from pochta_pr1 import Ui_Dialog
from pochta_pr2 import Ui_Form
from pochta_pr3 import Ui_Form2
from pochta_pr4 import Ui_Form3


client_data = []


def check_password(password):
    check = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm', 'йцукенгшщзхъ', 'фывапролджэё', 'ячсмитьбю']
    if len(password) <= 8:
        return 'LengthError'
    if not any(i.islower() for i in password) or not any(i.isupper() for i in password):
        return 'LetterError'
    if not any(i.isnumeric() for i in password):
        return 'DigitError'
    k = 0
    for i in password:
        if k + 2 < len(password) + 1:
            for j in check:
                if password[k - 1:k + 2]:
                    if password[k - 1:k + 2].lower() in j:
                        return 'SequenceError'
        k += 1
    return 'ok'


def get_client_data(client):
    con1 = sqlite3.connect("my_project_bd.db")
    cur1 = con1.cursor()
    client_data_false = cur1.execute(f"""SELECT * from clients_all WHERE
                            client_login LIKE '{client}'""").fetchone()
    con1.close()
    if client_data_false:
        return list(client_data_false)
    else:
        return None


class MyWidget(QDialog, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.exit)
        self.pushButton_2.clicked.connect(self.registr)

    def registr(self):
        ex.hide()
        ex3.show()

    def exit(self):
        ex.hide()
        ex2.show()


class MySecondWidget(QWidget, Ui_Form):
    def __init__(self):
        self.con = sqlite3.connect("my_project_bd.db")
        self.cur = self.con.cursor()
        self.man = []
        super().__init__()
        self.my_forth_widg = MyFourthWidget()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.login)

    def login(self):
        global client_data
        self.man = []
        if len(self.textEdit.toPlainText()) >= 8:
            self.man = get_client_data(self.textEdit.toPlainText())
            self.con.commit()
            if self.man:
                if self.man[3] == self.textEdit_2.toPlainText():
                    client_data = self.man
                    self.con.close()
                    ex2.hide()
                    self.my_forth_widg.show()
                    self.my_forth_widg.label_2.setText(client_data[2])
                    self.my_forth_widg.label_3.setText(client_data[1])
                else:
                    self.label_3.setText('Неверный Пароль')
            else:
                self.label_3.setText('Неверный Логин')


class MyThirdWidget(QWidget, Ui_Form2):
    def __init__(self):
        self.con = sqlite3.connect("my_project_bd.db")
        self.cur = self.con.cursor()
        super().__init__()
        self.my_forth_widg = MyFourthWidget()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.login)
        self.sps = [False, False, False, False]

    def login(self):
        global client_data
        if self.textEdit.toPlainText() != 'Имя'\
                and len(self.textEdit.toPlainText()) > 0 and all(i.isalpha() for i in self.textEdit.toPlainText()):
            self.sps[0] = True
        else:
            self.sps[0] = False
        if len(self.textEdit_2.toPlainText()) >= 8 and all(i.isascii() for i in self.textEdit_2.toPlainText()):
            if not get_client_data(self.textEdit_2.toPlainText()):
                self.sps[1] = True
            else:
                self.sps[1] = False
                self.label_5.setText('Login already taken')
        else:
            self.sps[1] = False
        if check_password(self.textEdit_3.toPlainText()) == 'ok':
            self.sps[2] = True
            if self.textEdit_3.toPlainText() == self.textEdit_4.toPlainText():
                self.sps[3] = True
            else:
                self.sps[3] = False
        else:
            self.label_5.setText(check_password(self.textEdit_4.toPlainText()))
            self.sps[2] = False
        if self.sps[0]:
            self.label.setText('✔')
        else:
            self.label.setText('❌')
        if self.sps[1]:
            self.label_2.setText('✔')
        else:
            self.label_2.setText('❌')
        if self.sps[2]:
            self.label_3.setText('✔')
        else:
            self.label_3.setText('❌')
        if self.sps[3]:
            self.label_4.setText('✔')
        else:
            self.label_4.setText('❌')

        if all(i is True for i in self.sps):
            self.cur.execute(f"""INSERT INTO clients_all(client_login, client_name, passwword)
             VALUES('{self.textEdit_2.toPlainText()}', '{self.textEdit.toPlainText()}',
'{self.textEdit_3.toPlainText()}')  """)
            self.con.commit()
            self.con.close()
            client_data = get_client_data(self.textEdit_2.toPlainText())
            self.my_forth_widg.show()
            self.my_forth_widg.label_2.setText(client_data[2])
            self.my_forth_widg.label_3.setText(client_data[1])
            ex3.hide()

        else:
            pass


class MyFourthWidget(QWidget, Ui_Form3):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        global client_data
        self.msg = None
        self.con = sqlite3.connect('my_project_bd.db')
        self.cur = self.con.cursor()
        self.comboBox.addItems(
            [i[0] for i in self.cur.execute("""SELECT client_login FROM clients_all""").fetchall()])
        self.pushButton_5.clicked.connect(self.send_msg)
        self.pushButton_4.clicked.connect(self.get_msg)
        self.pushButton_8.clicked.connect(self.delete_msg)
        self.pushButton_7.clicked.connect(self.open_txtfile)
        self.pushButton.clicked.connect(self.change_name)
        self.pushButton_2.clicked.connect(self.change_login)
        self.pushButton_3.clicked.connect(self.change_profile)
        self.my_change_widget = ChangeWidget()
        self.plainTextEdit_2.setReadOnly(True)

    def send_msg(self):
        g = str(self.textEdit_2.toPlainText())
        if g:
            while True:
                if self.cur.execute(f"""SELECT * FROM msges WHERE label LIKE '{g}' AND addressee 
                LIKE '{self.comboBox.currentText()}'""").fetchall():
                    g += '1'
                else:
                    break
            self.cur.execute(f"""INSERT INTO msges(addressee, sender, label, msg, status)
                         VALUES('{self.comboBox.currentText()}',
    '{client_data[1]}', '{g}', '{str(self.plainTextEdit.toPlainText())}', 0) """)
            self.con.commit()
            self.textEdit_2.clear()
            self.plainTextEdit.clear()

    def get_msg(self):
        if self.comboBox_2.currentText() != '':
            self.plainTextEdit_2.clear()
            self.msg = self.cur.execute(f"""SELECT * FROM msges WHERE addressee LIKE '{client_data[1]}' and label LIKE
            '{self.comboBox_2.currentText()}'""").fetchall()
            self.plainTextEdit_2.appendPlainText(f'Send by: {self.msg[0][2]}')
            self.plainTextEdit_2.appendPlainText(f'Title: {self.msg[0][3]}')
            if self.msg[0][-1] == 0:
                self.plainTextEdit_2.appendPlainText('Status: Непрочитанно')
                self.cur.execute(f"""UPDATE msges SET status = 1 WHERE addressee LIKE
                '{self.msg[0][1]}' AND sender LIKE '{self.msg[0][2]}' AND label LIKE '{self.msg[0][3]}' AND
                msg LIKE '{self.msg[0][4]}'""")
                self.con.commit()
            elif self.msg[0][-1] == 1:
                self.plainTextEdit_2.appendPlainText('Status: Прочитанно')
            self.plainTextEdit_2.appendPlainText(self.msg[0][4])
        self.activate()

    def activate(self):
        self.comboBox_2.clear()
        self.comboBox_2.addItems([i[0] for i in self.cur.execute(f"""SELECT label FROM msges WHERE
                 addressee like '{client_data[1]}'""")])

    def delete_msg(self):
        if self.msg:
            self.cur.execute(f"""DELETE FROM msges WHERE addressee LIKE
                '{self.msg[0][1]}' AND label LIKE '{self.msg[0][3]}' """)
            self.con.commit()

    def open_txtfile(self):
        s = f'{self.msg[0][2]}'
        while True:
            try:
                f = open((s + '.txt'))
                f.close()
                s += '_copy'
            except FileNotFoundError:
                break
        with open((s + '.txt'), 'w+', encoding='utf-8') as out:
            out.write(self.plainTextEdit_2.toPlainText())

    def change_profile(self):
        if client_data[-1]:
            self.label.setPixmap(QtGui.QPixmap(client_data[-1]))
        else:
            self.label.setPixmap(QtGui.QPixmap("picture.png"))
        self.my_change_widget.cod = 3
        self.my_change_widget.plainTextEdit_2.clear()
        self.my_change_widget.textEdit.clear()
        self.my_change_widget.plainTextEdit_2.appendPlainText(
            'Укажите ваш новый путь к картинке профиля и подтвердите его!')
        self.my_change_widget.show()

    def change_name(self):
        self.label_2.setText(client_data[2])
        self.my_change_widget.cod = 1
        self.my_change_widget.plainTextEdit_2.clear()
        self.my_change_widget.textEdit.clear()
        self.my_change_widget.plainTextEdit_2.appendPlainText('Укажите ваше новое имя и подтвердите его!')
        self.my_change_widget.show()

    def change_login(self):
        self.label_3.setText(client_data[1])
        self.my_change_widget.cod = 2
        self.my_change_widget.plainTextEdit_2.clear()
        self.my_change_widget.textEdit.clear()
        self.my_change_widget.plainTextEdit_2.appendPlainText('Укажите ваш новый логин и подтвердите его!')
        self.my_change_widget.show()


class ChangeWidget(QDialog, Ui_Dialog1):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.con = sqlite3.connect('my_project_bd.db')
        self.cur = self.con.cursor()
        self.cod = 0
        self.pushButton.clicked.connect(self.close_widg)
        self.pushButton_2.clicked.connect(self.ok)
        self.plainTextEdit_2.setReadOnly(True)

    def close_widg(self):
        self.hide()

    def ok(self):
        global client_data
        if self.cod == 1:
            if self.textEdit.toPlainText() != 'Имя' \
                    and len(self.textEdit.toPlainText()) > 0 and all(i.isalpha() for i in self.textEdit.toPlainText()):
                self.cur.execute(f"""UPDATE clients_all SET client_name = '{self.textEdit.toPlainText()}' 
                WHERE client_login LIKE '{client_data[1]}'""")
                self.con.commit()
                client_data = get_client_data(client_data[1])
                self.hide()
        elif self.cod == 2:
            if len(self.textEdit.toPlainText()) >= 8 and all(i.isascii() for i in self.textEdit.toPlainText()):
                if not get_client_data(self.textEdit.toPlainText()):
                    self.cur.execute(f"""UPDATE clients_all SET client_login = '{self.textEdit.toPlainText()}' 
                    WHERE client_login LIKE '{client_data[1]}'""")
                    self.con.commit()
                    self.cur.execute(f"""UPDATE msges SET addressee = '{self.textEdit.toPlainText()}' 
                    WHERE addressee LIKE '{client_data[1]}'""")
                    self.con.commit()
                    self.cur.execute(f"""UPDATE msges SET sender = '{self.textEdit.toPlainText()}' 
                                        WHERE sender LIKE '{client_data[1]}'""")
                    self.con.commit()
                    client_data = get_client_data(self.textEdit.toPlainText())
                    self.hide()
        elif self.cod == 3:
            if self.textEdit.toPlainText():
                self.cur.execute(f"""UPDATE clients_all SET profile_pic = '{self.textEdit.toPlainText()}' 
                WHERE client_login LIKE '{client_data[1]}'""")
                self.con.commit()
                client_data = get_client_data(client_data[1])
                self.hide()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex3 = MyThirdWidget()
    ex2 = MySecondWidget()
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
