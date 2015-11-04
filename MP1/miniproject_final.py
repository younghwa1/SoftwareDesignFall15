from pattern.web import *

g = Bing()
listurl = []
for result in g.search('Reflection lyrics'):
	listurl.append(result.url)

url = URL(string=listurl[0])

lyrics = url.download()
lyrics = plaintext(lyrics)

lyricslist = lyrics.split("\n")

num = 0
while num<len(lyricslist):
	text = lyricslist[num]
	lyricslist[num] = text.encode('ascii','ignore')
	num = num + 1


a = lyricslist.index('* Hands Of Love LyricsMiley Cyrus') + 1
list1 = lyricslist[a:]
#b = list1.index('Songwriters')
#list2 = list1[:b]


nm = 0
while nm<len(list1):
	string = list1[nm]
	list1[nm] = string.split()
	nm = nm + 1

num = 0
listnew = []
for i in range(len(list1)):
	listnew = listnew + list1[i]
print listnew


counts = {}
for i in listnew:
	if i in counts:
		counts[i] += 1
	else:
		counts[i] = 1

from collections import Counter
counter = Counter(counts)
print counter.most_common()