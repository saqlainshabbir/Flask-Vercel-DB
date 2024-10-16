"""Create subscription table

Revision ID: 5e8ff40a85ac
Revises: 
Create Date: 2024-10-11 17:15:32.049458

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5e8ff40a85ac'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # Create the subscription table
    op.create_table('subscription',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=False),
    sa.Column('father_name', sa.String(length=120), nullable=False),
    sa.Column('phone_number', sa.String(length=120), nullable=True),
    sa.Column('subscribed_at', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )


def downgrade():
    # Drop the subscription table in case of downgrade
    op.drop_table('subscription')