class Salesperson:
    def __init__(self, employee_id, name):
        self.employee_id = employee_id
        self,name = name
        self.sales = []

    def enter_sale(self, sale):
        self.sales.append(sale)

    def total_sale(self, sale):
        my_sale = 0
        return my_sale(self.sale)

    def get_sales(self, sales):
        i = []
        for i in range(len(float(self.sales))):
            if self.sales[i] >= sales:
                return i

    def net_quote(self):
        return self.quote_sales()

    def compare_to(self, other):
        i = -1
        for i in len(self.other):
            if self.sales[i] >= other:
                return i

