from flask import Flask,redirect,url_for,render_template,request
from decimal import Decimal
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')



@app.route('/compare',methods = ['POST','GET'])
def compare():
	u1 = request.form['user1']
	u2 = request.form['user2']

	address = 'http://codeforces.com/api/user.info?handles='+u1+';'+u2
	r = requests.get(address)
	r = r.json()
	r = r['result']


	address = 'http://codeforces.com/api/user.status?handle='+u1+'&from=1&count=100'
	r1 = requests.get(address)
	r1 = r1.json()
	r1 = r1['result']

	address = 'http://codeforces.com/api/user.status?handle='+u2+'&from=1&count=100'
	r2 = requests.get(address)
	r2 = r2.json()
	r2 = r2['result']

	address = 'http://codeforces.com/api/user.rating?handle='+u1
	r3 = requests.get(address)
	r3 = r3.json()
	r3 = r3['result']

	address = 'http://codeforces.com/api/user.rating?handle='+u2
	r4 = requests.get(address)
	r4 = r4.json()
	r4 = r4['result']

	country1 = '-'
	country2 = '-'
	pic1 = None
	pic2 = None
	rating1 = 'Unrated'
	rating2 = 'Unrated'
	maxrating1 = 'Unrated'
	maxrating2 = 'Unrated'
	rank1 = 'Unrated'
	rank2 = 'Unrated'
	sub1 = None
	sub2 = None
	friend1 = None
	friend2 = None
	contribution1 = None
	contribution2 = None
	org1 = 'None'
	org2 = 'None'
	maxjump1 = None
	maxjump2 = None
	col1 = '#000000'
	col2 = '#000000'

	if 'country' in r[0].keys():
		country1 = str(r[0]['country'])
		print 'yo'
	if 'country' in r[1].keys():
		country2 = str(r[1]['country'])

	if 'titlePhoto' in r[0].keys():
		pic1 = str(r[0]['titlePhoto'])
	if 'titlePhoto' in r[1].keys():
		pic2 = str(r[1]['titlePhoto'])

	if 'rating' in r[0].keys():
		rating1 = str(r[0]['rating'])
	if 'rating' in r[1].keys():
		rating2 = str(r[1]['rating'])

	if 'maxRating' in r[0].keys():
		maxrating1 = str(r[0]['maxRating'])
	if 'maxRating' in r[1].keys():
		maxrating2 = str(r[1]['maxRating'])

	if 'rank' in r[0].keys():
		rank1 = str(r[0]['rank'])
	if 'rank' in r[1].keys():
		rank2 = str(r[1]['rank'])

	if (rank1=='legendary grandmaster'):
		col1 = '#800000'
	elif (rank1=='international grandmaster'):
		col1 = '#ff0000'
	elif (rank1=='grandmaster'):
		col1 = 'ff6666'
	elif (rank1=='international master'):
		col1 = '#ffa64d'
	elif (rank1=='master'):
		col1 = 'ffd480'
	elif (rank1=='candidate master'):
		col1 = '#b300b3'
	elif (rank1=='expert'):
		col1 = '#0000ff'
	elif (rank1=='specialist'):
		col1 = '#80ffe5'
	elif (rank1=='pupil'):
		col1 = '00cc00'
	elif (rank1=='newbie'):
		col1 = '#808080'
	else:
		col1 = '#000000'

	if (rank2=='legendary grandmaster'):
		col2 = '#800000'
	elif (rank2=='international grandmaster'):
		col2 = '#ff0000'
	elif (rank2=='grandmaster'):
		col2 = 'ff6666'
	elif (rank2=='international master'):
		col2 = '#ffa64d'
	elif (rank2=='master'):
		col2 = 'ffd480'
	elif (rank2=='candidate master'):
		col2 = '#b300b3'
	elif (rank2=='expert'):
		col2 = '#0000ff'
	elif (rank2=='specialist'):
		col2 = '#80ffe5'
	elif (rank2=='pupil'):
		col2 = '00cc00'
	elif (rank2=='newbie'):
		col2 = '#808080'
	else:
		col2 = '#000000'

	sub1 = str(len(r1))
	sub2 = str(len(r2))

	if 'friendOfCount' in r[0].keys():
		friend1 = str(r[0]['friendOfCount'])
	if 'friendOfCount' in r[1].keys():
		friend2 = str(r[1]['friendOfCount'])

	if 'contribution' in r[0].keys():
		contribution1 = str(r[0]['contribution'])
	if 'contribution' in r[1].keys():
		contribution2 = str(r[1]['contribution'])

	if 'organization' in r[0].keys():
		org1 = str(r[0]['organization'])
	if 'organization' in r[1].keys():
		org2 = str(r[1]['organization'])

	AC1 = 0
	WA1 = 0
	TLE1 = 0
	RE1 = 0
	CE1 = 0
	other1 = 0
	acc1 = 0

	AC2 = 0
	WA2 = 0
	TLE2 = 0
	RE2 = 0
	CE2 = 0
	other2 = 0
	acc2 = 0

	for i in range(eval(sub1)):
		if (str(r1[i]['verdict'])=='OK'):
			AC1+=1
		elif (str(r1[i]['verdict'])=='WRONG_ANSWER'):
			WA1+=1
		elif (str(r1[i]['verdict'])=='RUNTIME_ERROR'):
			RE1+=1
		elif (str(r1[i]['verdict'])=='TIME_LIMIT_EXCEEDED'):
			TLE1+=1
		elif (str(r1[i]['verdict'])=='COMPILATION_ERROR'):
			CE1+=1

	other1 = eval(sub1)-AC1-WA1-TLE1-RE1-CE1
	acc1 = round(Decimal((AC1*100.0)/(AC1+WA1+TLE1+RE1)),2)

	for i in range(eval(sub2)):
		if (str(r2[i]['verdict'])=='OK'):
			AC2+=1
		elif (str(r2[i]['verdict'])=='WRONG_ANSWER'):
			WA2+=1
		elif (str(r2[i]['verdict'])=='RUNTIME_ERROR'):
			RE2+=1
		elif (str(r2[i]['verdict'])=='TIME_LIMIT_EXCEEDED'):
			TLE2+=1
		elif (str(r2[i]['verdict'])=='COMPILATION_ERROR'):
			CE2+=1

	other2 = eval(sub2)-AC2-WA2-TLE2-RE2-CE2
	acc2 = round(Decimal((AC2*100.0)/(AC2+WA2+TLE2+RE2)),2)

	for i in range(len(r3)):
		if (maxjump1==None):
			maxjump1 = r3[i]['newRating']-r3[i]['oldRating']
		elif (r3[i]['newRating']-r3[i]['oldRating']>maxjump1):
			maxjump1 = r3[i]['newRating']-r3[i]['oldRating']

	for i in range(len(r4)):
		if (maxjump2==None):
			maxjump2 = r4[i]['newRating']-r4[i]['oldRating']
		elif (r4[i]['newRating']-r4[i]['oldRating']>maxjump2):
			maxjump2 = r4[i]['newRating']-r4[i]['oldRating']

	return render_template('result.html',col1 = col1,col2 = col2,maxjump1 = maxjump1,maxjump2 = maxjump2,acc1 = acc1,acc2 = acc2,other1 = other1,other2 = other2,AC1 = AC1,WA1 = WA1,TLE1 = TLE1,RE1 = RE1,CE1 = CE1,AC2 = AC2,WA2 = WA2,TLE2 = TLE2,RE2 = RE2,CE2 = CE2,user1 = u1,user2 = u2,pic1 = pic1,pic2 = pic2,country1 = country1,country2 = country2,rating1 = rating1,rating2 = rating2,rank1 = rank1,rank2 = rank2,maxrating1 = maxrating1,maxrating2 = maxrating2,sub1 = sub1,sub2 = sub2,friend1 = friend1,friend2 = friend2,contribution1 = contribution1,contribution2 = contribution2,org1 = org1,org2 = org2)

if __name__ == '__main__':
	app.debug = True
	app.run()
