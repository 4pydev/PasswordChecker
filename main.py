import urwid


def is_very_long(password):
    return len(password)>12


def has_digits(password):
    return any(char.isdigit() for char in password)


def has_letters(password):
    return any(char.isalpha() for char in password)


def has_upper_letters(password):
    return any(char.isupper() for char in password)


def has_lower_letters(password):
    return any(char.islower() for char in password)


def has_symbol(password):
    return any(
        (not char.isdigit() and not char.isalpha()) for char in password
    )


def has_not_only_symbols(password):
    return any(has_symbol(char) for char in password)


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
