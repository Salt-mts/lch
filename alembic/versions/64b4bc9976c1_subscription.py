"""subscription

Revision ID: 64b4bc9976c1
Revises: b338da2f4ab7
Create Date: 2023-12-05 20:55:19.544165

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '64b4bc9976c1'
down_revision: Union[str, None] = 'b338da2f4ab7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
