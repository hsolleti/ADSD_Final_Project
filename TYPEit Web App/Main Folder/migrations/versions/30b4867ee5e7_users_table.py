"""users table

Revision ID: 30b4867ee5e7
Revises: 
Create Date: 2020-05-23 18:07:26.886692

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '30b4867ee5e7'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'topic', ['name'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'topic', type_='unique')
    # ### end Alembic commands ###
