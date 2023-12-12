"""catalog img

Revision ID: f55266ed4f51
Revises: e6f231655e35
Create Date: 2023-12-12 12:25:35.546164

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f55266ed4f51'
down_revision: Union[str, None] = 'e6f231655e35'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("catalog", sa.Column("images", sa.String()))
    op.drop_column("catalog", "image1")
    op.drop_column("catalog", "image3")
    op.drop_column("catalog", "image2")
    pass


def downgrade() -> None:
    pass
