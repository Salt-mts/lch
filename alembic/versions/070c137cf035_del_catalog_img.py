"""del catalog img

Revision ID: 070c137cf035
Revises: 387ac5f60bca
Create Date: 2024-01-16 23:56:22.794762

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '070c137cf035'
down_revision: Union[str, None] = '387ac5f60bca'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.drop_column("catalog", "images")


def downgrade() -> None:
    pass
