# 1.框架

```python
class Solution:
    def problemName(self, s: str) -> int:
        # Step 1: 定义需要维护的变量们 (对于滑动窗口类题目，这些变量通常是最小长度，最大长度，或者哈希表)
        x, y = ..., ...

        # Step 2: 定义窗口的首尾端 (start, end)， 然后滑动窗口
        start = 0
        for end in range(len(s)):
            # Step 3: 更新需要维护的变量, 有的变量需要一个if语句来维护 (比如最大最小长度)
            x = new_x
            if condition:
                y = new_y

            '''
            ------------- 下面是两种情况，读者请根据题意二选1 -------------
            '''
            # Step 4 - 情况1
            # 如果题目的窗口长度固定：用一个if语句判断一下当前窗口长度是否达到了限定长度 
            # 如果达到了，窗口左指针前移一个单位，从而保证下一次右指针右移时，窗口长度保持不变, 
            # 左指针移动之前, 先更新Step 1定义的(部分或所有)维护变量 
            if 窗口长度达到了限定长度:
                # 更新 (部分或所有) 维护变量 
                # 窗口左指针前移一个单位保证下一次右指针右移时窗口长度保持不变

            # Step 4 - 情况2
            # 如果题目的窗口长度可变: 这个时候一般涉及到窗口是否合法的问题
            # 如果当前窗口不合法时, 用一个while去不断移动窗口左指针, 从而剔除非法元素直到窗口再次合法
            # 在左指针移动之前更新Step 1定义的(部分或所有)维护变量 
            while 不合法:
                # 更新 (部分或所有) 维护变量 
                # 不断移动窗口左指针直到窗口再次合法

        # Step 5: 返回答案
        return ...
```

下面以几个例子来阐述这五个步骤
从浅入深

# 2.入门例题

## 643.子数组最大平均数Ⅰ

### 题目：

给你一个由 n 个元素组成的整数数组 nums 和一个整数 k 。
请你找出平均数最大且 长度为 k 的连续子数组，并输出该最大平均数。
任何误差小于 10-5 的答案都将被视为正确答案。

示例 1：

```
输入：nums = [1,12,-5,-6,50,3], k = 4
输出：12.75
解释：最大平均数 (12-5-6+50)/4 = 51/4 = 12.75
```

示例 2：

```
输入：nums = [5], k = 1
输出：5.00000
```

### 题解代码：

```python
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # Step 1
        # 定义需要维护的变量
        # 本题求最大平均值 (其实就是求最大和)，所以需要定义sum_, 同时定义一个max_avg (初始值为负无穷)
        sum_, max_avg = 0, -math.inf

        # Step 2: 定义窗口的首尾端 (start, end)， 然后滑动窗口
        start = 0
        for end in range(len(nums)):
            # Step 3: 更新需要维护的变量 (sum_, max_avg), 不断把当前值积累到sum_上
            sum_ += nums[end]
            if end - start + 1 == k:  
                max_avg = max(max_avg, sum_ / k)

            # Step 4
            # 根据题意可知窗口长度固定，所以用if
            # 窗口首指针前移一个单位保证窗口长度固定, 同时提前更新需要维护的变量 (sum_)
            if end >= k - 1:
                sum_ -= nums[start]
                start += 1
        # Step 5: 返回答案
        return max_avg

```

现在再来让我们看看3. 无重复字符的最长子串这道题，你会发现其实写法也是差不多的，就是多了个哈希表然后if变成了while

## 3. 无重复字符的最长子串

### 题目：

给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串 的长度。

  示例1：

```
  输入: s = "abcabcbb"
输出: 3 
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
```

  示例2：

```
  输入: s = "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
```

### 代码：

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Step 1: 定义需要维护的变量, 本题求最大长度，所以需要定义max_len, 该题又涉及去重，因此还需要一个哈希表
        max_len, hashmap = 0, {}

        # Step 2: 定义窗口的首尾端 (start, end)， 然后滑动窗口
        start = 0
        for end in range(len(s)):
            # Step 3
            # 更新需要维护的变量 (max_len, hashmap)
            # i.e. 把窗口末端元素加入哈希表，使其频率加1，并且更新最大长度
            hashmap[s[end]] = hashmap.get(s[end], 0) + 1
            if len(hashmap) == end - start + 1:  # 当哈希表里的元素数量等于滑窗长度时就意味着没有重复元素，所以就要更新最大长度
                max_len = max(max_len, end - start + 1)
          
            # Step 4: 
            # 根据题意,  题目的窗口长度可变: 这个时候一般涉及到窗口是否合法的问题
            # 这时要用一个while去不断移动窗口左指针, 从而剔除非法元素直到窗口再次合法
            # 当窗口长度大于哈希表长度时候 (说明存在重复元素)，窗口不合法
            # 所以需要不断移动窗口左指针直到窗口再次合法, 同时提前更新需要维护的变量 (hashmap)
            while end - start + 1 > len(hashmap):
                head = s[start]
                hashmap[head] -= 1
                if hashmap[head] == 0:
                    del hashmap[head]
                start += 1
        # Step 5: 返回答案 (最大长度)
        return max_len
```

**由上述两个例子可得，滑动窗口的思路就是除非是固定长度的窗口，否则就不停地右移窗口右边界，直到窗口不符合条件，则收缩窗口左边界，使其符合条件。
下面来一题比较特殊的题目，这个题目要求的是符合条件的最小长度，与上面的最长长度不同，最长长度的话可以不需要考虑其他东西，只需要不停地扩充有边界即可，但是本题要求最短的长度，则需要在每个符合条件的循环内，增加一个while循环，将左边界收缩，直到不符合条件为止。**

## 209. 长度最小的子数组

### 题目：

给定一个含有 n 个正整数的数组和一个正整数 target 。
找出该数组中满足其和 ≥ target 的长度最小的 连续子数组 [nums`<sub>`l`</sub>`, nums`<sub>`l+1`</sub>`, ..., nums`<sub>`r-1`</sub>`, nums`<sub>`r`</sub>`] ，并返回其长度。如果不存在符合条件的子数组，返回 0 。

示例1：

```
输入：target = 7, nums = [2,3,1,2,4,3]
输出：2
解释：子数组 [4,3] 是该条件下的长度最小的子数组。
```

示例2：

```
输入：target = 11, nums = [1,1,1,1,1,1,1,1]
输出：0
```

### 代码：

```python
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # Step 1: 定义需要维护的变量, 本题求最小长度，所以需要定义min_len, 本题又涉及求和，因此还需要一个sum变量
        min_len, sum_ = math.inf, 0

        # Step 2: 定义窗口的首尾端 (start, end)， 然后滑动窗口
        start = 0
        for end in range(len(nums)):
            # Step 3: 更新需要维护的变量 (min_len, sum_)
            sum_ += nums[end]

            # 这一段可以删除，因为下面的while已经handle了这一块儿逻辑，不过写在这也没影响
            if sum_ >= target:
                min_len = min(min_len, end - start + 1)

            # Step 4
            # 这一题这里稍微有一点特别: sum_ >= target其实是合法的，但由于我们要求的是最小长度，
            # 所以当sum_已经大于target的时候继续移动右指针没有意义，因此还是需要移动左指针慢慢逼近答案
            # 由于左指针的移动可能影响min_len和sum_的值，因此需要在移动前将它们更新
            while sum_ >= target:
                min_len = min(min_len, end - start + 1)
                sum_ -= nums[start]
                start += 1
        # Step 5：返回答案 (最小长度)
        if min_len == math.inf:
            return 0
        return min_len
```

下面则是将相关的题目汇总起来：

# 各汇总例题

## 1695. 删除子数组的最大得分

### 题目：

给你一个正整数数组 nums ，请你从中删除一个含有 若干不同元素 的子数组。删除子数组的 得分 就是子数组各元素之 和 。
返回 只删除一个 子数组可获得的 最大得分 。

示例1：

```
输入：nums = [4,2,4,5,6]
输出：17
解释：最优子数组是 [2,4,5,6]
```

示例2：

```
输入：nums = [5,2,1,2,5,2,1,2,5]
输出：8
解释：最优子数组是 [5,2,1] 或 [1,2,5]
```

### 代码：

```python
class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        # Step 1
        # 定义需要维护的变量, 本题最大得分，所以需要定义当前得分sum_和最大得分max_sum
        # 本题又涉及去重 (题目规定子数组不能有重复)，因此还需要一个哈希表
        sum_, max_sum, hashmap = 0, 0, {}

        # Step 2: 定义窗口的首尾端 (start, end)， 然后滑动窗口
        start = 0
        for end in range(len(nums)):
            # Step 3
            # 更新需要维护的变量 (sum_, hashmap)
            # sum和hashmap需要更新就不说了，max_sum当且仅当哈希表里面没有重复元素时 (end - start + 1 == len(hashmap)) 更新
            tail = nums[end]
            sum_ += tail
            hashmap[tail] = hashmap.get(tail, 0) + 1
            if end - start + 1 == len(hashmap):
                max_sum = max(max_sum, sum_)
          
            # Step 4
            # 根据题意,  题目的窗口长度可变: 这个时候一般涉及到窗口是否合法的问题
            # 这时要用一个while去不断移动窗口左指针, 从而剔除非法元素直到窗口再次合法
            # 哈希表里面有重复元素时 (end - start + 1 > len(hashmap)) 窗口不合法
            # 所以需要不断移动窗口左指针直到窗口再次合法, 同时提前更新需要维护的变量 (hashmap， sum_)
            while end - start + 1 > len(hashmap):
                head = nums[start]
                hashmap[head] -= 1
                if hashmap[head] == 0:
                    del hashmap[head]
                sum_ -= nums[start]
                start += 1
        # Step 5: 返回答案
        return max_sum
```

**没啥好说，就是典型的滑动窗口去重问题**

## 438. 找到字符串中所有字母异位词

### 题目：

给定两个字符串 s 和 p，找到 s 中所有 p 的 异位词 的子串，返回这些子串的起始索引。不考虑答案输出的顺序。
异位词 指由相同字母重排列形成的字符串（包括相同的字符串）。

示例1：

```
输入: s = "cbaebabacd", p = "abc"
输出: [0,6]
解释:
起始索引等于 0 的子串是 "cba", 它是 "abc" 的异位词。
起始索引等于 6 的子串是 "bac", 它是 "abc" 的异位词。
```

示例2：

```
输入: s = "abab", p = "ab"
输出: [0,1,2]
解释:
起始索引等于 0 的子串是 "ab", 它是 "ab" 的异位词。
起始索引等于 1 的子串是 "ba", 它是 "ab" 的异位词。
起始索引等于 2 的子串是 "ab", 它是 "ab" 的异位词。
```

**这个题目有点意思，因为有可能配对的字符串中会含有相同的元素，所以这里不能使用set()来进行判断，但是可以使用哈希表，通过在滑窗更新时增添和删除哈希表中的元素来维护哈希表。**

### 代码：

```python
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # Step 1: 
        # 定义需要维护的变量
        # 本文需要对比两组字符串是否为异位词，所以用哈希表 (abc和bac是异位词是因为他们对应的哈希表相等)
        # 同时我们需要找到所有合法解，所以还需要一个res数组
        res, hashmap = [], {}

        # Step 1.1： 同时把p的哈希表也建立了 (这个哈希表不需要维护，为定值)
        hashmap_p = {}
        for char in p:
            hashmap_p[char] = hashmap_p.get(char, 0) + 1

        # Step 2: 定义窗口的首尾端 (start, end)， 然后滑动窗口
        start = 0
        for end in range(len(s)):
            # Step 3: 更新需要维护的变量 (hashmap)， 如果hashmap == hashmap_p，代表找到了一个解，加入到res
            hashmap[s[end]] = hashmap.get(s[end], 0) + 1
            if hashmap == hashmap_p:
                res.append(start)

            # Step 4 
            # 根据题意可知窗口长度固定，所以用if
            # 窗口左指针前移一个单位保证窗口长度固定, 同时提前更新需要维护的变量 (hashmap)
            if end >= len(p) - 1:
                hashmap[s[start]] -= 1
                if hashmap[s[start]] == 0:
                    del hashmap[s[start]]
                start += 1
        # Step 5: 返回答案
        return res
```

## 567. 字符串的排列

### 题目：

给你两个字符串 s1 和 s2 ，写一个函数来判断 s2 是否包含 s1 的排列。如果是，返回 true ；否则，返回 false 。
换句话说，s1 的排列之一是 s2 的 子串 。

示例1：

```
输入：s1 = "ab" s2 = "eidbaooo"
输出：true
解释：s2 包含 s1 的排列之一 ("ba").
```

示例2：

```
输入：s1= "ab" s2 = "eidboaoo"
输出：false
```

**题目整体来说思路跟上一题类似，都是用哈希表来进行字串的判断，并通过哈希表和滑动窗口同步增删数据的方法来进行维护。**

### 代码：

```python
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Step 1
        # 定义需要维护的变量
        # 因为和排列相关 (元素相同，顺序可以不同)，使用哈希表
        hashmap2 = {}

        # Step 1.1: 同时建立s1的哈希表 (这个哈希表不需要维护，为定值)
        hashmap1 = {}
        for char in s1:
            hashmap1[char] = hashmap1.get(char, 0) + 1
      
        # Step 2: 定义窗口的首尾端 (start, end)， 然后滑动窗口
        start = 0
        for end in range(len(s2)):
            # Step 3: 更新需要维护的变量 (hashmap2)， 如果hashmap1 == hashmap2，代表s2包含s1的排列，直接return
            tail = s2[end]
            hashmap2[tail] = hashmap2.get(tail, 0) + 1
            if hashmap1 == hashmap2:
                    return True

            # Step 4: 
            # 根据题意可知窗口长度固定，所以用if
            # 窗口左指针前移一个单位保证窗口长度固定, 同时提前更新需要维护的变量 (hashmap2)
            if end >= len(s1) - 1:
                head = s2[start]
                hashmap2[head] -= 1
                if hashmap2[head] == 0:
                    del hashmap2[head]
                start += 1
        # Step 5： 没有在s2中找到s1的排列，返回False
        return False
```

## 1004. 最大连续1的个数 III

### 题目：

给定一个二进制数组 nums 和一个整数 k，如果可以翻转最多 k 个 0 ，则返回 数组中连续 1 的最大个数 。

示例1：

```
输入：nums = [1,1,1,0,0,0,1,1,1,1,0], K = 2
输出：6
解释：[1,1,1,0,0,1,1,1,1,1,1]
粗体数字从 0 翻转到 1，最长的子数组长度为 6。
```

示例2：

```
输入：nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], K = 3
输出：10
解释：[0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
粗体数字从 0 翻转到 1，最长的子数组长度为 10。
```

**这道题初看有点难，但是转换思路之后就很简单，可以将容许翻转的次数看作是前面不许重复的字串问题中容许重复的次数。
同理，都是建立一个哈希表，前面是记载相同元素的次数，到了这里则是记录0的个数，当0的个数超标之后，则像前面那样，通过左边界右移来将多余的0剔除出去。**

### 代码：

```python
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        max_len, hashmap = 0, {}

        start =  0
        for end in range(len(nums)):
            tail = nums[end]
            hashmap[tail] = hashmap.get(tail, 0) + 1
            if hashmap.get(0, 0) <= k:
                max_len = max(max_len, end - start + 1)

            # 相比较于上一题，只需要把1改成k
            while hashmap.get(0, 0) > k:
                head = nums[start]
                hashmap[head] -= 1
                start += 1
        return max_len
```

## 1208. 尽可能使字符串相等

### 题目：

给你两个长度相同的字符串，s 和 t。
将 s 中的第 i 个字符变到 t 中的第 i 个字符需要 |s[i] - t[i]| 的开销（开销可能为 0），也就是两个字符的 ASCII 码值的差的绝对值。
用于变更字符串的最大预算是 maxCost。在转化字符串时，总开销应当小于等于该预算，这也意味着字符串的转化可能是不完全的。
如果你可以将 s 的子字符串转化为它在 t 中对应的子字符串，则返回可以转化的最大长度。
如果 s 中没有子字符串可以转化成 t 中对应的子字符串，则返回 0。

示例1：

```
输入：s = "abcd", t = "bcdf", maxCost = 3
输出：3
解释：s 中的 "abc" 可以变为 "bcd"。开销为 3，所以最大长度为 3。
```

示例2：

```
输入：s = "abcd", t = "cdef", maxCost = 3
输出：1
解释：s 中的任一字符要想变成 t 中对应的字符，其开销都是 2。因此，最大长度为 1。
```

**没啥难度，就是一道很普通的题，唯一的难度可能是将其转成ASC码的ord函数**

### 代码：

```python
class Solution:
    def equalSubstring(self, s: str, t: str, max_cost: int) -> int:
        # Step 1: 定义需要维护的变量
        # 因为是求最大长度，所以有max_len，又同时涉及计算开销 (和求和一个道理)， 所以还要一个cur_cost
        cur_cost, max_len = 0, 0
      
        # Step 2: 定义窗口的首尾端 (start, end)， 然后滑动窗口
        start = 0
        for end in range(len(t)):
            # Step 3
            # 更新需要维护的变量 (cur_cost)
            # 每一对字符的order差值就是当前时间点的开销，直接累积在cur_cost上即可
            # cur_cost只要不超过最大开销，就更新max_len
            cur_cost += abs(ord(s[end]) - ord(t[end]))
            if cur_cost <= max_cost:
                max_len = max(max_len, end - start + 1)

            # Step 4
            # 根据题意,  题目的窗口长度可变: 这个时候一般涉及到窗口是否合法的问题
            # 这时要用一个while去不断移动窗口左指针, 从而剔除非法元素直到窗口再次合法
            # 当cur_cost大于最大开销时候，窗口不合法
            # 所以需要不断移动窗口左指针直到窗口再次合法 (cur_cost <= max_cost)
            while cur_cost > max_cost:
                cur_cost -= abs(ord(s[start])-  ord(t[start]))
                start += 1
        # Step 5: 返回答案 (最大长度)
        return max_len
```

## 1052. 爱生气的书店老板

### 题目

有一个书店老板，他的书店开了 n 分钟。每分钟都有一些顾客进入这家商店。给定一个长度为 n 的整数数组 customers ，其中 customers[i] 是在第 i 分钟开始时进入商店的顾客数量，所有这些顾客在第 i 分钟结束后离开。
在某些时候，书店老板会生气。 如果书店老板在第 i 分钟生气，那么 grumpy[i] = 1，否则 grumpy[i] = 0。
当书店老板生气时，那一分钟的顾客就会不满意，若老板不生气则顾客是满意的。
书店老板知道一个秘密技巧，能抑制自己的情绪，可以让自己连续 minutes 分钟不生气，但却只能使用一次。
请你返回 这一天营业下来，最多有多少客户能够感到满意 。

示例1：

```
输入：customers = [1,0,1,2,1,1,7,5], grumpy = [0,1,0,1,0,1,0,1], minutes = 3
输出：16
解释：书店老板在最后 3 分钟保持冷静。
感到满意的最大客户数量 = 1 + 1 + 1 + 1 + 7 + 5 = 16.
```

示例2：

```
输入：customers = [1], grumpy = [0], minutes = 1
输出：1
```

**这道题最难的点是如何与滑动窗口联系起来，以往的题目中的容忍度参数都是一个确定的累计值，但是这里的容忍度则是一段连续时间，这段时间里可能会含有本身就是冷静的时间，所以我们无法确定保持的冷静的具体时间。
所以这里的滑窗则是以这一段连续冷静期为窗口，去探究在哪一段连续的时间中收益最高，然后再把其他冷静的收益给累加进来**

### 代码：

```python
class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        # Step 1
        # 定义需要维护的变量,
        # 因为涉及求和所以定义sum_和max_sum, 同时需要知道老板什么时候'发动技能'，再定义一个max_start
        sum_, max_sum, max_start = 0, 0, 0
  
        # Step 2: 定义窗口的首尾端 (start, end)， 然后滑动窗口
        start = 0
        for end in range(len(customers)):
            # Step 3
            # 更新需要维护的变量 (sum_)
            # 注意：这里只要当老板在当前时间点会发脾气的时候才维护
            # sum_就不说了，和前面N道题的维护方法一样，新多出来的max_start也就是记录一样时间点而已，没什么fancy的
            if grumpy[end] == 1:
                sum_ += customers[end]
            if sum_ > max_sum:
                max_sum = sum_
                max_start = start

            # Step 4
            # 根据题意可知窗口长度固定 (老板技能持续时间固定)，所以用if
            # 窗口左指针前移一个单位保证窗口长度固定, 同时提前更新需要维护的变量 (sum_, max_avg)
            if end >= minutes - 1:
                if grumpy[start]:
                    sum_ -= customers[start]
                start += 1

        # 这里对比其他题目多了一小步: 在找到老板发动技能的最大收益时间点(max_start)后
        # 需要把受技能影响时间段中的grumpy全部置0 - 代表老板成功压制了自己的怒火
        for i in range(max_start, max_start + minutes):
            grumpy[i] = 0

        # Step 5: 再遍历一遍数组求customer总数量并且返回结果
        res = 0
        for i in range(len(customers)):
            if not grumpy[i]:
                res += customers[i]
        return res
```

## 1423. 可获得的最大点数

### 题目：

几张卡牌 排成一行，每张卡牌都有一个对应的点数。点数由整数数组 cardPoints 给出。
每次行动，你可以从行的开头或者末尾拿一张卡牌，最终你必须正好拿 k 张卡牌。
你的点数就是你拿到手中的所有卡牌的点数之和。
给你一个整数数组 cardPoints 和整数 k，请你返回可以获得的最大点数。

示例1：

```
输入：cardPoints = [1,2,3,4,5,6,1], k = 3
输出：12
解释：第一次行动，不管拿哪张牌，你的点数总是 1 。但是，先拿最右边的卡牌将会最大化你的可获得点数。最优策略是拿右边的三张牌，最终点数为 1 + 6 + 5 = 12 。
```

示例2：

```
输入：cardPoints = [2,2,2], k = 2
输出：4
解释：无论你拿起哪两张卡牌，可获得的点数总是 4 。
```

**这道题的思路则是，既然取到的牌在数组内是不连续的，那么未被取到的牌在数组就一定是连续的，所以反其道而行之，将题目转变成求连续子串和的最小值，这个字串的长度则为数组的长度减去k值，这样就转成一道很简单的题目，固定滑窗长度的最小和**

### 代码：

```python
class Solution:
    # 这题相比前面的题目加了一丢丢小的变通: 题目要求首尾串最大点数，其实就是求非首尾串的连续序列的最小点数
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        # 特解
        n = len(cardPoints)
        if k == n:
            return sum(cardPoints)

        # Step 1
        # 定义需要维护的变量，因为涉及求和所以定义sum_和min_sum
        m = n - k
        sum_, min_sum = 0, math.inf

        # Step 2: 定义窗口的首尾端 (start, end)， 然后滑动窗口
        start = 0
        for end in range(n):
            # Step 3
            # 更新需要维护的变量 (sum_)
            sum_ += cardPoints[end]

            # Step 4
            # 根据题意可知窗口长度固定，所以用if
            # 窗口左指针前移一个单位保证窗口长度固定, 同时提前更新需要维护的变量 (min_sum， sum_)
            if end >= m - 1:
                min_sum = min(min_sum, sum_)
                sum_ -= cardPoints[start]
                start += 1
        # Step 5: 返回答案 (总点数减去非首尾串的连续序列的最小点数就可以得到首尾串的最大点数)
        return sum(cardPoints) - min_sum
```

## 1151. 最少交换次数来组合所有的 1

### 题目：

给出一个二进制数组 data，你需要通过交换位置，将数组中 任何位置 上的 1 组合到一起，并返回所有可能中所需 最少的交换次数。

示例1：

```
输入：[1,0,1,0,1]
输出：1
解释： 
有三种可能的方法可以把所有的 1 组合在一起：
[1,1,1,0,0]，交换 1 次；
[0,1,1,1,0]，交换 2 次；
[0,0,1,1,1]，交换 1 次。
所以最少的交换次数为 1。
```

示例2：

```
输入：[0,0,0,1,0]
输出：0
解释： 
由于数组中只有一个 1，所以不需要交换。
```

示例3：

```
输入：[1,0,1,0,1,0,0,1,1,0,1]
输出：3
解释：
交换 3 次，一种可行的只用 3 次交换的解决方案是 [0,0,0,0,0,1,1,1,1,1,1]。
```

**这道题初看又是不知道如何将其与滑动窗口联系起来。
但我们先想一种完美的情况，即交换0次的情况，在这种情况下，数组内会有一个连续的字串，其各元素都为1，并且该字串的长度为该数组所有1的长度。
若要我们通过滑动窗口的方法去寻找这个字串的话，那就是将窗口的长度设定为数组中1的数目，设定一个哈希表来统计各元素的数目，当窗口滑动到该字串时，哈希表中0的数目则为0。
那么，当不完美时，即我们需要交换时，我们从上述的例子中发现，当前窗口需要交换的数量跟当前窗口中0的数量相等，所以我们可以通过一个长度等于数组中1的数量的窗口进行滑动，统计其0的数量，返回各窗口中最小0的数量即可得出最小交换次数**

### 代码：

```python
class Solution:
    def minSwaps(self, data: List[int]) -> int:
        # 先数出一共有多少个1，输出来的个数就是窗口的长度
        num_ones = 0
        for i in range(len(data)):
            if data[i] == 1:
                num_ones += 1

        # Step 1
        # 定义需要维护的变量，求最小swap次数其实就是求窗口中0个数的最小值，因此定义num_zeros, min_num_zeros
        num_zeros, min_num_zeros = 0, math.inf

        # Step 2: 定义窗口的首尾端 (start, end)， 然后滑动窗口
        start = 0
        for end in range(len(data)):
            # Step 3
            # 更新需要维护的变量 (num_zeros， min_num_zeros)
            if data[end] == 0:
                num_zeros += 1
            if end - start + 1 == num_ones:
                min_num_zeros = min(min_num_zeros, num_zeros)

            # Step 4
            # 根据题意可知窗口长度固定 (数组1的总个数)，所以用if
            # 窗口左指针前移一个单位保证窗口长度固定, 同时提前更新需要维护的变量 (num_zeros)
            if end >= num_ones - 1:
                if data[start] == 0:
                    num_zeros -= 1
                start += 1
      
        # Step 5: 返回答案 (如果min_num_zeros依旧是math.inf说明数组没有1存在，不能swap，返回0即可)
        if min_num_zeros == math.inf:
            return 0
        return min_num_zeros
```
