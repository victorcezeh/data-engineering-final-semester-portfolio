from db_manager import start_postgres_connection, query_database

conn = start_postgres_connection()
query = """
    select count(*)
    from ink_store.customers
    """

result = query_database(connection=conn, query_str=query)

print(result)