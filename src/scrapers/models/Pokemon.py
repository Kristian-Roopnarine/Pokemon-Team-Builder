class Pokemon:
    STATS_ORDER = ["HP", "Attack", "Defense", "Sp. Atk", "Sp. Def", "Speed"]

    def __init__(
        self, number, name, types, total, hp, atk, defense, sp_atk, sp_def, spd
    ):
        self.number = number
        self.name = self.clean_name(name)
        self.type_1 = types[0]
        self.type_2 = types[1]
        self.total = total
        self.hp = hp
        self.atk = atk
        self.defense = defense
        self.sp_atk = sp_atk
        self.sp_def = sp_def
        self.spd = spd

    def get_stats(self):
        return [self.hp, self.atk, self.defense, self.sp_atk, self.sp_def, self.spd]

    def get_name(self):
        return self.name

    def get_info(self):
        return [
            self.number,
            self.name,
            self.type_1,
            self.type_2,
            self.total,
        ] + self.get_stats()

    def clean_name(self, ele):
        name_list = ele.split(" ")
        return " ".join(name_list[:-1])

    def __str__(self):
        return f"#{self.number} {self.name} - {self.type_1}, {self.type_2} {self.get_stats()}"
