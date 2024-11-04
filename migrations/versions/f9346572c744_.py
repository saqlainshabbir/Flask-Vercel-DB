"""empty message

Revision ID: f9346572c744
Revises: b0f76156db6f
Create Date: 2024-11-04 16:01:51.237045

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'f9346572c744'
down_revision = 'b0f76156db6f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('union_councils_dunyapur',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('Union_council_name', sa.String(length=100), nullable=False),
    sa.Column('Union_council_discription', sa.String(length=200), nullable=False),
    sa.Column('published_at', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('union_councils_kahrorpacca',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('Union_council_name', sa.String(length=100), nullable=False),
    sa.Column('Union_council_discription', sa.String(length=200), nullable=False),
    sa.Column('published_at', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('union_councils_lodhran',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('Union_council_name', sa.String(length=100), nullable=False),
    sa.Column('Union_council_discription', sa.String(length=200), nullable=False),
    sa.Column('published_at', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('union_councils')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('union_councils',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('Union_council_name', sa.VARCHAR(length=100), autoincrement=False, nullable=False),
    sa.Column('Union_council_discription', sa.VARCHAR(length=200), autoincrement=False, nullable=False),
    sa.Column('published_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='union_councils_pkey')
    )
    op.drop_table('union_councils_lodhran')
    op.drop_table('union_councils_kahrorpacca')
    op.drop_table('union_councils_dunyapur')
    # ### end Alembic commands ###