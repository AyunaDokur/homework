def is_contains(string, list_ = ['.com', '.ru', '.net']):
    after_coma = string[string.rfind('.'): : 1]
    flag = 0
    if string.find('@') == -1:
        return False
    else:
        for i in list_:
            if i == after_coma:
                flag = 1
                break
    if flag == 1:
        return True
    else:
        return False
def send_email(messege, recipient,*,sender = 'university.help@gmail.com'):
    if is_contains(sender) is False or is_contains(recipient) is False:
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
    elif sender == recipient:
        print('Нельзя отправить письмо самому себе!')
    elif sender == 'university.help@gmail.com':
        print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}.')
    else:
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}')


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')