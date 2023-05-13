class Calculator(object):

    def __init__(self, total, value):
        self.total = total
        self.value = value

    def percentage(self):
        try:
            percentage = self.value / self.total * 100
            percentage = f'{percentage}%'
            return percentage
        except Exception as e:
            print(f'An error occurred: {e}')


c = Calculator('a', 20)
print(c.percentage())




