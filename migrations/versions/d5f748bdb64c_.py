"""empty message

Revision ID: d5f748bdb64c
Revises: 815d9054a042
Create Date: 2024-11-02 13:00:58.121329

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd5f748bdb64c'
down_revision = '815d9054a042'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('computers',
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
    op.create_table('laboratories',
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
    op.drop_table('laboratories')
    op.drop_table('computers')
    # ### end Alembic commands ###
