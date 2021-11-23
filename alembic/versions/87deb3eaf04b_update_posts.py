"""update_posts

Revision ID: 87deb3eaf04b
Revises: 1a061f98b39a
Create Date: 2021-11-23 12:43:20.160722

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql.schema import Column, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String


# revision identifiers, used by Alembic.
revision = '87deb3eaf04b'
down_revision = '1a061f98b39a'
branch_labels = None
depends_on = None

def upgrade():
    op.add_column(
        'posts',
        sa.Column('published', sa.Boolean, server_default="True", nullable=False),
        # sa.Column('owner_id', sa.Integer, sa.ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    )


def downgrade():
    op.drop_column(
        'posts',
        'published'
    )
