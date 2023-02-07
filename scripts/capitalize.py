def capitalize(text):
    if text == '':
        return ''
    head, *chars = text.strip()
    return f'{head.upper()}{"".join(chars)}'
