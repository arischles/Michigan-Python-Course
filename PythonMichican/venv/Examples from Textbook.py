#Count the number of characters in string str1. Do not use len(). Save the number in variable numbs.

str1 = "I like nonsense, it wakes up the brain cells. Fantasy is a necessary ingredient in living."
numbs = 0
for i in str1:
    numbs += 1
print(numbs)


#Create a list of numbers 0 through 40 and assign this list to the variable numbers. Then, accumulate the total of the list’s values and assign that sum to the variable sum1.
numbers = range(41)
accum = 0
for sum1 in range(41):
    accum+=sum1 #aka accum = accum + sum1
print(accum)


#how many times is the letter P printed...ANSWER is 3 times.
s = "python"
for idx in range(len(s)):
   print(s[idx % 2])

#printing intermediate results...This will help making code easier to understand and read!
    #Block1
w = range(10)
tot = 0
for num in w:
    tot += num
print(tot)

    # Block2
w = range(10)
tot = 0
for num in w:
    print(num)
    tot += num
print(tot)

    # Block3
w = range(10)
tot = 0
for num in w:
    print(num)
    tot += num
    print(tot)
print(tot)

    # Block4
w = range(10)
tot = 0
print("***** Before the For Loop ******")
for num in w:
    print("***** A New Loop Iteration ******")
    print("Value of num:", num)
    tot += num
    print("Value of tot:", tot)
print("***** End of For Loop *****")
print("Final total:", tot)

#Keeping Track of Your Iterator Variable and Your Iterable¶ EXAMPLE
item = ["M", "I", "S", "S", "O", "U", "R", "I"]
for val in item:
    val = val + "!"
    print(val)

#Write one for loop to print out each character of the string my_str on a separate line.
my_str = "MICHIGAN"
for num in my_str:
    print(num)

#Write one for loop to print out each element of the list several_things. Then, write another for loop to print out the TYPE of each element of the list several_things. To complete this problem you should have written two different for loops, each of which iterates over the list several_things, but each of those 2 for loops should have a different result.
several_things = ["hello", 2, 4, 6.0, 7.5, 234352354, "the end", "", 99]

for elem in several_things:
    print(elem)

for elem2 in several_things:
    print(type(elem2))

#Write code that uses iteration to print out the length of each element of the list stored in str_list.
str_list = ["hello", "", "goodbye", "wonderful", "I love Python"]
accum = 0
for c in str_list:
    accum = len(c)
    print(accum)

#Write code to count the number of characters in original_str using the accumulation pattern and assign the answer to a variable num_chars. NO len func
original_str = "The quick brown rhino jumped over the extremely lazy fox."

num_chars = 0
for c in original_str:
    num_chars+=1
print(num_chars)

#addition_str is a string with a list of numbers separated by the + sign. Write code that uses the accumulation pattern to take the sum of all of the numbers and assigns it to sum_val (an integer). (You should use the .split("+") function to split by "+" and int() to cast to an integer).
addition_str = "2+5+10+20"
addition_str_spliz = addition_str.split("+")

sum_val = 0
for i in addition_str_spliz:
    sum_val+=int(i)
    #print(sum_val)
print(sum_val)


#week_temps_f is a string with a list of fahrenheit temperatures separated by the , sign. Write code that uses the accumulation pattern to compute the average (sum divided by number of items) and assigns it to avg_temp. Do not hard code your answer (i.e., make your code compute both the sum or the number of items in week_temps_f) (You should use the .split(",") function to split by "," and float() to cast to a float).
week_temps_f = "75.1,77.7,83.2,82.5,81.0,79.5,85.7"
week_temps_f_spliz = week_temps_f.split(",")

avg_temp = 0
n = 0
for tot in week_temps_f_spliz:
    avg_temp+=(float(tot))
    n+=1
#print(avg_temp)
#print(n)
print(avg_temp/n)

