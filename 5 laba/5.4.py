import json
import pandas

file = input('json2csv: ')
x = open(file, 'r', encoding='utf-8')
f_p = pandas.DataFrame(json.load(x))
x.close()
f_p.to_csv(file.replace('.json', '.csv'), index=False)
