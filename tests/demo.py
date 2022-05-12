import pytest

@pytest.mark.smoke
def test_product_price1():
    assert 1==2, 'Did not match'

@pytest.mark.regression
def test_product_price2():
    assert 1==1, 'Did not match' 

@pytest.mark.skip
def test_add_to_cart():
    assert 'a'=='A', 'Did not match'