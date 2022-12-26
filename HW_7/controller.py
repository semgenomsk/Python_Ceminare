import view
from logger import log
import model


def start():
    view.greeting()
    while True:
        match view.menu():
            case '1':
                pass
            case '2':
                pass
            case '3':
                break
