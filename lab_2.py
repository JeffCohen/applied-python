# Objects and Iteration

class Product:
    def __init__(self, name, price, sku):
        self.name = name
        self.price = price
        self.sku = sku
        self.discount_pct = 0

    @property
    def value(self):
        return self.price

    @property
    def potential_revenue(self):
        return self.price * ((100-self.discount_pct)/100)

class ProductWarehouse:
    pass





#########################################
# Do not touch the code below.
#########################################

if __name__ == '__main__':
    iPhone = Product(name='iPhone', price=699, sku='SKU123')
    dishwasher = Product(name='Dishwasher', price=750, sku='SKU789')
    sofa  = Product(name='Sofa', price=1200, sku='SKU456')
    sofa.discount_pct = 10

    warehouse = ProductWarehouse()
    warehouse.receive(iPhone, qty=100)    # Put 100 iPhones in the warehouse
    warehouse.receive(sofa, qty=10)       # Put 10 sofas in the warehouse
    warehouse.receive(dishwasher, qty=1)  # Put 1 dishwasher in the warehouse


    assert (100*699 + 10*1200 + 750*1) == warehouse.value
    assert (100*699 + 10*1200*0.9 + 750*1) == warehouse.potential_revenue

    warehouse.ship(iPhone, 1)
    warehouse.ship(sofa, 1)

    assert (99*699 + 9*1200 + 750*1) == warehouse.value
    assert (99*699 + 9*1200*0.9 + 750*1) == warehouse.potential_revenue

    print("All tests passed!")
