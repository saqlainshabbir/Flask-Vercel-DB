"""empty message

Revision ID: 815d9054a042
Revises: 9ca686372b1c
Create Date: 2024-11-02 12:48:16.486928

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '815d9054a042'
down_revision = '9ca686372b1c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cement_shops',
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
    op.create_table('gynaecologists',
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
    op.drop_table('gynaecologists')
    op.drop_table('cement_shops')
    # ### end Alembic commands ###