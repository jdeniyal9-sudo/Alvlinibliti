from neo4j import GraphDatabase

URI = "neo4j+s://159483fc.databases.neo4j.io"
USER = "neo4j"
PASSWORD = "n4c-CVx99lchFmWg2bD00rqESAsk94YGYnj0xl27h0U"

driver = GraphDatabase.driver(
    URI,
    auth=(USER, PASSWORD)
)

def test_connection():
    with driver.session() as session:
        result = session.run("RETURN 'Neo4j Connected' AS msg")
        print(result.single()["msg"])

if __name__ == "__main__":
    test_connection()
