def make_list(strings):

    def html_list():
        res = "<ol>\n"
        for s in strings:
            res += f"  <li>{s}</li>\n"
        res += "</ol>"
        return res

    return html_list
