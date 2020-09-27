from random import choice


class GenerateInfo:

    NAME = "".join(
        [
            choice("1234567890abcdefghigklmnopqrstuvyxwzABCDEFGHIGKLMNOPQRSTUVYXWZ")
            for i in range(8)
        ]
    )

    def password(self):
        self.password = self.NAME + str(choice("!.#&"))
        return self.password

    def username(self):
        self.username = "".join(
            [choice("1234567890abcdefghigklmnopqrstuvyxwz") for x in range(8)]
        )
        return self.username

    def email(self):
        mails = [
            "@gmail.com",
            "@ukr.net",
            "@rambler.ru",
            "@mail.ru",
            "@yandex.ru",
            "@meta.ua",
        ]
        self.email = self.NAME.lower() + choice(mails)
        return self.email

    def russian_name(self):
        self.names = [
            "Александр",
            "Алексей",
            "Анастасия",
            "Сергей",
            "Никита",
            "Дмитрий",
            "Олег",
            "Влад",
            "Женя",
            "Максим",
            "Виталий",
            "Виктория",
        ]
        return choice(self.names)


if __name__ == "__main__":
    print(
        f"Почта: {GenerateInfo().email()}",
        f"Имя: {GenerateInfo().russian_name()}",
        f"Никнейм: {GenerateInfo().username()}",
        f"Пароль: {GenerateInfo().password()}",
        sep="\n",
    )
