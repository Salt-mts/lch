"""catalog and certification tbl

Revision ID: 146053b0dfbf
Revises: 5def247c53fd
Create Date: 2023-11-27 11:30:22.458926

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '146053b0dfbf'
down_revision: Union[str, None] = '5def247c53fd'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table("catalog",
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('business_id', sa.Integer(), nullable=False),
                    sa.Column('name', sa.String(), nullable=False),
                    sa.Column('price', sa.Float(), nullable=True),
                    sa.Column('description', sa.Text(), nullable=True),
                    sa.Column('image1', sa.String(), nullable=False),
                    sa.Column('image2', sa.String(), nullable=True),
                    sa.Column('image3', sa.String(), nullable=True),
                    
                    sa.PrimaryKeyConstraint("id"),
                    )

    op.create_foreign_key('catlog_business_fk', source_table='catalog', referent_table='business', local_cols=['business_id'], remote_cols=['id'], ondelete='CASCADE'
    )


    op.create_table("certificates",
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('business_id', sa.Integer(), nullable=False),
                    sa.Column('name', sa.String(), nullable=False),
                    sa.Column('image', sa.String(), nullable=False),
                    
                    sa.PrimaryKeyConstraint("id")
                    )

    op.create_foreign_key('cert_business_fk', source_table='certificates', referent_table='business', local_cols=['business_id'], remote_cols=['id'], ondelete='CASCADE'
    )
    pass


def downgrade() -> None:
    op.drop_constraint('catlog_business_fk', table_name='catalog')
    op.drop_table("catalog")

    op.drop_constraint('cert_business_fk', table_name='certificates')
    op.drop_table("certificates")
    pass