"""user tbl

Revision ID: 047f533ae61c
Revises: a05ca6d554f7
Create Date: 2023-11-27 10:28:07.382398

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '047f533ae61c'
down_revision: Union[str, None] = 'a05ca6d554f7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table("users",
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('unik', sa.Integer(), nullable=False),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.Column('firstname', sa.String(), nullable=False),
                    sa.Column('lastname', sa.String(), nullable=False),
                    sa.Column('phone', sa.String(), nullable=False),
                    sa.Column('sex', sa.String(), nullable=False),
                    sa.Column('image', sa.String(), nullable=False),
                    sa.Column('is_active', sa.Boolean(), nullable=False, default=True),
                    sa.Column('verification_code', sa.Integer(), nullable=False, default=111111),
                    sa.Column('email_verified', sa.Integer(), nullable=False, default=0),
                    sa.Column('date_created', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('now()')),

                    sa.PrimaryKeyConstraint("id"),
                    sa.UniqueConstraint("unik"),
                    sa.UniqueConstraint("email")
                    )
    pass


def downgrade() -> None:
    op.drop_table("users")
    pass
