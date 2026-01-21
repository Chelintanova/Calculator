import re
import sys

class CalculatorError(Exception):
    """Пользовательские исключения для калькулятора"""
    pass

class Calculator:

    def main(self):
        while True:
            try:
                user_input = input(""">: """).strip()

                if user_input.lower() == 'выход':
                    print("Программа завершена.")
                    sys.exit(0)


                expression = user_input.replace(" ", "")

                if not expression:
                    raise CalculatorError("Пустой ввод")

                a, b, operator = self.validate_and_split(expression)
                result = self.calculate(a, b, operator)
                print(result)

            except CalculatorError as e:
                print(f"{e}")
                print("Программа завершена.")
                sys.exit(1)

            except Exception as e:
                print(f"Непредвиденная ошибка: {e}")
                print("Программа завершена.")
                sys.exit(1)

    def validate_and_split(self, expression):
        operator = None
        operators_exist = []
        errors = []


        for op in ["+", "-", "*", "/"]:
            if op in expression:
                operators_exist.append(op)

        if len(operators_exist) == 0:
            raise CalculatorError("""Неверный формат выражения, ожидается операнд#1, оператор(+,-,*,/), операнд#2""")
        elif len(operators_exist) > 1:
            raise CalculatorError(f"Неверный формат")
        else:
            operator = operators_exist[0]

        parts = re.split(re.escape(operator), expression)

        if len(parts) != 2:
            raise CalculatorError(f"Неверный формат выражения, ожидается операнд#1 {operator} операнд#2")

        left_part, right_part = parts

        if not left_part:
            errors.append("Отсутствует первый операнд")
        else:
            try:
                a = int(left_part)
                if a < 1 or a > 10:
                    errors.append("Некорректное значение первого операнда")
            except ValueError:
                errors.append("Первый операнд не является целым числом")

        if not right_part:
            errors.append("Отсутствует второй операнд")
        else:
            try:
                b = int(right_part)
                if b < 1 or b > 10:
                    errors.append("Некорректное значение второго операнда")
            except ValueError:
                errors.append("Второй операнд не является целым числом")

        if errors:
            error_message = "Обнаружены ошибки:\n" + "\n".join(f"- {error}" for error in errors)
            raise CalculatorError(error_message)

        a = int(left_part)
        b = int(right_part)

        return a, b, operator

    def calculate (self, a, b, operator):
        if operator == "+":
            return a + b
        elif operator == "-":
            return a - b
        elif operator == "*":
            return a * b
        elif operator == "/":
            if b == 0:
                raise CalculatorError("На ноль делить нельзя")
            return a // b


if __name__ == "__main__":
    calculator = Calculator()
    calculator.main()