
from .cli import parse_args
from .draw import plot_sankey
from .extract import get_numeric_annotations
from .io import read_sankey_script, write_plotly
from .parse import parse_sankey_script


def main():
    args = parse_args()
    sankey_script = read_sankey_script(args.input)
    nodes, links = parse_sankey_script(sankey_script)

    nodes["pad"] = 100
    numeric_annotations = get_numeric_annotations(nodes, links)
    nodes["label"] = [
        f"{x} ({y})" for x, y in zip(nodes["label"], numeric_annotations)
    ]

    fig = plot_sankey(nodes, links)
    if args.outpath is not None:
        write_plotly(fig, args.outpath)
    if args.show:
        fig.show()


if __name__ == "__main__":
    main()
