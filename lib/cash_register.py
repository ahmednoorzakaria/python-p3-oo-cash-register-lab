#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self.total = 0
        self.items = []
        self.discount = discount

    def add_item(self, title, price, quantity=1):
        self.total += price * quantity
        self.items.append((title, price, quantity))

    def apply_discount(self):
        if self.discount > 0:
            self.total = self.total * (1 - self.discount / 100)
            print("After the discount, the total comes to ${}".format(self.total))

    def get_items_list(self):
        return [item[0] for item in self.items]

    def void_last_transaction(self):
        if len(self.items) > 0:
            last_item = self.items.pop()
            self.total -= last_item[1] * last_item[2]

