"""updt Sub

Revision ID: 561465a6e809
Revises: 64b4bc9976c1
Create Date: 2023-12-05 21:23:51.309863

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '561465a6e809'
down_revision: Union[str, None] = '64b4bc9976c1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table("subscriptions", 
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('business_id', sa.Integer(), nullable=False),
                    sa.Column('is_active', sa.Boolean(), default=True, nullable=False),
                    sa.Column('start_date', sa.TIMESTAMP(timezone=True), nullable=False),
                    sa.Column('end_date', sa.TIMESTAMP(timezone=True), nullable=False),
                    sa.PrimaryKeyConstraint('id')
                    )
    pass


def downgrade() -> None:
    op.drop_table('subscriptions')
    pass
