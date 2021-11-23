"""Create User Table

Revision ID: 646c6b3c6c0e
Revises: 5954af6b1ba7
Create Date: 2021-11-23 13:18:04.546851

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql.schema import PrimaryKeyConstraint


# revision identifiers, used by Alembic.
revision = '646c6b3c6c0e'
down_revision = '5954af6b1ba7'
branch_labels = None
depends_on = None


def upgrade():
     op.create_table(
        'users', 
        sa.Column('id', sa.Integer, nullable=False, 
        # primary_key=True
        ),
        sa.Column('email', sa.String, nullable=False, 
        # unique=True
        ),
        sa.Column('password', sa.String, nullable=False),
        sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('now()')),
        
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('email')
    )


def downgrade():
    op.drop_table(
        'users'
    )
