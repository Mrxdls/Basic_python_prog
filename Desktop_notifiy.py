from plyer import notification
import time
if __name__ == '__main__':
    while True:
        notification.notify(
            title = "BREAK",
            message = "Take 5 min break",
            app_icon = "/home/cyphersage/Downloads/python_projects/Py_begineer_projects/Icon.ico",
            timeout = 5
        )
        time.sleep(45*60)
        