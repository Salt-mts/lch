"""uodt msg

Revision ID: aea6e9f6fd9e
Revises: b9f7fd2a7533
Create Date: 2023-12-18 09:21:16.713359

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'aea6e9f6fd9e'
down_revision: Union[str, None] = 'b9f7fd2a7533'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.drop_table("participants")
    op.drop_table("messages")
    op.drop_table("conversations")



def downgrade() -> None:
    pass
