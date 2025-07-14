"""create phone number for user column

Revision ID: d4e9e28eba63
Revises: 
Create Date: 2025-07-14 11:58:10.986000

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd4e9e28eba63'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('users', sa.Column('phone_number', sa.String(20), nullable=True))
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
