import command_system
from models import Person as Passport
from config import db

command_distribution = command_system.Command()

def name():
    from_id = command_system.arg['system_vars']['from_id']
    User = Passport.query.filter_by(vk_id=from_id).first()
    if command_system.arg['notsystem_vars'][1] == None:
        message = 'Имя не найдено а переменных сообщения, пожайлуста напишите имя в сообщении\np.s. Убедитесь в том что у вас нет лишних пробелов!'
    else:
        new_name = ''
        for n in command_system.arg['notsystem_vars'][1:]:
            new_name += n + ' '
        name = new_name[:-1]
        User.Name = name
        db.session.commit()
        message = 'Имя [id' + str(from_id) + '|пользователя] установленно как ' + name + '!'
    attachment = ''
    keyboard = {}
    return message, attachment, keyboard

command_distribution.keysm = ['name', 'имя']
command_distribution.keysp = ['set_name']
command_distribution.desciption = 'Устанавивает ваше имя в паспорте'
command_distribution.process = name
