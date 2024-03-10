import webbrowser
import traceback

def debugger(func):
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


if __name__ == "__main__":
    @canyoubaidu
    @debugger
    def faulty_function():
        return 1 / 0

    faulty_function()