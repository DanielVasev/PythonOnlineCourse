

from collections import Counter


text = "It's a route map, but it's only big enough to get to the starting point. Many businesses have been asking\
 when they will be allowed to reopen. Now they have some rough indication, pencilled in to the calendar, but far from\
  all of them, and with distancing still required. In contrast with Boris Johnson's approach for England, Nicola\
   Sturgeon's statement at Holyrood was not a route map to a late summer of socialising, concerts, sports and travel.\
 The plan is far more cautious. Nicola Sturgeon's idea of release, maybe by late April, is to get through the doors\
  of a restaurant or bar. Both leaders had said they were putting data ahead of dates, but it was the prime minister's\
   dates that the public notice, remember and plan on. Travel bookings soared on Monday and Tuesday."


words = text.split()

counter = Counter(words)
top_three = counter.most_common(3)
print(top_three)


# print(words)
# sum = 1
# for n in words:
  #   print(n, sum )
   #  sum +=1

