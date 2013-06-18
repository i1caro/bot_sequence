from bots_something import run_bots
from bots_something import B,O

def test_bot_no_switch():
    button_sequence = ((O,2), (O,4))
    response = 5
    assert run_bots(button_sequence) == response

def test_bot_switch():
    button_sequence = ((O,2), (B,5))
    response = 5
    assert run_bots(button_sequence) == response


def test_bot_four_steps():
    button_sequence = ((O,2),(B,1), (B,2), (O,4))
    response = 6
    assert run_bots(button_sequence) == response

def test_bot_three_steps():
    button_sequence = ((O,5),(O,8), (B,100))
    response = 100
    assert run_bots(button_sequence) == response

def test_bot_two_steps():
    button_sequence = ((B,2),(B,1))
    response = 4
    assert run_bots(button_sequence) == response

def test_bot_break_test():
    button_sequence = ((O,100),(B,100),(O,1),(B,1))
    response = 201
    assert run_bots(button_sequence) == response

