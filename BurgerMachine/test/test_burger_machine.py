import pytest
import random
# make sure there's an __init__.py in this tests folder and that
# the tests folder is in the same folder as the IcecreamMachine stuff
from BurgerMachine import BurgerMachine
from BurgerMachineExceptions import ExceededRemainingChoicesException, InvalidChoiceException, InvalidStageException, OutOfStockException
#this is an example test showing how to cascade fixtures to build up state

@pytest.fixture
def machine():
    bm = BurgerMachine()
    return bm

# add required test cases below
def test_first_selection(machine):
    """ rr284 March 19 2023
        Test to see if an exception is raised when a patty is chosen befoe bun.
    """
    try:
        machine.handle_patty("turkey")
        machine.handle_patty("next")
        machine.handle_toppings("cheese")
        machine.handle_toppings("done")
        assert False
    except InvalidStageException:
        assert True
        
def test_patties_in_stock(machine):
    """ rr284 March 19 2023
        Test to see if a exception is raised when a chosen patty is out of stock.
        Here we assume that the turkey patty is out of stock.
    """
    try:
        temp = machine.patties[0].quantity
        machine.patties[0].quantity = 0
        machine.handle_bun("Lettuce Wrap")
        machine.handle_patty("turkey")
        assert False
    except OutOfStockException:
        machine.patties[0].quantity = temp
        assert True

def test_toppings_in_stock(machine):
    """ rr284 March 19 2023
        Tests if an exception is raised when a chosen topping is out of stock. 
        we assume BBQ topping is out of stock.
    """
    try:
        temp = machine.toppings[-1].quantity
        machine.toppings[-1].quantity = 0
        machine.handle_bun("Lettuce Wrap")
        machine.handle_patty("turkey")
        machine.handle_patty("next")
        machine.handle_toppings("BBQ")
        assert False
    except OutOfStockException:
        machine.toppings[-1].quantity = temp
        assert True
        
def test_max_patties(machine):
    """ rr284 March 19 2023
        Test to check if an exception is raised when four or more number patties are chosen.
    """
    try:
        machine.handle_bun("white burger bun")
        machine.handle_patty("turkey")
        machine.handle_patty("veggie")
        machine.handle_patty("Turkey")
        machine.handle_patty("Beef")
        assert False
    except ExceededRemainingChoicesException:
        assert True

def test_max_toppings(machine):
    """ rr284 March 19 2023
        Test to check if an exception is raised when four or more number Toppings are chosen.
    """
    try:
        machine.handle_bun("white burger bun")
        machine.handle_patty("turkey")
        machine.handle_patty("Beef")
        machine.handle_patty("next")
        machine.handle_toppings("tomato")
        machine.handle_toppings("cheese")
        machine.handle_toppings("bbq")
        machine.handle_toppings("mayo")
        assert False
    except ExceededRemainingChoicesException:
        assert True

def test_calculated_cost(machine):
    """ rr284 March 19 2023
        To verify if the cost is calculated properly for 3 different combinations of burgers 
        that are chosen at random. 
    """
    for i in range(3):
        machine.reset()
        expected_cost = 0
        bun = random.choice(machine.buns)
        patty_1 = random.choice(machine.patties)
        patty_2 = random.choice(machine.patties)
        topping_1 = random.choice(machine.toppings)
        topping_2 = random.choice(machine.toppings)
        topping_3 = random.choice(machine.toppings)
        
        expected_cost = bun.cost + patty_1.cost + patty_2.cost + topping_1.cost + topping_2.cost + topping_3.cost
        
        machine.handle_bun(bun.name)
        machine.handle_patty(patty_1.name)
        machine.handle_patty(patty_2.name)
        machine.handle_patty("next")
        machine.handle_toppings(topping_1.name)
        machine.handle_toppings(topping_2.name)
        machine.handle_toppings(topping_3.name)
        machine.handle_toppings("done")
        if f"{machine.calculate_cost():.2f}" != f"{expected_cost:.2f}":
            assert False
        machine.handle_pay(machine.calculate_cost(), f"{expected_cost:.2f}")
    machine.reset()
    assert True
            
    
''' rr284 March 19 2023
    To test if the total sales cost is calculated properly for 3 different valid burgers 
    while maintaining the currency format.
'''
@pytest.fixture
def first_order(machine):
    machine.reset()
    machine.handle_bun("Lettuce Wrap")
    machine.handle_patty("beef")
    machine.handle_patty("next")
    machine.handle_toppings("cheese")
    machine.handle_toppings("mayo")
    machine.handle_toppings("Mustard")
    machine.handle_toppings("done")
    machine.handle_pay(machine.calculate_cost(), f"{machine.calculate_cost():.2f}")
    return machine

@pytest.fixture
def second_order(first_order, machine):
    machine.handle_bun("lettuce wrap")
    machine.handle_patty("turkey")
    machine.handle_patty("beef")
    machine.handle_patty("next")
    machine.handle_toppings("Mustard")
    machine.handle_toppings("mayo")
    machine.handle_toppings("bbq")
    machine.handle_toppings("done")
    machine.handle_pay(machine.calculate_cost(), f"{machine.calculate_cost():.2f}")
    return machine

@pytest.fixture
def third_order(second_order, machine):
    machine.handle_bun("Wheat Burger Bun")
    machine.handle_patty("veggie")
    machine.handle_patty("beef")
    machine.handle_patty("next")
    machine.handle_toppings("lettuce")
    machine.handle_toppings("tomato")
    machine.handle_toppings("cheese")
    machine.handle_toppings("done")
    machine.handle_pay(machine.calculate_cost(), f"{machine.calculate_cost():.2f}")
    return machine

def test_total(third_order):
    first_order_cost_expected = 3.25
    second_order_cost_expected = 4.25
    third_order_cost_expected = 4.00
    assert third_order.total_sales == first_order_cost_expected + second_order_cost_expected + third_order_cost_expected

def test_burger_increment(third_order):
    """ rr284 March 19 2023
        Testing if the total number of burgers is incremented properly. 
        We use the previously defined function that orders three burgers.
        this is possible since we dont Reset the "Machine" at the end of the function.
    """
    assert third_order.total_burgers == 3