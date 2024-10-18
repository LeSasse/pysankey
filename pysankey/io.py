def read_sankey_script(path):
    with open(path, "r") as f:
        return f.read()


def write_plotly(fig, outpath):
    format = outpath.suffix[1:]
    fig.write_image(outpath, format=format)
