"""msg

Revision ID: 7540b3f80c34
Revises: 7846b636b7e6
Create Date: 2023-12-17 23:02:35.082131

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7540b3f80c34'
down_revision: Union[str, None] = '7846b636b7e6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
