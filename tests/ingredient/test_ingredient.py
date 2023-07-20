from src.models.ingredient import Ingredient, restriction_map  # noqa: F401, E261, E501


# Req 1
def test_ingredient():

    ingredient = Ingredient("Tomato")
    assert isinstance(ingredient, Ingredient)

    assert ingredient.restrictions == restriction_map().get(
        "Tomato", set()
        )

    assert repr(ingredient) == f"Ingredient('{ingredient.name}')"

    ingredient1 = Ingredient("Tomato")
    ingredient2 = Ingredient("Tomato")
    assert ingredient1 == ingredient2
    assert ingredient1 == ingredient1
    assert hash(ingredient1) == hash(ingredient2)

    ingredient1 = Ingredient("Tomato")
    ingredient2 = Ingredient("Potato")
    assert hash(ingredient1) != hash(ingredient2)

    assert ingredient.name == "Tomato"

    ingredient1 = Ingredient("Tomato")
    ingredient2 = Ingredient("Potato")
    assert ingredient1 != ingredient2

    assert ingredient.restrictions == restriction_map().get(
        "Tomato", set()
        )

    assert ingredient == ingredient
