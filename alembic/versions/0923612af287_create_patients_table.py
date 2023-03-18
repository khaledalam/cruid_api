"""create patient table

Revision ID: 8ccac142ce40
Revises:
Create Date: 2023-03-17 18:01:39.011788

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '8ccac142ce40'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('patients',
                    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
                    sa.Column('name', sa.String(length=255), nullable=True),
                    sa.Column('email', sa.String(length=255), nullable=True),
                    sa.Column('dob', sa.String(length=225), nullable=False),
                    sa.Column('medical_record_number', sa.String(length=225), nullable=False),
                    sa.Column('created', sa.DateTime(), nullable=False),
                    sa.Column('updated', sa.DateTime(), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    mysql_engine='InnoDB',
                    mysql_charset='utf8mb4',
                    )
    op.create_index(op.f('idx_patient_email'), 'patients', ['email'], unique=True)
    op.create_index(op.f('idx_medical_record_number'), 'patients', ['medical_record_number'], unique=True)
    # pass


def downgrade():
    op.drop_index(op.f('idx_patient_email'), table_name='patients')
    op.drop_index(op.f('idx_medical_record_number'), table_name='patients')
    op.drop_table('patients')
    # pass
