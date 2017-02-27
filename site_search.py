#Export your bookmarks as 'bookmarks.json'
import json

#load the compromised sites
tfile = open('sorted_unique_cf.txt','r')
compromised = tfile.read()
tfile.close()

#load bookmarked sites
tfile = open('bookmarks.json','r')
used = tfile.read()
tfile.close()

compromised = compromised.split('\n')
used = json.loads(used)

#This drills into sub-dictionaries and sub-arrays to find values of the key 'k'
def d_search(d,k):
  if isinstance(d,dict):
    for i in d:
      if i == k:
        yield d[i]
      elif type(d[i]) in [type({}),type([])]:
        yield from d_search(d[i],k)
  elif isinstance(d,list):
    for i in d:
      if type(i) in [type({}),type([])]:
        yield from d_search(i,k)

used = list(d_search(used,'uri'))

#sort both lists for faster intersection computation
used.sort()
compromised.sort()

#This is the actual comparison. Using a set ensures unique results.
results = set()
k = 0
for i in used:
  try:
    while(k < len(compromised) and i.split('/')[2] >= compromised[k]):
      if i.split('/')[2] == compromised[k]:
        results.add(compromised[k])
        #print(compromised[k])
      k += 1
  except (Exception):
    pass
    #print('Exception:',i)

[print(i) for i in results]
