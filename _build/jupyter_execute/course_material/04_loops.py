#!/usr/bin/env python
# coding: utf-8

# # Loops
# 
# ## `while` loop
# 
# You can make a block of code execute over and over again with a `while` statement. The code in a `while` clause will be executed as long as the `while` statement’s condition is `True`. In code, a `while` statement always consists of the following:
# 
# - The `while` keyword
# 
# - A condition (that is, an expression that evaluates to `True` or `False`)
# 
# - A colon(**:**)
# 
# - Starting on the next line, an indented block of code (called the `while` clause)
# 
# You can see that a `while` statement looks similar to an `if` statement. The difference is in how they behave. At the end of an `if` clause, the program execution continues after the `if` statement. But at the end of a `while` clause, the program execution jumps back to the start of the `while` statement. The `while` clause is often called the *while loop* or just the loop.
# 
# Let’s look at an `if` statement and a `while` loop that use the same condition and take the same actions based on that condition.

# In[1]:


# Here is the code with an 'if' statement:

value = 0
if value < 5:
    print('Hello, world.')
    value = value + 1


# In[2]:


# Here is the code with a 'while' statement:

value = 0
while value < 5:
    print('Hello, world.')
    value = value + 1


# These statements are similar—both `if` and `while` check the `value` variable, and if it’s less than five, they print a message. But when you run these two code snippets, something very different happens for each one. For the `if` statement, the output is simply `"Hello, world."`. But for the `while` statement, it’s `"Hello, world."` repeated five times! Take a look at the flowcharts for these two pieces of code, to see why this happens.
# 
# ![](../images/000091.png) 

# In the `while` loop, the condition is always checked at the start of each iteration (that is, each time the loop is executed). If the condition is `True`, then the clause is executed, and afterward, the condition is checked again. The first time the condition is found to be `False`, the `while` clause is skipped.

# #### An annoying `while` Loop
# Here’s a small example program that will keep asking you to type, literally, *your name*.

# In[1]:


name = '' 
while name != 'your name':
    print('Please type your name')
    name = input() 
print('thank you!') 


# First, the program sets the `name` variable to an empty string. This is so that the `name != 'your name'` condition will evaluate to `True` and the program execution will enter the `while` loop’s clause.
# 
# The code inside this clause asks the user to type their name, which is assigned to the `name` variable. Since this is the last line of the block, the execution moves back to the start of the while loop and reevaluates the condition. If the value in `name` is not equal to the string `'your name'`, then the condition is `True`, and the execution enters the `while` clause again.
# 
# But once the user types `'your name'`, the condition of the `while` loop will evaluate to `False`. Instead of  re-entering the `while` loop’s clause, the program execution will skip past it and continues running the rest of the program.

# If you never enter `your name`, then the `while` loop’s condition will never be `False`, and the program will just keep asking forever. Here, the `input()` call lets the user enter the right string to make the program move on. In other programs, the condition might never actually change, and that can be a problem.

# ## `for` loop
# 
# The `while` loop keeps looping while its condition is `True` (which is the reason for its name), but what if you want to execute a block of code only a certain number of times? You can do this with a `for` loop statement and the `range()` function.
# 
# In code, a `for` statement looks something like `for i in range(5):` and always includes the following:
# 
# - The `for` keyword
# 
# - A *variable name*
# 
# - The `in` keyword
# 
# - A call to the `range()` method with up to three integers passed to it
# 
# - A colon(:)
# 
# - Starting on the next line, an indented block of code (called the `for` clause)
# 
# This is how the complete code looks like . . . 

# In[2]:


print('My name is')
for i in range(5):
    print('Rahul Five Times (' + str(i) + ')')


# The code in the `for` loop’s clause is run five times. The first time it is run, the variable `i` is set to 0. The `print()` call in the clause will print `Rahul Five Times (0)`. After Python finishes an iteration through all the code inside the `for` loop’s clause, the execution goes back to the top of the loop, and the `for` statement increments `i` by one. This is why `range(5)` results in five iterations through the clause, with `i` being set to 0, then 1, then 2, then 3, and then 4. The variable `i` will go up to, but will not include, the integer passed to `range()`.
# 
# ![](../images/000102.png)

# #### An equivalent `while` Loop
# 
# You can actually use a `while` loop to do the same thing as a `for` loop; for loops are just more concise. Let’s rewrite it, to use a `while` loop equivalent of a `for` loop.

# In[1]:


print('My name is')
i = 0
while i < 5:
    print('Rahul Five Times (' + str(i) + ')')
    i = i+1


# Here is another example, consider that you have to sum all the numbers from 0 to 100. You can easily do it, in just few seconds, using `for` loop. Here is the working code . . .

# In[6]:


total = 0 
for num in range(101): 
    total = total + num 
print(total) 


# When the program first starts, the `total` variable is set to 0. The `for` loop then executes `total = total + num` 100 times. By the time the loop has finished all of its 100 iterations, every integer from 0 to 100 will have been added to `total`. At this point, `total` is printed to the screen. Even on the slowest computers, this program takes less than a second to complete.

# ## `range()` function
# 
# Some functions can be called with multiple arguments separated by a comma, and `range()` is one of them. This lets you change the integer passed to `range()` to follow any sequence of integers, including starting at a number other than zero.

# In[7]:


for i in range(12, 16):
    print(i)


# The first argument will be where the `for` loop’s variable *starts*, and the second argument will be *upto*, but not including, the number to stop at.
# 
# The `range()` function can also be called with **three arguments**. The first two arguments will be the *start* and *stop* values, and the third will be the *step* argument. The *step* is the amount that the variable is increased by after each iteration.

# In[8]:


for i in range(0, 10, 2):
    print(i)


# So calling `range(0, 10, 2)` will count from zero to eight by intervals of two.
# 
# The `range()` function is extremely flexible in the sequence of numbers it can produce. For example, you can even use a negative number for the *step* argument to make the `for` loop count down instead of up.

# In[9]:


for i in range(5, -1, -1):
    print(i)


# Running a `for` loop to print `i` with `range(5, -1, -1)` should print from five down to zero.

# Let’s look at how you can break out of any loop.

# ## `break` statement
# 
# The `break` statement breaks-out of the loop entirely.
# 
# Here is an example of a `break` statement used for a less trivial task. This loop will print even numbers.

# In[3]:


for n in range(20):
    if n % 2 == 0:
        print(n, end=' ')
        break


# ## `continue` statement
# 
# The `continue` statement skips the remainder of the current loop, and goes to the next iteration. These can be used in both `for` and `while` loops.
# 
# Here is an example of using `continue` to print a string of odd numbers.

# In[1]:


for n in range(20):
    if n % 2 == 0:
        continue
    print(n, end=' ')


# In this case, the result could be accomplished just as well with an `if-else` statement, but sometimes the `continue` statement can be a more convenient way to express the idea you have in mind.

# ## Conclusion
# 
# You can execute code over and over again in a loop while a certain condition evaluates to `True`.
# 
# ### Questionaire
# 
# 1. How `while` loop is different than `for` loop?
# 2. Define `range()` function in python and also its arguments.
# 3. How to use `break` and `continue` statements in a loop?
# 4. What loop is used to create *infinite* loop
# 5. Can we use float value in step in `range()`?
