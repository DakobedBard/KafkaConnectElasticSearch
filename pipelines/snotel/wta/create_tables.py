from pipelines.snotel.wta.sql_queries import create_trip_report_table, trip_location
from pipelines.snotel.utils.postgresConnection import get_postgres_connection


conn = get_postgres_connection()
cur = conn.cursor()
create_table_queries = [create_trip_report_table, trip_location]

for query in create_table_queries:
    cur.execute(query)
conn.commit()