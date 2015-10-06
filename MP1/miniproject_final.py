from pattern.web import *

g = Bing()
listurl = []
# it would be cool if you took the song title as a user input
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
	# when you use a while loop with a counter like this,
	# this is exactly the point at which you would use a for loop
	# it's what they were made for
	# this works, but a for loop woulld be considered more appropriate


a = lyricslist.index('Get "Reflection" Ringtone') + 1
list1 = lyricslist[a:]
b = list1.index('Songwriters')
list2 = list1[:b]
# as you pointed out in your reflection, this is 
# very specific both to the song you pick and the website you pull from
# thinking more about ways to make this work always no matter the song or website would be good

nm = 0
while nm<len(list2):
	string = list2[nm]
	list2[nm] = string.split()
	nm = nm + 1

num = 0 # this variable doesn't get used
listnew = []
for i in range(len(list2)):
	listnew = listnew + list2[i]

# these two loops are well cone and work well to make the list of words you want
# but in terms of efficiency, you could have combined them and added to listnew
# inside of the while loop, instead of having two separate loops


counts = {}
for i in listnew:
	if i in counts:
		counts[i] += 1
	else:
		counts[i] = 1

from collections import Counter
counter = Counter(counts)
print counter.most_common()