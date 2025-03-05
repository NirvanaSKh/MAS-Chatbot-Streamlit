import json

class GraphsRuleAgent:
    def select_graph_type(self, data_type):
        graph_rules = {"distribution": "histogram", "default": "line"}
        return graph_rules.get(data_type, graph_rules["default"])
    