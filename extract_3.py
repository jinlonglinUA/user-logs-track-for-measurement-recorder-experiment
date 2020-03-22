#python3
import mysql.connector
from datetime import datetime
import datetime
import time
import os
import sys



def define_term_duration():
	db = mysql.connector.connect(host="localhost",    # your host, usually localhost
	                     user="root",         # your username
	                     password="",  # your password
	                     database="author_production")        # name of the data base
	cur = db.cursor()
	cur.execute("SELECT DISTINCT user_id FROM user_logs")
	ids = cur.fetchall()
	dic = {}
	for user_id in ids:
		cur.execute("SELECT * FROM user_logs WHERE user_id = %s", (user_id))
		raw_data = cur.fetchall()
		data = []
		for row in raw_data:
			if row[2] == 'In Method, added from':
				if data == []:
					data.append(row)
				elif data[-1][2] == 'In Method, added from':
					data[-1] = row 
				else:
					data.append(row)
			if row[2] == 'In Method, add definition for term':
				if data == []:
					pass
				elif data[-1][2] == 'In Method, added from':
					data.append(row)
				else:
					pass
		if (not data == []) and (not data[-1][2] == 'In Method, add definition for term'):
			del data[-1]
		if not data == []:
			dic[data[0][1]] = data
	db.close()
	result = []
	for item in dic:
		data = iter(dic[item])
		for row in data:
			start = row
			end = next(data)
			start_time = start[6]
			end_time = end[6]
			term = end[3].split(',')[0].replace('term=', '')
			defn = end[3].split(',')[1].replace(' definition=', '')
			task = start[3].split('in ')[-1].replace('"', '')
			result.append({'user_id':int(row[1]), 'start' : start_time, 'end' : end_time, 'duration': end_time - start_time, 'term' : term, "def" : defn, "task" : task})
	return result

def create_char_duration():
	db = mysql.connector.connect(host="localhost",    # your host, usually localhost
	                     user="root",         # your username
	                     password="",  # your password
	                     database="author_production")        # name of the data base
	cur = db.cursor()
	cur.execute("SELECT DISTINCT user_id FROM user_logs")
	ids = cur.fetchall()
	dic = {}
	for user_id in ids:
		cur.execute("SELECT * FROM user_logs WHERE user_id = %s", (user_id))
		raw_data = cur.fetchall()
		data = []
		for row in raw_data:
			if row[2] == 'new character':
				if data == []:
					data.append(row)
				elif data[-1][2] == 'new character':
					data[-1] = row 
				else:
					data.append(row)
			if 'clicked on Save for' in row[2]:
				if data == []:
					pass
				elif data[-1][2] == 'new character' and data[-1][3] == row[2].replace('clicked on Save for ', '').replace('"',""):
					data.append(row)
				else:
					pass
		if (not data == []) and (data[-1][2] == 'new character'):
			del data[-1]
		if not data == []:
			dic[data[0][1]] = data
	db.close()
	result = []
	for item in dic:
		data = iter(dic[item])
		for row in data:
			start = row
			end = next(data)
			start_time = start[6]
			end_time = end[6]
			character = start[3]
			result.append({'user_id':int(row[1]), 'start' : start_time, 'end' : end_time, 'duration': end_time - start_time, 'character' : character})
	return result

def edit_term_duration():
	db = mysql.connector.connect(host="localhost",    # your host, usually localhost
	                     user="root",         # your username
	                     password="",  # your password
	                     database="author_production")        # name of the data base
	cur = db.cursor()
	cur.execute("SELECT DISTINCT user_id FROM user_logs")
	ids = cur.fetchall()
	dic = {}
	for user_id in ids:
		cur.execute("SELECT * FROM user_logs WHERE user_id = %s", (user_id))
		raw_data = cur.fetchall()
		data = []
		for row in raw_data:
			if 'clicked on "Edit Icon" on ' in row[2]:
				#print row
				if data == []:
					data.append(row)
				elif 'clicked on "Edit Icon" on ' in data[-1][2]:
					data[-1] = row 
				else:
					data.append(row)
			if row[2] == 'clicked the "Use This" button':
				#print row
				if data == []:
					pass
				elif not 'clicked on "Edit Icon" on ' in data[-1][2]:
					pass
				else:
					data.append(row)
			if row[2] == 'clicked the "Clone and Enhance" button':
				#print row
				if data == []:
					pass
				elif not 'clicked on "Edit Icon" on ' in data[-1][2]:
					pass
				else:
					data.append(row)
			if 'clicked on Save for ' in row[2]:
				if len(data) < 3:
					pass
				elif not 'clicked on "Edit Icon" on ' in data[-1][2]:
					pass
				elif not data[-1][2].replace('clicked on "Edit Icon" on ', "").replace('"', "") == row[2].replace('clicked on Save for ', "").replace('"', ""):
					pass
				elif not 'Edit Icon" on' in data[-3][2]:
					pass
				elif not data[-3][2].replace('clicked on "Edit Icon" on ', "").replace('"', "") == row[2].replace('clicked on Save for ', "").replace('"', ""):
					pass
				else:
					data.append(row)
			if 'clicked on Cancel for ' in row[2]:
				if data == []:
					pass
				elif not 'clicked on "Edit Icon" on ' in data[-1][2]:
					pass
				else:
					data.append(row)
		if (not data == []) and ('clicked on "Edit Icon" on ' in data[-1][2]):
			del data[-1]
		if not data == []:
			dic[data[0][1]] = data
	db.close()	
	result = []
	for item in dic:
		data = iter(dic[item])
		for row in data:
			start = row
			end = next(data)
			start_time = start[6]
			end_time = end[6]
			term = start[2].replace('clicked on "Edit Icon" on ', "").replace('"', "")
			action = end[2].replace(' "' + term + '"', "")
			result.append({'user_id':int(row[1]), 'start' : start_time, 'end' : end_time, 'duration': end_time - start_time, 'term' : term, 'action' : action})
	return result

def added_terms():
	
	db = mysql.connector.connect(host="localhost",    # your host, usually localhost
		                     user="root",         # your username
		                     password="",  # your password
		                     database="author_production")        # name of the data base
	cur = db.cursor()
	cur.execute("SELECT DISTINCT user_id FROM user_logs")
	ids = cur.fetchall()
	
	data = []
	tasks = []
	for user_id in ids:
		user_id = user_id
		cur.execute("SELECT * FROM user_logs WHERE user_id = %s", (user_id))
		raw_data = cur.fetchall()
		term = {
			'user_id':None,
			'task':None,
			'From' : None,
			'From_def' : None,
			'To' : None,
			'To_def' : None,
			'Include' : None,
			'Include_def' : None,
			'Exclude' : None,
			'Exclude_def' : None,
			'At' : None,
			'At_def' : None
			}
		for row in raw_data:
			if 'clicked on Save for' in row[2]:
				if not term == {}:
					term['user_id'] = user_id[0]
					term['task'] = row[2].split('"')[1]
					data.append(term)
					term = {
						'user_id':None,
						'task':None,
						'From' : None,
						'From_def' : None,
						'To' : None,
						'To_def' : None,
						'Include' : None,
						'Include_def' : None,
						'Exclude' : None,
						'Exclude_def' : None,
						'At' : None,
						'At_def' : None
						}
			elif 'In Method, added From' == row[2]:
				term['From'] = row[3]
			elif 'In Method, added To' == row[2]:
				term['To'] = row[3]
			elif 'In Method, added Include' == row[2]:
				term['Include'] = row[3]
			elif 'In Method, added Exclude' == row[2]:
				term['Exclude'] = row[3]
			elif 'In Method, added At' == row[2]:
				term['At'] = row[3]
			elif 'In Method, add definition for term' == row[2]:
				_value = row[3].split(',')[0].split('=')[-1]
				_term = row[3].split(',')[1].split('=')[-1]
				for key in list(term.keys()):
					if term[key] is not None and _value in term[key] and "_def" not in key:
						term[key+'_def'] = _term

	db.close()
	return data
	
	
# task_record
result = define_term_duration()
print("user_id, task, term, definition, completion_time")
for r in result:
	timeFormat = time.strptime(str(r['duration']),'%H:%M:%S')
	seconds = datetime.timedelta(hours=timeFormat.tm_hour,minutes=timeFormat.tm_min,seconds=timeFormat.tm_sec).total_seconds()
	print ('%s,%s,%s,%s,%s' % (r['user_id'], r['task'], r['term'], r['def'].split(" in")[0], seconds))

# task_duration
# result = create_char_duration()
# print("user_id, task, completion_time")
# for r in result:
# 	timeFormat = time.strptime(str(r['duration']),'%H:%M:%S')
# 	seconds = datetime.timedelta(hours=timeFormat.tm_hour,minutes=timeFormat.tm_min,seconds=timeFormat.tm_sec).total_seconds()	
# 	print('%s,%s,%s' % (r['user_id'], r['character'], seconds))

# Extra
# result = edit_term_duration()
# for r in result:
# 	print('user_id: %s, action: %s, start: %s, end: %s, duration: %s, term: %s' % (r['user_id'], r['action'], r['start'], r['end'], r['duration'], r['term']))

#term_record
# data=added_terms()
# exp = set([f.replace(".txt", "") for f in os.listdir("/Users/jinlonglin/Dropbox/JL/wikidata/all3Ontology") if os.path.isfile(os.path.join("/Users/jinlonglin/Dropbox/JL/wikidata/all3Ontology", f)) and f.endswith(".txt")])
# sys.stdout.write("user_id, tasks, filled, added, ignored\n")
# for d in data:
# 	filled=set()
# 	added=set()
# 	ignored=()
# 	sys.stdout.write('"%s","%s","' % (d['user_id'], d['task']))
# 	for k, v in d.items():
# 		if k == 'user_id' or k == 'task':
# 			continue
# 		if "def" not in k and v is not None:
# 			filled.add(v.split(" in")[0])
# 			continue
# 		if "def" in k and v is not None:
# 			added.add(d[k.replace("_def", "")].split(" in")[0])
# 	ignored = filled - added - exp
	
# 	for k in filled:
# 		sys.stdout.write('%s,' % (k))
# 	sys.stdout.write('","')
# 	for v in added:
# 		sys.stdout.write('%s,' % (v))
# 	sys.stdout.write('","')
# 	for k in ignored:
# 		sys.stdout.write('%s,' % (k))
# 	sys.stdout.write('"\n')


