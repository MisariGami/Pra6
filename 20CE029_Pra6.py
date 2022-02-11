# 20CE029 Misari Gami
# GitHub repository link : https://github.com/MisariGami/Pra6/blob/main/20CE029_Pra6.py

# You are given n words. Some words may repeat. For each word, output its number of occurrences. The output order should correspond with the input order of appearance of the word. See the sample input/output for clarification. 

# Sample Input 
# 4 
# bcdef 
# abcdefg 
# bcde 
# bcdef 

# Sample Output 
# 3 
# 2 1 1 

# Explanation: There are 3 distinct words. Here, "bcdef" appears twice in the input at the first and last positions. The other words appear once each. The order of the first appearances are "bcdef", "abcdefg" and "bcde" which corresponds to the output.


from collections import OrderedDict
# no of words in n
n = int(input())
word_list = OrderedDict()
lst = []
ans = ''

# appdend word into lst
for i in range(n):
    lst.append(input())

# count frequency of word in lst
for w in lst:
    if w not in word_list:
        word_list[w] = 1
    else:
        word_list[w] = word_list[w] + 1 

print(len(word_list))
for i in word_list:
    ans = ans + str(word_list[i]) + ' '
print(ans)
