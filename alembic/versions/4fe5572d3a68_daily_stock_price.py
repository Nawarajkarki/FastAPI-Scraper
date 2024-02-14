"""daily stock price

Revision ID: 4fe5572d3a68
Revises: dfc1a9cca426
Create Date: 2024-02-14 00:02:17.471027

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4fe5572d3a68'
down_revision: Union[str, None] = 'dfc1a9cca426'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "daily_stock_price",
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True, nullable=False),
        sa.Column('date', sa.Date, nullable=False),
        sa.Column('company_id', sa.Integer, sa.ForeignKey('company.id'), nullable=False),
        sa.Column('openPrice', sa.Float,),
        sa.Column('closePrice', sa.Float ),
        sa.Column('highPrice', sa.Float),
        sa.Column('lowPrice', sa.Float),
        sa.Column('previousClose', sa.Float),
        sa.Column('volume', sa.Integer),
    )
    pass


def downgrade() -> None:
    op.drop_table('daily_stock_price')
    pass
