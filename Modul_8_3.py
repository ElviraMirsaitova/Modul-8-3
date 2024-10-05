class Car:

    def __init__(self, model, __vin, __numbers):
        self.model = model
        if self.__is_valid_vin(__vin):
            self.vin = __vin
        if self.__is_valid_numbers(__numbers):
            self.vin = __numbers

    def __is_valid_vin(self, __vin):
        self.vin = __vin
        if not isinstance(self.vin, int):
            raise IncorrectVinNumber('Некорректный тип vin номер')
        if not 1000000 <= self.vin <= 9999999:
            raise IncorrectVinNumber('Некорректный тип vin номер')
        try:
            return self.vin
        except IncorrectVinNumber as exc:
            print(exc.message)

    def __is_valid_numbers(self, __numbers):
        self.numbers = __numbers
        if not isinstance(self.numbers, str):
            raise IncorrectCarNumbers('Некорректный тип данных для номеров')
        if len(self.numbers) != 6:
            raise IncorrectCarNumbers('Неверная длина номера')
        try:
            return self.numbers
        except IncorrectCarNumbers as exc:
            print(exc.message)


class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message


class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        self.message = message


try:
  first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{first.model} успешно создан')

try:
  second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{second.model} успешно создан')

try:
  third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{third.model} успешно создан')
