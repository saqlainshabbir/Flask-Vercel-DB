"""Added name and father_name to Subscription

Revision ID: ab6f9cd863e0
Revises: 5e8ff40a85ac
Create Date: 2024-10-12 11:17:42.251904

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ab6f9cd863e0'
down_revision = '5e8ff40a85ac'
branch_labels = None
depends_on = None


def upgrade():
    # Add columns with default values to avoid NOT NULL errors for existing rows
    with op.batch_alter_table('subscription', schema=None) as batch_op:
        batch_op.add_column(sa.Column('name', sa.String(length=120), nullable=False, server_default='Unknown'))
        batch_op.add_column(sa.Column('father_name', sa.String(length=120), nullable=False, server_default='Unknown'))
        batch_op.add_column(sa.Column('phone_number', sa.String(length=120), nullable=False, server_default='Unknown'))

def downgrade():
    # Remove the added columns in case of downgrade
    with op.batch_alter_table('subscription', schema=None) as batch_op:
        batch_op.drop_column('father_name')
        batch_op.drop_column('name')