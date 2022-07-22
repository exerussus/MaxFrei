

class NameRandom:

    @staticmethod
    def choice(gender=None):
        from data.sql_commander import full_random_name
        from random import choice

        firsts, seconds, orders = full_random_name(gender)
        first_name = choice(firsts)
        second_name = choice(seconds)
        order = choice(orders)
        return f"{first_name} {second_name} из ордена {order}"
