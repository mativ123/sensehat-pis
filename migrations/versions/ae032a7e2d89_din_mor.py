"""din mor

Revision ID: ae032a7e2d89
Revises: c63a127270a0
Create Date: 2023-01-18 10:48:46.679445

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ae032a7e2d89'
down_revision = 'c63a127270a0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('pickle',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('kmkort', sa.Float(), nullable=True),
    sa.Column('tankstrl', sa.Integer(), nullable=True),
    sa.Column('kml', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_index('ix_user_username')

    op.drop_table('user')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('username', sa.VARCHAR(length=64), nullable=True),
    sa.Column('password_hash', sa.VARCHAR(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.create_index('ix_user_username', ['username'], unique=False)

    op.drop_table('pickle')
    # ### end Alembic commands ###
