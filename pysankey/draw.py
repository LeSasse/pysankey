import plotly.graph_objects as go


def plot_sankey(nodes, links):

    fig = go.Figure(data=[go.Sankey(node=nodes, link=links)])

    fig.update_layout(font_size=20, width=1200, height=800)

    return fig
