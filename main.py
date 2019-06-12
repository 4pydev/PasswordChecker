import urwid


def is_very_long(password):
    return True if len(password)>12 else False


def has_digits(password):
    for char in password:
        if char.isdigit():
            return True
    return False


def has_letters(password):
    for char in password:
        if char.isalpha():
            return True
    return False


def has_upper_letters(password):
    for char in password:
        if char.isupper():
            return True
    return False


def has_lower_letters(password):
    for char in password:
        if char.islower():
            return True
    return False


def has_symbol(password):
    for char in password:
        if not char.isdigit() and not char.isalpha():
            return True
    return False


def has_not_only_symbols(password):
    for char in password:
        if not has_symbol(char):
            return True
    return False


def get_score(password):
    score = 0
    rating_funcs = [
        is_very_long,
        has_digits,
        has_letters,
        has_upper_letters,
        has_lower_letters,
        has_symbol,
        has_not_only_symbols
    ]
    for func in rating_funcs:
        if func(password):
            score += 2
    return score


def main():

    def on_ask_change(edit, new_edit_text):
        reply.set_text('Password rating: %s of 14' % (get_score(new_edit_text)))


    ask = urwid.Edit('Enter a password: ')
    reply = urwid.Text("")
    menu = urwid.Pile([ask, reply])
    menu = urwid.Filler(menu, valign='top')
    urwid.connect_signal(ask, 'change', on_ask_change)
    urwid.MainLoop(menu).run()


if __name__ == '__main__':
    main()
