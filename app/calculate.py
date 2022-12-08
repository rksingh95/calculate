class Calculator:
    """
    Class that performs the complex calculation following
    mathematical principles
    """

    def __init__(self, input_number):
        """
        Initializer of the constructor
        :param input_number:
        """
        self.result = None
        _input = input_number.replace(" ", "")
        input_list = [y for x, y in enumerate(_input)]
        self.number_list = []
        self.valid_numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "."]
        self.operator_list = []
        self.temp_num = ""
        self.calc_operations(input_list)

    def calc_operations(self, input_list: list) -> None:
        """
        Performs the mathematical operations based on operands
        :param input_list: list of numbers and operads
        :return:
        """
        try:
            number_list, operator_list = self.from_number(input_list)
            number_list = list(filter(lambda num: num != 0, number_list))
            number_list, operator_list = self.solve(number_list, operator_list)
            operator_list = [
                operator
                for operator in operator_list
                if operator in ["+", "-", "*", "/", "^"]
            ]
            number_list, operator_list = self.solve(number_list, operator_list)
            self.result = number_list[0]
        except IndexError:
            raise IndexError("Invalid encoded value passed for calculation")

    def solve_for_brackets(self, _input: list) -> int:
        """
        Performs the mathematical operations inside the brackets
        :param _input:
        :return:
        """
        if isinstance(_input, float):
            return 0
        input_list = [y for x, y in enumerate(_input)]
        number_list, operator_list = [], []
        temp_num = ""
        for y, x in enumerate(input_list):
            if str(x) in self.valid_numbers:
                temp_num += str(x)
            else:
                if temp_num != "":
                    number_list.append(float(temp_num))
                temp_num = ""
                operator_list.append(x)
            if y + 1 == len(input_list):
                if temp_num != "":
                    number_list.append(float(temp_num))
                temp_num = ""
        number_list, operator_list = self.solve(number_list, operator_list)
        operator_list = [
            operator
            for operator in operator_list
            if operator in ["+", "-", "*", "/", "^"]
        ]
        if operator_list:
            number_list, operator_list = self.solve(number_list, operator_list)
        return number_list[0]

    def from_number(self, input_list: list) -> [list, list]:
        """
        Breaks down string into the list of numbers and operands
        :param input_list:
        :return:
        """
        try:
            temp_num = ""
            number_list = []
            operator_list = []
            brackets = False
            for y, x in enumerate(input_list):
                if str(x) == "(":
                    brackets = True
                    continue
                elif str(x) == ")":
                    brackets = False
                    temp_num = self.solve_for_brackets(temp_num)
                    number_list.append(temp_num)
                    continue
                if brackets:
                    temp_num += str(x)
                else:
                    if str(x) in self.valid_numbers:
                        temp_num = temp_num + str(x)
                    else:
                        if temp_num and temp_num != "":
                            number_list.append(float(temp_num))
                        temp_num = ""
                        operator_list.append(x)
                    if y + 1 is len(input_list):
                        number_list.append(float(temp_num))
                        temp_num = ""
        except (TypeError, ValueError):
            raise "Invalid operations"
        else:
            return number_list, operator_list

    @staticmethod
    def solve(number_list: list, operator_list: list) -> [list, list]:
        """
        Performs the mathematical operations based on numbers and
        operands
        :param number_list:
        :param operator_list:
        :return:
        """
        try:
            for x, y in enumerate(operator_list):
                if y == "^":
                    number_list[x] = float(number_list[x]) ** number_list[x + 1]
                    number_list.remove(number_list[x + 1])
                    operator_list.remove(y)
            for x, y in enumerate(operator_list):
                if y == "/":
                    number_list[x] = float(number_list[x]) / number_list[x + 1]
                    number_list.remove(number_list[x + 1])
                    operator_list.remove(y)
            for x, y in enumerate(operator_list):
                if y == "*":
                    number_list[x] = float(number_list[x]) * number_list[x + 1]
                    number_list.remove(number_list[x + 1])
                    operator_list.remove(y)
            for x, y in enumerate(operator_list):
                if y == "+":
                    number_list[x] = float(number_list[x]) + number_list[x + 1]
                    number_list.remove(number_list[x + 1])
                    operator_list.remove(y)
            for x, y in enumerate(operator_list):
                if y == "-":
                    number_list[x] = float(number_list[x]) - number_list[x + 1]
                    number_list.remove(number_list[x + 1])
                    operator_list.remove(y)
        except IndexError:
            raise IndexError("Invalid encoded value passed for calculation")
        else:
            return number_list, operator_list
