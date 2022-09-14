"""empty message

Revision ID: 4cd654a2b6f6
Revises: 814418511fd0
Create Date: 2022-07-04 18:38:31.249284

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4cd654a2b6f6'
down_revision = '814418511fd0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('t_user', sa.Column('create_time', sa.DateTime(), nullable=True))
    op.add_column('t_user', sa.Column('update_time', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('t_user', 'update_time')
    op.drop_column('t_user', 'create_time')
    # ### end Alembic commands ###
