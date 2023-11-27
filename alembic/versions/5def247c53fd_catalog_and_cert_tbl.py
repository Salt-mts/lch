"""catalog and cert tbl

Revision ID: 5def247c53fd
Revises: a0f1b504d0a4
Create Date: 2023-11-27 11:13:38.365974

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5def247c53fd'
down_revision: Union[str, None] = 'a0f1b504d0a4'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table("business",
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('owner_id', sa.Integer(), nullable=False),
                    sa.Column('name', sa.String(), nullable=False),
                    sa.Column('about', sa.Text(), nullable=True),
                    sa.Column('work_experience', sa.String(), nullable=True),
                    sa.Column('years_of_experience', sa.Integer(), nullable=True),
                    sa.Column('address', sa.String(), nullable=True),
                    sa.Column('city', sa.String(), nullable=True),
                    sa.Column('state', sa.String(), nullable=True),
                    sa.Column('country', sa.String(), nullable=True),
                    sa.Column('days', sa.String(), nullable=True),
                    sa.Column('hour_from', sa.String(), nullable=True),
                    sa.Column('hour_to', sa.String(), nullable=True),
                    sa.Column('website', sa.String(), nullable=True),
                    sa.Column('facebook', sa.String(), nullable=True),
                    sa.Column('instagram', sa.String(), nullable=True),
                    sa.Column('twitter', sa.String(), nullable=True),
                    sa.Column('linkedin', sa.String(), nullable=True),
                    sa.PrimaryKeyConstraint("id"),
                    )

    op.create_foreign_key('user_business_fk', source_table='business', referent_table='users', local_cols=['owner_id'], remote_cols=['id'], ondelete='CASCADE'
    )
    pass


def downgrade() -> None:
    op.drop_constraint('user_business_fk', table_name='business')
    op.drop_table("business")
    pass
