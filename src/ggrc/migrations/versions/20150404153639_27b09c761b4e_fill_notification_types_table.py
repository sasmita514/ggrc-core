
"""fill notification_types table

Revision ID: 27b09c761b4e
Revises: 4f9f00e4faca
Create Date: 2015-04-04 15:36:39.540261

"""

from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import table, column

# revision identifiers, used by Alembic.
revision = '27b09c761b4e'
down_revision = '4f9f00e4faca'


def upgrade():
  notification_types_table = table(
      'notification_types',
      column('id', sa.Integer),
      column('name', sa.String),
      column('description', sa.Text),
      column('template', sa.String),
      column('advance_notice', sa.Integer),
      column('created_at', sa.DateTime),
      column('modified_by_id', sa.Integer),
      column('updated_at', sa.DateTime),
      column('context_id', sa.Integer),
  )

  op.bulk_insert(
      notification_types_table,
      [
          {"name": "instant",
           "description": "instant notification upon manual cycle creation",
           "template": "email_notificaiton_tasks",
           "advance": 0,
           },
          {"name": "tg_change",
           "description": "email owners on task group change",
           "template": "owner changed",
           "advance": 0,
           },
      ]
  )


def downgrade():
  pass