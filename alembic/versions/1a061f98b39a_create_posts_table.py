"""Create Posts Table

Revision ID: ef9714cab0e2
Revises: 
Create Date: 2021-11-23 12:10:33.659847

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql.schema import Column


# revision identifiers, used by Alembic.
# revision = 'ef9714cab0e2'
revision = '1a061f98b39a'
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    op.create_table(
        'posts', 
        sa.Column('id', sa.Integer, nullable=False, primary_key=True),
        sa.Column('title', sa.String, nullable=False),
        sa.Column('content', sa.String, nullable=False),
    )


def downgrade():
    op.drop_table(
        'posts'
    )
