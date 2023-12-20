"""drop msg colomn

Revision ID: b9f7fd2a7533
Revises: 50ccf32c0821
Create Date: 2023-12-18 08:28:00.579081

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b9f7fd2a7533'
down_revision: Union[str, None] = '50ccf32c0821'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.drop_column("conversations", "receiver_id")
    pass


def downgrade() -> None:
    pass
