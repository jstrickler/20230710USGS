#!/usr/bin/env python
# (c)2015 John Strickler

# even though we are importing DatabaseConnection, it does not
# create a new connection
from dbconn import db_cursor

PEOPLE = [
    ('Bill', 'Gates', 'Microsoft'),
    ('Steve', 'Jobs', 'Apple'),
    ('Paul', 'Allen', 'Microsoft'),
    ('Larry', 'Ellison', 'Oracle'),
    ('Mark', 'Zuckerberg', 'Facebook'),
    ('Sergey','Brin', 'Google'),
    ('Larry', 'Page', 'Google'),
    ('Linux', 'Torvalds', 'Linux'),
]

def build_database():
    db_cursor.execute('''
        create table computer_people (
            first_name varchar(16),
            last_name varchar(16),
            known_for varchar(16)
        );
    ''')

    insert_query = '''
        insert into computer_people
        (first_name, last_name, known_for)
        values (?, ?, ?);
    '''

    db_cursor.executemany(insert_query, PEOPLE)
