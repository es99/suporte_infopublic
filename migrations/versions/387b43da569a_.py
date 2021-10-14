"""empty message

Revision ID: 387b43da569a
Revises: 
Create Date: 2021-10-14 15:56:50.528124

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '387b43da569a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('emails_enviados',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('data_envio', sa.DateTime(), nullable=True),
    sa.Column('cpf', sa.String(length=64), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_emails_enviados_cpf'), 'emails_enviados', ['cpf'], unique=False)
    op.create_index(op.f('ix_emails_enviados_email'), 'emails_enviados', ['email'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_emails_enviados_email'), table_name='emails_enviados')
    op.drop_index(op.f('ix_emails_enviados_cpf'), table_name='emails_enviados')
    op.drop_table('emails_enviados')
    # ### end Alembic commands ###
