
class BattleGround:

    def __init__(self, first_char, second_char):

        self.first_char = first_char
        self.second_char = second_char
        self.spells = []
        self.loser = None
        self.debug = False

# ************************************ НАЧАЛО ЛОГИКИ ************************************ #

    def checking_defeat_everybody(self):
        """Условие поражения для всех сразу"""
        if self.first_char.player and self.second_char.player and self.first_char.health <= 0 >= self.second_char.health:
            self.loser = 'everybody'

    def checking_defeat_first(self):
        """Условие поражения для второго персонажа"""

        if self.first_char.health <= 0:
            self.loser = self.first_char

    def checking_defeat_second(self):
        """Условие поражения для первого персонажа"""

        if self.second_char.health <= 0:
            self.loser = self.second_char

    def who_is_defeated(self):
        self.checking_defeat_everybody()
        if not self.loser:
            self.checking_defeat_first()
            self.checking_defeat_second()

    def checking_luck(self):
        """Отнимает удачу у проигравшего и проверяет оставшееся количество. Если удача = 0 --> убивает персонажа"""
        if self.loser != 'everybody':
            if self.loser.player:
                self.loser.luck -= 1
                if self.loser.luck < 0:
                    self.loser.alive = False
        else:
            for i in [self.first_char, self.second_char]:
                i.luck -= 1
                if i.luck < 0:
                    i.alive = False

# ************************************* КОНЕЦ ЛОГИКИ ************************************ #

    def refresh(self):
        for i in [self.first_char, self.second_char]:
            if i.mana < 0:
                i.mana = 0
            i.mana += 10 + i.dark_magic_skill*0.05 + i.light_magic_skill*0.05
            if i.mana > 100:
                i.mana = 100
            if i.psyche < 0:
                i.psyche = 0
            i.psyche += i.psyche*0.07 + 1
            if i.psyche > 100:
                i.psyche = 100

    def spell_activate(self):
        """Проверяет активность, если активен - вызывает эффект, а так же удаляет отработанные спеллы"""
        spell_list_len = len(self.spells)
        for _ in range(spell_list_len):
            for spell in self.spells:
                # Проверка на активность спелла (кастился ли он уже)
                if spell.activated:
                    if spell.count > 0:
                        spell.do()
                        spell.count -= 1
                        spell.activated = False
                    else:
                        # Удаление отработанного спелла
                        self.spells.remove(spell)
                        break

    def debug_mod(self, text):
        if self.debug:
            print(text)
# ***************************** ТУТ НАЧИНАЕТСЯ САМОЕ ВАЖНОЕ ***************************** #

    def main(self):
        """Здесь кастуются спелы и проходят проверки. Работает, пока кто-нибудь не проиграет"""
        from mechanics.action_choice import ActionChoice

        while not self.loser:
            # Выбор спелла игроками
            first_set = ActionChoice.do(self.first_char)
            second_set = ActionChoice.do(self.second_char)

            # Проверка скорости
            if first_set[0].speed < second_set[0].speed:

                # Условия таргета для первого игрока
                target = self.first_char if first_set[1] == 'self' else self.second_char
                first_spell = first_set[0].do(self.first_char, target)

                # Условия таргета для второго игрока
                target = self.second_char if first_set[1] == 'self' else self.first_char
                second_spell = second_set[0].do(self.second_char, target)
            else:
                # Условия таргета для второго игрока
                target = self.second_char if first_set[1] == 'self' else self.first_char
                first_spell = second_set[0].do(self.second_char, target)

                # Условие для таргета первого игрока
                target = self.first_char if first_set[1] == 'self' else self.second_char
                second_spell = first_set[0].do(self.first_char, target)

            # Добавление спеллов в стук спеллов
            self.spells.insert(0, second_spell)
            self.spells.insert(0, first_spell)
            # Поочередное применение спеллов
            self.spell_activate()

            # Прерывает сражение, если есть проигравший
            self.debug_mod(f"\n{self.first_char.name}: health - {self.first_char.health}")
            self.debug_mod(f"\n{self.second_char.name}: health - {self.second_char.health}")
            self.who_is_defeated()
            if self.loser:
                break
            self.debug_mod(f"\n{self.first_char.name}: health - {self.first_char.health}, "
                                                   f"psyche - {self.first_char.psyche}, "
                                                   f"mana - {self.first_char.mana}")
            self.debug_mod(f"{self.second_char.name}: health - {self.second_char.health}, "
                           f"psyche - {self.second_char.psyche}, "
                           f"mana - {self.second_char.mana}\n")
            self.refresh()
            self.debug_mod(f"\n{self.first_char.name}: health - {self.first_char.health}, "
                                                   f"psyche - {self.first_char.psyche}, "
                                                   f"mana - {self.first_char.mana}")
            self.debug_mod(f"\n{self.second_char.name}: health - {self.second_char.health}, "
                           f"psyche - {self.second_char.psyche}, "
                           f"mana - {self.second_char.mana}\n")

        self.checking_luck()

# *************************** ТУТ ЗАКАНЧИВАЕТСЯ САМОЕ ВАЖНОЕ **************************** #

