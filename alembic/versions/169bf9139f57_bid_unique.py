"""bid unique

Revision ID: 169bf9139f57
Revises: 293861e355ff
Create Date: 2023-11-28 02:15:48.486241

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '169bf9139f57'
down_revision: Union[str, None] = '293861e355ff'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
