"""add phone number to users

Revision ID: 479814767325
Revises: aa665b8ccc58
Create Date: 2021-11-23 14:38:51.883800

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '479814767325'
down_revision = 'aa665b8ccc58'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('phone_number', sa.String(), nullable=True))
    # op.drop_constraint('votes_user_id_fkey', 'votes', type_='foreignkey')
    # op.create_foreign_key(None, 'votes', 'users', ['user_id'], ['id'], ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    # op.drop_constraint(None, 'votes', type_='foreignkey')
    # op.create_foreign_key('votes_user_id_fkey', 'votes', 'posts_alchemy', ['user_id'], ['id'], ondelete='CASCADE')
    op.drop_column('users', 'phone_number')
    # ### end Alembic commands ###