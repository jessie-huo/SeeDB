import os

import psycopg2

# params
n_phase = 8
A = ['education', 'race', 'native_country']
M = ['fnlwgt', 'capital_gain']
F = ['avg', 'sum']
views = {}
for a in A:
    for m in M:
        for f in F:
            views[len(views)] = [a, m, f]

def share_based_optimization(curs):
    """
    for x in ['target', 'reference']:
        curs.execute('select {} '.format(','.join(A)))
    """

def create_tables(conn, curs):
    csv_filepath = os.getcwd() + '/CensusData/'
    curs.execute('DROP TABLE IF EXISTS all_data')
    curs.execute('create table all_data (age real, workclass text, fnlwgt real, education text, education_num real, marital_status text, occupation text, relationship text, race text, sex text, capital_gain real, capital_loss real, hours_per_week real, native_country text, economic_indicator text);')
    curs.execute(f"copy all_data from '%s' delimiter ',' csv;" % (csv_filepath+'adult.all'))
    curs.execute("create table target as select * from all_data where marital_status in (' Married-AF-spouse', ' Married-civ-spouse', ' Married-spouse-absent', ' Separated');")
    curs.execute("create table reference as select * from all_data where marital_status in (' Widowed', ' Never-married', ' Divorced');")
    for i in range(n_phase):
        curs.execute('create table t{} (age real, workclass text, fnlwgt real, education text, education_num real, marital_status text, occupation text, relationship text, race text, sex text, capital_gain real, capital_loss real, hours_per_week real, native_country text, economic_indicator text);'.format(i + 1))
        curs.execute("copy t{} from '{}phase_{}' delimiter ',' csv;".format(i + 1, csv_filepath, i + 1))
    conn.commit()

def create_db_session():
    conn = psycopg2.connect('dbname=test user=postgres password=secret host=localhost')
    curs = conn.cursor()
    return conn, curs

if __name__ == '__main__':
    conn, curs = create_db_session()
    create_tables(conn, curs)
    share_based_optimization(curs)