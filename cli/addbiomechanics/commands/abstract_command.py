import argparse
from typing import Any


class AbstractCommand:
    def register_subcommand(self, subparsers: argparse._SubParsersAction):
        pass

    def run(self, ctx: Any, args: argparse.Namespace):
        pass

    def run_local(self, args: argparse.Namespace) -> bool:
        return False
