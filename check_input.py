import re


class CheckInput:
    def verification_phone(self, phone: str) -> str:
        self.phone = phone
        try:
            phone = re.sub("[^0-9]", "", phone)  # оставляет только цифры
            if phone.startswith("0") or phone.startswith("+", 1):
                phone = "38" + phone
            elif phone.startswith("380") and len(phone) == 12:
                return phone
            elif phone == "" or phone == " ":
                print("\033[1;31m" + "Номер введён некорректно!")
                exit()
            elif phone.startswith("+"):
                phone = phone[1:]
                return phone
            else:
                return phone
        except Exception:
            print("\033[1;31m" + "Номер введён некорректно!")
            exit()

    def verification_cycles(self, cycles: str) -> int:
        try:
            self.cycles = cycles
            cycles = re.sub("[^0-9]", "", cycles)
            return int(cycles)
        except ValueError:
            print("\033[1;31m" + "Неправильное кол-во циклов!")
            exit()


if __name__ == "__main__":
    phone = input("Введите номер телефона: ")
    cycles = input("Введите колличество циклов: ")
    print(CheckInput().verification_phone(phone))
    print(CheckInput().verification_cycles(cycles))
