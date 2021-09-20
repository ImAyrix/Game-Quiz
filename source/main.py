from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import os
import sqlite3
import random
from panel import Ui_quiz

# Questions Database
conn = sqlite3.connect('questions.db')
c = conn.cursor()

# User information Database
conn2 = sqlite3.connect('info_user.db')
c2 = conn2.cursor()
c2.execute('''CREATE TABLE IF NOT EXISTS level(
            level text
            )''')
conn2.commit()

# default time question
time = 8

# answer question variable
answer_question = 0

check_answer = True

# Page status variable (question page/other page)
status_question = False

# level variable
level = 0

# check buy time and wrong option
status_buy_time = True
status_buy_option = True


class Root(QMainWindow):

    def __init__(self):
        global level

        QMainWindow.__init__(self)
        self.ui = Ui_quiz()
        self.ui.setupUi(self)
        self.oldPos = []
        self.show()

        # set timer
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.timer_func)
        self.timer.start(1000)

        # set info user
        self.ui.username.setText(os.getlogin())
        self.ui.profile.setText(str(os.getlogin())[0].lower())
        self.ui.username2.setText(os.getlogin())

        # Set level
        try:
            c2.execute('SELECT * FROM level')
            level = c2.fetchone()[0]
            self.ui.level.setText(level)
            self.ui.level2.setText(level)
        except:
            c2.execute('INSERT INTO level VALUES(1)')
            conn2.commit()

        # Set Button
        self.ui.letsgo.clicked.connect(lambda: self.ui.pages.setCurrentWidget(self.ui.select))
        self.ui.tech.clicked.connect(self.tech)
        self.ui.sport.clicked.connect(self.sport)
        self.ui.info.clicked.connect(self.info)
        self.ui.cinema.clicked.connect(self.cinema)
        self.ui.math.clicked.connect(self.math)
        self.ui.nature.clicked.connect(self.nature)

        # set option
        self.ui.one.clicked.connect(self.one)
        self.ui.two.clicked.connect(self.two)
        self.ui.three.clicked.connect(self.three)
        self.ui.four.clicked.connect(self.four)

        # set Button end question
        self.ui.end.clicked.connect(lambda: self.ui.pages.setCurrentWidget(self.ui.select))
        self.ui.end.clicked.connect(self.end_question)
        self.ui.end2.clicked.connect(lambda: self.ui.pages.setCurrentWidget(self.ui.select))
        self.ui.end2.clicked.connect(self.end_question)

        # help user
        self.ui.buy_option.clicked.connect(self.wrong_option)
        self.ui.buy_time.clicked.connect(self.buy_time)

    def mousePressEvent(self, evt):
        self.oldPos = evt.globalPos()

    def mouseMoveEvent(self, evt):

        delta = QPoint(evt.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = evt.globalPos()

    # Technology category
    def tech(self):
        global conn
        global c
        global time
        global check_answer
        global status_question

        self.ui.next.clicked.connect(self.tech)
        self.ui.next2.clicked.connect(self.tech)
        self.ui.pages.setCurrentWidget(self.ui.question)

        c.execute('SELECT * FROM tech')
        questions = c.fetchall()
        tedad = len(questions)
        ran = random.randrange(0, tedad)
        questions = questions[ran]
        self.set_qu(questions[0], questions[1], questions[2], questions[3], questions[4], questions[5])

        check_answer = True
        status_question = True
        time = 8

    # Sports category
    def sport(self):
        global conn
        global c
        global time
        global check_answer
        global status_question

        self.ui.next.clicked.connect(self.sport)
        self.ui.next2.clicked.connect(self.sport)
        self.ui.pages.setCurrentWidget(self.ui.question)

        c.execute('SELECT * FROM Football')
        questions = c.fetchall()
        tedad = len(questions)
        ran = random.randrange(0, tedad)
        questions = questions[ran]
        self.set_qu(questions[0], questions[1], questions[2], questions[3], questions[4], questions[5])

        check_answer = True
        status_question = True
        time = 8

    def info(self):
        global conn
        global c
        global time
        global check_answer
        global status_question

        self.ui.next.clicked.connect(self.info)
        self.ui.next2.clicked.connect(self.info)
        self.ui.pages.setCurrentWidget(self.ui.question)

        c.execute('SELECT * FROM information')
        questions = c.fetchall()
        tedad = len(questions)
        ran = random.randrange(0, tedad)
        questions = questions[ran]
        self.set_qu(questions[0], questions[1], questions[2], questions[3], questions[4], questions[5])

        check_answer = True
        status_question = True
        time = 8

    def cinema(self):
        global conn
        global c
        global time
        global check_answer
        global status_question

        self.ui.next.clicked.connect(self.cinema)
        self.ui.next2.clicked.connect(self.cinema)
        self.ui.pages.setCurrentWidget(self.ui.question)

        c.execute('SELECT * FROM cinema')
        questions = c.fetchall()
        tedad = len(questions)
        ran = random.randrange(0, tedad)
        questions = questions[ran]
        self.set_qu(questions[0], questions[1], questions[2], questions[3], questions[4], questions[5])

        check_answer = True
        status_question = True
        time = 8

    def math(self):
        global conn
        global c
        global time
        global check_answer
        global status_question

        self.ui.next.clicked.connect(self.math)
        self.ui.next2.clicked.connect(self.math)
        self.ui.pages.setCurrentWidget(self.ui.question)

        c.execute('SELECT * FROM math')
        questions = c.fetchall()
        tedad = len(questions)
        ran = random.randrange(0, tedad)
        questions = questions[ran]
        self.set_qu(questions[0], questions[1], questions[2], questions[3], questions[4], questions[5])

        check_answer = True
        status_question = True
        time = 8

    def nature(self):
        global conn
        global c
        global time
        global check_answer
        global status_question

        self.ui.next.clicked.connect(self.nature)
        self.ui.next2.clicked.connect(self.nature)
        self.ui.pages.setCurrentWidget(self.ui.question)

        c.execute('SELECT * FROM nature')
        questions = c.fetchall()
        tedad = len(questions)
        ran = random.randrange(0, tedad)
        questions = questions[ran]
        self.set_qu(questions[0], questions[1], questions[2], questions[3], questions[4], questions[5])

        check_answer = True
        status_question = True
        time = 8

    # Set option questions
    def set_qu(self, question, one, two, three, four, answer):
        global answer_question
        global check_answer
        global status_buy_option
        global status_buy_time

        # clear Ui
        self.ui.quest.clear()
        self.ui.quest_2.clear()

        status_buy_time = True
        status_buy_option = True

        self.ui.line1.hide()
        self.ui.line2.hide()
        self.ui.line3.hide()
        self.ui.line4.hide()

        if len(question) <= 45:
            self.ui.quest.setText(question)
            self.ui.quest_2.clear()
        else:
            self.ui.quest.setText(question[:40])
            self.ui.quest_2.setText(question[40:])

        self.ui.quest_win.setText(question)
        self.ui.quest_lost.setText(question)
        self.ui.one.setText(one)
        self.ui.two.setText(two)
        self.ui.three.setText(three)
        self.ui.four.setText(four)
        answer_question = answer
        if answer == 1:
            self.ui.answer_win.setText(one)
            self.ui.answer_lost.setText(one)
        elif answer == 2:
            self.ui.answer_win.setText(two)
            self.ui.answer_lost.setText(two)
        elif answer == 3:
            self.ui.answer_win.setText(three)
            self.ui.answer_lost.setText(three)
        else:
            self.ui.answer_win.setText(four)
            self.ui.answer_lost.setText(four)

    # One second timer
    def timer_func(self):
        global time
        global status_question
        global level

        if status_question:
            # timer
            time -= 1
            if len(str(time)) == 2:
                self.ui.time.setText('00:'+str(time))
            else:
                self.ui.time.setText('00:0' + str(time))
            if time == 0 and check_answer:
                self.ui.pages.setCurrentWidget(self.ui.False_answer)
                status_question = False

            c2.execute('SELECT * FROM level')
            level = c2.fetchone()[0]
            self.ui.level.setText(level)
            self.ui.level2.setText(level)

    # Option one to four
    def one(self):
        self.check(1)

    def two(self):
        self.check(2)

    def three(self):
        self.check(3)

    def four(self):
        self.check(4)

    # Check user answer
    def check(self, user_answer):
        global check_answer
        global answer_question
        global level

        if user_answer == answer_question:
            check_answer = False
            self.ui.pages.setCurrentWidget(self.ui.True_answer)
            new_level = float(level) + 1
            sql_update_query = f"""Update level set level = {new_level} where level = {level}"""
            c2.execute(sql_update_query)
            conn2.commit()
        else:
            self.ui.pages.setCurrentWidget(self.ui.False_answer)

    # help user (show wrong option)
    def wrong_option(self):
        global answer_question
        global level
        global status_buy_option

        if status_buy_option:
            status_buy_option = False
            if answer_question != 1:
                self.ui.line1.show()
            elif answer_question != 2:
                self.ui.line2.show()
            elif answer_question != 3:
                self.ui.line3.show()
            elif answer_question != 4:
                self.ui.line4.show()
            new_level = float(level) - 0.5
            sql_update_query = f"""Update level set level = {new_level} where level = {level}"""
            c2.execute(sql_update_query)
            conn2.commit()

    # buy time
    @staticmethod
    def buy_time():
        global time
        global level
        global status_buy_time

        if status_buy_time:
            time += 5
            status_buy_time = False
            new_level = float(level) - 0.5
            sql_update_query = f"""Update level set level = {new_level} where level = {level}"""
            c2.execute(sql_update_query)
            conn2.commit()

    # end question
    @staticmethod
    def end_question():
        global status_question
        status_question = False


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    root = Root()
    sys.exit(app.exec_())
