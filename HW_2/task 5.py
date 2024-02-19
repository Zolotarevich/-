import string

def password_level(password):
    if len(password) < 8:
        return "Недопустимый пароль"
    elif password.isdigit() or ((password.lower() == password or password.upper() == password) and all(map(lambda x: x.isalpha(), list(password)))):
        return "Ненадежный пароль"
    elif all([set(password) & set(string.ascii_lowercase) == set(password),  set(password) & set(string.ascii_uppercase) == set(password)]) or (set(password) & (set(string.ascii_lowercase) | set('0123456789')) == set(password) or set(password) & (set(string.ascii_uppercase) | set('0123456789')) == set(password)):
        return "Слабый пароль"
    elif all([len(set(password) & set(string.ascii_lowercase)), len(set(password) & set(string.ascii_uppercase)), len(set(password) & set('0123456789')), len(set(password) & set('@#$%&*().,-_+'))]):
        return "Надежный пароль"

