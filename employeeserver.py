import mysql.connector
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("mysql-server")

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


@mcp.tool()
def query_mysql(query: str):
    """Execute a SQL query on MySQL database"""
    return run_query(query)


if __name__ == "__main__":
    mcp.run()