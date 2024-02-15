"""sullable company sector

Revision ID: cb6a5ab16b96
Revises: 4fe5572d3a68
Create Date: 2024-02-14 21:44:49.571463

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'cb6a5ab16b96'
down_revision: Union[str, None] = '4fe5572d3a68'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.alter_column('company', 'sector_id', nullable=True)
    
    pass


def downgrade() -> None:
    op.alter_column('compnay', 'sector_id', nullable=False)
    pass
