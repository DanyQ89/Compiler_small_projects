import re


class PasswordError(Exception):
    pass


class LengthError(PasswordError):
    pass


class LetterError(PasswordError):
    pass


class DigitError(PasswordError):
    pass


class SequenceError(PasswordError):
    pass


def check_password(password):
    try:
        if password != 'Ctrl+Break':
            try:
                if len(password) >= 9:
                    try:
                        if password != password.lower() and password != password.upper():
                            try:
                                if re.findall('\d+', password):
                                    try:
                                        qwerty = ('qwertyuiopйцукенгшщзхъ asdfghjklфывапролджэё zxcvbnmячсмитьбю'
                                                  ' 1234567890')
                                        password_low = password.lower()
                                        for i in range(len(password_low) - 2):
                                            word = password_low[i] + password_low[i + 1] + password_low[i + 2]
                                            if word in qwerty:
                                                raise SequenceError('error')
                                        return 'ok'
                                    except SequenceError as err:
                                        raise SequenceError(err)
                                else:
                                    raise DigitError('error')
                            except DigitError as err:
                                raise DigitError(err)
                        else:
                            raise LetterError('error')
                    except LetterError as err:
                        raise LetterError(err)
                else:
                    raise LengthError('error')
            except LengthError as err:
                raise LengthError(err)
        else:
            raise KeyboardInterrupt('Bye-Bye')
    except KeyboardInterrupt:
        return 'Bye-Bye'


arr = []
while True:
    a = input()
    try:

        arr.append(check_password(a))
        break
    except Exception as err:
        arr.append(err.__class__.__name__)

print(*arr, sep='\n')
