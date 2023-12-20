"""auto msg

Revision ID: 62529de0eb00
Revises: aea6e9f6fd9e
Create Date: 2023-12-20 01:13:55.937316

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '62529de0eb00'
down_revision: Union[str, None] = 'aea6e9f6fd9e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('conversations',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('receiver_id', sa.Integer(), nullable=False),
    sa.Column('sender_id', sa.Integer(), nullable=False),
    sa.Column('last_message', sa.String(), nullable=False),
    sa.Column('date_updated', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
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
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_participants_id'), table_name='participants')
    op.drop_table('participants')
    op.drop_index(op.f('ix_messages_id'), table_name='messages')
    op.drop_table('messages')
    op.drop_index(op.f('ix_conversations_id'), table_name='conversations')
    op.drop_table('conversations')
    # ### end Alembic commands ###
