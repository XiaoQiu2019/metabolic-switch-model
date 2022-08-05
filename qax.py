#!/usr/bin/env python
# coding: UTF-8
# xq_05132022_v6
import numpy as np
import random
import math
import csv
from scipy.integrate import odeint
import multiprocessing as mp
#import matplotlib.pyplot as plt
#import time
import copy
def observe_data():
	## qa_gene
	time_point = [30,60,90,120,240,360,480]

	f2 = csv.reader(open("qa2.csv"))
	qa2a = []
	qa2b = []
	for row in f2:
		qa2a.append([row[1],row[2]])
	qa2b = qa2a[1:]	
	count = 0
	for i in range(len(qa2b)):
		if int(qa2b[i][0]) == 480:
			count+=1
	qa2c = [[] for i in range(len(time_point))]
	for i in range(len(qa2b)):
		if int(qa2b[i][0]) == 30:
			qa2c[0].append(float(qa2b[i][1]))
		if int(qa2b[i][0]) == 60:
			qa2c[1].append(float(qa2b[i][1]))
		if int(qa2b[i][0]) == 90:
			qa2c[2].append(float(qa2b[i][1]))
		if int(qa2b[i][0]) == 120:
			qa2c[3].append(float(qa2b[i][1]))
		if int(qa2b[i][0]) == 240:
			qa2c[4].append(float(qa2b[i][1]))
		if int(qa2b[i][0]) == 360:
			qa2c[5].append(float(qa2b[i][1]))
		if int(qa2b[i][0]) == 480:
			qa2c[6].append(float(qa2b[i][1]))
	qa2d = np.array(qa2c)

	f3 = csv.reader(open("qa3.csv"))
	qa3a = []
	qa3b = []
	for row in f3:
		qa3a.append([row[1],row[2]])
	qa3b = qa3a[1:]
	count = 0
	for i in range(len(qa3b)):
		if int(qa3b[i][0]) == 480:
			count+=1
	qa3c = [[] for i in range(len(time_point))]
	for i in range(len(qa3b)):
		if int(qa3b[i][0]) == 30:
			qa3c[0].append(float(qa3b[i][1]))
		if int(qa3b[i][0]) == 60:
			qa3c[1].append(float(qa3b[i][1]))
		if int(qa3b[i][0]) == 90:
			qa3c[2].append(float(qa3b[i][1]))
		if int(qa3b[i][0]) == 120:
			qa3c[3].append(float(qa3b[i][1]))
		if int(qa3b[i][0]) == 240:
			qa3c[4].append(float(qa3b[i][1]))
		if int(qa3b[i][0]) == 360:
			qa3c[5].append(float(qa3b[i][1]))
		if int(qa3b[i][0]) == 480:
			qa3c[6].append(float(qa3b[i][1]))
	qa3d = np.array(qa3c)

	f4 = csv.reader(open("qa4.csv"))
	qa4a = []
	qa4b = []
	for row in f4:
		qa4a.append([row[1],row[2]])
	qa4b = qa4a[1:]
	count = 0
	for i in range(len(qa4b)):
		if int(qa4b[i][0]) == 480:
			count+=1
	qa4c = [[] for i in range(len(time_point))]
	for i in range(len(qa4b)):
		if int(qa4b[i][0]) == 30:
			qa4c[0].append(float(qa4b[i][1]))
		if int(qa4b[i][0]) == 60:
			qa4c[1].append(float(qa4b[i][1]))
		if int(qa4b[i][0]) == 90:
			qa4c[2].append(float(qa4b[i][1]))
		if int(qa4b[i][0]) == 120:
			qa4c[3].append(float(qa4b[i][1]))
		if int(qa4b[i][0]) == 240:
			qa4c[4].append(float(qa4b[i][1]))
		if int(qa4b[i][0]) == 360:
			qa4c[5].append(float(qa4b[i][1]))
		if int(qa4b[i][0]) == 480:
			qa4c[6].append(float(qa4b[i][1]))
	qa4d = np.array(qa4c)

	fx = csv.reader(open("qax.csv"))
	qaxa = []
	qaxb = []
	for row in fx:
		qaxa.append([row[1],row[2]])
	qaxb = qaxa[1:]
	count = 0
	for i in range(len(qaxb)):
		if int(qaxb[i][0]) == 480:
			count+=1
	qaxc = [[] for i in range(len(time_point))]
	for i in range(len(qaxb)):
		if int(qaxb[i][0]) == 30:
			qaxc[0].append(float(qaxb[i][1]))
		if int(qaxb[i][0]) == 60:
			qaxc[1].append(float(qaxb[i][1]))
		if int(qaxb[i][0]) == 90:
			qaxc[2].append(float(qaxb[i][1]))
		if int(qaxb[i][0]) == 120:
			qaxc[3].append(float(qaxb[i][1]))
		if int(qaxb[i][0]) == 240:
			qaxc[4].append(float(qaxb[i][1]))
		if int(qaxb[i][0]) == 360:
			qaxc[5].append(float(qaxb[i][1]))
		if int(qaxb[i][0]) == 480:
			qaxc[6].append(float(qaxb[i][1]))
	qaxd = np.array(qaxc)

	fy = csv.reader(open("qay.csv"))
	qaya = []
	qayb = []
	for row in fy:
		qaya.append([row[1],row[2]])
	qayb = qaya[1:]
	count = 0
	for i in range(len(qayb)):
		if int(qayb[i][0]) == 480:
			count+=1
	qayc = [[] for i in range(len(time_point))]
	for i in range(len(qayb)):
		if int(qayb[i][0]) == 30:
			qayc[0].append(float(qayb[i][1]))
		if int(qayb[i][0]) == 60:
			qayc[1].append(float(qayb[i][1]))
		if int(qayb[i][0]) == 90:
			qayc[2].append(float(qayb[i][1]))
		if int(qayb[i][0]) == 120:
			qayc[3].append(float(qayb[i][1]))
		if int(qayb[i][0]) == 240:
			qayc[4].append(float(qayb[i][1]))
		if int(qayb[i][0]) == 360:
			qayc[5].append(float(qayb[i][1]))
		if int(qayb[i][0]) == 480:
			qayc[6].append(float(qayb[i][1]))
	qayd = np.array(qayc)

	ff = csv.reader(open("qa1f.csv"))
	qafa = []
	qafb = []
	for row in ff:
		qafa.append([row[1],row[2]])
	qafb = qafa[1:]
	count = 0
	for i in range(len(qafb)):
		if int(qafb[i][0]) == 480:
			count+=1
	qafc = [[] for i in range(len(time_point))]
	for i in range(len(qafb)):
		if int(qafb[i][0]) == 30:
			qafc[0].append(float(qafb[i][1]))
		if int(qafb[i][0]) == 60:
			qafc[1].append(float(qafb[i][1]))
		if int(qafb[i][0]) == 90:
			qafc[2].append(float(qafb[i][1]))
		if int(qafb[i][0]) == 120:
			qafc[3].append(float(qafb[i][1]))
		if int(qafb[i][0]) == 240:
			qafc[4].append(float(qafb[i][1]))
		if int(qafb[i][0]) == 360:
			qafc[5].append(float(qafb[i][1]))
		if int(qafb[i][0]) == 480:
			qafc[6].append(float(qafb[i][1]))
	qafd = np.array(qafc)

	fs = csv.reader(open("qa1s.csv"))
	qasa = []
	qasb = []
	for row in fs:
		qasa.append([row[1],row[2]])
	qasb = qasa[1:]
	count = 0
	for i in range(len(qasb)):
		if int(qasb[i][0]) == 480:
			count+=1
	qasc = [[] for i in range(len(time_point))]
	for i in range(len(qasb)):
		if int(qasb[i][0]) == 30:
			qasc[0].append(float(qasb[i][1]))
		if int(qasb[i][0]) == 60:
			qasc[1].append(float(qasb[i][1]))
		if int(qasb[i][0]) == 90:
			qasc[2].append(float(qasb[i][1]))
		if int(qasb[i][0]) == 120:
			qasc[3].append(float(qasb[i][1]))
		if int(qasb[i][0]) == 240:
			qasc[4].append(float(qasb[i][1]))
		if int(qasb[i][0]) == 360:
			qasc[5].append(float(qasb[i][1]))
		if int(qasb[i][0]) == 480:
			qasc[6].append(float(qasb[i][1]))
	qasd = np.array(qasc)
	qa_gene = [qa2d,qa3d,qa4d,qaxd,qayd,qafd,qasd]


	#species
	ala = csv.reader(open("alanine_data.csv"))
	ala1 = zip(*ala)
	ala2 = []
	for row in ala1:
		b = [float(item) for item in row]
		ala2.append(b)
	alanine = [ala2[5],ala2[6],ala2[1],ala2[9]]

	etha = csv.reader(open("ethanol_data.csv"))
	etha1 = zip(*etha)
	etha2 = []
	for row in etha1:
		b = [float(item) for item in row]
		etha2.append(b)
	ethanol = [etha2[5],etha2[6],etha2[1],etha2[9]]

	fum = csv.reader(open("fumarate_data.csv"))
	fum1 = zip(*fum)
	fum2 = []
	for row in fum1:
		b = [float(item) for item in row]
		fum2.append(b)
	fumarate = [fum2[5],fum2[6],fum2[1],fum2[9]]

	glu = csv.reader(open("glucose_data.csv"))
	glu1 = zip(*glu)
	glu2 = []
	for row in glu1:
		b = [float(item) for item in row]
		glu2.append(b)
	glucose = [glu2[5],glu2[6],glu2[1],glu2[9]]

	hg = csv.reader(open("HGA_data.csv"))
	hg1 = zip(*hg)
	hg2 = []
	for row in hg1:
		b = [float(item) for item in row]
		hg2.append(b)
	HGA = [hg2[5],hg2[6],hg2[1],hg2[9]]

	phe = csv.reader(open("phenylalanine_data.csv"))
	phe1 = zip(*phe)
	phe2 = []
	for row in phe1:
		b = [float(item) for item in row]
		phe2.append(b)
	phenylalanine = [phe2[5],phe2[6],phe2[1],phe2[9]]

	tyr = csv.reader(open("tyrosine_data.csv"))
	tyr1 = zip(*tyr)
	tyr2 = []
	for row in tyr1:
		b = [float(item) for item in row]
		tyr2.append(b)
	tyrosine = [tyr2[5],tyr2[6],tyr2[1],tyr2[9]]

	q = csv.reader(open("qa_data.csv"))
	q1 = zip(*q)
	q2 = []
	for row in q1:
		b = [float(item) for item in row]
		q2.append(b)
	qa = [q2[5],q2[6],q2[1],q2[9]]

	t = csv.reader(open("time_data.csv"))
	t1 = zip(*t)
	t2 = []
	for row in t1:
		b = [float(item) for item in row]
		t2.append(b)
	time = [t2[5],t2[6],t2[1],t2[9]]
	return qa_gene,time,qa,alanine,ethanol,fumarate,glucose,phenylalanine,tyrosine,HGA

def init_parameters():
	theta = {}
	# rate coefficients	 
	theta['n'] = 1
	theta['m'] = 2
	theta['gammas'] = 45.85839872
	theta['P1'] = 4.92e-19
	theta['P2'] = 5.27e-16
	theta['Af'] = 0.525402573
	theta['Afbar'] = 8.069026736
	theta['Bf'] = 8.168365513
	theta['Sf'] = 24.1415877
	theta['Sfw'] = 1.17e-22
	theta['Lf'] = 1.285934853
	theta['As'] = 0.16513093
	theta['Asbar'] = 3.56e-20
	theta['Bs'] = 2.13e-17
	theta['Ss'] = 18.42648529
	theta['Ssw'] = 2.92e-21
	theta['Ls'] = 2.888878037
	theta['Ay'] = 0.724755478
	theta['A3'] = 6.26e-200
	theta['A2'] = 1.11e-22
	theta['A4'] = 1.97e-21
	theta['Ax'] = 1.28e-20
	theta['Aybar'] = 1.16e-23
	theta['A3bar'] = 0.530036393
	theta['A2bar'] = 0.732707409
	theta['A4bar'] = 4.722622609
	theta['Axbar'] = 4.880081557
	theta['By'] = 24.84684176
	theta['B3'] = 2.80434364
	theta['B2'] = 3.286385779
	theta['B4'] = 1.696658398
	theta['Bx'] = 16.62191435
	theta['Sy'] = 62.03952631
	theta['S3'] = 1488.528112
	theta['S2'] = 17.62570991
	theta['S4'] = 221.2886554
	theta['Sx'] = 264.4651366
	theta['Syw'] = 5.14e-21
	theta['S3w'] = 6.37e-21
	theta['S2w'] = 2.79e-17
	theta['S4w'] = 2.52e-22
	theta['Sxw'] = 1.47e-20
	theta['Ly'] = 3.44e-20
	theta['L3'] = 3.26e-20
	theta['L2'] = 2.57e-19
	theta['L4'] = 1.76e-21
	theta['Lx'] = 1.23e-21
	theta['D1'] = 2.307895063995687
	theta['D2'] = 3.673355888694578
	theta['D3'] = 1.2934975306172002e-31
	theta['D4'] = 6.837240515677334
	theta['D6'] = 2.321196467034394
	theta['D7'] = 1.1380415594648774e-31
	theta['D8'] = 77.9813484883717
	theta['D9'] = 9.359336344759207e-39
	theta['D10'] = 2.0278723542656527
	theta['D11'] = 6.77757616974399e-33
	theta['D12'] = 2.2349004317513343
	theta['D13'] = 1.8029243686966928e-36
	theta['D14'] = 4.327971816695225
	theta['D15'] = 1.5700689494098467e-33
	theta['gammas2'] = 0.00398379481110053
	theta['eta'] = 1.3403687106492758e-18
	theta['etaext'] = 3.898956216938551e-23
	theta['adh'] = 72.46905056104566
	theta['AN'] = 5.068856231379223e-20
	theta['ANbar'] = 1.187589263393685e-22
	theta['BN'] = 2.2619736661267068e-23
	theta['SN'] = 2.8157883842171522e-11
	theta['SNw'] = 8.578069102549092e-27
	theta['LN'] = 6.744261529899068e-26
	theta['C1'] = 1.0600051452776248e-14
	theta['C2'] = 1.3332106897808494e-15
	theta['C3'] = 7.325368257484657e-14
	theta['C4'] = 0.009380970078423255
	theta['C5'] = 7.819222016246585e-23
	theta['C6'] = 5.93319850529006e-19
	theta['C7'] = 2.942519412249683e-26
	theta['C8'] = 0.00011176109134949621
	theta['C9'] = 8.917784892524603e-32
	theta['C10'] = 1.0613306407498765e-08
	theta['C11'] = 8.122648966357278e-14
	theta['C12'] = 1.984452935001935e-10
	theta['C13'] = 0.00026257378621950876
	theta['C14'] = 0.006890920337829732
	theta['C15'] = 0.02738123473531944
	theta['C16'] = 0.00305254590140134
	theta['C17'] = 2.4127647251545105e-06
	theta['C18'] = 1.5666321821550106e-09
	theta['C19'] = 0.060354518555970973
	theta['C20'] = 1.246809599092961e-15
	theta['C21'] = 0.7236980252698452
	theta['C22'] = 0.0006264359888782566
	theta['C23'] = 2.466773278544072e-08
	theta['C24'] = 0.16258481877487949
	theta['C25'] = 0.014850927767924627
	theta['C26'] = 0.2457193141744379
	theta['C27'] = 2.049043640315709e-05
	theta['C28'] = 1.9233753860664872e-15
	theta['C29'] = 7.070858969468158e-22
	theta['C30'] = 0.03603216647802292
	theta['C31'] = 0.6719026259582499
	theta['C32'] = 9.528928158009826e-18
	theta['C33'] = 0.034763464786497764
	theta['C34'] = 3.500940536862122e-19
	theta['C35'] = 0.0008270625479137297
	theta['C36'] = 1.7921702792001565e-19
	theta['C37'] = 0.0013774673633126686
	theta['C38'] = 1.7159367090995547e-14
	theta['C39'] = 3.696239064771796e-23
	theta['C40'] = 0.012507193902594931
	theta['C41'] = 0.0005866547473151924
	theta['C42'] = 0.0554740624777978
	theta['T1'] = 0.07596601590070746
	theta['T2'] = 0.05504829
	theta['T3'] = 0.06020704152400431
	theta['T4'] = 0.0020845996754157376
	theta['T5'] = 0.0
	theta['T6'] = 3.668843232815721
	theta['T7'] = 0.004697507433784131
	theta['T8'] = 0.0
	theta['T9'] = 0.0004530537032829862
	theta['T10'] = 0.008911539634573917
	theta['R1'] = 5.656593355946411e-17
	theta['R2'] = 0.004046030097302273
	theta['R3'] = 0.40377625337608364
	theta['R4'] = 0.0005995734533390774
	theta['R5'] = 0.0014980668187597696
	theta['R6'] = 3.16090252797501
	theta['R7'] = 8.499484809544501e-14
	theta['R8'] = 1.2687095417728334e-23
	theta['R9'] = 0.00829297
	theta['R10'] = 0.008587340314853305
	theta['R11'] = 0.0748943960116288
	theta['D5'] = 6.130304886192471e-13
	theta['D16'] = 0.03052380932028004
	theta['D17'] = 1.407620393259236e-22
	theta['D18'] = 3.560404398595148e-18
	theta['D19'] = 4.0783796915710256e-13
	theta['D20'] = 9.804652035491286e-16
	theta['D21'] = 6.918477665445141e-20
	theta['e1'] = 2.2474903748429213e-11
	theta['e2'] = 6.830846546752428e-05
	theta['e3'] = 4.754039858143949e-08
	theta['e4'] = 3.0037674973481667e-22
	theta['e5'] = 199.26478838525696
	theta['e6'] = 13.624213755752907
	theta['e7'] = 21.602285012133137
	theta['e8'] = 5764.741226057514
	theta['e9'] = 109.52952574890764
	theta['e10'] = 3.0457314346413405e-15
	theta['e11'] = 7521.669101245502
	theta['e12'] = 35.487753544104685
	theta['e13'] = 259.1233598983401
	theta['e14'] = 2.70808261880721e-12
	theta['e15'] = 46.401085261219215
	theta['e16'] = 3018.8165775244147
	theta['e17'] = 44505.53196557061
	theta['e18'] = 6.159402704866467
	theta['e19'] = 1.0143530148464069e-19
	theta['e20'] = 565.7516615867132
	theta['e21'] = 8.975283187820482e-18
	theta['e22'] = 16.381696333327323
	theta['e23'] = 5.316092756196492e-10
	theta['e24'] = 31.55559264951068
	theta['e25'] = 1576.6139528984756
	theta['e26'] = 5.196428722362481
	theta['e27'] = 102.75328756631261
	theta['e28'] = 1.525199482189804e-12
	theta['e29'] = 384.94565602230057
	theta['e30'] = 164.9375291640907
	theta['e31'] = 60.72756583369043
	theta['e32'] = 67.36872107429639
	theta['e33'] = 73.60227
	theta['e34'] = 38.89937290280141
	theta['e35'] = 7270.526674171013
	theta['e36'] = 6.899364201797211e-18
	theta['e37'] = 16.98498107229618
	theta['e38'] = 1.5691738351811955e-20
	theta['e39'] = 324.05804032659233
	theta['e40'] = 1.8207096245307361
	theta['e41'] = 2.0048413374333015e-13
	theta['e42'] = 4.25822406647511e-10
	theta['e43'] = 3.506776871098764e-14
	theta['e44'] = 3.8110950878485963
	theta['e45'] = 4.543687723447367e-15
	theta['e46'] = 7.841126973602304
	theta['e47'] = 105.2463
	theta['e48'] = 7.279670274452679e-14
	theta['e49'] = 1.0135746345656136
	theta['e50'] = 4.165320965904298e-13
	theta['e51'] = 1.0371246628431065e-15
	theta['e52'] = 3.3999753359364706
	theta['e53'] = 0.004650236895765062
	theta['e54'] = 1747.8961785989798
	theta['e55'] = 340.84360148753325
	theta['e56'] = 1.7831803873948748
	theta['C1w'] = 0.34058688
	theta['C2w'] = 0.5416716
	theta['C3w'] = 0.012111164
	theta['C4w'] = 0.33118192
	theta['C5w'] = 0.007880168
	theta['C6w'] = 0.002873816
	theta['C7w'] = 0.00401462
	theta['C8w'] = 119.3652
	theta['C9w'] = 0.0025851844
	theta['C10w'] = 0.05961612
	theta['C11w'] = 0.05156132
	theta['C12w'] = 0.30477344
	theta['C13w'] = 0.015721116
	theta['C14w'] = 0.07452604
	theta['C15w'] = 0.12132348
	theta['C16w'] = 0.026362976
	theta['C17w'] = 0.0011367
	theta['C18w'] = 0.022745808
	theta['C19w'] = 0.022531808
	theta['C20w'] = 0.005326164
	theta['C21w'] = 1.7833948
	theta['C22w'] = 0.0030954552
	theta['C23w'] = 0.00076113
	theta['C24w'] = 0.4764604
	theta['C25w'] = 0.0012042028
	theta['C26w'] = 8.450248
	theta['C27w'] = 0.0002571696
	theta['C28w'] = 1.6515412
	theta['C29w'] = 0.08191136
	theta['C30w'] = 0.14405616
	theta['C31w'] = 0.016241488
	theta['C32w'] = 0.09276416
	theta['C33w'] = 0.04765252
	theta['C34w'] = 19.83458
	theta['C35w'] = 0.08481912
	theta['C36w'] = 0.0007442868
	theta['C37w'] = 0.004486004
	theta['C38w'] = 0.033248244
	theta['C39w'] = 0.01068798
	theta['C40w'] = 0.1120156
	theta['C41w'] = 0.038424264
	theta['C42w'] = 0.13197068
	theta['T1w'] = 0.180095
	theta['T2w'] = 0.22019316
	theta['T3w'] = 0.0892032
	theta['T4w'] = 0.16280024
	theta['T5w'] = 0.0
	theta['T6w'] = 15.28722
	theta['T7w'] = 0.03647632
	theta['T8w'] = 0.0
	theta['T9w'] = 0.011561768
	theta['T10w'] = 0.020020272
	theta['R2w'] = 0.018890784
	theta['R3w'] = 1.0576436
	theta['R4w'] = 0.007732212
	theta['R5w'] = 0.0017293032
	theta['R6w'] = 12.76002
	theta['R7w'] = 0.0039053332
	theta['R8w'] = 0.0004642692
	theta['R9w'] = 0.03317188
	theta['R10w'] = 0.03730436
	theta['R11w'] = 0.25499764

	theta_key = ['gammas2','eta','etaext',
				'adh','AN','ANbar','BN',
				'SN','SNw','LN','C1','C2','C3','C4','C5','C6',
				'C7','C8','C9','C10','C11','C12','C13','C14',
				'C15','C16','C17','C18','C19','C20','C21',
				'C22','C23','C24','C25','C26','C27','C28',
				'C29','C30','C31','C32','C33','C34','C35','C36',
				'C37','C38','C39','C40','C41','C42',
				'R1','R2','R3','R4','R5','R6','R7','R8','R9',
				'R10','R11','T1','T2','T3','T4','T5',
				'T6','T7','T8','T9','T10','D1','D2',
				'D3','D4','D6','D7','D8','D9','D10','D11',
				'D12','D13','D14','D15','D5','D16','D17',
				'D18','D19','D20','D21','e1','e2','e3','e4',
				'e5','e6','e7','e8','e9','e10','e11','e12',
				'e13','e14','e15','e16','e17','e18','e19',
				'e20','e21','e22','e23','e24','e25','e26',
				'e27','e28','e29','e30','e31','e32','e33',
				'e34','e35','e36','e37','e38','e39','e40',
				'e41','e42','e43','e44','e45','e46','e47',
				'e48','e49','e50','e51','e52','e53','e54','e55','e56']
	return theta,theta_key

def init_species0():
	N=[0,	
	1283.211681172949,	3.708972712708936e-158,	1.541067069324658e-141,	8.496494530806277e-88,	
	286.3605545080295,	5.159421797980635e-160,	825.6859226271874,	29865.800183592793,	
	1.7628985675247722e-72,	
	216.0277026305384,	9.37476547852068e-153,	8.076384872739322e-131,	5.387289971758247e-84,	
	454.7178316180131,	12.635602996670173,	5.908733910163608e-159,	2.8281252488306145e-85,	
	1514.6905022546377,	3.0022126334885404e-139,	605.3831772466783,	1.2464831317370901e-94,	
	523.7501167268347,	7.253645085643314e-138,	655.6468947379253,	9.991362070662777e-68,	
	0.0,	0.0,	0.0,	0.0,	
	1.4549832470527927e-24,	4.382815002090942e-28,	9.797846386454583e-17,	5.045055714578352e-10,	
	3.375913069038617e-16,	15.628278217891419,	1.960905827854063e-30,	8.866499494409277e-15,	2.2470192463934697e-22,	1.8662569020111465e-30,	1.268700933574343e-30,	1.933094303796933e-33,	0.05447502935784321,	0.021255499203313835,	4.130598469531738e-25,	2.394826064702598e-22,	1.7927952292581285e-26,	8.876220797164126e-29,	2.543163005490403e-28,	0.3531245945163675,	2.735115236535657e-09,	0.4577703234470519,	3.716582949644335e-30,	2.2441258398174056e-20,	1.8094418683686628e-25,	1.6172371665454334e-16,	3.792388800807894e-23,	9.52112349103317e-29,	0.7834491850861367,	1.0653800746500813e-31,	15.640859151722056,	1.0267688031389432e-05,	1.2635576144107748e-22,	6.454788589830524e-29,	2.1943705577047317e-31,	3.2675396659835936e-28,	6.701724742579041e-22,	0.0008125989347918587,	4.6147455714983036e-32,	1.7585815865151466e-22,	7.647737084633258e-26,	3.602052651254416,	4.0723964925463434e-35,	9.85627861787093e-06,	1.0705633258596526e-24,	0.2047798411190387,	1.0873872010797443e-27,	8.83483995514423e-26,	1.8305347770832743e-18,	0.00012917913292733975,	1.1933569515629054e-25,	7.18766726655992e-36,	0.00046040755770823596,	0.00033773914042842864,	7.986777599215332e-34,	3.8838303500758525e-25

];
	return N

def init_species1():
	N=[0,	
	1283.211681172949,	3.708972712708936e-158,	1.541067069324658e-141,	8.496494530806277e-88,	
	286.3605545080295,	5.159421797980635e-160,	825.6859226271874,	29865.800183592793,	
	1.7628985675247722e-72,	
	216.0277026305384,	9.37476547852068e-153,	8.076384872739322e-131,	5.387289971758247e-84,	
	454.7178316180131,	12.635602996670173,	5.908733910163608e-159,	2.8281252488306145e-85,	
	1514.6905022546377,	3.0022126334885404e-139,	605.3831772466783,	1.2464831317370901e-94,	
	523.7501167268347,	7.253645085643314e-138,	655.6468947379253,	9.991362070662777e-68,	
	222.87538572954787,	1.4898300067485722e-151,	2.66428631162394e-160,	3.929792270193981e-75,	
	1.0982254072232773e-24,	1.2970575834850262e-29,	6.347882565155009e-32,	3.2769500246658158e-15,	
	7.271035520943009e-22,	15.633299015064025,	1.0232595124656561e-23,	5.0770021433681905e-25,	2.3782531910819327e-24,	3.419209256728429e-30,	4.933816702039063e-17,	1.4324987503271385e-25,	1.582041160834811e-22,	6.937516809910712e-24,	2.5535532158735423e-39,	2.1552963239852226e-30,	1.4202510714736332e-20,	7.309782970614017e-29,	1.1705452001368278e-24,	0.3480532735516375,	6.0348451431332515e-24,	1.0146446002687065e-05,	2.3507844829750166e-32,	1.3222592813857895e-25,	9.470548068350052e-32,	5.289096807453013e-14,	3.98174308767438e-33,	3.43149535491493e-27,	1.1235133005475135,	140.28154783922454,	15.414940408332749,	1.0176372273040977e-05,	6.914386647405245e-26,	8.885475024620644e-33,	6.110649373288063e-28,	3.1708520256229455e-33,	4.5752669601466485e-31,	1.2193180495209202e-30,	1.6846059672794526e-30,	6.601444161981117e-30,	1.0960840427399643e-20,	0.5338723573967938,	1.0892429213257463e-24,	0.31024085399680995,	1.011062706949063e-28,	0.1800027272357247,	1.7660475469769375e-17,	6.363579720243122e-17,	8.252484479579664e-18,	10.949582647216086,	3.026094818492812e-23,	4.029896918337229e-25,	1.6779969551831162e-20,	2.3828087586377413e-32,	5.859324769634375e-19,	0.0004581898984255566

];
	return N

def init_species2():
	N=[0,	
	1283.211681172949,	3.708972712708936e-158,	1.541067069324658e-141,	8.496494530806277e-88,	
	286.3605545080295,	5.159421797980635e-160,	825.6859226271874,	29865.800183592793,	
	1.7628985675247722e-72,	
	216.0277026305384,	9.37476547852068e-153,	8.076384872739322e-131,	5.387289971758247e-84,	
	454.7178316180131,	12.635602996670173,	5.908733910163608e-159,	2.8281252488306145e-85,	
	1514.6905022546377,	3.0022126334885404e-139,	605.3831772466783,	1.2464831317370901e-94,	
	523.7501167268347,	7.253645085643314e-138,	655.6468947379253,	9.991362070662777e-68,	
	0.0,	0.0,	0.0,	0.0,	
	1.1975939374906526e-26,	2.6766137032900608e-21,	2.9111983437955614e-27,	150.79846619361447,	
	1.6858034224153427e-17,	15.573745082232043,	4.4229606257764824e-32,	1.968314770082436e-24,	5.331354600917116e-24,	9.398229027996429e-25,	1.0695975344715423,	3.828519619715091e-24,	6.38774935293297e-27,	2.5267689118794136e-31,	1.0642090504135543e-26,	1.4839597297785046e-25,	3.768033869598971e-23,	1.2083337978829702e-35,	3.5809772909383946e-31,	0.463470507528839,	3.2443972334853792e-09,	0.5832785901249113,	1.0560754260202862e-27,	9.186234989305353e-25,	2.691739114403912e-23,	3.1396988386003564,	4.458936455599532e-26,	4.686159709284195e-12,	3.048705899319824,	37.8260057757607,	21.76793550913047,	1.0103318936786596e-05,	2.9353081669423024e-19,	1.826382988858537e-24,	1.3815010814599853e-22,	1.819704121638245e-29,	1.5148404350446143e-24,	5.318819832195329e-21,	3.383450189057311e-28,	6.608131213616102e-29,	1.849407939815551e-23,	6.105254737350151e-23,	6.4527485997001425e-24,	1.015317912275055e-05,	4.26972494635592e-28,	0.2148552648169727,	5.281329276571568e-16,	2.277648049484877e-16,	6.454358233404625e-25,	0.0001315588193123599,	6.260213906677443e-28,	2.2667702654646e-31,	3.0166768790729484e-29,	1.141422276797736e-31,	2.271455372150379e-31,	0.0004673549816980831

];
	return N

def init_species3():
	N=[0,	
	1283.211681172949,	3.708972712708936e-158,	1.541067069324658e-141,	8.496494530806277e-88,	
	286.3605545080295,	5.159421797980635e-160,	825.6859226271874,	29865.800183592793,	
	1.7628985675247722e-72,	
	216.0277026305384,	9.37476547852068e-153,	8.076384872739322e-131,	5.387289971758247e-84,	
	454.7178316180131,	12.635602996670173,	5.908733910163608e-159,	2.8281252488306145e-85,	
	1514.6905022546377,	3.0022126334885404e-139,	605.3831772466783,	1.2464831317370901e-94,	
	523.7501167268347,	7.253645085643314e-138,	655.6468947379253,	9.991362070662777e-68,	
	222.87538572954787,	1.4898300067485722e-151,	2.66428631162394e-160,	3.929792270193981e-75,
	3.4510799642733516e-16,	2.4078034228119013e-25,	4.5936773435855307e-35,	1.7193320864972742e-12,	
	2.2541109931435856e-18,	15.60915862,	3.470635938798875e-18,	2.2713092726106245e-26,	3.2331068044902593e-13,	7.806685762676864e-24,	1.139588669310019e-22,	284.87141005773617,	3.224776655757159e-23,	2.6915347935264266e-22,	6.916500227930341e-28,	9.75674787410462e-25,	1.7158603460693045e-18,	9.894869828810851e-29,	4.668670993009455e-35,	0.44480210260555253,	1.4412817809138988e-32,	9.985659734512492e-06,	1.2498314548523134e-18,	9.283817164602258e-26,	1.7186740010878696e-15,	7.456999573739599e-17,	7.980670077930025e-25,	2.841791825551729e-25,	3.4353705435771436,	3.1809217932033847e-07,	18.208809916572278,	0.0664581088980408,	1.9604772910718952e-20,	7.789996230491702e-32,	2.6079735725182516e-22,	1.1431079572154868e-18,	3.434692784036606e-25,	9.188562059146971e-40,	220.98039426909767,	9.400369820671652e-25,	1.2696462634167752e-22,	4.4174784952215564e-17,	1.2352926973552204e-23,	9.264845095065033e-06,	1.415274469387453e-24,	0.28420834555671504,	1.7298002654594832e-16,	4.707053694338238e-31,	7.702890171811727e-27,	0.00014622070522304114,	8.785949910584174e-31,	7.638922692939291e-17,	5.323774005551649e-26,	1.5587643658194696e-25,	8.869266774831844e-26,	3.761980951401283e-29

];
	return N

def ode_fun(N,t,theta):
	dNdt = [0,
	-theta['Bf'] * N[1] * N[4] * N[35]/(1+theta['gammas']*N[8]**theta['n'])- theta['Af'] * N[1] + theta['Afbar'] * N[2], 
	theta['Bf'] * N[1] * N[4] * N[35]/(1+theta['gammas']*N[8]**theta['n'])+ theta['Af'] * N[1] - theta['Afbar'] * N[2],
	-theta['D1'] * N[3] + theta['Sfw'] * N[1] + theta['Sf'] * N[2],
	theta['Lf'] * N[3] - theta['D2'] * N[4] - theta['P1'] * N[4] * N[8] * N[73] + theta['P2'] * N[9] * N[35],
   
	-theta['Bs'] * N[5] * N[4] * N[35]/(1+theta['gammas']*N[8]**theta['n']) - theta['As'] * N[5] + theta['Asbar'] * N[6],
	theta['Bs'] * N[5] * N[4] * N[35]/(1+theta['gammas']*N[8]**theta['n']) + theta['As'] * N[5] - theta['Asbar'] * N[6],
	-theta['D3'] * N[7] + theta['Ssw'] * N[5] + theta['Ss'] * N[6],
	theta['Ls'] * N[7] - theta['D4'] * N[8] + theta['P2'] * N[9] * N[35] - theta['P1'] * N[4] * N[8] * N[73],
 
	- theta['P2'] * N[9] * N[35] + theta['P1'] * N[4] * N[8] * N[73],

	-theta['By'] * N[10] * N[4] * N[35]/(1+theta['gammas']*N[8]**theta['n']) - theta['Ay'] * N[10] + theta['Aybar'] * N[11],
	theta['By'] * N[10] * N[4] * N[35]/(1+theta['gammas']*N[8]**theta['n']) + theta['Ay'] * N[10] - theta['Aybar'] * N[11],
	theta['Syw'] * N[10] - theta['D6'] * N[12] + theta['Sy'] * N[11] ,
	theta['Ly'] * N[12] - theta['D7'] * N[13],
   
	-theta['B3'] * N[14] * N[4] * N[35]/(1+theta['gammas']*N[8]**theta['n']) - theta['A3'] * N[14] + theta['A3bar'] * N[15],
	theta['B3'] * N[14] * N[4] * N[35]/(1+theta['gammas']*N[8]**theta['n']) + theta['A3'] * N[14] - theta['A3bar'] * N[15],
	theta['S3w'] * N[14] - theta['D8'] * N[16] + theta['S3'] * N[15] ,
	theta['L3'] * N[16] - theta['D9'] * N[17],

	-theta['B2'] * N[18] * N[4] * N[35]/(1+theta['gammas']*N[8]**theta['n']) - theta['A2'] * N[18] + theta['A2bar'] * N[19],
	theta['B2'] * N[18] * N[4] * N[35]/(1+theta['gammas']*N[8]**theta['n']) + theta['A2'] * N[18] - theta['A2bar'] * N[19],
	theta['S2w'] * N[18] - theta['D10'] * N[20] + theta['S2'] * N[19] ,
	theta['L2'] * N[20] - theta['D11'] * N[21],

	-theta['B4'] * N[22] * N[4] * N[35]/(1+theta['gammas']*N[8]**theta['n']) - theta['A4'] * N[22] + theta['A4bar'] * N[23],
	theta['B4'] * N[22] * N[4] * N[35]/(1+theta['gammas']*N[8]**theta['n']) + theta['A4'] * N[22] - theta['A4bar'] * N[23],
	theta['S4w'] * N[22] - theta['D12'] * N[24] + theta['S4'] * N[23] ,
	theta['L4'] * N[24] - theta['D13'] * N[25],

	-theta['Bx'] * N[26] * N[4] * N[35]/(1+theta['gammas']*N[8]**theta['n']) - theta['Ax'] * N[26] + theta['Axbar'] * N[27],
	theta['Bx'] * N[26] * N[4] * N[35]/(1+theta['gammas']*N[8]**theta['n']) + theta['Ax'] * N[26] - theta['Axbar'] * N[27],
	theta['Sxw'] * N[26] - theta['D14'] * N[28] + theta['Sx'] * N[27] ,
	theta['Lx'] * N[28] - theta['D15'] * N[29],

	-theta['BN'] * N[30] * N[4]*N[35]/[1+theta['gammas']*N[8]**theta['n']] - theta['AN'] * N[30] + theta['ANbar'] * N[31],
	theta['BN'] * N[30] * N[4]*N[35]/[1+theta['gammas']*N[8]**theta['n']] + theta['AN'] * N[30] - theta['ANbar'] * N[31],
	theta['SNw'] * N[30] - theta['D5'] * N[32] + theta['SN'] * N[31],
	theta['LN'] * N[32] - theta['D20'] * N[33] - theta['R1']*N[54]*N[33],
	#pathway
	-theta['C7']*N[13]*N[34]/[theta['C7w']+N[34]],#34

	-theta['D16']*N[35]+theta['C7']*N[13]*N[34]/[theta['C7w']+N[34]]-theta['C6']*N[17]*N[35]/[theta['C6w']+N[35]],#35

	theta['C6']*N[17]*N[35]/[theta['C6w']+N[35]]+theta['C1']*N[72]*theta['e1']/[theta['C1w']+N[72]]-theta['C8']*N[36]*N[21]/[theta['C8w']+N[36]],#36

	theta['C8']*N[36]*N[21]/[theta['C8w']+N[36]]-theta['C9']*N[25]*N[37]/[theta['C9w']+N[37]]-theta['C12']*N[37]*theta['e2']/[theta['C12w']+N[37]],#37

	theta['C9']*N[25]*N[37]/[theta['C9w']+N[37]]-theta['C10']*N[38]*theta['e3']/[theta['C10w']+N[38]],#38

	theta['C42'] * N[85] * theta['e56']/[theta['C42w'] + N[85]] -theta['C11']*N[39]*theta['e4']/[theta['C11w']\
	+N[39]]-theta['C33']*N[39]*theta['e46']/[theta['C33w']+N[39]],#39
	
	theta['C12']*N[37]*theta['e2']/[theta['C12w']+N[37]]-theta['C13']*N[40]*theta['e5']/[theta['C13w']+N[40]],#40
	
	theta['C13']*N[40]*theta['e5']/[theta['C13w']+N[40]]-theta['C14']*N[41]*theta['e6']/[theta['C14w']+N[41]],#41
	
	theta['C14']*N[41]*theta['e6']/[theta['C14w']+N[41]]-theta['C15']*N[42]*theta['e7']/[theta['C15w']+N[42]],#42
	
	theta['C15']*N[42]*theta['e7']/[theta['C15w']+N[42]]-theta['C16']*N[43]*theta['e8']/[theta['C16w']+N[43]]\
	-theta['C17']*N[43]*theta['e9']/[theta['C17w']+N[43]],#43
	
	theta['C17']*N[43]*theta['e9']/[theta['C17w']+N[43]]-theta['C18']*N[44]*theta['e10']/[theta['C18w']+N[44]]\
	-theta['C23']*N[44]*theta['e11']/[theta['C23w']+N[44]],#44
	
	theta['C18']*N[44]*theta['e10']/[theta['C18w']+N[44]],#45
	
	theta['C16']*N[43]*theta['e8']/[theta['C16w']+N[43]]-theta['C19']*N[46]*theta['e12']/[theta['C19w']+N[46]]\
	-theta['C24']*N[46]*theta['e13']/[theta['C24w']+N[46]],#46
	
	theta['C19']*N[46]*theta['e12']/[theta['C19w']+N[46]]-theta['C20']*N[47]*theta['e14']/[theta['C20w']+N[47]]\
	-theta['C21']*N[47]*theta['e15']/[theta['C21w']+N[47]]+theta['C22']*N[49]*theta['e16']/[theta['C22w']+N[49]],#47
	
	theta['C20']*N[47]*theta['e14']/[theta['C20w']+N[47]],#48
	
	theta['C21']*N[47]*theta['e15']/[theta['C21w']+N[47]]+theta['C23']*N[44]*theta['e11']/[theta['C23w']+N[44]]\
	-theta['C22']*N[49]*theta['e16']/[theta['C22w']+N[49]],#49
	
	theta['C24']*N[46]*theta['e13']/[theta['C24w']+N[46]]-theta['C25']*N[50]*theta['e17']/[theta['C25w']+N[50]]\
	-theta['C26']*N[50]*theta['e18']/[theta['C26w']+N[50]]-theta['C39']*N[50]*theta['e51']/[theta['C39w']+N[50]],#50
	
	theta['C26']*N[50]*theta['e18']/[theta['C26w']+N[50]]-theta['C37']*N[51]*theta['e53']/[theta['C37w']+N[51]],#51
	
	theta['C27']*theta['e52']*N[82]/[theta['C27w']+N[82]]-theta['C28']*N[52]*theta['e21']/[theta['C28w']+N[52]],#52
	
	theta['C11']*N[39]*theta['e4']/[theta['C11w']+N[39]]+theta['C28']*N[52]*theta['e21']/[theta['C28w']+N[52]]\
	+theta['R6']*N[56]*theta['e22']/[theta['R6w']+N[56]]+theta['R7']*N[57]*theta['e23']/[theta['R7w']+N[57]]\
	-theta['T7']*N[53]*N[69]*theta['e24']/[theta['T7w']+N[53]*N[69]]-theta['T3']*N[63]*N[53]*theta['e34']/[theta['T3w']\
	+N[63]*N[53]]-theta['R11']*N[53]*theta['e20']/[theta['R11w']+N[53]],#53
	
	theta['C29']*N[80]*theta['e19']/[theta['C29w']+N[80]]-theta['D19']*N[54]-theta['eta']*N[54]+theta['eta']*N[76]-theta['R1']*N[54]*N[33],#54
	
	theta['R1']*N[54]*N[33]-theta['D21']*N[55],#55
	
	-theta['R6']*N[56]*theta['e22']/[theta['R6w']+N[56]]+theta['R5']*N[59]*theta['e25']/[theta['R5w']+N[59]]\
	+theta['R11']*N[53]*theta['e20']/[theta['R11w']+N[53]],#56
	
	-theta['R7']*N[57]*theta['e23']/[theta['R7w']+N[57]]+theta['R2']*N[71]*theta['e26']/[theta['R2w']+N[71]]\
	-theta['R9']*N[57]*theta['e27']/[theta['R9w']+N[57]]-theta['R8']*N[57]*theta['e28']/[theta['R8w']+N[57]]\
	+theta['R10']*N[58]*theta['e47']/[theta['R10w']+N[58]],#57
	
	theta['R9']*N[57]*theta['e27']/[theta['R9w']+N[57]]-theta['R10']*N[58]*theta['e47']/[theta['R10w']+N[58]],#58
	
	-theta['R5']*N[59]*theta['e25']/[theta['R5w']+N[59]]+theta['R4']*N[60]*theta['e29']/[theta['R4w']+N[60]]\
	-theta['R3']*N[59]/[theta['R3w']+N[59]] * theta['adh']*N[55]/[1+theta['gammas2']*N[33]**theta['m']]\
	+theta['R8']*N[57]*theta['e28']/[theta['R8w']+N[57]],#59
	
	-theta['R4']*N[60]*theta['e29']/[theta['R4w']+N[60]]\
	+theta['R3']*N[59]/[theta['R3w']+N[59]]*theta['adh']*N[55]/[1+theta['gammas2']*N[33]**theta['m']],#60

	##TCA
	theta['C27']*theta['e52']*N[82]/[theta['C27w']+N[82]]+theta['T10']*N[68]*theta['e30']/[theta['T10w']+N[68]]\
	-theta['T1']*N[61]*theta['e31']/[theta['T1w']+N[61]],#61
	
	theta['T1']*N[61]*theta['e31']/[theta['T1w']+N[61]]+theta['T7']*N[53]*N[69]*theta['e24']/[theta['T7w']+N[53]*N[69]]\
	-theta['T2']*N[62]*theta['e32']/[theta['T2w']+N[62]]-theta['C30']*N[62]*theta['e33']/[theta['C30w']+N[62]],#62
	
	theta['T2']*N[62]*theta['e32']/[theta['T2w']+N[62]]-theta['T3']*N[63]*N[53]*theta['e34']/[theta['T3w']+N[63]*N[53]],#63
	
	theta['T3']*N[63]*N[53]*theta['e34']/[theta['T3w']+N[63]*N[53]]-theta['T4']*N[64]*theta['e35']/[theta['T4w']+N[64]],#64
	
	theta['T4']*N[64]*theta['e35']/[theta['T4w']+N[64]]-theta['T5']*N[65]*theta['e36']/[theta['T5w']+N[65]]\
	-theta['T6']*N[65]*theta['e37']/[theta['T6w']+N[65]],#65
	
	theta['T5']*N[65]*theta['e36']/[theta['T5w']+N[65]]-theta['T8']*N[66]*theta['e38']/[theta['T8w']+N[66]],#66
	
	theta['T8']*N[66]*theta['e38']/[theta['T8w']+N[66]]-theta['T9']*N[67]*theta['e39']/[theta['T9w']+N[67]]\
	+theta['C33']*N[39]*theta['e46']/[theta['C33w']+N[39]],#67
	
	theta['T9']*N[67]*theta['e39']/[theta['T9w']+N[67]]-theta['T10']*N[68]*theta['e30']/[theta['T10w']+N[68]]\
	+theta['T6']*N[65]*theta['e37']/[theta['T6w']+N[65]],#68
	
	theta['T6']*N[65]*theta['e37']/[theta['T6w']+N[65]]-theta['T7']*N[53]*N[69]*theta['e24']/[theta['T7w']+N[53]*N[69]],#69
	
	theta['C30']*N[62]*theta['e33']/[theta['C30w']+N[62]]-theta['C31']*N[70]*theta['e40']/[theta['C31w']+N[70]],#70
	
	theta['C31']*N[70]*theta['e40']/[theta['C31w']+N[70]]+theta['C34']*N[78]*theta['e48']/[theta['C34w']+N[78]]\
	-theta['C3']*N[71]*N[77]*theta['e42']/[theta['C3w']+N[71]*N[77]]-theta['R2']*N[71]*theta['e26']/[theta['R2w']+N[71]]\
	-theta['C5']*N[71]*theta['e43']/[theta['C5w']+N[71]],#71
	
	theta['C3']*N[71]*N[77]*theta['e42']/[theta['C3w']+N[71]*N[77]]-theta['C1']*N[72]*theta['e1']/[theta['C1w']+N[72]],#72
	
	-theta['C4']*N[73]*theta['e44']/[theta['C4w']+N[73]]-theta['D17']*N[73]+theta['C35']*theta['e49']*N[79]/[theta['C35w']+N[79]],#73
	
	theta['C4']*N[73]*theta['e44']/[theta['C4w']+N[73]]+theta['C5']*N[71]*theta['e43']/[theta['C5w']+N[71]]\
	-theta['C2']*N[74]*theta['e41']/[theta['C2w']+N[74]]-theta['C32']*N[74]*theta['e45']/[theta['C32w']+N[74]],#74
	
	theta['C25']*N[50]*theta['e17']/[theta['C25w']+N[50]]-theta['C36']*N[75]*theta['e50']/[theta['C36w']+N[75]],#75
	
	-theta['D18']*N[76]-theta['etaext']*N[76]+theta['etaext']*N[54],#76
	
	theta['C32']*N[74]*theta['e45']/[theta['C32w']+N[74]]-theta['C3']*N[71]*N[77]*theta['e42']/[theta['C3w']+N[71]*N[77]],#77
	
	theta['C2']*N[74]*theta['e41']/[theta['C2w']+N[74]]-theta['C34']*N[78]*theta['e48']/[theta['C34w']+N[78]],#78
	
	-theta['C35']*theta['e49']*N[79]/[theta['C35w']+N[79]],#79
	#additional eqs
	theta['C39'] * N[50] * theta['e51']/[theta['C39w'] +N[50]] - theta['C29'] * N[80]* theta['e19']/[theta['C29w']+N[80]], # % 80
    theta['C37'] * N[51] * theta['e53']/[theta['C37w'] + N[51]] - theta['C38'] * N[81] * N[29]/[theta['C38w'] + N[81]], #%81
    theta['C38'] * N[81] * N[29]/[theta['C38w'] + N[81]] - theta['C27'] * N[82] * theta['e52']/[theta['C27w'] + N[82]], #%82
    theta['C10'] * N[38] * theta['e3']/[theta['C10w'] + N[38]] - theta['C40'] * N[83] * theta['e54']/[theta['C40w'] + N[83]], #%83
    theta['C40'] * N[83] * theta['e54']/[theta['C40w'] + N[83]] - theta['C41'] * N[84] *theta['e55']/[theta['C41w'] + N[84]], #%84
    theta['C41'] * N[84] * theta['e55']/[theta['C41w'] + N[84]] - theta['C42'] * N[85] * theta['e56']/[theta['C42w'] + N[85]], #%85
	]
	return dNdt

def fitting0(t,y,time,qa_gene,alanine,qa,ethanol,fumarate,glucose,phenylalanine,tyrosine,HGA):	
	sigma = 0.2
	exp_qa2 = qa_gene[0].transpose()[0]
	exp_qa3 = qa_gene[1].transpose()[0]
	exp_qa4 = qa_gene[2].transpose()[0]
	exp_qay = qa_gene[4].transpose()[0]
	exp_qa1f = qa_gene[5].transpose()[0]
	exp_qa1s = qa_gene[6].transpose()[0]

	new_exp_qa2 = np.zeros((1,len(exp_qa2)))
	new_exp_qa3 = np.zeros((1,len(exp_qa3)))
	new_exp_qa4 = np.zeros((1,len(exp_qa4)))
	new_exp_qay = np.zeros((1,len(exp_qay)))
	new_exp_qa1f = np.zeros((1,len(exp_qa1f)))
	new_exp_qa1s = np.zeros((1,len(exp_qa1s)))

	for i in range(len(exp_qa1f)):
		new_exp_qa2[0,i] = math.log(exp_qa2[i])
		new_exp_qa3[0,i] = math.log(exp_qa3[i])
		new_exp_qa4[0,i] = math.log(exp_qa4[i])
		new_exp_qay[0,i] = math.log(exp_qay[i])
		new_exp_qa1f[0,i] = math.log(exp_qa1f[i])
		new_exp_qa1s[0,i] = math.log(exp_qa1s[i])
	
	sim_qa1f = y[:,3] 
	sim_qa1s = y[:,7] 
	sim_qa2 = y[:,20] 
	sim_qa3 = y[:,16] 
	sim_qa4 = y[:,24] 
	sim_qay = y[:,12] 
	
	time_point = [0.5,1.0,1.5,2.0,4.0,6.0,8.0]
	sim_qa1f_point = [] 
	sim_qa1s_point = [] 
	sim_qa2_point = [] 
	sim_qa3_point = [] 
	sim_qa4_point = [] 
	sim_qay_point = [] 
	

	t= t.tolist()
	for x in time_point:
		index = t.index(x)
		sim_qa2_point.append(math.log(sim_qa2[index]))
		sim_qa3_point.append(math.log(sim_qa3[index]))
		sim_qa4_point.append(math.log(sim_qa4[index]))
		sim_qay_point.append(math.log(sim_qay[index]))
		sim_qa1f_point.append(math.log(sim_qa1f[index]))
		sim_qa1s_point.append(math.log(sim_qa1s[index]))
		

	chi_qa2 = (((new_exp_qa2-sim_qa2_point)/sigma)**2).sum()
	
	chi_qa3 = (((new_exp_qa3-sim_qa3_point)/sigma)**2).sum()

	chi_qa4 = (((new_exp_qa4-sim_qa4_point)/sigma)**2).sum()

	chi_qay = (((new_exp_qay-sim_qay_point)/sigma)**2).sum()

	chi_qa1f = (((new_exp_qa1f-sim_qa1f_point)/sigma)**2).sum()

	chi1 = chi_qa2 + chi_qa3 + chi_qa4 + chi_qay + chi_qa1f 
########################################################################
	exp_time = time[0]
	exp_alanine = alanine[0]
	exp_qa = qa[0]
	exp_ethanol = ethanol[0]
	exp_fumarate = fumarate[0]
	exp_glucose = glucose[0]
	exp_phenylalanine = phenylalanine[0]
	exp_tyrosine = tyrosine[0]
	exp_HGA = HGA[0]

	sim_alanine = y[:,58] 
	sim_qa = y[:,35] 
	sim_ethanol = y[:,60] 
	sim_fumarate = y[:,61] 
	sim_glucose = y[:,73] 
	sim_phenylalanine = y[:,49] 
	sim_tyrosine = y[:,75] 
	sim_HGA = y[:,51] 

	exp_result = np.array([exp_alanine,exp_qa,exp_ethanol,exp_fumarate,
							exp_glucose,exp_phenylalanine,exp_tyrosine,exp_HGA])
	sim_result = np.zeros([len(exp_result),len(exp_result[0])])
	
	t1 = np.around(t,3)
	t = t1.tolist()
	
	for j in range(len(exp_time)):
		index = t.index(round(exp_time[j],3))
		sim_result[0][j] = sim_alanine[index]
		sim_result[1][j] = sim_qa[index]
		sim_result[2][j] = sim_ethanol[index]
		sim_result[3][j] = sim_fumarate[index]
		sim_result[4][j] = sim_glucose[index]
		sim_result[5][j] = sim_phenylalanine[index]
		sim_result[6][j] = sim_tyrosine[index]
		sim_result[7][j] = sim_HGA[index]

	for i in range(len(exp_result)):
		for j in range(len(exp_result[0])):
			if math.isnan(exp_result[i][j]):
				exp_result[i][j] = 0.00001
			else:
				exp_result[i][j] = exp_result[i][j]

	chi2 = (((np.log(exp_result) - np.log(sim_result))/sigma)**2).sum()
	
################################################################################
	chi_square = chi1 + chi2
	return chi_square

def fitting1(t,y,time,qa_gene,alanine,qa,ethanol,fumarate,glucose,phenylalanine,tyrosine,HGA):	
	sigma = 0.2
	exp_qa2 = qa_gene[0].transpose()[0]
	exp_qa3 = qa_gene[1].transpose()[0]
	exp_qa4 = qa_gene[2].transpose()[0]
	exp_qax = qa_gene[3].transpose()[0]
	exp_qay = qa_gene[4].transpose()[0]
	exp_qa1f = qa_gene[5].transpose()[0]
	exp_qa1s = qa_gene[6].transpose()[0]

	new_exp_qa2 = np.zeros((1,len(exp_qa2)))
	new_exp_qa3 = np.zeros((1,len(exp_qa3)))
	new_exp_qa4 = np.zeros((1,len(exp_qa4)))
	new_exp_qax = np.zeros((1,len(exp_qax)))
	new_exp_qay = np.zeros((1,len(exp_qay)))
	new_exp_qa1f = np.zeros((1,len(exp_qa1f)))
	new_exp_qa1s = np.zeros((1,len(exp_qa1s)))

	for i in range(len(exp_qa1f)):
		new_exp_qa2[0,i] = math.log(exp_qa2[i])
		new_exp_qa3[0,i] = math.log(exp_qa3[i])
		new_exp_qa4[0,i] = math.log(exp_qa4[i])
		new_exp_qax[0,i] = math.log(exp_qax[i])
		new_exp_qay[0,i] = math.log(exp_qay[i])
		new_exp_qa1f[0,i] = math.log(exp_qa1f[i])
		new_exp_qa1s[0,i] = math.log(exp_qa1s[i])
	
	sim_qa1f = y[:,3] 
	sim_qa1s = y[:,7] 
	sim_qa2 = y[:,20] 
	sim_qa3 = y[:,16] 
	sim_qa4 = y[:,24] 
	sim_qay = y[:,12] 
	sim_qax = y[:,28] 

	time_point = [0.5,1.0,1.5,2.0,4.0,6.0,8.0]
	sim_qa1f_point = [] 
	sim_qa1s_point = [] 
	sim_qa2_point = [] 
	sim_qa3_point = [] 
	sim_qa4_point = [] 
	sim_qay_point = [] 
	sim_qax_point = []

	t= t.tolist()
	for x in time_point:
		index = t.index(x)
		sim_qa2_point.append(math.log(sim_qa2[index]))
		sim_qa3_point.append(math.log(sim_qa3[index]))
		sim_qa4_point.append(math.log(sim_qa4[index]))
		sim_qay_point.append(math.log(sim_qay[index]))
		sim_qa1f_point.append(math.log(sim_qa1f[index]))
		sim_qa1s_point.append(math.log(sim_qa1s[index]))
		sim_qax_point.append(math.log(sim_qax[index]))

	chi_qa2 = (((new_exp_qa2-sim_qa2_point)/sigma)**2).sum()
	
	chi_qa3 = (((new_exp_qa3-sim_qa3_point)/sigma)**2).sum()

	chi_qa4 = (((new_exp_qa4-sim_qa4_point)/sigma)**2).sum()

	chi_qay = (((new_exp_qay-sim_qay_point)/sigma)**2).sum()

	chi_qa1f = (((new_exp_qa1f-sim_qa1f_point)/sigma)**2).sum()

	chi_qax = (((new_exp_qax-sim_qax_point)/sigma)**2).sum()

	chi1 = chi_qa2 + chi_qa3 + chi_qa4 + chi_qay + chi_qa1f  + chi_qax
########################################################################
	exp_time = time[1]
	exp_alanine = alanine[1]
	exp_qa = qa[1]
	exp_ethanol = ethanol[1]
	exp_fumarate = fumarate[1]
	exp_glucose = glucose[1]
	exp_phenylalanine = phenylalanine[1]
	exp_tyrosine = tyrosine[1]
	exp_HGA = HGA[1]

	sim_alanine = y[:,58] 
	sim_qa = y[:,35] 
	sim_ethanol = y[:,60] 
	sim_fumarate = y[:,61] 
	sim_glucose = y[:,73] 
	sim_phenylalanine = y[:,49] 
	sim_tyrosine = y[:,75] 
	sim_HGA = y[:,51] 

	exp_result = np.array([exp_alanine,exp_qa,exp_ethanol,exp_fumarate,
						exp_glucose,exp_phenylalanine,exp_tyrosine,exp_HGA])
	sim_result = np.zeros([len(exp_result),len(exp_result[0])])
	
	t1 = np.around(t,3)
	t = t1.tolist()
	
	for j in range(len(exp_time)):
		index = t.index(round(exp_time[j],3))
		sim_result[0][j] = sim_alanine[index]
		sim_result[1][j] = sim_qa[index]
		sim_result[2][j] = sim_ethanol[index]
		sim_result[3][j] = sim_fumarate[index]
		sim_result[4][j] = sim_glucose[index]
		sim_result[5][j] = sim_phenylalanine[index]
		sim_result[6][j] = sim_tyrosine[index]
		sim_result[7][j] = sim_HGA[index]

	for i in range(len(exp_result)):
		for j in range(len(exp_result[0])):
			if math.isnan(exp_result[i][j]):
				exp_result[i][j] = 0.00001
			else:
				exp_result[i][j] = exp_result[i][j]

	chi2 = (((np.log(exp_result) - np.log(sim_result))/sigma)**2).sum()


################################################################################
	chi_square = chi1 + chi2
	return chi_square


def fitting2(t,y,time,qa_gene,alanine,qa,ethanol,fumarate,glucose,phenylalanine,tyrosine,HGA):	
	sigma = 0.2
	exp_qa2 = qa_gene[0].transpose()[0]
	exp_qa3 = qa_gene[1].transpose()[0]
	exp_qa4 = qa_gene[2].transpose()[0]
	exp_qay = qa_gene[4].transpose()[0]
	exp_qa1f = qa_gene[5].transpose()[0]
	exp_qa1s = qa_gene[6].transpose()[0]

	new_exp_qa2 = np.zeros((1,len(exp_qa2)))
	new_exp_qa3 = np.zeros((1,len(exp_qa3)))
	new_exp_qa4 = np.zeros((1,len(exp_qa4)))
	new_exp_qay = np.zeros((1,len(exp_qay)))
	new_exp_qa1f = np.zeros((1,len(exp_qa1f)))
	new_exp_qa1s = np.zeros((1,len(exp_qa1s)))

	for i in range(len(exp_qa1f)):
		new_exp_qa2[0,i] = math.log(exp_qa2[i])
		new_exp_qa3[0,i] = math.log(exp_qa3[i])
		new_exp_qa4[0,i] = math.log(exp_qa4[i])
		new_exp_qay[0,i] = math.log(exp_qay[i])
		new_exp_qa1f[0,i] = math.log(exp_qa1f[i])
		new_exp_qa1s[0,i] = math.log(exp_qa1s[i])
	
	sim_qa1f = y[:,3] 
	sim_qa1s = y[:,7] 
	sim_qa2 = y[:,20] 
	sim_qa3 = y[:,16] 
	sim_qa4 = y[:,24] 
	sim_qay = y[:,12] 
	
	time_point = [0.5,1.0,1.5,2.0,4.0,6.0,8.0]
	sim_qa1f_point = [] 
	sim_qa1s_point = [] 
	sim_qa2_point = [] 
	sim_qa3_point = [] 
	sim_qa4_point = [] 
	sim_qay_point = [] 
	

	t= t.tolist()
	for x in time_point:
		index = t.index(x)
		sim_qa2_point.append(math.log(sim_qa2[index]))
		sim_qa3_point.append(math.log(sim_qa3[index]))
		sim_qa4_point.append(math.log(sim_qa4[index]))
		sim_qay_point.append(math.log(sim_qay[index]))
		sim_qa1f_point.append(math.log(sim_qa1f[index]))
		sim_qa1s_point.append(math.log(sim_qa1s[index]))
		

	chi_qa2 = (((new_exp_qa2-sim_qa2_point)/sigma)**2).sum()
	
	chi_qa3 = (((new_exp_qa3-sim_qa3_point)/sigma)**2).sum()

	chi_qa4 = (((new_exp_qa4-sim_qa4_point)/sigma)**2).sum()

	chi_qay = (((new_exp_qay-sim_qay_point)/sigma)**2).sum()

	chi_qa1f = (((new_exp_qa1f-sim_qa1f_point)/sigma)**2).sum()

	chi1 = chi_qa2 + chi_qa3 + chi_qa4 + chi_qay + chi_qa1f  

########################################################################
	exp_time = time[2]
	exp_alanine = alanine[2]
	exp_qa = qa[2]
	exp_ethanol = ethanol[2]
	exp_fumarate = fumarate[2]
	exp_glucose = glucose[2]
	exp_phenylalanine = phenylalanine[2]
	exp_tyrosine = tyrosine[2]
	exp_HGA = HGA[2]

	sim_alanine = y[:,58] 
	sim_qa = y[:,35] 
	sim_ethanol = y[:,60] 
	sim_fumarate = y[:,61] 
	sim_glucose = y[:,73] 
	sim_phenylalanine = y[:,49] 
	sim_tyrosine = y[:,75] 
	sim_HGA = y[:,51] 

	exp_result = np.array([exp_alanine,exp_qa,exp_ethanol,exp_fumarate,
							exp_glucose,exp_phenylalanine,exp_tyrosine,exp_HGA])
	sim_result = np.zeros([len(exp_result),len(exp_result[0])])
	
	t1 = np.around(t,3)
	t = t1.tolist()
	
	for j in range(len(exp_time)):
		index = t.index(round(exp_time[j],3))
		sim_result[0][j] = sim_alanine[index]
		sim_result[1][j] = sim_qa[index]
		sim_result[2][j] = sim_ethanol[index]
		sim_result[3][j] = sim_fumarate[index]
		sim_result[4][j] = sim_glucose[index]
		sim_result[5][j] = sim_phenylalanine[index]
		sim_result[6][j] = sim_tyrosine[index]
		sim_result[7][j] = sim_HGA[index]

	for i in range(len(exp_result)):
		for j in range(len(exp_result[0])):
			if math.isnan(exp_result[i][j]):
				exp_result[i][j] = 0.00001
			else:
				exp_result[i][j] = exp_result[i][j]

	chi2 = (((np.log(exp_result) - np.log(sim_result))/sigma)**2).sum()

	
################################################################################
	chi_square = chi1 + chi2
	return chi_square

def fitting3(t,y,time,qa_gene,alanine,qa,ethanol,fumarate,glucose,phenylalanine,tyrosine,HGA):	
	sigma = 0.2
	exp_qa2 = qa_gene[0].transpose()[0]
	exp_qa3 = qa_gene[1].transpose()[0]
	exp_qa4 = qa_gene[2].transpose()[0]
	exp_qax = qa_gene[3].transpose()[0]
	exp_qay = qa_gene[4].transpose()[0]
	exp_qa1f = qa_gene[5].transpose()[0]
	exp_qa1s = qa_gene[6].transpose()[0]

	new_exp_qa2 = np.zeros((1,len(exp_qa2)))
	new_exp_qa3 = np.zeros((1,len(exp_qa3)))
	new_exp_qa4 = np.zeros((1,len(exp_qa4)))
	new_exp_qax = np.zeros((1,len(exp_qax)))
	new_exp_qay = np.zeros((1,len(exp_qay)))
	new_exp_qa1f = np.zeros((1,len(exp_qa1f)))
	new_exp_qa1s = np.zeros((1,len(exp_qa1s)))

	for i in range(len(exp_qa1f)):
		new_exp_qa2[0,i] = math.log(exp_qa2[i])
		new_exp_qa3[0,i] = math.log(exp_qa3[i])
		new_exp_qa4[0,i] = math.log(exp_qa4[i])
		new_exp_qax[0,i] = math.log(exp_qax[i])
		new_exp_qay[0,i] = math.log(exp_qay[i])
		new_exp_qa1f[0,i] = math.log(exp_qa1f[i])
		new_exp_qa1s[0,i] = math.log(exp_qa1s[i])
	
	sim_qa1f = y[:,3] 
	sim_qa1s = y[:,7] 
	sim_qa2 = y[:,20] 
	sim_qa3 = y[:,16] 
	sim_qa4 = y[:,24] 
	sim_qay = y[:,12] 
	sim_qax = y[:,28] 

	time_point = [0.5,1.0,1.5,2.0,4.0,6.0,8.0]
	sim_qa1f_point = [] 
	sim_qa1s_point = [] 
	sim_qa2_point = [] 
	sim_qa3_point = [] 
	sim_qa4_point = [] 
	sim_qay_point = [] 
	sim_qax_point = []

	t= t.tolist()
	for x in time_point:
		index = t.index(x)
		sim_qa2_point.append(math.log(sim_qa2[index]))
		sim_qa3_point.append(math.log(sim_qa3[index]))
		sim_qa4_point.append(math.log(sim_qa4[index]))
		sim_qay_point.append(math.log(sim_qay[index]))
		sim_qa1f_point.append(math.log(sim_qa1f[index]))
		sim_qa1s_point.append(math.log(sim_qa1s[index]))
		sim_qax_point.append(math.log(sim_qax[index]))

	chi_qa2 = (((new_exp_qa2-sim_qa2_point)/sigma)**2).sum()
	
	chi_qa3 = (((new_exp_qa3-sim_qa3_point)/sigma)**2).sum()

	chi_qa4 = (((new_exp_qa4-sim_qa4_point)/sigma)**2).sum()

	chi_qay = (((new_exp_qay-sim_qay_point)/sigma)**2).sum()

	chi_qa1f = (((new_exp_qa1f-sim_qa1f_point)/sigma)**2).sum()

	chi_qax = (((new_exp_qax-sim_qax_point)/sigma)**2).sum()

	chi1 = chi_qa2 + chi_qa3 + chi_qa4 + chi_qay + chi_qa1f  + chi_qax
########################################################################
	exp_time = time[3]
	exp_alanine = alanine[3]
	exp_qa = qa[3]
	exp_ethanol = ethanol[3]
	exp_fumarate = fumarate[3]
	exp_glucose = glucose[3]
	exp_phenylalanine = phenylalanine[3]
	exp_tyrosine = tyrosine[3]
	exp_HGA = HGA[3]

	sim_alanine = y[:,58] 
	sim_qa = y[:,35] 
	sim_ethanol = y[:,60] 
	sim_fumarate = y[:,61] 
	sim_glucose = y[:,73] 
	sim_phenylalanine = y[:,49] 
	sim_tyrosine = y[:,75] 
	sim_HGA = y[:,51] 

	exp_result = np.array([exp_alanine,exp_qa,exp_ethanol,exp_fumarate,
						exp_glucose,exp_phenylalanine,exp_tyrosine,exp_HGA])
	sim_result = np.zeros([len(exp_result),len(exp_result[0])])
	
	t1 = np.around(t,3)
	t = t1.tolist()
	
	for j in range(len(exp_time)):
		index = t.index(round(exp_time[j],3))
		sim_result[0][j] = sim_alanine[index]
		sim_result[1][j] = sim_qa[index]
		sim_result[2][j] = sim_ethanol[index]
		sim_result[3][j] = sim_fumarate[index]
		sim_result[4][j] = sim_glucose[index]
		sim_result[5][j] = sim_phenylalanine[index]
		sim_result[6][j] = sim_tyrosine[index]
		sim_result[7][j] = sim_HGA[index]

	for i in range(len(exp_result)):
		for j in range(len(exp_result[0])):
			if math.isnan(exp_result[i][j]):
				exp_result[i][j] = 0.00001
			else:
				exp_result[i][j] = exp_result[i][j]

	chi2 = (((np.log(exp_result) - np.log(sim_result))/sigma)**2).sum()

	
################################################################################
	chi_square = chi1 + chi2
	return chi_square

def run(p):
	sol = odeint(ode_fun,p[0],p[1],args=(p[2],))
	return sol

def pa_update_theta(new_w,theta,i,theta_key):
	f = np.random.uniform(0,1)
	new_theta = copy.deepcopy(theta)
	new_theta[theta_key[i]] = theta[theta_key[i]] + new_w*(2*f-1)*theta[theta_key[i]]
	return new_theta

def pa_update_initial(new_w,p0,p1,p2,p3,i,theta_key):
	f0 = np.random.uniform(0,1)
	f1 = np.random.uniform(0,1)
	f2 = np.random.uniform(0,1)
	f3 = np.random.uniform(0,1)
	new_p0 = p0[:]
	new_p1 = p1[:]
	new_p2 = p2[:]
	new_p3 = p3[:]
	new_p0[i-len(theta_key)] = p0[i-len(theta_key)] + new_w*(2*f0-1)*p0[i-len(theta_key)]
	new_p1[i-len(theta_key)] = p1[i-len(theta_key)] + new_w*(2*f1-1)*p1[i-len(theta_key)]
	new_p2[i-len(theta_key)] = p2[i-len(theta_key)] + new_w*(2*f2-1)*p2[i-len(theta_key)]
	new_p3[i-len(theta_key)] = p3[i-len(theta_key)] + new_w*(2*f3-1)*p3[i-len(theta_key)]
	return new_p0,new_p1,new_p2,new_p3

def MCMC_theta(w,t,chi,chi0,chi1,chi2,chi3,p0,p1,p2,p3,theta,sol,i,theta_key):
	new_theta = pa_update_theta(w,theta,i,theta_key)
	parameters = [[p0,t,new_theta],[p1,t,new_theta],[p2,t,new_theta],[p3,t,new_theta]]
    ####
	pool = mp.Pool(4)
	new_sol = pool.map(run,parameters) 
	pool.close()
	pool.join()
	####
	new_chi0 = fitting0(t,new_sol[0],time_exp,qa_gene,alanine,qa,ethanol,fumarate,glucose,phenylalanine,tyrosine,HGA)
	new_chi1 = fitting1(t,new_sol[1],time_exp,qa_gene,alanine,qa,ethanol,fumarate,glucose,phenylalanine,tyrosine,HGA)
	new_chi2 = fitting2(t,new_sol[2],time_exp,qa_gene,alanine,qa,ethanol,fumarate,glucose,phenylalanine,tyrosine,HGA)
	new_chi3 = fitting3(t,new_sol[3],time_exp,qa_gene,alanine,qa,ethanol,fumarate,glucose,phenylalanine,tyrosine,HGA)
	new_chi = new_chi0 + new_chi1 + new_chi2 + new_chi3
	if math.isnan(new_chi):
		out_chi = chi
		out_chi0 = chi0
		out_chi1 = chi1
		out_chi2 = chi2
		out_chi3 = chi3
		out_y = sol
		out_theta = theta
		accept = 0
	else:
		# uniform distribution
		u = np.random.uniform(0,1)
		deltaH = (-new_chi + chi)*100
		if deltaH > 0:
			a = 0
		else:
			a = max(round(deltaH,3),-1000)	
		alpha = min(1,np.exp(a))	
		if u <= alpha:
			out_chi = new_chi
			out_chi0 = new_chi0
			out_chi1 = new_chi1
			out_chi2 = new_chi2
			out_chi3 = new_chi3
			out_y = new_sol
			out_theta = new_theta
			accept = 1
		else:		
			out_chi = chi
			out_chi0 = chi0
			out_chi1 = chi1
			out_chi2 = chi2
			out_chi3 = chi3
			out_y = sol
			out_theta = theta
			accept = 0
	#print(chi)
	#print(out_chi)
	#print(accept)
	return out_chi,out_chi0,out_chi1,out_chi2,out_chi3,p0,p1,p2,p3,out_theta,out_y,theta_key,accept

def MCMC_initial(w,t,chi,chi0,chi1,chi2,chi3,p0,p1,p2,p3,theta,sol,i,theta_key):
	new_p0,new_p1,new_p2,new_p3 = pa_update_initial(w,p0,p1,p2,p3,i,theta_key)
	parameters = [[new_p0,t,theta],[new_p1,t,theta],[new_p2,t,theta],[new_p3,t,theta]]
    ####
	pool = mp.Pool(4)
	new_sol = pool.map(run,parameters) 
	pool.close()
	pool.join()
	####
	new_chi0 = fitting0(t,new_sol[0],time_exp,qa_gene,alanine,qa,ethanol,fumarate,glucose,phenylalanine,tyrosine,HGA)
	new_chi1 = fitting1(t,new_sol[1],time_exp,qa_gene,alanine,qa,ethanol,fumarate,glucose,phenylalanine,tyrosine,HGA)
	new_chi2 = fitting2(t,new_sol[2],time_exp,qa_gene,alanine,qa,ethanol,fumarate,glucose,phenylalanine,tyrosine,HGA)
	new_chi3 = fitting3(t,new_sol[3],time_exp,qa_gene,alanine,qa,ethanol,fumarate,glucose,phenylalanine,tyrosine,HGA)
	out_y = sol[:]
	if math.isnan(new_chi0):
		out_chi0 = chi0
		out_y[0] = sol[0]
		out_p0 = p0
		accept = 0
	else:
		# uniform distribution
		u0 = np.random.uniform(0,1)
		deltaH0 = (-new_chi0 + chi0)*100
		if deltaH0 > 0:
			a = 0
		else:
			a = max(round(deltaH0,3),-1000)	
		alpha0 = min(1,np.exp(a))	
		if u0 <= alpha0:
			out_chi0 = new_chi0
			out_y[0] = new_sol[0]
			out_p0 = new_p0
			accept = 1
		else:		
			out_chi0 = chi0
			out_y[0] = sol[0]
			out_p0 = p0
			accept = 0
	# 
	if math.isnan(new_chi1):
		out_chi1 = chi1
		out_y[1] = sol[1]
		out_p1 = p1
		accept = 0
	else:
		u1 = np.random.uniform(0,1)
		deltaH1 = (-new_chi1 + chi1)*100
		if deltaH1 > 0:
			a = 0
		else:
			a = max(round(deltaH1,3),-1000)	
		alpha1 = min(1,np.exp(a))	
		if u1 <= alpha1:
			out_chi1 = new_chi1
			out_y[1] = new_sol[1]
			out_p1 = new_p1
			accept = 1
		else:		
			out_chi1 = chi1
			out_y[1] = sol[1]
			out_p1 = p1
			accept = 0
	#
	if math.isnan(new_chi2):
		out_chi2 = chi2
		out_y[2] = sol[2]
		out_p2 = p2
		accept = 0
	else:
		u2 = np.random.uniform(0,1)
		deltaH2 = (-new_chi2 + chi2)*100
		if deltaH2 > 0:
			a = 0
		else:
			a = max(round(deltaH2,3),-1000)	
		alpha2 = min(1,np.exp(a))	
		if u2 <= alpha2:
			out_chi2 = new_chi2
			out_y[2] = new_sol[2]
			out_p2 = new_p2
			accept = 1
		else:		
			out_chi2 = chi2
			out_y[2] = sol[2]
			out_p2 = p2
			accept = 0
	#
	if math.isnan(new_chi3):
		out_chi3 = chi3
		out_y[3] = sol[3]
		out_p3 = p3
		accept = 0
	else:
		u3 = np.random.uniform(0,1)
		deltaH3 = (-new_chi3 + chi3)*100
		if deltaH3 > 0:
			a = 0
		else:
			a = max(round(deltaH3,3),-1000)	
		alpha3 = min(1,np.exp(a))	
		if u3 <= alpha3:
			out_chi3 = new_chi3
			out_y[3] = new_sol[3]
			out_p3 = new_p3
			accept = 1
		else:		
			out_chi3 = chi3
			out_y[3] = sol[3]
			out_p3 = p3
			accept = 0
	#print(chi)
	#print(out_chi)
	#print(accept)
	out_chi = out_chi0+out_chi1+out_chi2+out_chi3
	return out_chi,out_chi0,out_chi1,out_chi2,out_chi3,out_p0,out_p1,out_p2,out_p3,theta,out_y,theta_key,accept


if __name__=='__main__':
	
	sweeps = 1000
	p0 = init_species0() # qax
	p1 = init_species1()
	p2 = init_species2() # qax
	p3 = init_species3()
	theta,theta_key = init_parameters()
	
	qa_gene,time_exp,qa,alanine,ethanol,fumarate,glucose,phenylalanine,tyrosine,HGA = observe_data()	
	t=np.linspace(0,15,15001)
	parameters = [[p0,t,theta],[p1,t,theta],[p2,t,theta],[p3,t,theta]]
	####parallel
	pool = mp.Pool(4)
	sol = pool.map(run,parameters) 
	pool.close()
	pool.join()
	####
	chi0 = fitting0(t,sol[0],time_exp,qa_gene,alanine,qa,ethanol,fumarate,glucose,phenylalanine,tyrosine,HGA)
	chi1 = fitting1(t,sol[1],time_exp,qa_gene,alanine,qa,ethanol,fumarate,glucose,phenylalanine,tyrosine,HGA)
	chi2 = fitting2(t,sol[2],time_exp,qa_gene,alanine,qa,ethanol,fumarate,glucose,phenylalanine,tyrosine,HGA)
	chi3 = fitting3(t,sol[3],time_exp,qa_gene,alanine,qa,ethanol,fumarate,glucose,phenylalanine,tyrosine,HGA)
	chi = chi0 + chi1 + chi2 + chi3
	L = (len(p0)+len(theta_key))*sweeps# gene part initials fixed
	accept_number = 0
	w = 0.8
	#start = time.time()
	for j in range(L):	
		
		i = j%(len(p0)+len(theta_key))
		m = j//(len(p0)+len(theta_key))
		# MCMC
		if i < len(theta_key):
			chi,chi0,chi1,chi2,chi3,p0,p1,p2,p3,theta,sol,theta_key,accept = MCMC_theta(w,t,chi,chi0,chi1,chi2,chi3,p0,p1,p2,p3,theta,sol,i,theta_key)
			accept_number += accept
		else:
			chi,chi0,chi1,chi2,chi3,p0,p1,p2,p3,theta,sol,theta_key,accept = MCMC_initial(w,t,chi,chi0,chi1,chi2,chi3,p0,p1,p2,p3,theta,sol,i,theta_key)
			accept_number += accept	
		print('sweep'+str(m))
		print('iter'+str(i))		
		print(chi)
		if i == 0 and m > 0:
			#print(time.time()-start)
			#start= time.time()
			a = accept_number/(len(p0)+len(theta_key))		
			if a <= 0.45:
				w = w/2
			accept_number = 0
			
			f = open('chi.txt','a+')
			f.write('chi: '+str(chi)+'\n')
			f.close()	
			output_p0=open('out_p0.csv','a+')
			for i in range(len(p0)):
				output_p0.write(str(p0[i])+',')
				output_p0.write("\t")
			output_p0.write("\n")
			output_p0.close()

			output_p1=open('out_p1.csv','a+')
			for i in range(len(p1)):
				output_p1.write(str(p1[i])+',')
				output_p1.write("\t")
			output_p1.write("\n")
			output_p1.close()

			output_p2=open('out_p2.csv','a+')
			for i in range(len(p2)):
				output_p2.write(str(p2[i])+',')
				output_p2.write("\t")
			output_p2.write("\n")
			output_p2.close()

			output_p3=open('out_p3.csv','a+')
			for i in range(len(p3)):
				output_p3.write(str(p3[i])+',')
				output_p3.write("\t")
			output_p3.write("\n")
			output_p3.close()

			output_theta=open('out_theta.csv','a+')
			for key in theta:
				output_theta.write(str(key)+":"+str(theta[key])+',')
				output_theta.write("\t")
			output_theta.write("\n")
			output_theta.close()