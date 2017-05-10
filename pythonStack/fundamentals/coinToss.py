# 
# import random
#
# def toss(reps):
#     # print new_toss
#     attempt_count = 1
#     head_count = 0
#     tail_count = 0
#     result = ""
#     result_string_complete = ""
#
#     for x in range(1, reps):
#         new_toss = random.randint(0,1)
#         if new_toss == 1:
#             head_count += 1
#             result = "head"
#             print "Attempt #", attempt_count, ": Throwing a coin... It's a ", result, "! Got ", head_count, "head(s) so far and", tail_count, "tail(s) so far"
#         else:
#             tail_count += 1
#             result = "tail"
#             print "Attempt #", attempt_count, ": Throwing a coin... It's a ", result, "! Got ", head_count, "head(s) so far and", tail_count, "tail(s) so far"
#         attempt_count += 1
#
# toss(101)


#### assign coin toss
import random
def coin_toss():
  num_heads = 0
  num_tails = 0
  for i in range (1, 5001):
    rand_num = round(random.random())
    if rand_num == 0:
      num_heads = num_heads + 1
      print "Attempt #{}: Throwing a coin... It's a head! ... Got {} head(s) so far and {} tail(s) so far".format(i, num_heads, num_tails)
    else:
      num_tails = num_tails + 1
      print "Attempt #{}: Throwing a coin... It's a tail! ... Got {} head(s) so far and {} tail(s) so far".format(i, num_heads, num_tails)

coin_toss()
