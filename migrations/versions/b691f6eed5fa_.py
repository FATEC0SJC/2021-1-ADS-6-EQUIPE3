"""empty message

Revision ID: b691f6eed5fa
Revises: f30062764f4e
Create Date: 2021-05-12 22:14:25.936704

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b691f6eed5fa'
down_revision = 'f30062764f4e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('transactions_category', sa.String(length=30), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'transactions_category')
    # ### end Alembic commands ###
