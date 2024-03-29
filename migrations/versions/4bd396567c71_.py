"""empty message

Revision ID: 4bd396567c71
Revises: dc81afcac56f
Create Date: 2021-11-23 17:22:11.907902

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '4bd396567c71'
down_revision = 'dc81afcac56f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('tickets', 'hora',
               existing_type=mysql.TIME(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('tickets', 'hora',
               existing_type=mysql.TIME(),
               nullable=False)
    # ### end Alembic commands ###
