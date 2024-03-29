"""empty message

Revision ID: 7a9800479355
Revises: 11288f035787
Create Date: 2021-11-10 16:37:33.445183

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7a9800479355'
down_revision = '11288f035787'
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
    op.create_table('roles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('infopublic_acessos',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=64), nullable=True),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.Column('role_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['role_id'], ['roles.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_infopublic_acessos_email'), 'infopublic_acessos', ['email'], unique=True)
    op.create_index(op.f('ix_infopublic_acessos_username'), 'infopublic_acessos', ['username'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_infopublic_acessos_username'), table_name='infopublic_acessos')
    op.drop_index(op.f('ix_infopublic_acessos_email'), table_name='infopublic_acessos')
    op.drop_table('infopublic_acessos')
    op.drop_table('roles')
    op.drop_index(op.f('ix_emails_enviados_email'), table_name='emails_enviados')
    op.drop_index(op.f('ix_emails_enviados_cpf'), table_name='emails_enviados')
    op.drop_table('emails_enviados')
    # ### end Alembic commands ###
