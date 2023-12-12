"""bizness img

Revision ID: e6f231655e35
Revises: 29f8784a43a7
Create Date: 2023-12-12 10:16:49.278011

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e6f231655e35'
down_revision: Union[str, None] = '29f8784a43a7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("business", sa.Column("image", sa.String(), nullable=True))
    pass


def downgrade() -> None:
    op.drop_column("business", "image")
    pass
