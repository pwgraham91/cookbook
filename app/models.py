import datetime
from enum import IntEnum

from app import db


class User(db.Model):
    id = db.Column(db.BigInteger, primary_key=True)

    name = db.Column(db.String(64), nullable=False)
    email = db.Column(db.String(120), index=True, unique=True, nullable=False)
    username = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120))

    admin = db.Column(db.Boolean, default=False, nullable=False)
    avatar = db.Column(db.VARCHAR)

    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow(), nullable=False)
    deactivated_at = db.Column(db.DateTime)

    @property
    def is_authenticated(self):  # coverage: no cover
        return True

    @property
    def is_active(self):  # coverage: no cover
        return self.deactivated_at is None

    @property
    def is_anonymous(self):  # coverage: no cover
        return False

    @property
    def dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'username': self.username,
            'admin': self.admin,
            'avatar': self.avatar,
            'is_active': self.is_active,
            'created_at': str(self.created_at) if self.created_at else None,
        }


class Ingredient(db.Model):
    id = db.Column(db.BigInteger, primary_key=True)

    name = db.Column(db.String(120), nullable=False)
    image_url = db.Column(db.VARCHAR)


class Unit(IntEnum):
    POUNDS = 1
    OUNCES = 2
    LITERS = 3
    EACH = 4


class IngredientStock(db.Model):
    id = db.Column(db.BigInteger, primary_key=True)

    amount = db.Column(db.Integer, nullable=False)
    unit = db.Column(db.SmallInteger, nullable=False, default=Unit.EACH.value)

    ingredient_id = db.Column(db.BigInteger, db.ForeignKey('ingredient.id', ondelete="CASCADE"), nullable=False)
    ingredient = db.relationship("Ingredient", backref="in_stock")

    user_id = db.Column(db.BigInteger, db.ForeignKey('user.id', ondelete="CASCADE"), nullable=False)
    user = db.relationship("User", backref="whole_stock")


class Recipe(db.Model):
    id = db.Column(db.BigInteger, primary_key=True)

    name = db.Column(db.String(120), nullable=False)
    url = db.column(db.VARCHAR)


class RecipeIngredient(db.Model):
    id = db.Column(db.BigInteger, primary_key=True)

    amount = db.Column(db.Integer, nullable=False)
    unit = db.Column(db.SmallInteger, nullable=False, default=Unit.EACH.value)

    ingredient_id = db.Column(db.BigInteger, db.ForeignKey('ingredient.id', ondelete="CASCADE"), nullable=False)
    ingredient = db.relationship("Ingredient", backref="recipes")

    recipe_id = db.Column(db.BigInteger, db.ForeignKey('recipe.id', ondelete="CASCADE"), nullable=False)
    recipe = db.relationship("Recipe", backref="ingredients")
