from calc_art import logo


class Calculator(object):

    def __init__(self):
        pass

    def add(self, num1, num2):
        return self.num1 + self.num2

    def subtract(self, num1, num2):
        return self.num1 - self.num2

    def multiply(self, num1, num2):
        return self.num1 * self.num2

    def divide(self, num1, num2):
        return self.num1 / self.num2

    def percentage(self, num1, num2):
        if self.num1 > self.num2:
            self.value = self.num2
            self.total = self.num1
        else:
            self.value = self.num1
            self.total = self.num2

        try:
            percentage = self.value / self.total * 100
            percentage = f'{percentage}%'
            return percentage
        except Exception as e:
            print(f'An error occurred: {e}')

    def calculator(self):
        operations = {'+': self.add, '-': self.subtract, '*': self.multiply, '/': self.divide, '%': self.percentage}
        print(logo)

        cont = True
        answer = None

        while cont == True:

            if answer == None:
                self.num1 = float(input("First number: "))
            else:
                self.num1 = answer
            for key in operations:
                print(f"{key}\n")
            op_symbol = input("Pick an above operation: ")
            self.num2 = float(input("Second number: "))

            calc_func = operations[op_symbol]
            answer = calc_func(self.num1, self.num2)

            print(f"{self.num1} {op_symbol} {self.num2} = {answer}")
            continue_cond = input("Continue calculating (y) / start a new calculation (n) / or exit (x)? ")
            if continue_cond == "n":
                self.calculator()
            elif continue_cond == "x":
                cont == False





c = Calculator()
c.calculator()

#print(c.percentage())
#print(c.add(),c.subtract())




