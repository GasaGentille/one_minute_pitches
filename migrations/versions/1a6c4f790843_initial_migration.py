"""Initial Migration

Revision ID: 1a6c4f790843
Revises: 2d657480b63a
Create Date: 2019-09-24 18:45:36.624496

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1a6c4f790843'
down_revision = '2d657480b63a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('pitches', sa.Column('dislikes', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('pitches', 'dislikes')
    # ### end Alembic commands ###