class Customer:
    # 各問のコードが期待通り動作するように実装
    def __init__(self, first_name, family_name, age):
        self.first_name = first_name
        self.family_name = family_name
        self.age = age

    def full_name(self):
        return f"{self.first_name} {self.family_name}"

    def age(self):
        return f"{self.age}"

    def entry_fee(self):
        if self.age <= 3:
            entry_fee = 0
        elif self.age < 20:
            entry_fee = 1000
        elif 20 <= self.age < 65:
            entry_fee = 1500
        elif 65 <= self.age < 75:
            entry_fee = 1200
        else:
            entry_fee = 500
        return entry_fee

    def info_tsv(self):
        return f"{self.full_name()}\t{self.age}\t{self.entry_fee()}"

    def info_pipe(self):
        return f"{self.full_name()}|{self.age}|{self.entry_fee()}"


ken = Customer(first_name="Ken", family_name="Tanaka", age=15)
tom = Customer(first_name="Tom", family_name="Ford", age=57)
ieyasu = Customer(first_name="Ieyasu", family_name="Tokugawa", age=75)
michelle = Customer(first_name="Michelle", family_name="Tanner", age=3)

# c-5,6
print(ken.entry_fee())  # 1000 という値を出力
print(tom.entry_fee())  # 1500 という値を出力
print(ieyasu.entry_fee())  # 1200 という値を出力
print(michelle.entry_fee())  # 0 という値を出力

# c-7
print(ken.info_tsv())  # "Ken Tanaka,15,1000" という値を出力
print(tom.info_tsv())  # "Tom Ford,57,1500" という値を出力
print(ieyasu.info_tsv())  # "Ieyasu Tokugawa,75,1200" という値を出力
print(michelle.info_tsv())

# c-8
print(ken.info_pipe())  # "Ken Tanaka,15,1000" という値を出力
print(tom.info_pipe())  # "Tom Ford,57,1500" という値を出力
print(ieyasu.info_pipe())  # "Ieyasu Tokugawa,75,1200" という値を出
print(michelle.info_pipe())
