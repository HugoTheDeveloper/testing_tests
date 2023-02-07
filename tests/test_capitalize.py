from scripts.capitalize import capitalize


def test_capitalize():
    assert capitalize('hello') == 'Hello'
    # 'Function works incorrect!'

    assert capitalize('') == ''

    assert capitalize(' ask him') == 'Ask him'
    # "Function should strip a string"
    print('Function works pretty good')


if __name__ == '__main__':
    test_capitalize()
