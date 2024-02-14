"""ipos table

Revision ID: dfc1a9cca426
Revises: 6fb6584cc1be
Create Date: 2024-02-13 23:48:16.095746

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'dfc1a9cca426'
down_revision: Union[str, None] = '6fb6584cc1be'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'shareTypes',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True, unique=True),
        sa.Column('name', sa.VARCHAR(55), unique=True)
    )
    op.create_table(
        'ipo',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True, unique=True),
        sa.Column('companyName', sa.VARCHAR(255), nullable=False),
        sa.Column('symbol', sa.VARCHAR(20), nullable=False),
        sa.Column('sector_id', sa.Integer, sa.ForeignKey('sector.id')),
        sa.Column('shareType_id', sa.Integer, sa.ForeignKey('shareTypes.id')),
        sa.Column('totalUnits', sa.Integer, nullable=False),
        sa.Column('pricePerUnit', sa.Float, nullable=False),
        sa.Column('minUnits', sa.Integer, nullable=False),
        sa.Column('maxUnits', sa.Integer, nullable=False),
        sa.Column('ratings', sa.VARCHAR(50)),
        sa.Column('openingDate', sa.Date, nullable=False),
        sa.Column('closingDate', sa.Date, nullable=False),
        sa.Column('staus', sa.Boolean)
    )
    pass


def downgrade() -> None:
    op.drop_table('IPO')
    op.drop_table('shareTypes')
    pass
