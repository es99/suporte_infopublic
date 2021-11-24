"""empty message

Revision ID: 1d49c1051199
Revises: d269cd4ebacf
Create Date: 2021-11-23 22:43:31.656702

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1d49c1051199'
down_revision = 'd269cd4ebacf'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tickets', sa.Column('solucao', sa.Text(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('tickets', 'solucao')
    # ### end Alembic commands ###
