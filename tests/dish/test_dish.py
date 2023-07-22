from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient
import pytest


# Req 2
def test_dish():

    dish = Dish("Lasanha", 35.99)
    assert isinstance(dish, Dish)
    assert dish.name == "Lasanha"
    assert dish.price == 35.99

    assert repr(dish) == "Dish('Lasanha', R$35.99)"

    dish1 = Dish("Lasanha", 35.99)
    dish2 = Dish("Lasanha", 35.99)
    assert dish1 == dish2
    assert dish1 == dish1

    assert hash(dish1) == hash(dish2)

    dish3 = Dish("Strogonoff", 29.99)
    assert hash(dish1) != hash(dish3)

    assert repr(dish1) != repr(dish3)

    ingredient1 = Ingredient("Massa de Lasanha")
    ingredient2 = Ingredient("Queijo Mussarela")
    dish.add_ingredient_dependency(ingredient1, 2)
    dish.add_ingredient_dependency(ingredient2, 200)

    assert dish.recipe.get(ingredient1) == 2
    assert dish.recipe.get(ingredient2) == 200

    ingredient3 = Ingredient("Tomate")
    assert dish.recipe.get(ingredient3) is None

    restrictions = dish.get_restrictions()
    assert len(restrictions) == 0

    ingredients_set = dish.get_ingredients()
    assert ingredient1 in ingredients_set
    assert ingredient2 in ingredients_set
    assert ingredient3 not in ingredients_set

    with pytest.raises(TypeError):
        Dish("Strogonoff", "invalid_price")

    with pytest.raises(ValueError):
        Dish("Strogonoff", -10)
