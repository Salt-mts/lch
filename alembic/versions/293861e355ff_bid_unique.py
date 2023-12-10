"""bid unique

Revision ID: 293861e355ff
Revises: d8eeb60e7189
Create Date: 2023-11-28 01:51:50.598733

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '293861e355ff'
down_revision: Union[str, None] = 'd8eeb60e7189'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("business", sa.Column("bid", sa.String(), unique=True))
    pass


def downgrade() -> None:
    op.drop_column("business", "bid")
    pass
