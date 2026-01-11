"""add content colum to post table

Revision ID: b083b98c6b2a
Revises: 0010b5e53a9d
Create Date: 2026-01-10 09:55:08.781630

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b083b98c6b2a'
down_revision: Union[str, Sequence[str], None] = '0010b5e53a9d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))   
    pass


def downgrade():
    op.drop_column('post', 'content')
    pass