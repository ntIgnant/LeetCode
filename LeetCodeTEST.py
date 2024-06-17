# address = "255.100.50.0"
# listed_addr = list(address)
# print(listed_addr)
#
# for x in range(len(listed_addr)):
#     if listed_addr[x] == ".":
#         listed_addr[x] = "[.]"
# 
# # Joining the modified list back into a string
# modified_address = "".join(listed_addr)
# print(modified_address)
"-------------------------------------"
# operations = ["--X","X++","X++"]
# X = 0
# for element in operations:
#     if element == "++X" or element == "X++":
#         X += 1
#     elif element == "--X" or element == "X--":
#         X -= 1

# print(X)
"-------------------------------------"
# jewels = "aA"
# stones = "aAAbbbb"
# counter = 0

# for x in stones:
#     for y in jewels:
#         if x == y:
#             counter += 1
# print(counter)
"-------------------------------------"
# words = ["leet","code"]
# x = "e"
# output = []

# for my_ch, word in enumerate(words):
#     if x in word:
#         output.append(my_ch)
# print(output)
"-------------------------------------"
# command = "G()(al)"
# mydict={"G":"G","()":"o","(al)":"al"}
# output = ""
# for key in mydict:
#     command = command.replace(key,mydict[key])
# output = command
# print(output)
"-------------------------------------"
# sentences = ["w jrpihe zsyqn l dxchifbxlasaehj","nmmfrwyl jscqyxk a xfibiooix xolyqfdspkliyejsnksfewbjom","xnleojowaxwpyogyrayfgyuzhgtdzrsyococuqexggigtberizdzlyrdsfvryiynhg","krpwiazoulcixkkeyogizvicdkbrsiiuhizhkxdpssynfzuigvcbovm","rgmz rgztiup wqnvbucfqcyjivvoeedyxvjsmtqwpqpxmzdupfyfeewxegrlbjtsjkusyektigr","o lgsbechr lqcgfiat pkqdutzrq iveyv iqzgvyddyoqqmqerbmkxlbtmdtkinlk","hrvh efqvjilibdqxjlpmanmogiossjyxepotezo","qstd zui nbbohtuk","qsdrerdzjvhxjqchvuewevyzlkyydpeeblpc"]

# MXnum = 0
# count = []
# for item in sentences:
#     words = item.split(" ")
#     for x in words:
#         if x == " ":
#             count += 1
# count.append(count)
# MXnum = max(count)
# print(MXnum)
"-------------------------------------"
# s = "RLRRRLLRLL"
# Rs = 0
# Ls = 0
# maximum = 0
# for char in s:
#     if char == "R":
#         Rs += 1
#     else:
#         Ls += 1
#     if Rs == Ls:
#         maximum += 1
# print(maximum)
"-------------------------------------"
# word1 = ["ab", "c"]
# word2 = ["a", "bc"]
#
# w1 = "".join(word1)
# w2 = "".join(word2)
# if w1 == w2:
#     print("true")
# elif w1 != w2:
#     print("false")
#
# print(w1)
# print(w2)
"-------------------------------------"
# word1 = ["abc", "d", "defg"]
# word2 = ["abcddefg"]
#
# w1 = "".join(word1)
# w2 = "".join(word2)
# if w1 == w2:
#     A = True
# elif w1 != w2:
#     A = False
#
# print(A)
"-------------------------------------"
# s = "codeleet"
# indices = [4,5,6,7,0,2,1,3]
# new_indices = sorted(indices)
# print(new_indices) #I need to sort the inidce just at the senond half, when it statrs from 0 again
#
# word = ""
# for num in indices:
#     word += s[num]
# print(word)
#
# #UNSOLVED!
"-------------------------------------"
#https://leetcode.com/problems/truncate-sentence/description/
#
# s = "Hello how are you Contestant"
# k = 4
#
# separated_str = s.split(" ")
# sentence = separated_str[0:k]
# sentence = " ".join(sentence)
# # for word in separated_str:
#
# print(sentence)
"-------------------------------------"
#https://leetcode.com/problems/find-first-palindromic-string-in-the-array/description/
#Retunr the value of the first palandomic word of the list

# words = ["abc","car","ada","racecar","cool"]
#
# palindome = ""
# for word in words:
#     if word == word[::-1]:
#         palindome = word
#         break
#
# print(palindome)
"-------------------------------------"
#https://leetcode.com/problems/cells-in-a-range-on-an-excel-sheet/description/
# s = "K1:L2"
#
# letters = []
# nums = []
# cells = []
# for char in s:
#     if char.isdigit():
#         nums.append(int(char))
#     elif char.isalpha():
#         letters.append(char)
# max_num = max(nums)
# for x in range(max_num):
#     cells.append((letters[x], str(x+1)))
#
# print(cells)
#
# #!UNSOLVED
"-------------------------------------"
# #Replace the characters to lowercase
#
# s = "Hello"
# sl = s.lower()
# print(sl)
"-------------------------------------"
# # https://leetcode.com/problems/check-if-the-sentence-is-pangram/description/
# #Find if the sentence is a Paragram (every letter of the alphabet appears at least once)
#
# sentence = "thequickbrownfoxjumpsoverthelazydog"
# alp = "abcdefghijklmnopqrstuvwxyz"
# unique_ch = set(sentence)
# sorted_ch = sorted(unique_ch)
# sorted_ch = "".join(sorted_ch)
#
# if alp == sorted_ch:
#     result = True
# else:
#     result = False
# print(result)
"-------------------------------------"
# # https://leetcode.com/problems/reverse-words-in-a-string-iii/description/
# #Reverse each word of a string but without changing the order of the whole sentence.
#
# s = "Let's take LeetCode contest"
# divided_str = s.split(" ")
# for x in range(len(divided_str)):
#     divided_str[x] = divided_str[x][::-1]
#
# reversed_str = " ".join(divided_str)
# print(reversed_str)
"-------------------------------------"
# # https://leetcode.com/problems/convert-the-temperature/description/
# # You are given a non-negative floating point number rounded to two decimal places celsius, that denotes the temperature in Celsius.
#
# celsius = 36.50
# values = []
#
# Kelvin_val = celsius + 273.15
# values.append(Kelvin_val)
# Fahrenheit_val = celsius * 1.80 + 32.00
# values.append(Fahrenheit_val)
#
# print(values)
"-------------------------------------"
# # https://leetcode.com/problems/number-of-good-pairs/description/
# # Given an array of integers nums, return the number of good pairs.
# # A pair (i, j) is called good if nums[i] == nums[j] and i < j.
#
# nums = [1,2,3,1,1,3]
# count = {}
# good_pairs = 0
#
# for num in nums:
#     if num in count:
#         count[num] += 1
#     else:
#         count[num] = 1
#
# for key, value in count.items():
#     good_pairs += (value * (value - 1)) // 2
#
# print(good_pairs)
"-------------------------------------"
# # https://leetcode.com/problems/divisible-and-non-divisible-sums-difference/description/
# #
#
# n = 10
# m = 3
#
# num_sum = []
# for num_n in range(1, n+1):
#     if num_n % m == 0:
#         num_sum.append(num_n)
#
# final_sum = sum(num_sum)
# print(final_sum)
# #UNSOLVED!
"-------------------------------------"
# https://leetcode.com/problems/count-the-number-of-consistent-strings/description/


# allowed = "ab"
# words = ["ad","bd","aaab","baa","badab"]
#
# ord_allowed = sorted(allowed)
# ord_allowed = ''.join(ord_allowed)
# ord_words = sorted(words)
#
# unique_words = []
# for word in words:
#     values = "".join(set(ord_words))
#     unique_words.append(values)
#
# print(unique_words)
# UNSOLVED!
"-------------------------------------"
# https://leetcode.com/problems/concatenation-of-array/description/

# nums = [1,3,2,1]
# num_array = []
# for x in range(0, 2):
#     for num in nums:
#         num_array.append(num)

# print(num_array)
"-------------------------------------"











