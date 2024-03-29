"""catalog img

Revision ID: d08a06b21944
Revises: 950a6fc0caeb
Create Date: 2024-01-16 23:35:06.852988

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd08a06b21944'
down_revision: Union[str, None] = '950a6fc0caeb'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('catalog_img',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('catalog_id', sa.Integer(), nullable=False),
    sa.Column('image', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['catalog_id'], ['catalog.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_catalog_img_id'), 'catalog_img', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_catalog_img_id'), table_name='catalog_img')
    op.drop_table('catalog_img')
    # ### end Alembic commands ###
