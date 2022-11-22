import exerciseeleven.sqlitemanager as sql

FILEPATH = 'src/data/config.txt'


def main():
    """Main script for exercise eleven
    :return: None
    :rtype: NoneType
    """
    # Data to insert into a SQLite3 database
    data = [(1, 'Mario', 'Bros'),
            (2, 'Link', ''),
            (3, 'Donkey', 'Kong'),
            (4, 'Pikachu', ''),
            (5, 'Samus', 'Aran'),
            (6, 'Fox', 'McCloud'),
            (7, 'Falcon', ''),
            (8, 'Peach', 'Toadstool'),
            (9, 'Antonio', 'Rodriguez'),
            (10, 'Antonio', 'Sanchez'),
            (11, 'Antonio', 'Moreno'),
            (12, 'Antonio', '')]
    # Read config to obtain database path, table name, column names and types
    dbpath, table, columns, coltype = sql.read_config(FILEPATH)
    for element in data:
        # Insert data
        sql.insert_data(dbpath, table, columns, element)
    # Search for student
    selected = sql.search_student(dbpath, table, columns, coltype, 'Antonio')
    # Check result
    if len(selected) == 0:
        print('There is no such student')
    else:
        if len(selected) > 1:
            print(columns)
            for student in selected:
                print(student)
        else:
            print(selected)


if __name__ == '__main__':
    main()
