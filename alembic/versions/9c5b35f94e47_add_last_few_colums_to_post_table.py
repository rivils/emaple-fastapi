"""add last few colums to post table

Revision ID: 9c5b35f94e47
Revises: 2dcd60c13769
Create Date: 2026-01-10 11:09:34.704497

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9c5b35f94e47'
down_revision: Union[str, Sequence[str], None] = '2dcd60c13769'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.add_column('posts', sa.Column(
        'published', sa.Boolean(), nullable=False, server_default='True'),)
    op.add_column('posts', sa.Column(
        'created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default= sa.text
        ('NOW()')),)
    pass

def downgrade():
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass
