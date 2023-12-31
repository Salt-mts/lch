"""auto gen

Revision ID: dbe452184922
Revises: f610a3f2f27d
Create Date: 2023-11-27 13:11:12.952706

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = 'dbe452184922'
down_revision: Union[str, None] = 'f610a3f2f27d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('conversations',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('conversation_id', sa.String(), nullable=False),
    sa.Column('sender_id', sa.Integer(), nullable=False),
    sa.Column('receiver_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['receiver_id'], ['users.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['sender_id'], ['users.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('conversation_id')
    )
    op.create_index(op.f('ix_conversations_id'), 'conversations', ['id'], unique=False)
    op.create_table('messages',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('conversation_id', sa.String(), nullable=False),
    sa.Column('message', sa.Text(), nullable=True),
    sa.Column('image', sa.String(), nullable=True),
    sa.Column('read', sa.Integer(), nullable=False),
    sa.Column('date_added', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.ForeignKeyConstraint(['conversation_id'], ['conversations.conversation_id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_messages_id'), 'messages', ['id'], unique=False)
    op.add_column('business', sa.Column('category', sa.String(), nullable=True))
    op.alter_column('business', 'work_experience',
               existing_type=sa.VARCHAR(),
               type_=sa.Text(),
               existing_nullable=True)
    op.create_index(op.f('ix_business_id'), 'business', ['id'], unique=False)
    op.create_index(op.f('ix_catalog_id'), 'catalog', ['id'], unique=False)
    op.create_index(op.f('ix_category_id'), 'category', ['id'], unique=False)
    op.create_index(op.f('ix_certificates_id'), 'certificates', ['id'], unique=False)
    op.create_index(op.f('ix_comments_id'), 'comments', ['id'], unique=False)
    op.alter_column('rating', 'date_created',
               existing_type=postgresql.TIMESTAMP(timezone=True),
               type_=sa.TIMESTAMP(),
               existing_nullable=False,
               existing_server_default=sa.text('now()'))
    op.create_index(op.f('ix_rating_id'), 'rating', ['id'], unique=False)
    op.alter_column('users', 'email',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('users', 'firstname',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('users', 'lastname',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('users', 'phone',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('users', 'sex',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('users', 'image',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('users', 'is_active',
               existing_type=sa.BOOLEAN(),
               nullable=True)
    op.alter_column('users', 'date_created',
               existing_type=postgresql.TIMESTAMP(timezone=True),
               type_=sa.TIMESTAMP(),
               existing_nullable=False,
               existing_server_default=sa.text('now()'))
    op.drop_constraint('users_email_key', 'users', type_='unique')
    op.drop_constraint('users_unik_key', 'users', type_='unique')
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    op.create_index(op.f('ix_users_id'), 'users', ['id'], unique=False)
    op.drop_column('users', 'unik')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('unik', sa.INTEGER(), autoincrement=False, nullable=False))
    op.drop_index(op.f('ix_users_id'), table_name='users')
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.create_unique_constraint('users_unik_key', 'users', ['unik'])
    op.create_unique_constraint('users_email_key', 'users', ['email'])
    op.alter_column('users', 'date_created',
               existing_type=sa.TIMESTAMP(),
               type_=postgresql.TIMESTAMP(timezone=True),
               existing_nullable=False,
               existing_server_default=sa.text('now()'))
    op.alter_column('users', 'is_active',
               existing_type=sa.BOOLEAN(),
               nullable=False)
    op.alter_column('users', 'image',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('users', 'sex',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('users', 'phone',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('users', 'lastname',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('users', 'firstname',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('users', 'email',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.drop_index(op.f('ix_rating_id'), table_name='rating')
    op.alter_column('rating', 'date_created',
               existing_type=sa.TIMESTAMP(),
               type_=postgresql.TIMESTAMP(timezone=True),
               existing_nullable=False,
               existing_server_default=sa.text('now()'))
    op.drop_index(op.f('ix_comments_id'), table_name='comments')
    op.drop_index(op.f('ix_certificates_id'), table_name='certificates')
    op.drop_index(op.f('ix_category_id'), table_name='category')
    op.drop_index(op.f('ix_catalog_id'), table_name='catalog')
    op.drop_index(op.f('ix_business_id'), table_name='business')
    op.alter_column('business', 'work_experience',
               existing_type=sa.Text(),
               type_=sa.VARCHAR(),
               existing_nullable=True)
    op.drop_column('business', 'category')
    op.drop_index(op.f('ix_messages_id'), table_name='messages')
    op.drop_table('messages')
    op.drop_index(op.f('ix_conversations_id'), table_name='conversations')
    op.drop_table('conversations')
    # ### end Alembic commands ###
