import argparse
from addbiomechanics.commands.transfer_markerset import TransferMarkersetCommand
from addbiomechanics.commands.plot import PlotCommand
from addbiomechanics.commands.debug import DebugCommand
from addbiomechanics.commands.view import ViewCommand
from addbiomechanics.commands.view_energy import ViewEnergyCommand
from addbiomechanics.commands.compare import CompareCommand
from addbiomechanics.commands.post_process import PostProcessCommand
from addbiomechanics.commands.export_csv import ExportCSVCommand
from addbiomechanics.commands.describe_dataset import DescribeDatasetCommand
from addbiomechanics.commands.transfer_reviews import TransferReviewsCommand
from addbiomechanics.commands.create_b3d import CreateB3DCommand
from addbiomechanics.commands.clean_up import CleanUpCommand
from addbiomechanics.commands.stats import StatsCommand


def get_local_commands():
    return [PlotCommand(),
            DebugCommand(),
            ViewCommand(),
            ViewEnergyCommand(),
            CompareCommand(),
            TransferMarkersetCommand(),
            PostProcessCommand(),
            ExportCSVCommand(),
            DescribeDatasetCommand(),
            TransferReviewsCommand(),
            CreateB3DCommand(),
            CleanUpCommand(),
            StatsCommand()]


def build_parser(local_commands):
    parser = argparse.ArgumentParser(
        description='AddBiomechanics Command Line Interface (local-only mode)')

    # Split up by command
    subparsers = parser.add_subparsers(dest="command")

    # Add a parser for each command
    for command in local_commands:
        command.register_subcommand(subparsers)

    return parser


def main():
    local_commands = get_local_commands()

    # Create an ArgumentParser object
    parser = build_parser(local_commands)

    # Parse the arguments
    args = parser.parse_args()

    if args.command is None:
        parser.print_help()
        return

    for command in local_commands:
        if command.run_local(args):
            return
    parser.error('Unknown command: ' + args.command)


if __name__ == '__main__':
    main()
