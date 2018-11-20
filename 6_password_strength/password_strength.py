import re
from getpass import getpass


def has_upper_and_lower(password):
    return re.findall(r'[A-Z]', password) and re.findall(r'[a-z]', password)

def has_special_symbols(password):
    return re.findall(r'\W', password)


def has_digits(password):
    return re.findall(r'\d', password)


def enough_length(password):
    return len(password) > 7


def has_no_repeating_symbols(password):
    return max([password.count(c) for c in password]) < 3


def has_no_phone_numbers(password):
    return len(re.findall(r'^((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}$', password)) < 1


def get_password_strength(password):
    checks = {has_upper_and_lower,
              has_special_symbols,
              has_digits,
              enough_length,
              has_no_repeating_symbols,
              has_no_phone_numbers}

    check_cost = max_strengthg / len(checks)

    return int(check_cost * sum([1 if check(password) else 0 for check in checks]))


if __name__ == '__main__':
    max_strength = 10
    user_password = getpass('Введите пароль: ')
    print('Оценка пароля: ', get_password_strength(user_password))

