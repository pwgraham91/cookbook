#!/usr/bin/env python

import unittest

# import tests here to register them and they'll get run when this file is run
from app.test.model.user import UserTestCase
from app.test.model.ingredient_stock import IngredientStockTestCase

if __name__ == '__main__':
    unittest.main()
