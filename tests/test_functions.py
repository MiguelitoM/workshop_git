import pytest
from functions.add import execute as add
from functions.sub import execute as sub
from functions.division import execute as div
from functions.avg import execute as avg
from functions.max import execute as max
from functions.min import execute as min
from functions.mult import execute as mult

def test_add():
    assert add(2, 3) == 5, "Soma de 2 e 3 deve ser 5"
    assert add(-1, 1) == 0, "Soma de -1 e 1 deve ser 0"
    assert add(0, 0) == 0, "Soma de 0 e 0 deve ser 0"
    assert add(-5, -3) == -8, "Soma de -5 e -3 deve ser -8"

def test_sub():
    assert sub(5, 3) == 2, "Subtração de 5 por 3 deve ser 2"
    assert sub(3, 5) == -2, "Subtração de 3 por 5 deve ser -2"
    assert sub(0, 0) == 0, "Subtração de 0 por 0 deve ser 0"
    assert sub(-2, -3) == 1, "Subtração de -2 por -3 deve ser 1"

def test_mult():
    assert mult(5, 3) == 15, "multiplicação de 5 por 3 deve ser 15"
    assert mult(3, 5) == 15, "multiplicação de 3 por 5 deve ser 15"
    assert mult(0, 0) == 0, "multiplicação de 0 por 0 deve ser 0"
    assert mult(-2, -3) == 6, "multiplicação de -2 por -3 deve ser 6"

def test_avg():
    assert avg(5, 3) == 4, "media de 5 por 3 deve ser 4"
    assert avg(3, 5) == 4, "media de 3 por 5 deve ser 4"
    assert avg(0, 0) == 0, "media de 0 por 0 deve ser 0"
    assert avg(-2, -3) == -2.5, "media de -2 por -3 deve ser -2.5"

def test_div():
    assert div(5, 3) == 5/3, "media de 5 por 3 deve ser 5/3"
    assert div(3, 5) == 3/5, "media de 3 por 5 deve ser 3/5"
    assert div(0, 1) == 0, "media de 0 por 1 deve ser 0"
    assert div(-2, -3) == 2/3, "media de -2 por -3 deve ser 2/3"

def test_max():
    assert max(5, 3) == 5, "max de 5 por 3 deve ser 5"
    assert max(3, 5) == 5, "max de 3 por 5 deve ser 5"
    assert max(0, 0) == 0, "max de 0 por 0 deve ser 0"
    assert max(-2, -3) == -2, "max de -2 por -3 deve ser -2"

def test_min():
    assert min(5, 3) == 3, "min de 5 por 3 deve ser 3"
    assert min(3, 5) == 3, "min de 3 por 5 deve ser 3"
    assert min(0, 0) == 0, "min de 0 por 0 deve ser 0"
    assert min(-2, -3) == -3, "min de -2 por -3 deve ser -3"