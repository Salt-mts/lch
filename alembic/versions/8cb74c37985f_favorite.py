"""favorite

Revision ID: 8cb74c37985f
Revises: 94b3120b2e7b
Create Date: 2023-12-26 12:07:35.456585

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8cb74c37985f'
down_revision: Union[str, None] = '94b3120b2e7b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table("favorite", 
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('user_id', sa.Integer(), nullable=False),
                    sa.Column('business_id', sa.Integer(), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ondelete='CASCADE'),
                    sa.ForeignKeyConstraint(['business_id'], ['business.id'], ondelete='CASCADE')
                    )


def downgrade() -> None:
    pass
