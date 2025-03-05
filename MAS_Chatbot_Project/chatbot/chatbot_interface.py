from agents.query_analysis_agent import QueryAnalysisAgent
from agents.data_query_agent import DataQueryAgent
from agents.graphs_rule_agent import GraphsRuleAgent
from agents.build_graph_agent import BuildGraphAgent

def main(user_query):
    # Print query to see if it's being passed properly
    print(f"Received query: {user_query}")

    # Example query handler, modify based on your chatbot logic
    if "top selling products" in user_query.lower():
        return "The top selling products are: Product A, Product B, and Product C."
    elif "sales trend" in user_query.lower():
        return "The trend of sales over the past 5 years has been consistently upward."
    else:
        return "Sorry, I didn't understand that query. Could you rephrase?"


    # Build Graph
    build_graph_agent.build_graph(data, graph_type)

if __name__ == "__main__":
    main()
