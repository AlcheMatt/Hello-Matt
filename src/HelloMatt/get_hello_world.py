HELLO_WORLD = "Hello World!"


def get_string(s):
    return s if s else HELLO_WORLD


if __name__ == '__main__':
    get_string('')
