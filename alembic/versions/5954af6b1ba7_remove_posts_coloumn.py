"""remove_posts_coloumn

Revision ID: 5954af6b1ba7
Revises: 87deb3eaf04b
Create Date: 2021-11-23 12:48:45.562386

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5954af6b1ba7'
down_revision = '87deb3eaf04b'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column(
        'posts',
        sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('now()'))

    )


def downgrade():
    op.drop_column(
        'posts',
        'created_at'
    )
