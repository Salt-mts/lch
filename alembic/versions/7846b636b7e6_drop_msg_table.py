"""drop msg table

Revision ID: 7846b636b7e6
Revises: f55266ed4f51
Create Date: 2023-12-17 22:58:52.109397

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7846b636b7e6'
down_revision: Union[str, None] = 'f55266ed4f51'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.drop_table("messages")
    op.drop_table("conversations")
    pass


def downgrade() -> None:
    pass
