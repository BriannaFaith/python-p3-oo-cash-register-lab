#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount= 0, items = None):
        self._discount = discount
        self.total = 0
        self.last_item = None
        if items is None:
            self.items = []
        else:
            self.items = items

    @property
    def discount(self):
        return self._discount

    def add_item(self,title,price,quantity = 1):
       self.items = [*self.items,*([title]*quantity)]
       price *= quantity
       self.last_transaction = price
       self.total += price

    def apply_discount(self):
        if self._discount != 0:
            self.total -= (self.total * self.discount) / 100
            print(f"After the discount, the total comes to ${int(self.total)}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
       self.total -= self.last_transaction




cash_register = CashRegister(discount=10)
cash_register.add_item("eggs", 0.98)
cash_register.add_item("Justin's Peanut Butter Cups", 2.50, 2)
cash_register.apply_discount()
cash_register.void_last_transaction()
print(cash_register.total)




# new_register = CashRegister()
# new_register.add_item("eggs", 1.99, 2)
# new_register.add_item("tomato", 1.76, 3)
# print(new_register.items)
