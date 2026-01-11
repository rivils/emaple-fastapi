"""add foreugn-key to post table

Revision ID: 2dcd60c13769
Revises: 2af8c09f8ef6
Create Date: 2026-01-10 10:59:06.591049

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2dcd60c13769'
down_revision: Union[str, Sequence[str], None] = '2af8c09f8ef6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('post_user_fk', source_table="posts", referent_table="users",
    local_cols=[
                          'owner_id'], remote_cols=['id'], ondelete="CASCADE")
    pass


def downgrade():
   op.drop_constraint('post_users_fk', table_name="posts")
   op.drop_column('posts', 'owner_id')
   pass
