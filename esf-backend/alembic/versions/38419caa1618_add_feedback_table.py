"""Add feedback table

Revision ID: 38419caa1618
Revises:
Create Date: 2023-12-10 05:44:47.262634

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '38419caa1618'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'feedbacks',
        sa.Column('id', sa.Integer, primary_key=True, index=True),
        sa.Column('message', sa.String),
    )


def downgrade() -> None:
    op.drop_table('feedbacks')
