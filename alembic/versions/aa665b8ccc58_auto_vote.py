"""auto vote

Revision ID: aa665b8ccc58
Revises: c393468028ef
Create Date: 2021-11-23 13:59:01.395695

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql
from sqlalchemy.sql.schema import ForeignKeyConstraint

# revision identifiers, used by Alembic.
revision = 'aa665b8ccc58'
down_revision = 'c393468028ef'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        'votes',
        sa.Column(
            'post_id', 
            sa.Integer, 
            # sa.ForeignKey("posts_alchemy.id", ondelete="CASCADE"), 
            nullable=False,
            # primary_key=True
            ),
        sa.Column(
            'user_id', 
            sa.Integer, 
            # sa.ForeignKey("posts_alchemy.id", ondelete="CASCADE"), 
            nullable=False,
            # primary_key=True
            ),
        sa.ForeignKeyConstraint(['post_id'], ['posts_alchemy.id'], ondelete='CASCADE'),
        sa.ForeignKeyConstraint(['user_id'], ['users.id'], ondelete='CASCADE'),
        sa.PrimaryKeyConstraint('user_id', 'post_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table(
        "votes"
    )
    # ### end Alembic commands ###