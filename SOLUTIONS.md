# LeetCode Solutions

## 1. Two Sum

**Задача:** Дан массив целых чисел `nums` и целевое значение `target`. Найти индексы двух чисел, которые в сумме дают `target`.

**Решение:**
```python
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        prev_map = {}
        
        for i, n in enumerate(nums):
            diff = target - n
            if diff in prev_map:
                return [prev_map[diff], i]
            prev_map[n] = i
        return []
```

---

## 3. Longest Substring Without Repeating Characters

**Задача:** Найти длину самой длинной подстроки без повторяющихся символов.

**Решение:**
```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_map = {}
        result = 0
        left = 0

        for right, char in enumerate(s):
            if char in char_map and char_map[char] >= left:
                left = char_map[char] + 1

            char_map[char] = right

            if (current_len := right - left + 1) > result:
                result = current_len
        
        return result
```

---

## 20. Valid Parentheses

**Задача:** Проверить, является ли строка с скобками `()`, `[]`, `{}` корректной (каждая открывающая скобка имеет соответствующую закрывающую в правильном порядке).

**Решение:**
```python
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        values_dict = {
            "}": "{",
            ")": "(",
            "]": "["
        }

        for elem in s:
            if elem in values_dict:
                if stack and stack[-1] == values_dict[elem]:
                    stack.pop()
                    continue
            stack.append(elem)

        return not stack
```

---

## 21. Merge Two Sorted Lists

**Задача:** Объединить два отсортированных связных списка в один отсортированный список.

**Решение:**
```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        return_node = ListNode(None)
        current = return_node

        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            
            current = current.next

        current.next = list1 if list1 else list2

        return return_node.next
```

---

## 49. Group Anagrams

**Задача:** Сгруппировать строки-анаграммы вместе из заданного массива строк.

**Решение:**
```python
from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)

        for word in strs:
            sorted_key = "".join(sorted(word))
            anagram_map[sorted_key].append(word)

        return list(anagram_map.values())
```

**Решение без defaultdict:**
```python
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = {}

        for word in strs:
            sorted_key = "".join(sorted(word))
            if sorted_key not in anagram_map:
                anagram_map[sorted_key] = []
            anagram_map[sorted_key].append(word)

        return list(anagram_map.values())
```

---

## 70. Climbing Stairs

**Задача:** Подниматься по лестнице можно на 1 или 2 ступени за раз. Найти количество различных способов подняться на `n` ступенек.

**Решение:**
```python
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        previous = 1
        return_ = 2

        for step in range(3, n+1):
            previous, return_ = return_, previous + return_

        return return_
```

---

## 104. Maximum Depth of Binary Tree

**Задача:** Найти максимальную глубину бинарного дерева.

**Решение (рекурсивное):**
```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        
        return 1 + max(left_depth, right_depth)
```

**Решение (итеративное):**
```python
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        queue = [(root, 1)]
        max_depth = 0
        
        while queue:
            node, depth = queue.pop(0)
            max_depth = max(max_depth, depth)
            
            if node.left:
                queue.append((node.left, depth + 1))
            if node.right:
                queue.append((node.right, depth + 1))
        
        return max_depth
```

---

## 125. Valid Palindrome

**Задача:** Проверить, является ли строка палиндромом, учитывая только буквенно-цифровые символы и игнорируя регистр.

**Решение:**
```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left < right:
            if not s[left].isalnum():
                left += 1
            elif not s[right].isalnum():
                right -= 1
            elif s[left].lower() != s[right].lower():
                return False
            else:
                left += 1
                right -= 1

        return True
```

---

## 200. Number of Islands

**Задача:** Подсчитать количество островов в 2D сетке, где `'1'` — земля, `'0'` — вода. Остров — группа соседних (по горизонтали/вертикали) единиц.

**Решение:**
```python
from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        islands = 0
        rows, cols = len(grid), len(grid[0])

        def helper(helper_row, helper_col):
            if (
                helper_row < 0
                or helper_row >= rows
                or helper_col < 0
                or helper_col >= cols
                or grid[helper_row][helper_col] != "1"
            ):
                return

            grid[helper_row][helper_col] = "2"

            helper(helper_row + 1, helper_col)
            helper(helper_row - 1, helper_col)
            helper(helper_row, helper_col + 1)
            helper(helper_row, helper_col - 1)

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    helper(row, col)
                    islands += 1

        return islands
```

---

## 206. Reverse Linked List

**Задача:** Развернуть односвязный список.

**Решение:**
```python
class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        previous_steps = []

        while head:
            previous_steps.append(head.val)
            head = head.next

        return_head = ListNode(val=previous_steps.pop())
        next_step = ListNode()
        return_head.next = next_step

        while previous_steps:
            next_step.val = previous_steps.pop()
            next_step.next = ListNode() if previous_steps else None
            next_step = next_step.next

        return return_head
```

---

## 217. Contains Duplicate

**Задача:** Проверить, содержит ли массив дубликаты.

**Решение:**
```python
from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        frequency_set = set()

        for elem in nums:
            if elem not in frequency_set:
                frequency_set.add(elem)
            else:
                return True

        return False
```

---

## 226. Invert Binary Tree

**Задача:** Инвертировать бинарное дерево (зеркально отразить).

**Решение:**
```python
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        root.left, root.right = root.right, root.left
        Solution().invertTree(root.left)
        Solution().invertTree(root.right)
        
        return root
```

---

## 231. Power of Two

**Задача:** Определить, является ли число степенью двойки.

**Решение:**
```python
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 1:
            return True

        if n % 2 != 0:
            return False

        return Solution().isPowerOfTwo(n//2)
```

---

## 242. Valid Anagram

**Задача:** Проверить, являются ли две строки анаграммами.

**Решение:**
```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        frequency = {}

        for elem in s:
            frequency[elem] = frequency.get(elem, 0) + 1
    
        for elem in t:
            if elem not in frequency or frequency[elem] == 0:
                return False
            frequency[elem] -= 1

        return True
```

---

## 258. Add Digits

**Задача:** Суммировать все цифры числа до тех пор, пока не останется одна цифра.

**Решение:**
```python
class Solution:
    def addDigits(self, num: int) -> int:
        if num < 10:
            return num

        return Solution().addDigits(
            sum(int(digit) for digit in str(num))
        )
```

---

## 344. Reverse String

**Задача:** Развернуть строку in-place (массив символов).

**Решение:**
```python
from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        def helper(start, finish):
            if start > finish:
                return

            s[start], s[finish] = s[finish], s[start]
            helper(start+1, finish-1)

        helper(0, len(s) - 1)
```

---

## 509. Fibonacci Number

**Задача:** Найти n-ое число Фибоначчи.

**Решение:**
```python
class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1

        return Solution().fib(n-1) + Solution().fib(n-2)
```

---

## 704. Binary Search

**Задача:** Выполнить бинарный поиск элемента в отсортированном массиве.

**Решение:**
```python
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while right >= left:
            mid = (right + left) // 2

            if nums[mid] == target:
                return mid
            elif target > nums[mid]:
                left = mid + 1
            else:
                right = mid - 1

        return -1
```
