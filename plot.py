import matplotlib.pyplot as plt
import numpy as np

def plot(a, m, f, target_dict, reference_dict, fig_name): # target and reference dictionary both with format {a:f(m)}
    x_coordinates = np.arange(len(target_dict))
    width = 0.2
    plt.subplots()
    plt.xlabel(a)
    plt.ylabel('{}({})'.format(f, m))
    plt.xticks(x_coordinates + 0.5 * width, target_dict.keys())
    plt.bar(x_coordinates, target_dict.values(), width, label='target')
    plt.bar(x_coordinates + width, reference_dict.values(), width, label='reference')
    plt.legend()
    # plt.show()
    plt.savefig(fig_name)
"""
target1 = {' Black': 236659.80868075386, ' Other': 208043.9128205128, ' Asian-Pac-Islander': 163645.46980676329, ' White': 185462.30190251354, ' Amer-Indian-Eskimo': 124841.8426395939}
target2 = {' Some-college': 189041.12158647593, ' Assoc-acdm': 189671.74180865005, ' Bachelors': 186632.08043875685, ' 11th': 195828.9815100154, ' 9th': 195762.6377171216, ' HS-grad': 185903.5856894841, ' 12th': 193234.10087719298, ' 7th-8th': 185391.70333333334, ' 10th': 201986.44462279294, ' Assoc-voc': 177039.8324225865, ' 5th-6th': 226348.5227963526, ' Prof-school': 190857.79541734862, ' Doctorate': 182187.11915887852, ' Preschool': 257428.55263157896, ' Masters': 182803.01630094045, ' 1st-4th': 238022.67741935485}
target3 = {' Cambodia': 189237.82352941178, ' Haiti': 233732.275, ' Cuba': 243623.0823529412, ' Jamaica': 196763.3125, ' Dominican-Republic': 208306.71698113208, ' Peru': 299064.4166666667, ' South': 160820.71666666667, ' Honduras': 213201.11111111112, ' Hong': 208053.9, ' Taiwan': 170842.76923076922, ' China': 165202.29347826086, ' Italy': 179814.08974358975, ' Nicaragua': 339073.6818181818, ' Ecuador': 179543.39285714287, ' Iran': 187631.30555555556, ' Hungary': 201311.5, ' Philippines': 168258.51764705882, ' United-States': 185038.82674017918, ' Vietnam': 165164.05263157896, ' Columbia': 232255.23913043478, ' India': 165301.31132075473, ' Germany': 193876.57142857142, ' Scotland': 153432.25, ' Thailand': 159184.66666666666, ' France': 192732.66666666666, ' Puerto-Rico': 204097.15789473685, ' Poland': 179460.3392857143, ' England': 179042.80701754385, ' Laos': 204697.4, ' Ireland': 142552.64705882352, ' Trinadad&Tobago': 185047.2, ' ?': 195375.125, ' Canada': 204293.76470588235, ' Japan': 196690.28846153847, ' Outlying-US(Guam-USVI-etc)': 219239.5, ' Guatemala': 248460.74285714285, ' Portugal': 136920.9090909091, ' Greece': 144597.14285714287, ' El-Salvador': 225588.53623188406, ' Mexico': 284787.3511586453, ' Yugoslavia': 214228.46666666667}
reference1 = {' Black': 226800.01022494887, ' Other': 184322.30805687205, ' Asian-Pac-Islander': 155185.4023154848, ' White': 188430.31420209334, ' Amer-Indian-Eskimo': 116697.14285714286}
reference2 = {' Some-college': 190714.44859514688, ' Assoc-acdm': 197367.87828162292, ' Bachelors': 190435.57824061386, ' 11th': 194696.7403267412, ' 9th': 202710.5864022663, ' HS-grad': 191470.5748704663, ' 12th': 199825.668997669, ' 7th-8th': 191301.38591549295, ' 10th': 192096.8263707572, ' Assoc-voc': 182136.19106957424, ' 5th-6th': 236274.78333333333, ' Prof-school': 174881.20179372196, ' Doctorate': 188997.93373493975, ' Preschool': 223331.6222222222, ' Masters': 179493.17137476458, ' 1st-4th': 229962.55434782608}
reference3 = {' Cambodia': 217386.27272727274, ' Cuba': 235760.64150943398, ' Haiti': 199416.8, ' Jamaica': 223457.44827586206, ' Peru': 241727.81818181818, ' South': 174124.23636363636, ' Dominican-Republic': 198773.32, ' Honduras': 260892.27272727274, ' Hong': 222628.5, ' Taiwan': 205364.3076923077, ' China': 196019.86666666667, ' Italy': 176954.59259259258, ' Nicaragua': 240250.77777777778, ' Ecuador': 176984.70588235295, ' Iran': 203568.1739130435, ' Hungary': 195122.11111111112, ' Philippines': 157109.8, ' United-States': 189216.2782888476, ' Vietnam': 175368.29166666666, ' Columbia': 200867.15384615384, ' India': 166323.86666666667, ' Germany': 192083.58415841585, ' Thailand': 207266.53333333333, ' Scotland': 160476.88888888888, ' France': 180897.45, ' Puerto-Rico': 205173.22471910113, ' Poland': 191764.83870967742, ' Laos': 205029.375, ' England': 187262.04285714286, ' Ireland': 149103.55, ' Trinadad&Tobago': 237394.83333333334, ' ?': 191485.90839694656, ' Holand-Netherlands': 27882.0, ' Canada': 151897.425, ' Japan': 192349.975, ' Outlying-US(Guam-USVI-etc)': 173387.0, ' Guatemala': 261568.5283018868, ' Portugal': 177874.4347826087, ' Greece': 165180.0, ' El-Salvador': 270796.6395348837, ' Mexico': 284158.3435897436, ' Yugoslavia': 209338.875}
plot('race', 'fnlwgt', 'avg', target1, reference1)
plot('education', 'fnlwgt', 'avg', target2, reference2)
#plot('native_country', 'fnlwgt', 'avg', target3, reference3)

target4 = {' Cambodia': 1062.235294117647, ' Haiti': 558.05, ' Cuba': 628.4, ' Jamaica': 997.3333333333334, ' Dominican-Republic': 119.15094339622641, ' Peru': 0.0, ' South': 1549.9166666666667, ' Honduras': 167.33333333333334, ' Hong': 751.2, ' Taiwan': 3135.4615384615386, ' China': 1702.2282608695652, ' Italy': 935.4230769230769, ' Nicaragua': 0.0, ' Ecuador': 335.2142857142857, ' Iran': 2025.0, ' Hungary': 746.8, ' Philippines': 2375.5882352941176, ' United-States': 1665.8104295887892, ' Vietnam': 746.8947368421053, ' Columbia': 231.65217391304347, ' India': 4311.066037735849, ' Germany': 1372.047619047619, ' Scotland': 431.5, ' Thailand': 486.53333333333336, ' France': 0.0, ' Puerto-Rico': 414.0842105263158, ' Poland': 733.1607142857143, ' England': 1794.3508771929824, ' Laos': 192.33333333333334, ' Ireland': 803.3529411764706, ' Trinadad&Tobago': 209.13333333333333, ' ?': 3073.040948275862, ' Canada': 1220.578431372549, ' Japan': 3182.7115384615386, ' Outlying-US(Guam-USVI-etc)': 0.0, ' Guatemala': 317.1142857142857, ' Portugal': 309.72727272727275, ' Greece': 982.8857142857142, ' El-Salvador': 850.7536231884058, ' Mexico': 467.45454545454544, ' Yugoslavia': 1183.4666666666667}
reference4 = {' Cambodia': 133.72727272727272, ' Cuba': 217.37735849056602, ' Haiti': 0.0, ' Jamaica': 80.94827586206897, ' Peru': 83.22727272727273, ' South': 1818.1636363636364, ' Dominican-Republic': 2066.48, ' Honduras': 0.0, ' Hong': 0.0, ' Taiwan': 168.30769230769232, ' China': 504.6333333333333, ' Italy': 400.5925925925926, ' Nicaragua': 251.62962962962962, ' Ecuador': 316.88235294117646, ' Iran': 653.0434782608696, ' Hungary': 205.33333333333334, ' Philippines': 330.024, ' United-States': 521.3280464041329, ' Vietnam': 492.3125, ' Columbia': 0.0, ' India': 570.7111111111111, ' Germany': 739.7920792079208, ' Thailand': 0.0, ' Scotland': 0.0, ' France': 793.2, ' Puerto-Rico': 251.30337078651687, ' Poland': 0.0, ' Laos': 0.0, ' England': 492.0571428571429, ' Ireland': 232.5, ' Trinadad&Tobago': 0.0, ' ?': 194.38931297709922, ' Canada': 1249.9875, ' Japan': 174.025, ' Outlying-US(Guam-USVI-etc)': 0.0, ' Guatemala': 69.32075471698113, ' Portugal': 0.0, ' Greece': 1502.857142857143, ' El-Salvador': 25.302325581395348, ' Mexico': 341.874358974359, ' Yugoslavia': 415.625}
target5 = {' Some-college': 988.0240572171651, ' Assoc-acdm': 977.694626474443, ' Bachelors': 2492.4878884826326, ' 11th': 353.0231124807396, ' 9th': 220.92307692307693, ' HS-grad': 788.515128968254, ' 12th': 437.3464912280702, ' 7th-8th': 332.94166666666666, ' 10th': 555.3579454253612, ' Assoc-voc': 1029.5646630236795, ' 5th-6th': 510.80547112462006, ' Prof-school': 12499.800327332243, ' Doctorate': 5736.441588785046, ' Preschool': 1583.2105263157894, ' Masters': 3334.7561128526645, ' 1st-4th': 152.93548387096774}
reference5 = {' Some-college': 244.65501277139208, ' Assoc-acdm': 326.7052505966587, ' Bachelors': 887.2175938613319, ' 11th': 120.43336199484092, ' 9th': 418.971671388102, ' HS-grad': 348.52396373056996, ' 12th': 86.997668997669, ' 7th-8th': 89.98028169014084, ' 10th': 134.10966057441254, ' Assoc-voc': 492.4579439252336, ' 5th-6th': 85.39444444444445, ' Prof-school': 5344.107623318386, ' Doctorate': 5705.409638554217, ' Preschool': 13.2, ' Masters': 1455.4661016949153, ' 1st-4th': 74.15217391304348}
target6 = {' Black': 920.4654483152484, ' Other': 1322.297435897436, ' Asian-Pac-Islander': 2260.6485507246375, ' White': 1689.0052307549877, ' Amer-Indian-Eskimo': 502.3553299492386}
reference6 = {' Black': 389.892978868439, ' Other': 669.8625592417062, ' Asian-Pac-Islander': 670.4645441389291, ' White': 519.5170395356913, ' Amer-Indian-Eskimo': 565.4029304029305}
plot('native_country', 'capital_gain', 'avg', target4, reference4)
plot('education', 'capital_gain', 'avg', target5, reference5)
plot('race', 'capital_gain', 'avg', target6, reference6)
"""
file = open('plot_data.txt', 'r')
count = 0
while True:
    a = file.readline()
    if not a:
        break
    m = file.readline()
    f = file.readline()
    print(a, m, f)
    print(type(a))
    target = dict(file.readline())
    reference = dict(file.readline())
    plot(a, m, f, target, reference, 'topk_{}'.format(count))
    count += 1