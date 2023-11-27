"""business tbl

Revision ID: a0f1b504d0a4
Revises: 047f533ae61c
Create Date: 2023-11-27 10:46:08.938250

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a0f1b504d0a4'
down_revision: Union[str, None] = '047f533ae61c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
