

class NameRandom:

    @staticmethod
    def choice(male):
        from data.data_names import data_names
        from random import choice
        first = choice(data_names[male]['first'])
        second = choice(data_names['second'])
        order = choice(data_names['order'])
        return f'{first} {second} из ордена {order}'
