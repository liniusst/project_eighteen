from typing import Dict, List
class CoffeeShop:

    def __init__(self, name: str,  orders: List[str]) -> None:
        self.name = name
        self.orders = orders
        self.total_amount = []
        self.menu_prices = []

        self.menu = {
            'salotos': {
            'price': 4.10,
            'category': 'food'
            },
            'karbonadas': {
            'price': 2.90,
            'category': 'food'
            },
            'kava': {
            'price': 0.90,
            'category': 'drinks'
            }
        } 

    def add_order(self, name: str):
        """adds the name of the item to the end of the orders list if it exists on the menu"""
        if name in self.menu.keys():
            self.orders.append(name)
        else:
            print('This item is currently unavailable!')
    
    def fulfill_order(self):
        """if the orders list is not empty, return "The {item} is ready!". If the orders list is empty, return "All orders have been fulfilled!"""
        if self.orders:
            for item in self.orders:
                print(f"The {item} is ready!")
        else:
            print("All orders have been fulfilled!")

    def due_amount(self):
        """due_amount: returns the total amount due for the orders taken."""
        for item_name in self.orders:
            item_price = self.menu[item_name]['price']
            self.total_amount.append(item_price)
        self.total_amount = sum(self.total_amount)
        return print(self.total_amount)
    
    def cheapest_item(self):
        """cheapest_item: returns the name of the cheapest item on the menu."""
        for item in self.menu:
            if item in self.menu:
                name = self.menu.keys
                prices = self.menu[item]['price']
                self.menu_prices.append(prices)
                min_price = min(self.menu_prices)
                # if min_price in self.menu.values:


# d = {'key1': 'aaa', 'key2': 'aaa', 'key3': 'bbb'}
# keys = [k for k, v in d.items() if v == 'bbb']

        # print(self.menu.keys())
                
        # print(min_price)
                # smallest_sum = min(prices)
            # print(smallest_sum)

            # print(points[max(points, key=points.get)])

        


    # list_orders: returns the item names of the orders taken, otherwise, an empty list.
    def list_orders(self):
        items = []
        if self.orders:
            for item in self.orders:
                items.append(item)
        return items



order = CoffeeShop(name= "ice cream", orders= [])
order.add_order("kava")
order.add_order("karbonadas")
# order.fulfill_order()
# order.due_amount()
order.cheapest_item()
# print(order.list_orders())

