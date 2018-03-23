from src.beer import Beer

def test_beer_attributes():
    b = Beer("Guinness", "12/12 OZ. BTL", "Stout", "30.00", "2")
    assert b.get_name() == "Guinness"
    assert b.get_size() == "12/12 OZ. BTL"
    assert b.get_style() == "Stout"
    assert b.get_price() == "30.00"
    assert b.get_quantity() == "2"
    assert b.is_available() == True

def test_non_available_beer():
    b = Beer("Natty Light", "24/12 OZ. CAN", "College", "20.00", "0")
    assert b.is_available() == False
    assert b.get_quantity() == "0"


def test_negative_quantity_beer():
    b = Beer("Lionshead", "24/12 OZ. CAN", "Pilsner", "30.00", "-1")
    assert b.is_available() == False
    assert b.get_quantity() == "-1"
