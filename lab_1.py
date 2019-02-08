# Classes, methods, and properties
# Your code goes here:



#########################################
# Do not touch the code below.
#########################################

if __name__ == '__main__':
    iPhone = Product(name='iPhone', price=699, sku='SKU123')
    sofa = Product(name='Sofa', price=1200, sku='SKU456')
    sofa.discount_pct = 10

    assert 'iPhone' == iPhone.name
    assert 'SKU123' == iPhone.sku
    assert 699 == iPhone.price
    assert 699 == iPhone.potential_revenue

    assert 'Sofa' == sofa.name
    assert 'SKU456' == sofa.sku
    assert 1200 == sofa.price
    assert 1080 == sofa.potential_revenue

    print("All tests passed!")
