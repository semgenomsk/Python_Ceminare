from datetime import datetime


def log(func):
    def wapper(*args):
        with open("log.csw", "a", encoding="utf-8") as log_file:
            log_file.write(f'{datetime.now()} - запущена функция {func.__name__} {"с аргументами" if args else "без аргументов"} ({func.__doc__})\n')
        return func(*args)
    return wapper
