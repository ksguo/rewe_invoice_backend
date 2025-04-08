"""add inovice model

Revision ID: 7f399e60d961
Revises: 1e99232a3de3
Create Date: 2025-04-07 16:31:32.976894

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '7f399e60d961'
down_revision: Union[str, None] = '1e99232a3de3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('invoice',
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('markt_name', sa.String(length=255), nullable=True),
    sa.Column('store_address', sa.Text(), nullable=True),
    sa.Column('telephone', sa.String(length=50), nullable=True),
    sa.Column('uid_number', sa.String(length=50), nullable=True),
    sa.Column('brand', sa.String(length=100), nullable=True),
    sa.Column('markt_id', sa.String(length=50), nullable=True),
    sa.Column('receipt_nr', sa.String(length=100), nullable=True),
    sa.Column('document_nr', sa.String(length=100), nullable=True),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.Column('time', sa.String(length=20), nullable=True),
    sa.Column('payment_method', sa.String(length=50), nullable=True),
    sa.Column('total', sa.Float(), nullable=True),
    sa.Column('items', postgresql.JSONB(astext_type=sa.Text()), nullable=True),
    sa.Column('ocr_text', sa.Text(), nullable=True),
    sa.Column('is_processed', sa.Boolean(), nullable=False),
    sa.Column('processing_errors', sa.Text(), nullable=True),
    sa.Column('file_id', sa.UUID(), nullable=False),
    sa.Column('user_id', sa.UUID(), nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.ForeignKeyConstraint(['file_id'], ['file.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    op.create_unique_constraint(None, 'file', ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'file', type_='unique')
    op.drop_table('invoice')
    # ### end Alembic commands ###
