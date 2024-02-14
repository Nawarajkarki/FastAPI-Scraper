"""sector table

Revision ID: 3fb96703a9ce
Revises: 
Create Date: 2024-02-13 23:45:03.487680

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3fb96703a9ce'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "sector",
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True, unique=True, index=True),
        sa.Column('name', sa.VARCHAR(255), unique=True, nullable=False),
    )
    pass


def downgrade() -> None:
    op.drop_table('sector')
    pass