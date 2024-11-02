"""empty message

Revision ID: e277565ca948
Revises: 7de7a6f7e9d6
Create Date: 2024-11-02 15:18:08.750623

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e277565ca948'
down_revision = '7de7a6f7e9d6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('pest_controls',
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
    op.drop_table('pest_controls')
    # ### end Alembic commands ###