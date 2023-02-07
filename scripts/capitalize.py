def capitalize(text):
    if text == '':
        return ''
    head, *chars = text
    return f'{head.upper()}{"".join(chars)}'
