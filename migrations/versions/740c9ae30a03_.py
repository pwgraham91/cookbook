"""empty message

Revision ID: 740c9ae30a03
Revises: 
Create Date: 2020-03-21 22:20:27.828311

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '740c9ae30a03'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('ingredient',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=False),
    sa.Column('image_url', sa.VARCHAR(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('recipe',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('username', sa.String(length=120), nullable=False),
    sa.Column('password', sa.String(length=120), nullable=True),
    sa.Column('admin', sa.Boolean(), nullable=False),
    sa.Column('avatar', sa.VARCHAR(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('deactivated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=True)
    op.create_table('ingredient_stock',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('amount', sa.Integer(), nullable=False),
    sa.Column('unit', sa.SmallInteger(), nullable=False),
    sa.Column('ingredient_id', sa.BigInteger(), nullable=False),
    sa.Column('user_id', sa.BigInteger(), nullable=False),
    sa.ForeignKeyConstraint(['ingredient_id'], ['ingredient.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('recipe_ingredient',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('amount', sa.Integer(), nullable=False),
    sa.Column('unit', sa.SmallInteger(), nullable=False),
    sa.Column('ingredient_id', sa.BigInteger(), nullable=False),
    sa.Column('recipe_id', sa.BigInteger(), nullable=False),
    sa.ForeignKeyConstraint(['ingredient_id'], ['ingredient.id'], ),
    sa.ForeignKeyConstraint(['recipe_id'], ['recipe.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('recipe_ingredient')
    op.drop_table('ingredient_stock')
    op.drop_index(op.f('ix_user_email'), table_name='user')
    op.drop_table('user')
    op.drop_table('recipe')
    op.drop_table('ingredient')
    # ### end Alembic commands ###
