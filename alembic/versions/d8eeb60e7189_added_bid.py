"""added bid

Revision ID: d8eeb60e7189
Revises: dbe452184922
Create Date: 2023-11-28 01:42:56.149133

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd8eeb60e7189'
down_revision: Union[str, None] = 'dbe452184922'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
