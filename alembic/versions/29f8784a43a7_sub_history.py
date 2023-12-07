"""sub history

Revision ID: 29f8784a43a7
Revises: 561465a6e809
Create Date: 2023-12-07 15:25:57.423704

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '29f8784a43a7'
down_revision: Union[str, None] = '561465a6e809'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table("sub_history", 
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('business_id', sa.Integer(), nullable=False),
                    sa.Column('start_date', sa.TIMESTAMP(timezone=True), nullable=False),
                    sa.Column('end_date', sa.TIMESTAMP(timezone=True), nullable=False),
                    sa.PrimaryKeyConstraint('id')
                    )
    pass


def downgrade() -> None:
    op.drop_table('sub_history')
    pass
