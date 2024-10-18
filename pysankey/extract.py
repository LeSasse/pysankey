def get_root_nodes(nodes, links):
    return [
        node
        for idx, node in enumerate(nodes["label"])
        if idx not in links["target"]
    ]


def get_numeric_annotations(nodes, links):
    root_nodes = get_root_nodes(nodes, links)
    annotations = []
    for idx, node in enumerate(nodes["label"]):
        if node in root_nodes:
            indices = [i for i, v in enumerate(links["source"]) if v == idx]
        else:
            indices = [i for i, v in enumerate(links["target"]) if v == idx]

        annotations.append(
            sum([v for i, v in enumerate(links["value"]) if i in indices])
        )

    return annotations
