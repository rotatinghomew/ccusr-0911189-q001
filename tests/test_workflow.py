import copy
import json
from pathlib import Path
import subprocess
import sys
import unittest

from errata.workflow import report


class WorkflowTest(unittest.TestCase):
    def setUp(self):
        self.path = Path(__file__).resolve().parents[1] / 'data' / 'sample.json'
        self.data = json.loads(self.path.read_text(encoding='utf-8'))

    def test_entry(self):
        result = subprocess.run([sys.executable, '-m', 'errata', 'shift', str(self.path)],
                                check=True, capture_output=True, text=True)
        self.assertEqual(json.loads(result.stdout), report(self.data))

    def test_separate_nonpersonal_copies(self):
        self.assertEqual(report(self.data)['anonymous_copies'], {'audio1': 24})
        self.assertEqual(report(self.data)['identified_contacts']['audio1'], 1)

    def test_dispatch_keeps_expired_consent_out(self):
        self.assertEqual(report(self.data)['dispatch'], {'routes': [['R1','phone'],['R1','sms']], 'failed':['N1']})

    def test_invalid_version_link(self):
        self.data['touches'][0]['version'] = 'missing'
        with self.assertRaises(KeyError):
            report(self.data)
