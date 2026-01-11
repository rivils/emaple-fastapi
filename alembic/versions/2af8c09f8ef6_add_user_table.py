"""add user table

Revision ID: 2af8c09f8ef6
Revises: b083b98c6b2a
Create Date: 2026-01-10 10:16:11.147775

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2af8c09f8ef6'
down_revision: Union[str, Sequence[str], None] = 'b083b98c6b2a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table('users',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True),
                              server_default=sa.text('now()'), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email')
                    )    
    pass


def downgrade():
    op.drop_table('users')
    pass
