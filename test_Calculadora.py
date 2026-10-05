from Calculadora import suma,resta,multiplicacion,division;

import pytest

def test_sumar_dispositivo ():
    assert suma (8, 1) == 8

def test_restar_dispositivo ():
    assert resta (-6, -3) == -3

def test_division_dispositivo ():
    with pytest.raises (ValueError): 
        division (4, 0)
