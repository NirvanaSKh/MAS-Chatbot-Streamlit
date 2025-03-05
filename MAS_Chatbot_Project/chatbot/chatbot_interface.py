from agents.query_analysis_agent import QueryAnalysisAgent
from agents.data_query_agent import DataQueryAgent
from agents.graphs_rule_agent import GraphsRuleAgent
from agents.build_graph_agent import BuildGraphAgent

def main():
    query = "SELECT * FROM data"
    query_agent = QueryAnalysisAgent()
    data_query_agent = DataQueryAgent()
    graph_rule_agent = GraphsRuleAgent()
    build_graph_agent = BuildGraphAgent()

    # Query Analysis
    intent = query_agent.process_query(query)
    print(f"Intent detected: {intent}")

    # Data Query
    data = data_query_agent.execute_query(query)
    print(f"Data retrieved: {data}")

    # Graph Rule Selection
    graph_type = graph_rule_agent.select_graph_type("distribution")
    print(f"Graph type selected: {graph_type}")

    # Build Graph
    build_graph_agent.build_graph(data, graph_type)

if __name__ == "__main__":
    main()
