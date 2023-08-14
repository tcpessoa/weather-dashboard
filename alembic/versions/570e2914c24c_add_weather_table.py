"""Add weather table

Revision ID: 570e2914c24c
Revises: 
Create Date: 2023-08-14 10:50:54.034032

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '570e2914c24c'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('weather_table',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('temperature', sa.Float(), nullable=True),
    sa.Column('latitude', sa.Float(), nullable=True),
    sa.Column('longitude', sa.Float(), nullable=True),
    sa.Column('humidity', sa.Float(), nullable=True),
    sa.Column('pressure', sa.Float(), nullable=True),
    sa.Column('location', sa.String(length=256), nullable=True),
    sa.Column('weather_description', sa.String(length=256), nullable=True),
    sa.Column('timestamp', sa.TIMESTAMP(), server_default=sa.text('now()'), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_weather_table_id'), 'weather_table', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_weather_table_id'), table_name='weather_table')
    op.drop_table('weather_table')
    # ### end Alembic commands ###
