"""Add is_active to User model

Revision ID: 8e7027ab80b5
Revises: 7d1fc8c0caa7
Create Date: 2024-10-08 14:42:47.021342

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8e7027ab80b5'
down_revision: Union[str, None] = '7d1fc8c0caa7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('is_active', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'is_active')
    # ### end Alembic commands ###
