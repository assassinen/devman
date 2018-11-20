import vk
from getpass import getpass


APP_ID = '5825013'


def get_user_login():
    return input('Введите ваш логин: \n')


def get_user_password():
    return getpass('Введите ваш пароль: \n')


def get_online_friends(login, password):
    session = vk.AuthSession(
        app_id=APP_ID,
        user_login=login,
        user_password=password,
        scope='friends'
    )
    api = vk.API(session)
    friends_id_online = api.friends.getOnline()
    friends_info = api.users.get(
        user_ids=friends_id_online,
    )
    return friends_info


def output_friends_to_console(friends_online):
    for friend in friends_online:
        print(friend['first_name'], friend['last_name'])


if __name__ == '__main__':
    login = get_user_login()
    password = get_user_password()
    friends_online = get_online_friends(login, password)
    output_friends_to_console(friends_online)
