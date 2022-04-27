import psycopg2

n_phase = 8

def create_tables_for_phases(conn, curs):
    for i in range(n_phase):
        curs.execute('create table t{} (age real, workclass text, fnlwgt real, education text, education_num real, marital_status text, occupation text, relationship text, race text, sex text, capital_gain real, capital_loss real, hours_per_week real, native_country text, economic_indicator text);'.format(i + 1))
        curs.execute("copy t{} from CensusData/phase_{} delimiter ',' csv;".format(i + 1, i + 1))
    conn.commit()

def create_db_session():
    conn = psycopg2.connect('dbname=test user=postgres password=secret host=localhost')
    curs = conn.cursor()
    return conn, curs

if __name__ == '__main__':
    conn, curs = create_db_session()
    create_tables_for_phases(conn, curs)