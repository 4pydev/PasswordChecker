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
    password = input('Enter a password: ')

    print('Password rating: {} of 14'.format(get_score(password)))


if __name__ == '__main__':
    main()
