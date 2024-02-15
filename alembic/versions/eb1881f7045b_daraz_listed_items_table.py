"""daraz listed items table

Revision ID: eb1881f7045b
Revises: cb6a5ab16b96
Create Date: 2024-02-16 00:24:51.554327

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'eb1881f7045b'
down_revision: Union[str, None] = 'cb6a5ab16b96'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "daraz_products",
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True, nullable=False),
        sa.Column('productName', sa.VARCHAR(255), nullable=False, index=True),
        sa.Column('price', sa.FLOAT, nullable=False, index=True),
        sa.Column('free_delivery', sa.Boolean, default=False),
        sa.Column('ratings', sa.Float),
        sa.Column('num_of_ratings', sa.Float),
        sa.Column('total_sold', sa.Integer, default=0),
        sa.Column('url', sa.VARCHAR(500))
        
    )
    pass

def downgrade() -> None:
    op.drop_table('daraz_products')
    pass
