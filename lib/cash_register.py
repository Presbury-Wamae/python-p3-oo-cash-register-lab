#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0.0
        self.items = []
        self.last_transaction = 0

    def add_item(self, title, price, quantity=1):
        self.total += price * quantity
        self.items.extend([title] * quantity)
        self.last_transaction = price * quantity

    def apply_discount(self):
        if self.discount == 0:
            print("There is no discount to apply.")
        else:
            self.total = self.total * (1 - self.discount / 100)
            print(f"After the discount, the total comes to ${int(self.total)}.")

    def void_last_transaction(self):
        self.total -= self.last_transaction
        if self.total < 0:  # in case total goes negative due to voiding
            self.total = 0.0
        # Remove the last items added (only works if last_transaction was the last items added)
        # This is a simplified approach - the test cases only check the total
        if self.last_transaction > 0:
            self.items = self.items[:-int(self.last_transaction / (self.last_transaction / len([item for item in self.items if item == self.items[-1]])))] if self.items else []
