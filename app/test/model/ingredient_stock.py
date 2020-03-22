#!flask/bin/python
import unittest

from app.models import User, IngredientStock, Unit
from app.test.base import BaseTestCase


class IngredientStockTestCase(BaseTestCase):
    def setUp(self) -> None:
        self.setUpDB()

    def tearDown(self) -> None:
        self.tearDownDB()

    def test_ingredient_stock(self):
        u = self.get_test_user()
        celery = self.get_test_ingredient("Celery")
        potato = self.get_test_ingredient("Potato")

        user_celery = IngredientStock()
        user_celery.user = u
        user_celery.ingredient = celery
        user_celery.amount = 3

        user_potato = IngredientStock()
        user_potato.user = u
        user_potato.ingredient = potato
        user_potato.amount = 5
        user_potato.unit = Unit.POUNDS.value

        self.session.add_all([u, celery, potato, user_celery, user_potato])

        returned_user = self.session.query(User).one()

        self.assertEqual(len(returned_user.whole_stock), 2)


if __name__ == '__main__':
    unittest.main()
