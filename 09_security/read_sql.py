from pathlib import Path

sql_path = Path(__file__).parent / "sql"

def read_sql_file(sql_filename):
    with open (sql_path / sql_filename, 'r') as sql_file:
        return sql_file.read()
