"""empty message

Revision ID: efd51ab60f1f
Revises: 974108a9aca7
Create Date: 2021-06-05 16:05:47.815393

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'efd51ab60f1f'
down_revision = '974108a9aca7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('csvdata_name_key', 'csvdata', type_='unique')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint('csvdata_name_key', 'csvdata', ['name'])
    # ### end Alembic commands ###