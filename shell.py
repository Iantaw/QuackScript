import quackscript

while True:
    text = input('quackscript > ')
    result, error = quackscript.run('<stdin>', text)
    
    if error: print(error.as_string())
    elif result: print(repr(result))