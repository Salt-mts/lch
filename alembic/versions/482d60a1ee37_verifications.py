"""verifications

Revision ID: 482d60a1ee37
Revises: 0d57a448ecbc
Create Date: 2023-12-21 02:40:36.110399

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '482d60a1ee37'
down_revision: Union[str, None] = '0d57a448ecbc'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("business", sa.Column("is_verified", sa.Boolean(), default=False))
    op.add_column("business", sa.Column("level", sa.Integer(), default=1))
    op.add_column("users", sa.Column("phone_verified", sa.Integer(), default=0))
    pass


def downgrade() -> None:
    pass
