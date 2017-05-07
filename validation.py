from flask import flash


def is_valid_form(lower, upper):
    return (is_int(lower) and is_int(upper) and is_positive(int(lower)) and
            is_positive(int(upper)) and is_bigger(int(lower), int(upper)))


def is_int(number):
    try:
        int(number)
        return True
    except:
        try:
            flash('Du må skrive inn eit tal')
        except:
            pass
        return False


def is_positive(number):
    if number <= 0:
        try:
            flash('Begge tal må vere positive')
        except:
            pass
        return False
    return True


def is_bigger(lower, upper):
    if lower >= upper:
        try:
            flash('"Til" må vere større enn "Frå"')
        except:
            pass
        return False
    return True
