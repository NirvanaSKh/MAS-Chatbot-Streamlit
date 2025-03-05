import spacy
from db.database_connection import connect_to_db

# Load the spaCy model for English language processing
nlp = spacy.load("en_core_web_sm")

def extract_intent_and_entities(user_query):
    # Process the query with spaCy
    doc = nlp(user_query)

    # Extract entities (e.g., product names, dates)
    entities = [ent.text for ent in doc.ents]

    # Extract intent (e.g., "top selling products", "sales trend")
    intent = None
    if "top selling products" in user_query.lower():
        intent = "top_selling_products"
    elif "sales trend" in user_query.lower():
        intent = "sales_trend"

    return intent, entities

def generate_sql_query(intent, entities):
    if intent == "top_selling_products":
        # Assuming products have a column like `quantity_sold` or `sales`
        return "SELECT product_name FROM products ORDER BY price DESC LIMIT 5"
    
    elif intent == "sales_trend":
        # Assuming a sales_trends table exists with columns for year and sales
        return "SELECT year, sales FROM sales_trends WHERE year > 2018 ORDER BY year"
    
    return None

def main(user_query):
    # Step 1: Extract intent and entities from the user query
    intent, entities = extract_intent_and_entities(user_query)
    
    if not intent:
        return "Sorry, I couldn't understand your query. Could you try rephrasing?"

    # Step 2: Generate SQL query dynamically
    sql_query = generate_sql_query(intent, entities)
    if not sql_query:
        return "Sorry, I couldn't generate a valid query from your input."

    # Step 3: Connect to the database and execute the query
    connection = connect_to_db()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute(sql_query)
            rows = cursor.fetchall()
            # Process rows and return results
            return format_query_results(rows)
        except Exception as e:
            return f"Error querying the database: {e}"
        finally:
            cursor.close()
            connection.close()

    return "Could not connect to the database."

def format_query_results(rows):
    # Format query results into a readable response
    formatted_results = []
    for row in rows:
        formatted_results.append(str(row))
    return "\n".join(formatted_results)
