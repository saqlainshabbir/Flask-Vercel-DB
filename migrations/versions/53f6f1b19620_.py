"""empty message

Revision ID: 53f6f1b19620
Revises: a0c38a88845a
Create Date: 2024-11-04 14:43:58.705628

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '53f6f1b19620'
down_revision = 'a0c38a88845a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('private_hospitals',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('phone_number', sa.String(length=15), nullable=False),
    sa.Column('district', sa.String(length=50), nullable=False),
    sa.Column('tehsil', sa.String(length=50), nullable=False),
    sa.Column('address', sa.String(length=200), nullable=False),
    sa.Column('town', sa.String(length=50), nullable=False),
    sa.Column('published_at', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('private_hospitals')
    # ### end Alembic commands ###