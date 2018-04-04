from abv.beer import Beer


def test_beer_attributes():
    beer_attribute = Beer("Guinness", "12/12 OZ. BTL", "Stout", "30.00", "2")
    assert beer_attribute.get_name() == "Guinness"
    assert beer_attribute.get_size() == "12/12 OZ. BTL"
    assert beer_attribute.get_style() == "Stout"
    assert beer_attribute.get_price() == "30.00"
    assert beer_attribute.get_quantity() == "2"
    assert beer_attribute.is_available() is True


def test_non_available_beer():
    non_beer = Beer("Natty Light", "24/12 OZ. CAN", "College", "20.00", "0")
    assert non_beer.is_available() is False
    assert non_beer.get_quantity() == "0"


def test_negative_quantity_beer():
    negative_beer = Beer("Lionshead", "24/12 OZ. CAN", "Pilsner", "30.00", "-1")
    assert negative_beer.is_available() is False
    assert negative_beer.get_quantity() == "-1"
