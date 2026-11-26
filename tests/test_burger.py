import pytest
from unittest.mock import Mock
from data import Data as d


class TestBurger:

    def test_burger_init_without_bun(self, burger):
        assert burger.bun is None

    def test_burger_init_without_ingredients(self, burger):
        assert burger.ingredients == []

    def test_set_buns_sets_buns(self, burger):
        bun = Mock()
        burger.set_buns(bun)
        assert burger.bun is bun

    def test_add_ingredient_adds_ingredient(self, burger):
        ingredient = Mock()
        burger.add_ingredient(ingredient)
        assert burger.ingredients == [ingredient]

    def test_remove_ingredient_removes_ingredient_by_index(self, burger):
        ingredient_1 = Mock()
        ingredient_2 = Mock()
        burger.add_ingredient(ingredient_1)
        burger.add_ingredient(ingredient_2)
        burger.remove_ingredient(0)
        assert burger.ingredients == [ingredient_2]

    def test_move_ingredient_moves_ingredient_by_index(self, burger):
        ingredient_1 = Mock()
        ingredient_2 = Mock()
        burger.add_ingredient(ingredient_1)
        burger.add_ingredient(ingredient_2)
        burger.move_ingredient(0,1)
        assert burger.ingredients == [ingredient_2, ingredient_1]

    @pytest.mark.parametrize("bun_price, ingredient_price, expected",
        d.PRICE_DATA)
    def test_get_price_returns_correct_price(self, burger, bun_price, ingredient_price, expected):
        bun = Mock()
        bun.get_price.return_value = bun_price
        burger.set_buns(bun)

        ingredient = Mock()
        ingredient.get_price.return_value = ingredient_price
        burger.add_ingredient(ingredient)

        result = burger.get_price()
        assert result == expected

    def test_get_receipt_returns_correct_receipt(self, burger):
        bun = Mock()
        bun.get_name.return_value = "Пшеничная"
        bun.get_price.return_value = 150
        burger.set_buns(bun)

        ingredient = Mock()
        ingredient.get_price.return_value = 60
        ingredient.get_type.return_value = 'SAUCE'
        ingredient.get_name.return_value = "1000 островов"

        burger.add_ingredient(ingredient)

        result = burger.get_receipt()

        assert result == "(==== Пшеничная ====)\n= sauce 1000 островов =\n(==== Пшеничная ====)\n\nPrice: 360"

