import math
import os
import psycopg2
import numpy as np

# params
n_phase = 8
delta = 0.02
k = 5
A = ['education', 'race', 'native_country']
M = ['fnlwgt', 'capital_gain']
F = ['avg', 'sum']
views = {}
accept_views = []
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
    curs.execute('DROP TABLE IF EXISTS all_data, target, reference, t1, t2, t3, t4, t5, t6, t7, t8')
    curs.execute('create table all_data (age real, workclass text, fnlwgt real, education text, education_num real, marital_status text, occupation text, relationship text, race text, sex text, capital_gain real, capital_loss real, hours_per_week real, native_country text, economic_indicator text);')
    f = open(csv_filepath + 'adult.all')
    curs.copy_from(f, 'all_data', sep=',')
    f.close()
    curs.execute("create table target as select * from all_data where marital_status in (' Married-AF-spouse', ' Married-civ-spouse', ' Married-spouse-absent', ' Separated');")
    curs.execute("create table reference as select * from all_data where marital_status in (' Widowed', ' Never-married', ' Divorced');")
    for i in range(n_phase):
        curs.execute('create table t{} (age real, workclass text, fnlwgt real, education text, education_num real, marital_status text, occupation text, relationship text, race text, sex text, capital_gain real, capital_loss real, hours_per_week real, native_country text, economic_indicator text);'.format(i + 1))
        f = open(csv_filepath + 'phase_' + str(i + 1))
        curs.copy_from(f, 't' + str(i + 1), sep=',')
        f.close()
    conn.commit()

def create_db_session():
    conn = psycopg2.connect('dbname=jhuo user=jhuo host=cs645db.cs.umass.edu port=7645')
    curs = conn.cursor()
    return conn, curs

def calculate_epsilon_m(m, N = n_phase, delta = delta):
    return ((1-(m-1)/N)*((2*math.log2(math.log2(m)))+(math.log2(math.pi**2/3*delta)))/(2*m))**0.5

# views_scores = {view_1:SOME_VALUE(KL-divergence), view_2:SOME_VALUE, view_3:SOME_VALUE}
# m = current phase
# run once at end of each phase
# implemented based of ref[37] pseudocode
# assume views, views_scores only contains valid views (not including removed ones)
def CI_pruning(views_scores, m):
    global k
    epsilon_m = calculate_epsilon_m(m)
    stats = {}

    # loop through each view to calculate mean, lowerbound, upperbound
    for view, val in views_scores.items():
        stats[view]["mean"] = np.mean(val)
        stats[view]["upper"] = stats[view]["mean"] + epsilon_m
        stats[view]["lower"] = stats[view]["mean"] - epsilon_m

    # sort by upperbound, get top k views
    views_sort_by_upper = sorted(stats, key=lambda x: (stats[x]['upper']), reverse=True) # return views name
    top_k_views = views_sort_by_upper[:k]

    # find min(lowerbound) of top_k_views
    min_lower = stats[top_k_views[0]]["lower"]
    for view in top_k_views:
        min_lower = min(min_lower, stats[view]["lower"])

    for view, stat in stats.items():
        if view not in top_k_views:
            if stat["upper"] < min_lower:
                del views[view]

# run once at end of each phase
# implemented based of ref[37] pseudocode
# assume views, views_scores only contains valid views (not including removed ones)
# top-k-views  = accept_views + remaining_ones_in_views (sort by mean)
def MAB_pruning(views_scores):
    # loop through each view to calculate mean
    stats = {}
    for view, val in views_scores.items():
        stats[view]["mean"] = np.mean(val)

    # sort by mean
    views_sort_by_mean = sorted(stats, key=lambda x: (stats[x]['mean']), reverse=True)  # return views name
    delta_1 = stats[views_sort_by_mean[0]]["mean"] - stats[views_sort_by_mean[k]]["mean"]
    delta_n = stats[views_sort_by_mean[k-1]]["mean"] - stats[views_sort_by_mean[-1]]["mean"]
    if delta_1 > delta_n:
        accept_views.append(views_sort_by_mean[0])
        del views[views_sort_by_mean[0]]
    else:
        del views[views_sort_by_mean[-1]]



if __name__ == '__main__':
    conn, curs = create_db_session()
    create_tables(conn, curs)
    share_based_optimization(curs)