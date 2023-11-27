"""comments and rating tbl

Revision ID: fb84f3877fb1
Revises: 146053b0dfbf
Create Date: 2023-11-27 11:40:55.854195

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'fb84f3877fb1'
down_revision: Union[str, None] = '146053b0dfbf'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table("comments",
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('business_id', sa.Integer(), nullable=False),
                    sa.Column('user_id', sa.Integer(), nullable=False),
                    sa.Column('msg', sa.Text(), nullable=False),
                    sa.Column('date_created', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),                    
                    sa.PrimaryKeyConstraint("id"),
                    )

    op.create_foreign_key('comment_business_fk', source_table='comments', referent_table='business', local_cols=['business_id'], remote_cols=['id'], ondelete='CASCADE'
    )
    op.create_foreign_key('comment_user_fk', source_table='comments', referent_table='users', local_cols=['user_id'], remote_cols=['id'], ondelete='CASCADE'
    )


    op.create_table("rating",
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('business_id', sa.Integer(), nullable=False),
                    sa.Column('user_id', sa.Integer(), nullable=False),
                    sa.Column('rating', sa.Integer(), nullable=False),
                    sa.Column('date_created', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False), 
                    
                    sa.PrimaryKeyConstraint("id")
                    )

    op.create_foreign_key('rating_business_fk', source_table='rating', referent_table='business', local_cols=['business_id'], remote_cols=['id'], ondelete='CASCADE'
    )
    op.create_foreign_key('rating_user_fk', source_table='rating', referent_table='users', local_cols=['user_id'], remote_cols=['id'], ondelete='CASCADE'
    )
    pass


def downgrade() -> None:
    op.drop_constraint('rating_business_fk', table_name='rating')
    op.drop_constraint('rating_user_fk', table_name='rating')
    op.drop_table("rating")

    op.drop_constraint('comment_business_fk', table_name='comments')
    op.drop_constraint('comment_user_fk', table_name='comments')
    op.drop_table("comments")
    pass