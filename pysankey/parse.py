import plotly.colors as pc
import random
import re


def property_string_to_dict(property_string):
    if ";" in property_string:
        tokens = property_string.split(";")
    else:
        tokens = [property_string]

    tokens = [token.split(":") for token in tokens]
    return {a.strip(): b.strip() for a, b in tokens}


def parse_arrow_properties(arrow_properties_string):
    x = arrow_properties_string.replace("{", "")
    x = x.replace("}", "")
    return property_string_to_dict(x)


def parse_node_properties(line_string):
    pattern_parentheses = r"\((.*?)\)"

    source_dict, target_dict = (
        {"color": "rgba(255, 255, 255, 0.4)"},
        {"color": "rgba(255, 255, 255, 0.4)"},
    )

    source_string, target_string = line_string.split("[")

    if "(" in source_string:
        source_dict = property_string_to_dict(
            re.search(pattern_parentheses, source_string).group(1)
        )
        line_string = re.sub(pattern_parentheses, "", line_string, count=1)

    if "(" in target_string:
        target_dict = property_string_to_dict(
            re.search(pattern_parentheses, target_string).group(1)
        )
        line_string = re.sub(pattern_parentheses, "", line_string, count=1)

    return line_string, source_dict, target_dict


def parse_sankey_script(sankey_script):

    nodes = {"label": [], "color": []}
    links = {"source": [], "target": [], "value": [], "color": []}

    for line_nr, line_content in enumerate(sankey_script.split("\n")):
        line_content = line_content.strip()

        if line_content == "":
            continue

        if "{" in line_content:
            split_line = line_content.split("{")
            line_content, line_properties = split_line[0], "{" + split_line[1]
            arrow_properties = parse_arrow_properties(line_properties)

            for key, value in arrow_properties.items():
                links[key].append(value)
        else:
            default_arrow_properties = {
                "color": random.choice(pc.DEFAULT_PLOTLY_COLORS)
            }
            for key, value in default_arrow_properties.items():
                links[key].append(value)

        line_content, source_props, target_props = parse_node_properties(
            line_content
        )

        try:
            source, rest = line_content.split("[")
            source = source.strip()
            value_link, target = rest.split("]")
            target = target.strip()
        except ValueError:
            raise ValueError(f"Line {line_nr}: SyntaxError - {line_content}")

        if source not in nodes["label"]:
            nodes["label"].append(source)
            for key, value in source_props.items():
                nodes[key].append(value)

        if target not in nodes["label"]:
            nodes["label"].append(target)
            for key, value in target_props.items():
                nodes[key].append(value)

        links["source"].append(nodes["label"].index(source))
        links["target"].append(nodes["label"].index(target))
        links["value"].append(int(value_link))

    return nodes, links
