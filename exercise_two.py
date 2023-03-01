from typing import Dict, List
class CoffeeShop:

    def __init__(self, name: str,  *orders: List[str], **menu: Dict[str, int],) -> None:
        self.name = name
        self.menu = menu
        self.orders = orders

    def add_order(self, name: str):
        if self.name.get(name) in self.menu
        # if name in self.menu[name]:
        #     self.orders.append(name)
        #     print("Order added!")
        # else:
        #     print("This item is currently unavailable!")
    
    def fulfill_order(self):
        if self.orders:
            for item in self.orders:
                print(f"The {item} is ready!")
        else:
            print("All orders have been fulfilled!")

    # list_orders: returns the item names of the orders taken, otherwise, an empty list.
    def list_orders(self):
        items = []
        if self.orders:
            for item in self.orders:
                items.append(item)
        return items


menu = {
    'name' : {
    'ice cream' : {
    'price' : 1.99,
    'category' : 'food'
    },
    'capucino' : {
    'price' : 0.99,
    'category' : 'drink'
    }
    }
}

# print(my_dict['name']['NBA']['Team']['Chicago Bulls']['star']['name'])


order = CoffeeShop(name= "ice cream", menu= menu, orders= [])
order.add_order("ice cream")
order.add_order("ledai")
order.fulfill_order()
# print(order.list_orders())

