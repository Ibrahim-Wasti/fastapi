"""adding columns to posts table

Revision ID: 716401ace03b
Revises: 7a40acf2136a
Create Date: 2021-11-09 00:29:16.865867

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '716401ace03b'
down_revision = '7a40acf2136a'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('published', sa.Boolean(), nullable=False, server_default="True"))
    op.add_column('posts', sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('now()')))


def downgrade():
    op.drop_column('posts', 'published')
    op.drop_column('posts','created_at')
