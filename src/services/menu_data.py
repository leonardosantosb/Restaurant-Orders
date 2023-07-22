import csv
from models.dish import Dish
from models.ingredient import Ingredient


# Req 3
class MenuData:
    def __init__(self, source_path: str) -> None:
        self.dishes = set()
        self._load_data(source_path)

    def _load_data(self, source_path: str) -> None:
        with open(source_path, newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)

            for row in reader:
                dish_name = row["dish"]
                dish_price = float(row["price"])
                ingredient_name = row["ingredient"]
                ingredient_amount = int(row["recipe_amount"])

                ingredient = Ingredient(ingredient_name)

                dish = next(
                    (d for d in self.dishes if d.name == dish_name), None
                    )

                if not dish:
                    dish = Dish(dish_name, dish_price)
                    self.dishes.add(dish)

                dish.add_ingredient_dependency(ingredient, ingredient_amount)
