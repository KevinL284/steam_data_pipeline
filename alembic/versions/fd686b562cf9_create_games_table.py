"""create games table

Revision ID: fd686b562cf9
Revises:
Create Date: 2026-06-24 19:41:57.039493

"""

from typing import Sequence, Union

import sqlalchemy as sa

from alembic import op

revision: str = "fd686b562cf9"
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Create games table."""

    op.create_table(
        "games",
        sa.Column("id", sa.Integer(), primary_key=True, nullable=False),
        sa.Column("name", sa.String(), nullable=True),
        sa.Column("discount_percent", sa.Integer(), nullable=True),
        sa.Column("original_price", sa.Float(), nullable=True),
        sa.Column("final_price", sa.Float(), nullable=True),
        sa.Column("currency", sa.String(), nullable=True),
        sa.Column("windows_available", sa.Boolean(), nullable=True),
        sa.Column("mac_available", sa.Boolean(), nullable=True),
        sa.Column("linux_available", sa.Boolean(), nullable=True),
        sa.Column("controller_support", sa.String(), nullable=True),
    )


def downgrade() -> None:
    """Drop games table."""

    op.drop_table("games")
