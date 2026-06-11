from graph.neo4j_client import driver

def save_scan(data):

    domain = data.get("domain")

    with driver.session() as session:

        session.run(
            """
            MERGE (d:Domain {name:$domain})
            SET d.ip = $ip,
                d.server = $server,
                d.tech = $tech
            """,
            domain=domain,
            ip=data.get("ip"),
            server=data.get("headers", {}).get("Server"),
            tech=",".join(data.get("technologies", []))
        )

        for ns in data.get("name_servers", []):

            session.run(
                """
                MERGE (n:NameServer {name:$ns})
                MERGE (d:Domain {name:$domain})
                MERGE (d)-[:USES_NS]->(n)
                """,
                ns=ns,
                domain=domain
            )

        ssl_data = data.get("ssl", {})

        issuer = ssl_data.get("issuer", {}).get("commonName")

        if issuer:

            session.run(
                """
                MERGE (s:SSL {issuer:$issuer})
                MERGE (d:Domain {name:$domain})
                MERGE (d)-[:USES_SSL]->(s)
                """,
                issuer=issuer,
                domain=domain
            )
