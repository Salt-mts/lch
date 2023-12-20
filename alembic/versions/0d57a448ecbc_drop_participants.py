"""drop participants

Revision ID: 0d57a448ecbc
Revises: 62529de0eb00
Create Date: 2023-12-20 03:02:03.245438

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0d57a448ecbc'
down_revision: Union[str, None] = '62529de0eb00'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.drop_table("participants")
    pass


def downgrade() -> None:
    pass
