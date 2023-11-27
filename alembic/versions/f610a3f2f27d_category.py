"""category

Revision ID: f610a3f2f27d
Revises: fb84f3877fb1
Create Date: 2023-11-27 12:00:25.107305

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f610a3f2f27d'
down_revision: Union[str, None] = 'fb84f3877fb1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table("category",
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('name', sa.String(), nullable=False),
                    sa.Column('image', sa.String(), nullable=False, default="default.png"),
                    sa.Column('description', sa.String(), nullable=True),                   
                    sa.Column('parent_id', sa.Integer(), nullable=False, default=0),                   
                    sa.PrimaryKeyConstraint("id")
                    )
    pass


def downgrade() -> None:
    op.drop_table("category")
    pass
