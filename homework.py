import datetime as dt

# класс записи с автодатой

class Record:
    def __init__(self, amount, comment, date=None):
        self.amount = amount
        self.comment = comment
        if date is None:
            self.date = dt.date.today()
        else:
            self.date = dt.datetime.strptime(date, '%d.%m.%Y').date()

class Calculator:
    def __init__(self, limit):
        self.limit = limit

# функция записи записей в список

        self.records = []
    def add_record(self, new_record):
        self.records.append(new_record)

# сколько набрано было за сегодня или неделю

    def get_today_stats(self):
        today = dt.date.today()
        all_in_day = 0
        for rec in self.records:
            if rec.date == today:
                all_in_day += rec.amount
        return all_in_day
    def get_week_stats(self):
        today = dt.date.today()
        week_ago = today - dt.timedelta(days=7)
        all_in_week = 0
        for rec in self.records:
            if week_ago < rec.date <= today:
                all_in_week += rec.amount
        return all_in_week
    
# остаток от дневного лимита

    def get_today_remained(self):
        return self.limit - self.get_today_stats()

class CaloriesCalculator(Calculator):
    def get_calories_remained(self):
        available_today = self.get_today_remained()
        if available_today > 0:
            return ('Сегодня можно съесть что-нибудь ещё, '
                    f'но с общей калорийностью не более {available_today} кКал')
        else:
            return 'Хватит есть!'

class CashCalculator(Calculator):
    USD_RATE = 92.5
    EURO_RATE = 101.7
    def get_today_cash_remained(self, currency):
        currency_rate = {'rub':('руб', 1.0),
                         'usd':('USD', self.USD_RATE),
                         'eur':('Euro', self.EURO_RATE)}
        if currency not in currency_rate:
            return 'Доступны только валюты rub, usd или eur'

# считаем баланс и переводим в какую то валюту (изначально вводится все в рублях)  

        currency_name, currency_course = currency_rate[currency]
        balance_for_today = self.get_today_remained()
        balance_for_today_rate = round(abs(balance_for_today/currency_course), 2)

        if balance_for_today == 0:
            return 'Денег нет, держись'
        elif balance_for_today > 0:
            return f'На сегодня осталось {balance_for_today_rate} {currency_name}'
        else:
            return ('Денег нет, держись: ' 
                    f'твой долг - {balance_for_today_rate} {currency_name}')

# проверка

r7 = Record(145, comment="кофе") 
r8 = Record(amount=300, comment="Серёге за обед")
r9 = Record(3000, "бар в Танин др","01.09.2024")
r1 = Record(145, "Безудержный шопинг")
r2 = Record(amount=1568, comment="Наполнение потребительской корзины")
r3 = Record(amount=691, comment="Катание на такси")
r4 = Record(1186, "Кусок тортика. И ещё один.")
r5 = Record(amount=84, comment="Йогурт.")
r6 = Record(1140, comment="Баночка чипсов.")

rr1 = CashCalculator(1000)
rr2 = CaloriesCalculator(2500)
rr1.add_record(r1)
rr1.add_record(r7)
rr1.add_record(r8)
rr2.add_record(r4)
rr2.add_record(r5)
rr2.add_record(r6)
rr1.add_record(r9)
print(rr1.get_today_cash_remained("rub"))
print(rr2.get_calories_remained())