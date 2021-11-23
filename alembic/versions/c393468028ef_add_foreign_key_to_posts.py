"""add foreign key to posts

Revision ID: c393468028ef
Revises: 646c6b3c6c0e
Create Date: 2021-11-23 13:33:04.749957

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql.expression import table


# revision identifiers, used by Alembic.
revision = 'c393468028ef'
down_revision = '646c6b3c6c0e'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column(
        'posts',
        sa.Column('owner_id', sa.Integer, sa.ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    )

    # TO CREATE A FOREIGN KEY SEPERATELY
    # op.create_foreign_key(
    #     'posts_users_fk', 
    #     source_table="posts", 
    #     referent_table="users", 
    #     local_cols=['owner_id'], 
    #     remote_cols=['id'], 
    #     ondelete="CASCADE"
    #     )


def downgrade():
    # op.drop_constraint('posts_users_fk', table_name="posts")
    op.drop_column(
        'posts',
        'owner_id'
    )
