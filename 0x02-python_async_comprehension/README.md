Python's support for async/await comprehension goes a step further to make this dynamic concept even sweeter and cleaner
instead of writing
for i in iter():
    if i % 2:
	myList.append(i)
we can do this :-
myList = [i async for i in iter() if i % 2]
