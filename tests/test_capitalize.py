from scripts.capitalize import capitalize


def test_capitalize():
    if capitalize('hello') != 'Hello':
        raise Exception('Function works incorrect!')

    if capitalize('') != '':
        raise Exception('Function must work with empty string')

    if capitalize(' ask him') != 'Ask him':
        raise Exception("Function shouldn't strip a string")


test_capitalize()
if __name__ == '__main__':
    test_capitalize()
