"""del catimg

Revision ID: 387ac5f60bca
Revises: d08a06b21944
Create Date: 2024-01-16 23:47:27.051175

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '387ac5f60bca'
down_revision: Union[str, None] = 'd08a06b21944'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass
    


def downgrade() -> None:
    pass
