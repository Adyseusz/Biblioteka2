from connection import connect

def add_author(first_name, last_name):

    query = f"""
    INSERT INTO author (first_name, last_name) values ('{first_name}','{last_name}');
    """
    execute_query(query, False)

def add_book(title, id_author):
    query = f"""
        INSERT INTO book (title, author_id) values ('{title}','{id_author}');
        """
    execute_query(query, False)


def get_all_authors():
    query = """
    SELECT * FROM author;
    """
    return execute_query(query)

def get_all_books():
    query = """
        SELECT book.id, book.title, author.first_name, author.last_name 
        FROM book LEFT JOIN author on book.author_id = author.id;
        """
    return execute_query(query)



def execute_query(query, return_result=True):
    connection = connect()
    cursor = connection.cursor()
    cursor.execute(query)
    result = []
    if return_result:
        for item in cursor:
            result.append(item)
    connection.close()
    return result