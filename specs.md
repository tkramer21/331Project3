# Project 3: Doubly Linked Lists

**Due: Wednesday, September 28th @ 10:00PM ET**

*This is not a team project. Do not copy someone else’s work.*

# Assignment Overview

Doubly linked lists (DLLs) are a fundamental data structure used to store sequential information. DLLs consist of a chain of *nodes* linked to one another by *forward* and *backward* references, such that one may traverse the chain from the *head* to the *tail*, or vice-versa. Each node stores a *value*, which may be a number, string, or more complex object.

![](img/basic_DLL.png)

Traditional *arrays* provide a simpler means for storing sequential information, but come with a major drawback which DLLs avoid: arrays require contiguous blocks of memory, while DLLs may utilize memory wherever it is available. In settings where data is updated, manipulated or deleted frequently, DLLs outperform traditional arrays by avoiding the need for memory reallocation. [This article](https://www.geeksforgeeks.org/linked-list-vs-array/) gives a nice overview of the distinction between DLLs and arrays.

Also see [Zybooks](https://learn.zybooks.com/zybook/MSUCSE331OnsayFall2022/chapter/19/section/5) if you need further review of DLL.



# Assignment Notes
1. Time **and** space complexity account for 30% of the points on Project 3. Be sure to review the rubric and adhere to complexity requirements!
2. Docstrings (the multi-line comments beneath each function header) are NOT provided in Project 3 and will need to be completed for full credit.
3. Testcases are your friend: before asking about the form of input/output or what happens in a particular edge case, check to see if the testcases answer your question for you. By showing the expected output in response to each input, they supplement the specs provided here.
4. Don't be afraid to go to D2L Course Tools for tutorial videos on how to debug,  it will help you figure out where you're going wrong far more quickly than ad-hoc print statements!
5. Throughout the specs, we mention Python double-underscore "magic" methods. These are central to the structure of object-oriented programming in Python, and will continue to appear in future projects in CSE 331 and beyond. [This page](https://rszalski.github.io/magicmethods/) is a great reference if you'd like to learn more about how they work!
6. There are two functions which may seem a little odd to you *_find_nodes* and *_remove_node*. These functions are intended as helper functions to help you reuse code and allow you to practice writing modular code.
7. We **strongly** encourage you to avoid calling remove\_first in remove\_all. Why? It's far less efficient to repeatedly call remove\_first, as each call to remove\_first begins searching at the beginning of the list. In the worst case, this will lead our function to operate with O(n^2) time complexity, **violating the required time complexity.**
8. We **strongly** encourage you to implement reverse in-place, without creating any new Node objects and instead rearranging prev and next pointers. Why? It's far less efficient to rebuild the DLL than it is to simply adjust references, as it's far more work to construct a brand new Node object than it is to simply adjust an existing one's references.
9. In the testcases for this project, you will notice the use of assertEqual and assertIs. What's the difference? It ties back to the difference between == and is in Python. The double-equal sign compares *values* in Python, while the is operator compares *memory addresses* in Python. Put simply, the is keyword is stronger than ==: if two objects are at the same memory address, they must contain the same value. However, it is possible for two objects *not* at the same memory address to have the same value. In other words, if a is b then we know a == b as well, but if a == b we cannot conclude a is b. A great read on the subject is [available here](https://realpython.com/courses/python-is-identity-vs-equality/).

# Assignment Specifications

**class Node:**

*DO NOT MODIFY the following attributes/functions*

- **Attributes**
  - **value: T:** Value held by the Node. Note that this may be any type, such as a str, int, float, dict, or a more complex object.
  - **next: Node:** Reference to the next Node in the linked list (may be None).
  - **prev: Node:** Reference to the previous Node in the linked list (may be None).
- **\_\_init\_\_(self, value: T, next: Node = None, prev: Node = None) -> None**
  - Constructs a doubly linked list node.
  - **value: T:** Value held by the Node.
  - **next: Node:** Reference to the next Node in the linked list (may be None).
  - **prev: Node:** Reference to the previous Node in the linked list (may be None).
  - **Returns:** None.
- **\_\_str\_\_(self) -> str** and **\_\_repr\_\_(self) -> str**
  - Represents the Node as a string.
  - Note that Python will automatically invoke this function when using printing a Node to the console, and PyCharm will automatically invoke this function when displaying a Node in the debugger.
  - As with all double-underscore "magic" methods in Python (see note 5), this function may be called with str(node) or repr(node). It is not necessary (and stylistically improper) to use node.\_\_str\_\_() or node.\_\_repr\_\_(), just as it is preferable to call len(some\_list) instead of some\_list.\_\_len\_\_().
  - **Returns:** str.

**class DLL:**

*DO NOT MODIFY the following attributes/functions*

- **Attributes**
  - **head: Node:** Head (first node) of the doubly linked list (may be None).
  - **tail: Node:** Tail (last node) of the doubly linked list (may be None).
  - **size: int:** Number of nodes in the doubly linked list.
  - Note that the implementation in this project does not use a [sentinel node](https://en.wikipedia.org/wiki/Sentinel_node). As such, an empty DLL will have head and tail attributes which are None.
- **\_\_init\_\_(self) -> None**
  - Construct an empty DLL. Initialize the head and tail to None, and set the size to zero.
  - **Returns:** None.
- **\_\_str\_\_(self) -> str** and **\_\_repr\_\_(self) -> str**
  - Represents the DLL as a string of the form "value <-> value <-> ... <-> value."
  - Note that Python will automatically invoke this function when printing a DLL to the console, and PyCharm will automatically invoke this function when displaying a DLL in the debugger.
  - As with all double-underscore "magic" methods in Python (see note 5), this function may be called with str(dll) or repr(dll). It is not necessary (and stylistically improper) to use dll.\_\_str\_\_() or dll.\_\_repr\_\_(), just as it is preferable to call len(some\_list) instead of some\_list.\_\_len\_\_().
  - **Returns:** str.

*IMPLEMENT the following functions*

- **empty(self) -> bool**
  - Returns a boolean indicating whether the DLL is empty.
  - *Required time complexity:* O(1).
  - *Required space complexity:* O(1).
  - **Returns:** True if DLL is empty, else False.
- **push(self, val: T, back: bool = True) -> None**
  - Adds a Node containing val to the back (or front) of the DLL and updates size accordingly.
  - *Required time complexity:* O(1).
  - *Required space complexity:* O(1).
  - **val: T:** Value to be added to the DLL.
  - **back: bool:** If True, add val to the back of the DLL. If False, add to the front. Note that the default value is True.
  - **Returns:** None.
- **pop(self, back: bool = True) -> None**
  - Removes a Node from the back (or front) of the DLL and updates size accordingly.
  - In the case that the DLL is empty, pop does nothing.
  - *Required time complexity:* O(1).
  - *Required space complexity:* O(1).
  - **back: bool:** If True, remove from the back of the DLL. If False, remove from the front. Note that the default value is True.
  - **Returns:** None.
- **list\_to\_dll(self, source: list[T]) -> None**
  - Creates a DLL from a standard Python list.
  - *Required time complexity:* O(n).
  - *Required space complexity:* O(n).
  - **source: list[T]:** Standard Python list from which to construct DLL.
  - **Returns:** None.
- **dll\_to\_list(self) -> list[T]**
  - Creates a standard Python list from a DLL.
  - *Required time complexity:* O(n).
  - *Required space complexity:* O(n).
  - **Returns:** list[T] containing the **values** of the nodes in the DLL.
- **def \_find\_nodes(self, val: T, find\_first: bool =False) -> List[Node]:**
  - Construct list of Node with value val in the DLL and returns the associated Node object list
  - *Required time complexity:* O(n).
  - *Required space complexity:* O(n).
  - MUST BE CALLED FROM find AND find\_all
    - If find and find\_all do not call \_find\_nodes, **all testcase and manual points** for find and find\_all will be forfeited.
  - Will not be tested explicitly
    - Tests for find and find\_all will ensure functionality
  - **val: T:** Value to be found in the DLL.
  - **find\_first: bool:**  if True find only the first element in the DLL, if False find all instances of the elements in the DLL.
  - **Returns:** list of Node objects in the DLL whose value is val. If val does not exist in the DLL, returns None.
- **find(self, val: T) -> Node**
  - Finds first Node with value val in the DLL and returns the associated Node object.
  - *Requires call to* \_find\_nodes
    - Failure to call \_find\_nodes will result in **all testcase and manual points** being forfeited for find.
  - *Required time complexity:* O(n).
  - *Required space complexity:* O(1).
  - **val: T:** Value to be found in the DLL.
  - **Returns:** first Node object in the DLL whose value is val. If val does not exist in the DLL, returns None.
- **find\_all(self, val: T) -> list[Node]**
  - Finds all Node objects with value val in the DLL and returns a standard Python list of the associated Node objects.
  - *Requires call to* \_find\_nodes
    - Failure to call \_find\_nodes will result in **all testcase and manual points** being forfeited for find\_all.
  - *Required time complexity:* O(n).
  - *Required space complexity:* O(n).
  - **val: T:** Value to be found in the DLL.
  - **Returns:** standard Python list of all Node objects in the DLL whose value is val. If val does not exist in the DLL,  returns an empty list.
- **\_remove\_node(self, to\_remove: Node) -> None**
  - Given a reference to a node in the linked list, remove it
  - MUST BE CALLED FROM remove\_first  AND remove\_all
  - Will not be tested explicitly
    - Tests for remove\_first and remove\_all will ensure functionality
  - *Required time complexity:* O(1).
  - *Required space complexity:* O(1).
  - **to\_remove: Node:** Node to be removed from the DLL.
  - **Returns:** None.
- **remove(self, val: T) -> bool**
  - removes first Node with value val in the DLL.
  - MUST CALL \_remove\_node
    - Failure to call \_remove\_node will result in **all testcase and manual points** being forfeited for remove.
  - Hint
    - Use of `find` allows this to be implemented in less than 10 lines.
  - *Required time complexity:* O(n).
  - *Required space complexity:* O(1).
  - **val: T:** Value to be removed from the DLL.
  - **Returns:** True if a Node with value val was found and removed from the DLL, else False.
- **remove\_all(self, val: T) -> int**
  - removes all Node objects with value val in the DLL. See note 7.
  - MUST CALL \_remove\_node
    - Failure to call \_remove\_node will result in **all testcase and manual points** being forfeited for remove\_all.
  - Hint
    - Use of `find_all` allows this to be implemented in less than 10 lines.
  - *Required time complexity:* O(n).
  - *Required space complexity:* O(n).
  - **val: T:** Value to be removed from the DLL.
  - **Returns:** number of Node objects with value val removed from the DLL. If no node containing val exists in the DLL, returns 0.
- **reverse(self) -> None**
  - Reverses the DLL in-place by modifying all next and prev references of Node objects in DLL. Updates self.head and self.tail accordingly. See note 7.
  - *Required time complexity:* O(n).
  - *Required space complexity:* O(1).
  - **Returns:** None.

Application
-----------

You are a co-creator of a music player app, and there is a bug in your code that corrupted some of the users' playlists and left others untouched. As mentioned earlier, a music playlist can be represented as a doubly linked list.

There are three ways this bug affected your doubly linked lists:

1. Proper - No Change  
   ![](img/proper.png)

2. Broken - Unconnected Linked List that is linear  
   ![](img/broken.png)

3. Improper - Creates an incorrect cycle  
   ![](img/improper.png)


**Proper, broken and improper are names created just for this context and do not represent terms for linked lists!**

Task: Create a program using **Floyd's Cycle Finding Algorithm** that will correct the given playlists by either fixing the linked lists that do not make a cycle (scenario #2) or by identifying the linked lists that create incorrect circular dependencies (scenario #3).

#### **Floyd's Cycle Finding Algorithm**

Simple algorithm that uses two pointers, slow and fast in order to detect a cycle in a linked list. The slow moves at an increment of one node, while the fast moves at an increment of two. The nodes will either reach the end of the list or will run into each other, indicating a cyclic linked list.

![ezgif.com-crop.gif](https://s3.amazonaws.com/mimirplatform.production/files/cfc7d8f9-c3ad-4ddd-ac3e-81e4e986170e/ezgif.com-crop.gif)

**This is an example of Floyd's Algorithm on an improper linked list.**

[Wiki Resource on Floyd's Algorithm](https://en.wikipedia.org/wiki/Cycle_detection)

[Video on Floyd's Algorithm](https://www.youtube.com/watch?v=MFOAbpfrJ8g&ab_channel=HackerRank)

**fix\_playlist(lst: DLL) -> bool**

*   **lst**: List
*   You may use the inner function **fix\_playlist\_helper(slow, fast)**  we provided, but it is optional.
* We also provided an optional **connect_list** function. These optional functions are there to help you divide your work. It is entirely up to you to use them or not.
*   Your algorithm should Check if the given **lst** is proper(1), broken(2), or improper(3)
*   It is **broken** when there is no cycle
*   It is **improper** when **lst** forms a cycle with a node other than the root node
*   If **proper** or **broken**, return True. If **improper**, return False


* **MUST**
  *   You MUST fix Lists that are broken **in place** (O(1) space complexity)
  *   You MUST use Floyd's Cycle Finding Algorithm (above)


* **CANNOT**
  *   Do NOT call any List methods
  *   Do NOT create any new Nodes or Lists
  *   Do NOT read prev values on nodes, you can only assign them (i.e. `if lst.node.prev is None` is NOT allowed)


* _Note1_ : Fixing an improper list was not included in order to reduce the problem's difficulty level. I would suggest looking it up if you are curious on the possible implementations for this.
* _Note2_ : Recognize the difference between broken and improper. Broken does _not_ have a cycle while improper has an incorrect cycle.
* _Note3_ : This only accounts for forward pointers, you do not need to check for backwards pointers, but of course must have those properly assigned in the solution.
* Return: bool
* _Time Complexity: O(n)_
* _Space Complexity: O(1)_
### Examples
#### Example 1
Playlist provided as figure

![](img/AppQ1.png)

This provided playlist is broken. You fix this by connecting "Feeling Good" and "Stand by Me". Return **True**

#### Example 2
Playlist provided as figure

![](img/AppQ2.png)

This provided playlist is proper. So, no additional action needs to be made. Return **True**

#### Example 3
Playlist provided as figure

![](img/AppQ3.png)

This provided playlist is improper since there is a connection between "Die For You" and "Bad Habit", which create an improper loop. Return **False**




## **Submission**


#### **Deliverables**
In every project you will be given a file named as "**solution.py**". Your will work on this file to write your Python code.
We recommend that you **download your "solution.py" and "tests.py" to your local drive**, and work on your project using PyCharm so you can easily debug your code.

Below are the simple steps to work on any project locally in your personal computer in this class:

**APPROACH 1: USING D2L TO DOWNLOAD PROJECT'S STARTER PACKAGE:**
1. Make sure you installed PyCharm
2. You can download the starter package from D2L under Projects content. Watch the short tutorial video on how to download the starter package from D2L and open it up in PyCharm.
3. Work on your project as long as you want then upload your solution.py , (watch the short tutorial video on D2L for uploading your solution.py), and upload your solution.py to Codio.
4. Click Submit button on Guide when you are done!
![](img/Submit.png)

**APPROACH 2: USING CODIO TO DOWNLOAD solution.py and tests.py**
1. On your own computer make sure to create a local folder in your local drive, name it something like **ProjectXX**, replace xx with the actual project number, in this case your folder name would be **Project03**.
2. **Download** solution.py from Codio by simply right mouse clicking on the file tree, see image below
![](img/Codio_FileTree.png)
3. **Download** tests.py from Codio by simply right mouse clicking on the file tree as shown above.
4. Work locally using PyCharm as long as you need. 
5. When finished with your solution.py file, upload your file to Codio by right mouse clicking on the Project Directory on file tree.You should rename or remove the solution.py file that is currently existing in Codio before you upload your completed version. 
6. Go To Guide and click Submit button
![](img/Codio_Upload.png)


**It does not matter which approach you choose to work on your project, just be sure to upload your solution, “solution.py”, to Codio by and click on the Submit button by its deadline. **
Working locally is recommended so you can learn debugging. You can complete your entire solution.py using Codio editor, debugging may not as intuitive as PyCharm IDE. For this reason we recommend that you work locally as long as you need, then upload your code to Codio.


**Grading**

* **Auto Graded Tests (70 points)** see below for the point distribution for the auto graded tests:

      1.empty: 5 points
      2.push:  5 points
      3.pop:   5 points
      4.list_to_dll: 5 points
      5.dll_to_list: 5 points
      6.find: 7 points
      7.find_all: 7 points
      8.remove: 7 points
      9.remove_all: 7 points
      10.reverse: 7 points
      11.**fix_playlist( application problem )**:  10 points

* **Manual (30 points)**
  * Time and Space complexity points are **divided equally** for each function. If you fail to meet time **or** space complexity in a given function, you receive half of the manual points for that function.
  * Loss of 1 point per missing docstring (max 5 point loss)
  * Loss of 2 points per changed function signature (max 20 point loss)
  * Loss of complexity and loss of testcase points for the required functions in this project. You may not use any additional data structures such as dictionaries, and sets!”
  - **Using a Python's list to solve the DLL's application problem is -5pts**
  - empty: \_\_ / 1
  - push: \_\_ / 2
  - pop: \_\_ / 2
  - list\_to\_dll: \_\_ / 2
  - dll\_to\_list: \_\_ / 2
  - \_find\_nodes: \_/2
    - If find and find\_all do not call \_find\_nodes, **all testcase and manual points** for find and find\_all  will be forfeited.
    - If \_find\_nodes violates time and/or space complexity and is called by find and find\_all  (as it must be), **all manual points** will be forfeited for the three functions
  - find: \_\_ / 2
  - find\_all: \_\_ / 2
  - \_remove\_node: \_\_ / 2
    - If remove\_first  and remove\_all do not call \_remove\_node, **all testcase and manual points** for remove\_first  and remove\_all will be forfeited.
    - If \_remove\_node violates time and/or space complexity and is called by remove\_first  and remove\_all (as it must be), **all manual points** will be forfeited for the three functions.
  - remove: \_\_ / 2
  - remove\_all: \_\_ / 2
  - reverse: \_\_ / 2
  - fix\_playlist: \_\_ / 5

  * 2 pts  for feedback and citation. See text box below to complete.
* **Important reminder**
Note students can not use Chegg or similar sites, see syllabus for details, use of outside resources for the application problem is strictly forbidden, use of outside resources is limited to max of 2 functions in a project.


    * **DOCSTRING** is not provided for this project. Please use Project 1 as a template for your DOCSTRING . 
    To learn more on what is a DOCSTRING visit the following website: [What is Docstring?](https://peps.python.org/pep-0257/)
      * One point per function that misses DOCSTRING.
      * Up to 5 points of deductions

