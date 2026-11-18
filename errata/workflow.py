from .catalog import versions
from .dispatch import on_shift
from .touches import by_version


def report(data):
    known, anonymous = by_version(data['touches'], versions(data['versions']))
    return {'identified_contacts': known, 'anonymous_copies': anonymous,
            'dispatch': on_shift(data['contacts'], data['notices'])}
