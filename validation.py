from flask import flash


def is_valid_form(lower, upper):
    return (is_int(lower) and is_int(upper) and is_positive(int(lower)) and
            is_positive(int(upper)) and is_bigger(int(lower), int(upper)))


def is_bigger(lower, upper):
    return upper > lower


def is_positive(number):
    return number > 0


def is_int(number):
    try:
        int(number)
        return True
    except:
        flash('Du maa skrive inn eit tal')
        return False
