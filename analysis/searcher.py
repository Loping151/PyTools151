# This code is for fun only!

import webbrowser
import traceback
import string
import random

def stacksearch(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception:
            error_msg = traceback.format_exc().splitlines()[-1]
            print(f"Error: {error_msg}")
            webbrowser.open(f"https://stackoverflow.com/search?q={error_msg}")
            raise
    return wrapper


def canyoubaidu(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception:
            error_msg = traceback.format_exc().splitlines()[-1]
            print(f"Error: {error_msg}")
            webbrowser.open(f"https://buhuibaidu.me/?s={error_msg}")
            raise
    return wrapper


def aisearch151(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception:
            rid = ''.join(random.choices(string.ascii_letters + string.digits, k=30))
            error_msg = traceback.format_exc().splitlines()[-1]
            print(f"Error: {error_msg}")
            webbrowser.open(f"http://search.loping151.com/ui/search.html?q={error_msg}&rid={rid}")
            raise
    return wrapper


if __name__ == "__main__":
    @canyoubaidu
    @stacksearch
    @aisearch151
    def faulty_function():
        return 1 / 0

    faulty_function()