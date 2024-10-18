from argparse import ArgumentParser
from pathlib import Path


def parse_args():
    parser = ArgumentParser(
        description="Create simple sankey charts from local scripts.",
    )
    parser.add_argument(
        "input",
        type=Path,
        help="Path to a plain text file containing the sankey script.",
    )
    parser.add_argument(
        "-o",
        "--outpath",
        help=(
            "Path to output file. Supported formats: "
            "['png', 'jpg', 'jpeg', 'webp', 'svg', 'pdf', 'eps', 'json']",
        ),
        type=Path,
    )
    parser.add_argument(
        "-s",
        "--show",
        help="Immediately display the figure in a browser for manual editing.",
        action="store_true",
    )
    return parser.parse_args()
