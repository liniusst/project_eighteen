# Create a few examples of yourself where you show two pillars of OOP in action.
# A stack machine processes instructions by pushing and popping values to an internal stack. A simple example of this is a calculator.

class phones_specs:

    def __init__(self, warranty_year: int, warranty_cost: int) -> None:
        self.warranty_cost = warranty_cost
        self.warranty_year = warranty_year
        self.full_warranty_price = warranty_cost * warranty_year

    def get_warranty_cost(self) -> float:
        return self.full_warranty_price

class samsung(phones_specs):
    SPECIAL_SAMSUNG_PRICE = 500

    def get_full_cost(self) -> int:
        samsung_full_cost = self.SPECIAL_SAMSUNG_PRICE + self.full_warranty_price
        return samsung_full_cost
    
class apple(phones_specs):
    SPECIAL_APPLE_PRICE = 999

    def get_full_cost(self) -> int:
        apple_full_cost = self.SPECIAL_APPLE_PRICE + (self.full_warranty_price - self.warranty_cost)
        return apple_full_cost

samsung_phone = samsung(warranty_year= 5, warranty_cost= 59)
apple_phone = apple(warranty_year= 5, warranty_cost= 59)

print(f"Samsung phone full price with warranty for {samsung_phone.warranty_year} years: {samsung_phone.get_full_cost()}")
print(f"Apple phone full price with warranty for {apple_phone.warranty_year} years: {apple_phone.get_full_cost()}")