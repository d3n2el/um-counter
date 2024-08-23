import pytest
from um import count
def test1():
    assert count("um") ==1
    assert count("Hello, um, world") ==1
    assert count("I,um, like, um, arcade.") == 2
def test_longer():
    assert count("Um, thanks, um, regular expressions make sense now") == 2
    assert count("Um, thanks, um, regular expressions make sense now") == 2
def test_words():
    assert count("cryptosporidium") == 0
    assert count("microsporangium") == 0
    assert count("circumstantiate") == 0
