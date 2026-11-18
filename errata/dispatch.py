def on_shift(contacts, notices):
    routes = sorted({(row['person'], row['channel']) for row in contacts
                     if row['consent'] and row['available']})
    retry = sorted({row['key'] for row in notices if row['status'] == 'failed'})
    return {'routes': [list(route) for route in routes], 'failed': retry}
