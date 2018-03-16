"""empty message

Revision ID: 05f123d35ee9
Revises: 2b3149410897
Create Date: 2018-02-16 15:07:00.172584

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '05f123d35ee9'
down_revision = '2b3149410897'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('variants', sa.Column('image_name', sa.String(length=5000), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('variants', 'image_name')
    # ### end Alembic commands ###
