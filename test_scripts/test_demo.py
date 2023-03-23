from pyjavaproperties import Properties

pfile=Properties()
pfile.load(open('../config.properties'))
v=pfile['city']
print(v)
