import argparse
import unittest

from addbiomechanics.addb import build_parser, get_local_commands


class TestLocalOnlyCLI(unittest.TestCase):
    def _get_parser(self) -> argparse.ArgumentParser:
        return build_parser(get_local_commands())

    def _get_registered_commands(self):
        parser = self._get_parser()
        for action in parser._actions:
            if isinstance(action, argparse._SubParsersAction):
                return set(action.choices.keys())
        return set()

    def test_cloud_flags_are_removed(self):
        parser = self._get_parser()
        option_strings = set(parser._option_string_actions.keys())
        self.assertNotIn('-u', option_strings)
        self.assertNotIn('--username', option_strings)
        self.assertNotIn('-p', option_strings)
        self.assertNotIn('--password', option_strings)
        self.assertNotIn('-d', option_strings)
        self.assertNotIn('--deployment', option_strings)

    def test_cloud_commands_are_not_registered(self):
        commands = self._get_registered_commands()
        self.assertFalse({'ls', 'download', 'download-files', 'generate-credits', 'upload', 'analytics'}.intersection(commands))

    def test_core_local_commands_are_registered(self):
        commands = self._get_registered_commands()
        self.assertTrue({'post-process', 'export-csv', 'stats', 'plot', 'compare'}.issubset(commands))


if __name__ == '__main__':
    unittest.main()
