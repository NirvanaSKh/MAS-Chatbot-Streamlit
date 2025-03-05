from db.database_connection import connect_to_db

def main(user_query):
    # Connect to the database
    connection = connect_to_db()
    if connection:
        try:
            cursor = connection.cursor()

            # Example query based on user input
            if "top selling products" in user_query.lower():
                cursor.execute("SELECT product_name FROM products ORDER BY sales DESC LIMIT 5;")
                rows = cursor.fetchall()
                # Process rows and return as a response
                products = [row[0] for row in rows]
                return f"The top selling products are: {', '.join(products)}"
            elif "sales trend" in user_query.lower():
                cursor.execute("SELECT year, sales FROM sales_trends WHERE year > 2018 ORDER BY year;")
                rows = cursor.fetchall()
                # Process rows and return as a response
                sales_trend = [f"Year: {row[0]}, Sales: {row[1]}" for row in rows]
                return f"The sales trend over the past 5 years: {', '.join(sales_trend)}"
            else:
                return "Sorry, I didn't understand that query. Could you rephrase?"
        
        except Exception as e:
            return f"Error querying the database: {e}"
        finally:
            cursor.close()
            connection.close()
    else:
        return "Could not connect to the database."
