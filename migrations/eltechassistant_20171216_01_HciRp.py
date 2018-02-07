"""
file: migrations/eltechassistant_20171216_01_HciRp.py
"""

from yoyo import step

__depends__ = {}

steps = [
    #
    step("""CREATE TABLE table_name
(
    id INTEGER DEFAULT nextval('table_name_id_seq'::regclass) PRIMARY KEY NOT NULL,
    name TEXT NOT NULL,
    "Обучение" TEXT
);"""),
    step("""CREATE UNIQUE INDEX table_name_name_uindex ON table_name (name);"""),
    step("""CREATE TABLE table_name3
(
    "Teacher Name" TEXT NOT NULL,
    id INTEGER NOT NULL,
    name TEXT NOT NULL,
    CONSTRAINT table_name3_name_fkey FOREIGN KEY (name) REFERENCES table_name (name) ON DELETE CASCADE ON UPDATE CASCADE
);""")
]
