"""create posts table

Revision ID: 0010b5e53a9d
Revises: 
Create Date: 2026-01-10 09:27:57.902138

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0010b5e53a9d'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table('post', sa.Column('id', sa.Integer(), nullable=False, primary_key=True)
                    , sa.Column('title', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_table('posts')   
    pass
