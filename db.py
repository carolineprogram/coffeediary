import streamlit as st
from st_supabase_connection import SupabaseConnection

def get_connection():
    # op Supabase
    return st.connection("supabase", type=SupabaseConnection)

def run_query(query, table, data=None, where=None, order=None):
    """
       Executes a query on the Supabase database.

       :param query: Type of query ("select", "insert", "update", "delete").
       :param table: Table name.
       :param data: Data for insertion, update, or selected columns (list or dict).
       :param where: Dictionary of column-value pairs for filtering.
       :param order: Column name for ordering (optional).
       :return: Query result or None if an error occurs.
       """
    #SupabaseConnection does not support the context manager protocol
    # (i.e., it does not have __enter__ and __exit__ methods).
    # This means you cannot use it with a with statement.

    try:
        conn = get_connection()  # Get connection

        q = conn.table(table)  # Initialize table

        if query == "select":
            if isinstance(data, list):
                q = q.select(",".join(data))  # Convert list to string
            else:
                q = q.select("*")  # Default: Select all

            if where:
                for col, val in where.items():
                    q = q.eq(col, val)  # Apply where conditions
            if order:
                q = q.order(order)

            result = q.execute()
            
        elif query == "joinselect":
        result = conn.table('koffie_soort').select('naam, koffie_winkel(waardegekocht)').execute()
        return result

        elif query == "insert":
            result = q.insert(data).execute()

        elif query == "update":
            rows = conn.table(tabel).update(dict).eq().execute()
            if not where:
                raise ValueError("Update queries require a 'where' condition.")
            for col, val in where.items():
                q = q.eq(col, val)
            result = q.update(data).execute()

        elif query == "delete":
            if not where:
                raise ValueError("Delete queries require a 'where' condition.")
            for col, val in where.items():
                q = q.eq(col, val)
            result = q.delete().execute()

        else:
            raise ValueError(f"Invalid query type: {query}")

        return result

    except Exception as e:
        print(f"An error occurred: {e}")
        return None
