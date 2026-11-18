from collections import Counter


def by_version(rows, catalog):
    identified = Counter()
    anonymous = Counter()
    for row in sorted(rows, key=lambda row: row['tick']):
        version = catalog[row['version']]['id']
        if row['person'] is None:
            anonymous[version] += row['copies']
        else:
            identified[version] += 1
    return dict(identified), dict(anonymous)
