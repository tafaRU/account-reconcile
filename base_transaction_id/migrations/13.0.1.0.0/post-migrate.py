#  Copyright 2022 Simone Rubino - Agile Business Group
#  License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

def migrate(cr, installed_version):
    cr.execute(
        """
        UPDATE account_move am
            SET transaction_id = ai.transaction_id
        FROM account_invoice ai
        WHERE am.id = ai.move_id AND ai.state not in ('draft', 'cancel')
        """
    )
