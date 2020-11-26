from connection import connect

def add_author(first_name, last_name):

    query = f"""
    INSERT INTO author (first_name, last_name) values ('{first_name}','{last_name}');
    """
    execute_query(query)

def get_all_authors():
    query = """
    SELECT * FROM author;
    """
    return execute_query(query)



def execute_query(query):
    connection = connect()
    cursor = connection.cursor()
    cursor.execute(query)
    result = []
    if cursor.rowcount > 0:
        for item in cursor:
            result.append(item)
    connection.close()
    return result