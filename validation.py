from flask import flash


def is_valid_form(lower, upper):
    return (is_int(lower) and is_int(upper) and is_positive(int(lower)) and
            is_positive(int(upper)) and is_bigger(int(lower), int(upper)))


def is_int(number):
    try:
        int(number)
        return True
    except:
        flash('Du må skrive inn eit tal')
        return False


def is_positive(number):
    if number <= 0:
        flash('Begge tal må vere positive')
        return False
    return True


def is_bigger(lower, upper):
    if lower >= upper:
        flash('"Til" må vere større enn "Frå"')
        return False
    return True
