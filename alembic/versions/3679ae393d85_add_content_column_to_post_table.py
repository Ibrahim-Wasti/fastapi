"""add content column to post table

Revision ID: 3679ae393d85
Revises: ff33f45648e2
Create Date: 2021-11-09 00:10:11.534341

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3679ae393d85'
down_revision = 'ff33f45648e2'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts',
    sa.Column('content', sa.String(), nullable=False))


def downgrade():
    op.drop_column('posts', 'content')
