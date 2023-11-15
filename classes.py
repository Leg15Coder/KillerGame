import datetime as dt


DATE_MASK = "%d.%m.%Y"
GREETING = "textes/greeting.html"
HELP = 'textes/help.html'


class User(object):
    def __init__(self, **kwargs):
        self.id = kwargs['id']
        self.name = kwargs['name']
        self.surname = kwargs['surname']
        self.patronymic = kwargs['patronymic']
        self.birth_date = dt.datetime.strptime(kwargs['birth_date'], DATE_MASK)
        self.grade = kwargs['grade']
        self.balance = kwargs['balance']
        self.completed = kwargs['completed']
        self.failed = kwargs['failed']
        self.caught = kwargs['caught']
        self.state = kwargs['state']

    def age(self):
        return (dt.datetime.today() - self.birth_date).years
