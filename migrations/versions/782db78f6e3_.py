"""empty message

Revision ID: 782db78f6e3
Revises: d85694981ec
Create Date: 2015-11-02 17:53:27.377915

"""

# revision identifiers, used by Alembic.
revision = '782db78f6e3'
down_revision = 'd85694981ec'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('notes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_date', sa.DateTime(), nullable=True),
    sa.Column('content', sa.Text(), nullable=False),
    sa.Column('created_by', sa.String(), nullable=False),
    sa.Column('tenant_id', sa.String(), nullable=False),
    sa.Column('contact_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['contact_id'], ['contacts.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('notes')
    ### end Alembic commands ###
