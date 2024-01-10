"""defaut biz img

Revision ID: 8e5c38df51a7
Revises: fc962368b7fb
Create Date: 2024-01-05 15:00:36.752780

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8e5c38df51a7'
down_revision: Union[str, None] = 'fc962368b7fb'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
