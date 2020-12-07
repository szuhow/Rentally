"""Truck schema

Revision ID: a142a8446da6
Revises: 901c5b90e55f
Create Date: 2020-12-07 21:13:55.225888

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'a142a8446da6'
down_revision = '901c5b90e55f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('truck',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('loading_capacity', sa.Float(), nullable=True),
                    sa.Column('boot_width', sa.Float(), nullable=True),
                    sa.Column('boot_height', sa.Float(), nullable=True),
                    sa.Column('boot_length', sa.Float(), nullable=True),
                    sa.ForeignKeyConstraint(['id'], ['car.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_index(op.f('ix_truck_id'), 'truck', ['id'], unique=False)
    op.create_index(op.f('ix_truck_loading_capacity'), 'truck', ['loading_capacity'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_truck_loading_capacity'), table_name='truck')
    op.drop_index(op.f('ix_truck_id'), table_name='truck')
    op.drop_table('truck')
    # ### end Alembic commands ###
