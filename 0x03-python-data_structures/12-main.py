0x03. Python - Data Structures: Lists, Tuples

Python

 By: Guillaume Weight: 1 Project will start Dec 1, 2023 6:00 AM, must end by Dec 5, 2023 6:00 AM Checker was released at Dec 2, 2023 6:00 AM An auto review will be launched at the deadline

Resources

Read or watch:

3.1.3. ListsData structures (until 5.3. Tuples and Sequences included)Learn to Program 6 : ListsLearning Objectives

At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

GeneralWhy Python programming is awesomeWhat are lists and how to use themWhat are the differences and similarities between strings and listsWhat are the most common methods of lists and how to use themHow to use lists as stacks and queuesWhat are list comprehensions and how to use themWhat are tuples and how to use themWhen to use tuples versus listsWhat is a sequenceWhat is tuple packingWhat is sequence unpackingWhat is the del statement and how to use itCopyright - PlagiarismYou are tasked to come up with solutions for the tasks below yourself to meet with the above learning objectives.You will not be able to meet the objectives of this or any following project by copying and pasting someone else’s work.You are not allowed to publish any content of this project.Any form of plagiarism is strictly forbidden and will result in removal from the program.RequirementsPython ScriptsAllowed editors: vi, vim, emacsAll your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)All your files should end with a new lineThe first line of all your files should be exactly #!/usr/bin/python3A README.md file, at the root of the folder of the project, is mandatoryYour code should use the pycodestyle (version 2.8.*)All your files must be executableThe length of your files will be tested using wcCAllowed editors: vi, vim, emacsAll your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)All your files should end with a new lineYour code should use the Betty style. It will be checked using betty-style.pl and betty-doc.plYou are not allowed to use global variablesNo more than 5 functions per fileIn the following examples, the main.cfiles are shown as examples. You can use them to test your functions, but you don’t have to push them to your repo (if you do we won’t take them into account). We will use our own main.c files at compilation. Our main.c files might be different from the one shown in the examplesThe prototypes of all your functions should be included in your header file called lists.hDon’t forget to push your header fileAll your header files should be include guarded

Quiz questions

Great! You've completed the quiz successfully! Keep going! (Show quiz)

Tasks

0. Print a list of integers

mandatory

Write a function that prints all integers of a list.

Prototype: def print_list_integer(my_list=[]):Format: one integer per line. See exampleYou are not allowed to import any moduleYou can assume that the list only contains integersYou are not allowed to cast integers into stringsYou have to use str.format() to print integersguillaume@ubuntu:~/0x03$ cat 0-main.py #!/usr/bin/python3 print_list_integer = __import__('0-print_list_integer').print_list_integer my_list = [1, 2, 3, 4, 5] print_list_integer(my_list) guillaume@ubuntu:~/0x03$ ./0-main.py 1 2 3 4 5 guillaume@ubuntu:~/0x03$ 

Repo:

GitHub repository: alx-higher_level_programmingDirectory: 0x03-python-data_structuresFile: 0-print_list_integer.py

 Done? Help Check your codeGet a sandbox

1. Secure access to an element in a list

mandatory

Write a function that retrieves an element from a list like in C.

Prototype: def element_at(my_list, idx):If idx is negative, the function should return NoneIf idx is out of range (> of number of element in my_list), the function should return NoneYou are not allowed to import any moduleYou are not allowed to use try/exceptguillaume@ubuntu:~/0x03$ cat 1-main.py #!/usr/bin/python3 element_at = __import__('1-element_at').element_at my_list = [1, 2, 3, 4, 5] idx = 3 print("Element at index {:d} is {}".format(idx, element_at(my_list, idx))) guillaume@ubuntu:~/0x03$ ./1-main.py Element at index 3 is 4 guillaume@ubuntu:~/0x03$ 

Repo:

GitHub repository: alx-higher_level_programmingDirectory: 0x03-python-data_structuresFile: 1-element_at.py

 Done? Help Check your codeGet a sandbox

2. Replace element

mandatory

Write a function that replaces an element of a list at a specific position (like in C).

Prototype: def replace_in_list(my_list, idx, element):If idx is negative, the function should not modify anything, and returns the original listIf idx is out of range (> of number of element in my_list), the function should not modify anything, and returns the original listYou are not allowed to import any moduleYou are not allowed to use try/exceptguillaume@ubuntu:~/0x03$ cat 2-main.py #!/usr/bin/python3 replace_in_list = __import__('2-replace_in_list').replace_in_list my_list = [1, 2, 3, 4, 5] idx = 3 new_element = 9 new_list = replace_in_list(my_list, idx, new_element) print(new_list) print(my_list) guillaume@ubuntu:~/0x03$ ./2-main.py [1, 2, 3, 9, 5] [1, 2, 3, 9, 5] guillaume@ubuntu:~/0x03$ 

Repo:

GitHub repository: alx-higher_level_programmingDirectory: 0x03-python-data_structuresFile: 2-replace_in_list.py

 Done? Help Check your codeGet a sandbox

3. Print a list of integers... in reverse!

mandatory

Write a function that prints all integers of a list, in reverse order.

Prototype: def print_reversed_list_integer(my_list=[]):Format: one integer per line. See exampleYou are not allowed to import any moduleYou can assume that the list only contains integersYou are not allowed to cast integers into stringsYou have to use str.format() to print integersguillaume@ubuntu:~/0x03$ cat 3-main.py #!/usr/bin/python3 print_reversed_list_integer = __import__('3-print_reversed_list_integer').print_reversed_list_integer my_list = [1, 2, 3, 4, 5] print_reversed_list_integer(my_list) guillaume@ubuntu:~/0x03$ ./3-main.py 5 4 3 2 1 guillaume@ubuntu:~/0x03$ 

Repo:

GitHub repository: alx-higher_level_programmingDirectory: 0x03-python-data_structuresFile: 3-print_reversed_list_integer.py

 Done? Help Check your codeGet a sandbox

4. Replace in a copy

mandatory

Write a function that replaces an element in a list at a specific position without modifying the original list (like in C).

Prototype: def new_in_list(my_list, idx, element):If idx is negative, the function should return a copy of the original listIf idx is out of range (> of number of element in my_list), the function should return a copy of the original listYou are not allowed to import any moduleYou are not allowed to use try/exceptguillaume@ubuntu:~/0x03$ cat 4-main.py #!/usr/bin/python3 new_in_list = __import__('4-new_in_list').new_in_list my_list = [1, 2, 3, 4, 5] idx = 3 new_element = 9 new_list = new_in_list(my_list, idx, new_element) print(new_list) print(my_list) guillaume@ubuntu:~/0x03$ ./4-main.py [1, 2, 3, 9, 5] [1, 2, 3, 4, 5] guillaume@ubuntu:~/0x03$ 

Repo:

GitHub repository: alx-higher_level_programmingDirectory: 0x03-python-data_structuresFile: 4-new_in_list.py

 Done? Help Check your codeGet a sandbox

5. Can you C me now?

mandatory

Write a function that removes all characters cand C from a string.

Prototype: def no_c(my_string):The function should return the new stringYou are not allowed to import any moduleYou are not allowed to use str.replace()guillaume@ubuntu:~/0x03$ cat 5-main.py #!/usr/bin/env python3 no_c = __import__('5-no_c').no_c print(no_c("Best School")) print(no_c("Chicago")) print(no_c("C is fun!")) guillaume@ubuntu:~/0x03$ ./5-main.py Best Shool hiago is fun! guillaume@ubuntu:~/0x03$ 

Repo:

GitHub repository: alx-higher_level_programmingDirectory: 0x03-python-data_structuresFile: 5-no_c.py

 Done? Help Check your codeGet a sandbox

6. Lists of lists = Matrix

mandatory

Write a function that prints a matrix of integers.

Prototype: def print_matrix_integer(matrix=[[]]):Format: see exampleYou are not allowed to import any moduleYou can assume that the list only contains integersYou are not allowed to cast integers into stringsYou have to use str.format() to print integersguillaume@ubuntu:~/0x03$ cat 6-main.py #!/usr/bin/python3 print_matrix_integer = __import__('6-print_matrix_integer').print_matrix_integer matrix = [ [1, 2, 3], [4, 5, 6], [7, 8, 9] ] print_matrix_integer(matrix) print("--") print_matrix_integer() guillaume@ubuntu:~/0x03$ ./6-main.py | cat -e 1 2 3$ 4 5 6$ 7 8 9$ --$ $ guillaume@ubuntu:~/0x03$ 

Repo:

GitHub repository: alx-higher_level_programmingDirectory: 0x03-python-data_structuresFile: 6-print_matrix_integer.py

 Done? Help Check your codeGet a sandbox

7. Tuples addition

mandatory

Write a function that adds 2 tuples.

Prototype: def add_tuple(tuple_a=(), tuple_b=()):Returns a tuple with 2 integers:The first element should be the addition of the first element of each argumentThe second element should be the addition of the second element of each argumentYou are not allowed to import any moduleYou can assume that the two tuples will only contain integersIf a tuple is smaller than 2, use the value 0 for each missing integerIf a tuple is bigger than 2, use only the first 2 integersguillaume@ubuntu:~/0x03$ cat 7-main.py #!/usr/bin/python3 add_tuple = __import__('7-add_tuple').add_tuple tuple_a = (1, 89) tuple_b = (88, 11) new_tuple = add_tuple(tuple_a, tuple_b) print(new_tuple) print(add_tuple(tuple_a, (1, ))) print(add_tuple(tuple_a, ())) guillaume@ubuntu:~/0x03$ ./7-main.py (89, 100) (2, 89) (1, 89) guillaume@ubuntu:~/0x03$ 

Repo:

GitHub repository: alx-higher_level_programmingDirectory: 0x03-python-data_structuresFile: 7-add_tuple.py

 Done? Help Check your codeGet a sandbox

8. More returns!

mandatory

Write a function that returns a tuple with the length of a string and its first character.

Prototype: def multiple_returns(sentence):If the sentence is empty, the first character should be equal to NoneYou are not allowed to import any moduleguillaume@ubuntu:~/0x03$ cat 8-main.py #!/usr/bin/python3 multiple_returns = __import__('8-multiple_returns').multiple_returns sentence = "At school, I learnt C!" length, first = multiple_returns(sentence) print("Length: {:d} - First character: {}".format(length, first)) guillaume@ubuntu:~/0x03$ ./8-main.py Length: 22 - First character: A guillaume@ubuntu:~/0x03$ 

Repo:

GitHub repository: alx-higher_level_programmingDirectory: 0x03-python-data_structuresFile: 8-multiple_returns.py

 Done? Help Check your codeGet a sandbox

9. Find the max

mandatory

Write a function that finds the biggest integer of a list.

Prototype: def max_integer(my_list=[]):If the list is empty, return NoneYou can assume that the list only contains integersYou are not allowed to import any moduleYou are not allowed to use the builtin max()guillaume@ubuntu:~/0x03$ cat 9-main.py #!/usr/bin/python3 max_integer = __import__('9-max_integer').max_integer my_list = [1, 90, 2, 13, 34, 5, -13, 3] max_value = max_integer(my_list) print("Max: {}".format(max_value)) guillaume@ubuntu:~/0x03$ ./9-main.py Max: 90 guillaume@ubuntu:~/0x03$ 

Repo:

GitHub repository: alx-higher_level_programmingDirectory: 0x03-python-data_structuresFile: 9-max_integer.py

 Done? Help Check your code


