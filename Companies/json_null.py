"""
All json paths that lead to null

{
    "Jon": "Smith",
    "Adam": ["Jake", null, "Nancy"],
    "Alex": {
        "Muller": [null, "Sam"],
        "Phil": null,
        "Xav": ["Mike", "Tom"]
    }
    "Lex": null,
}

Output: ["Adam.1", "Alex.Muller.0", "Alex.Phil", "Lex"]
"""
import json
def path_to_null(json_str):
    def find_null(node, path, res):
        if node is None:
           res.append(".".join(path))
           return

        if isinstance(node, list):
            for idx, item in enumerate(node):
                path.append(str(idx))
                find_null(item, path, res)
                path.pop()

        if isinstance(node, dict):
            for k, v in node.items():
                path.append(k)
                find_null(v, path, res)
                path.pop()


    path, res = [], []
    json_dict = json.loads(json_str)
    find_null(json_dict, path, res)
    return res


json_str = '{"Jon": "Smith", "Adam": ["Jake", null, "Nancy"], "Alex": { "Muller": [null, "Sam"],\
 "Phil": null, "Xav": ["Mike", "Tom"] }, "Lex": null}'

print(path_to_null(json_str))