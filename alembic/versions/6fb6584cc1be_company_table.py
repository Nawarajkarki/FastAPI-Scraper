"""company table

Revision ID: 6fb6584cc1be
Revises: 3fb96703a9ce
Create Date: 2024-02-13 23:47:33.253840

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6fb6584cc1be'
down_revision: Union[str, None] = '3fb96703a9ce'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "company",
        sa.Column('id', sa.INTEGER, primary_key=True, autoincrement=True, unique=True, index=True),
        sa.Column('name', sa.VARCHAR(255), nullable=False, index=True, unique=True),
        sa.Column('symbol', sa.VARCHAR(20), nullable=False, index=True, unique=True),
        sa.Column('sector_id', sa.INTEGER, sa.ForeignKey('sector.id'), nullable=False),
    )
    pass


def downgrade() -> None:
    op.drop_table('company')
    pass
