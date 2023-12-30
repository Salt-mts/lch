"""Added chat tables

Revision ID: 50ccf32c0821
Revises: 7540b3f80c34
Create Date: 2023-12-17 23:17:22.236741

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '50ccf32c0821'
down_revision: Union[str, None] = '7540b3f80c34'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('conversations',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('receiver_id', sa.Integer(), nullable=False),
    sa.Column('date_added', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.ForeignKeyConstraint(['receiver_id'], ['users.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_index(op.f('ix_conversations_id'), 'conversations', ['id'], unique=False)
    op.create_table('messages',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('conversation_id', sa.Integer(), nullable=False),
    sa.Column('sender_id', sa.Integer(), nullable=False),
    sa.Column('message', sa.Text(), nullable=True),
    sa.Column('image', sa.String(), nullable=True),
    sa.Column('read', sa.Integer(), nullable=False),
    sa.Column('date_added', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.ForeignKeyConstraint(['conversation_id'], ['conversations.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['sender_id'], ['users.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_messages_id'), 'messages', ['id'], unique=False)
    op.create_table('participants',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('receiver_id', sa.Integer(), nullable=False),
    sa.Column('conversation_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['conversation_id'], ['conversations.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['receiver_id'], ['users.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_participants_id'), 'participants', ['id'], unique=False)
    op.alter_column('business', 'tag',
               existing_type=sa.TEXT(),
               nullable=False)
    op.alter_column('business', 'is_active',
               existing_type=sa.BOOLEAN(),
               nullable=False)
    op.alter_column('catalog', 'images',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.create_index(op.f('ix_sub_history_id'), 'sub_history', ['id'], unique=False)
    op.create_foreign_key(None, 'sub_history', 'business', ['business_id'], ['id'], ondelete='CASCADE')
    op.create_index(op.f('ix_subscriptions_id'), 'subscriptions', ['id'], unique=False)
    op.create_foreign_key(None, 'subscriptions', 'business', ['business_id'], ['id'], ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'subscriptions', type_='foreignkey')
    op.drop_index(op.f('ix_subscriptions_id'), table_name='subscriptions')
    op.drop_constraint(None, 'sub_history', type_='foreignkey')
    op.drop_index(op.f('ix_sub_history_id'), table_name='sub_history')
    op.alter_column('catalog', 'images',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('business', 'is_active',
               existing_type=sa.BOOLEAN(),
               nullable=True)
    op.alter_column('business', 'tag',
               existing_type=sa.TEXT(),
               nullable=True)
    op.drop_index(op.f('ix_participants_id'), table_name='participants')
    op.drop_table('participants')
    op.drop_index(op.f('ix_messages_id'), table_name='messages')
    op.drop_table('messages')
    op.drop_index(op.f('ix_conversations_id'), table_name='conversations')
    op.drop_table('conversations')
    # ### end Alembic commands ###