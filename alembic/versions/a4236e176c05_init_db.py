"""init db

Revision ID: a4236e176c05
Revises: 
Create Date: 2022-11-09 20:02:18.892812

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a4236e176c05'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('alumno',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(), nullable=True),
    sa.Column('apedillo_1', sa.String(), nullable=True),
    sa.Column('apedillo_2', sa.String(), nullable=True),
    sa.Column('edad', sa.String(), nullable=True),
    sa.Column('email', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_alumno_apedillo_1'), 'alumno', ['apedillo_1'], unique=False)
    op.create_index(op.f('ix_alumno_apedillo_2'), 'alumno', ['apedillo_2'], unique=False)
    op.create_index(op.f('ix_alumno_edad'), 'alumno', ['edad'], unique=False)
    op.create_index(op.f('ix_alumno_email'), 'alumno', ['email'], unique=True)
    op.create_index(op.f('ix_alumno_id'), 'alumno', ['id'], unique=False)
    op.create_index(op.f('ix_alumno_nombre'), 'alumno', ['nombre'], unique=False)
    op.create_table('asignatura',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre_asignatura', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_asignatura_id'), 'asignatura', ['id'], unique=False)
    op.create_index(op.f('ix_asignatura_nombre_asignatura'), 'asignatura', ['nombre_asignatura'], unique=False)
    op.create_table('profesor',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(), nullable=True),
    sa.Column('apedillo_1', sa.String(), nullable=True),
    sa.Column('apedillo_2', sa.String(), nullable=True),
    sa.Column('edad', sa.String(), nullable=True),
    sa.Column('email', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_profesor_apedillo_1'), 'profesor', ['apedillo_1'], unique=False)
    op.create_index(op.f('ix_profesor_apedillo_2'), 'profesor', ['apedillo_2'], unique=False)
    op.create_index(op.f('ix_profesor_edad'), 'profesor', ['edad'], unique=False)
    op.create_index(op.f('ix_profesor_email'), 'profesor', ['email'], unique=True)
    op.create_index(op.f('ix_profesor_id'), 'profesor', ['id'], unique=False)
    op.create_index(op.f('ix_profesor_nombre'), 'profesor', ['nombre'], unique=False)
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('full_name', sa.String(), nullable=True),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('hashed_password', sa.String(), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.Column('is_superuser', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=True)
    op.create_index(op.f('ix_user_full_name'), 'user', ['full_name'], unique=False)
    op.create_index(op.f('ix_user_id'), 'user', ['id'], unique=False)
    op.create_table('item',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('owner_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['owner_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_item_description'), 'item', ['description'], unique=False)
    op.create_index(op.f('ix_item_id'), 'item', ['id'], unique=False)
    op.create_index(op.f('ix_item_title'), 'item', ['title'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_item_title'), table_name='item')
    op.drop_index(op.f('ix_item_id'), table_name='item')
    op.drop_index(op.f('ix_item_description'), table_name='item')
    op.drop_table('item')
    op.drop_index(op.f('ix_user_id'), table_name='user')
    op.drop_index(op.f('ix_user_full_name'), table_name='user')
    op.drop_index(op.f('ix_user_email'), table_name='user')
    op.drop_table('user')
    op.drop_index(op.f('ix_profesor_nombre'), table_name='profesor')
    op.drop_index(op.f('ix_profesor_id'), table_name='profesor')
    op.drop_index(op.f('ix_profesor_email'), table_name='profesor')
    op.drop_index(op.f('ix_profesor_edad'), table_name='profesor')
    op.drop_index(op.f('ix_profesor_apedillo_2'), table_name='profesor')
    op.drop_index(op.f('ix_profesor_apedillo_1'), table_name='profesor')
    op.drop_table('profesor')
    op.drop_index(op.f('ix_asignatura_nombre_asignatura'), table_name='asignatura')
    op.drop_index(op.f('ix_asignatura_id'), table_name='asignatura')
    op.drop_table('asignatura')
    op.drop_index(op.f('ix_alumno_nombre'), table_name='alumno')
    op.drop_index(op.f('ix_alumno_id'), table_name='alumno')
    op.drop_index(op.f('ix_alumno_email'), table_name='alumno')
    op.drop_index(op.f('ix_alumno_edad'), table_name='alumno')
    op.drop_index(op.f('ix_alumno_apedillo_2'), table_name='alumno')
    op.drop_index(op.f('ix_alumno_apedillo_1'), table_name='alumno')
    op.drop_table('alumno')
    # ### end Alembic commands ###
