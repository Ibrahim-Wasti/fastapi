"""create posts table

Revision ID: ff33f45648e2
Revises: 
Create Date: 2021-11-08 23:54:29.142929

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ff33f45648e2'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('posts', 
    sa.Column('id', sa.Integer, nullable=False, primary_key=True),
    sa.Column('title', sa.String, nullable=False))
    


def downgrade():
    op.drop_table('posts')
    
