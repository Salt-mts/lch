"""updt biz

Revision ID: b338da2f4ab7
Revises: 169bf9139f57
Create Date: 2023-12-05 19:43:47.455656

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b338da2f4ab7'
down_revision: Union[str, None] = '169bf9139f57'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("business", sa.Column("is_active", sa.Boolean(), default=True))
    op.add_column("business", sa.Column("tag", sa.Text()))
    pass


def downgrade() -> None:
    op.drop_column("business", "is_active")
    op.drop_column("business", "tag")
    pass
