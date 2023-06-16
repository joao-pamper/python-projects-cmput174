"""
Unit tests for the Pokemon class.
"""

from pokemon2 import Pokemon


def test_init():
    """
    Test the __init__ method.
    """
    pokemon = Pokemon("Pikachu", 55, 40, 35, 35)
    assert pokemon.name == "Pikachu"
    assert pokemon.attack == 55
    assert pokemon.defense == 40
    assert pokemon.max_health == 35
    assert pokemon.current_health == 35


def test_str():
    """
    Test the __str__ method.
    """
    pokemon = Pokemon("Pikachu", 55, 40, 35, 35)
    assert str(pokemon) == "Pikachu (health: 35/35)"


def test_lose_health():
    """
    Test the lose_health method.
    """
    pokemon = Pokemon("Pikachu", 55, 40, 35, 35)
    pokemon.lose_health(5)
    assert pokemon.current_health == 30


def test_lose_health_negative():
    """
    Test the lose_health method with a negative amount.
    """
    pokemon = Pokemon("Pikachu", 55, 40, 35, 35)
    pokemon.lose_health(-5)
    assert pokemon.current_health == 35


def test_lose_health_greater_than_health():
    """
    Test the lose_health method with a greater amount than health.
    """
    pokemon = Pokemon("Pikachu", 55, 40, 35, 35)
    pokemon.lose_health(40)
    assert pokemon.current_health == 0


def test_is_alive():
    """
    Test the is_alive method.
    """
    pokemon = Pokemon("Pikachu", 55, 40, 35, 35)
    assert pokemon.is_alive() is True


def test_is_alive_zero():
    """
    Test the is_alive method with zero health.
    """
    pokemon = Pokemon("Pikachu", 55, 40, 35, 0)
    assert pokemon.is_alive() is False


def test_revive():
    """
    Test the revive method.
    """
    pokemon = Pokemon("Pikachu", 55, 40, 35, 0)
    pokemon.revive()
    assert pokemon.current_health == 35
