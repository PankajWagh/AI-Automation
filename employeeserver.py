
from fastmcp import FastMCP
import mysql.connector

app = FastMCP("mysqlserver")

def run_query(query: str):
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="company"
    )
    cursor = conn.cursor(dictionary=True)
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result

@app.tool()
def query_mysql(query: str):
    return run_query(query)

if __name__ == "__main__":
    # For stdio transport (works with stdio_client)
    app.run(transport="sse", host="localhost", port=9000)


    # If you want SSE transport, remove the line above and instead run:
    # app.run(transport="sse")
    # Then start with: uvicorn employeeserver:app --host 127.0.0.1 --port 8000
