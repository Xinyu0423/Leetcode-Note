# Coding

## 深度遍历 & 广度遍历 结构

## 二叉树前中后序遍历

preorder 根左右

```
while(root != null && !stack.isEmpty()) {
while(root != null) {
	res.add(root.val);
	stack.push(root);
	root = root.left;}
TreeMpde cur = stack.pop();
root = cur.right;
}


```

inorder 左根右

```
while(root != null && !stack.isEmpty()) {
	while(root != null){
	stack.push(root);
	root = root.left;}
	root = stack.pop();
	res.add(root.val);
	root = root.right;

}
```

postorder 左右根

```
while(root != null && !stack.isEmpty()) {
	while(root != null) {
	res.add(root.val);
	stack.push(root);
	root = root.right;}
	TreeNode cur = stack.pop();
	root = cur.left;
}
Colletions.reverse(res);
return res;
```

## ~~给定x，y，交换x和y的值，并且不能占用新的内存~~

x =x + y

y = x(x + y) - y

x = x - y

## leetcode 683

```
unix find
class searchDetail {
public:
        string name;
        int size;       
        string path;

        searchType(string name, string path, int size) {
                this->name = name;
                this->path = path;
                this->size = size;
        }
};

class find {
public:
        vector `<string>` output;
        searchDetail schDitl;

        find(string name, string path, int size){
                schDitl = new SearchDetail(name, path, size);
        }

        vector `<string>` getFiles() {
                File f = new File(schDitl.path);
                findFiles(f);
                return output;
        }

        void findFiles(File f) {
                if (f.isDirectory()) {
                        for (File subFile : f) {
                                find(subFile);
                        }
                } else {
                        if ( (schDitl.name == "" || f.name() == schDitl.name) && f.size() == schDitl.size) {
                                output.push_back(f.path());
                        }               
                }
        }
}
       

int main(){
        find f = new Find("sample.txt", "/usr/bin", 50);
        vector `<string>` res = f.getFiles();
        return 0;
}

def get_list(input_list): # input list of json, output list of json
    res = []
    m = {}
    for element in input_list:
        res.append(dfs(element, m))
    return res

def dfs(element, m):
    if element['id'] in m:
        j = json.loads('{}')
        j['id'] = element['id']
        j['items_in_bundle'] = m[element['id']][0]
        j['price'] = m[element['id']][1]
        return j
    price_sum = 0
    quantity_sum = 0
    if 'children' in element:
        child_list = element['children']
        for child in child_list:
            child_j = dfs(child, m)
            price_sum += child_j['price'] * child['qty']
            quantity_sum += child_j['items_in_bundle'] * child['qty']
        m[element['id']] = [quantity_sum, price_sum]
    else:
        price_sum = element['price']
        quantity_sum = 1
        m[element['id']] = [quantity_sum, price_sum]
    j = json.loads('{}')
    j['id'] = element['id']
    j['items_in_bundle'] = quantity_sum
    j['price'] = price_sum
    return j
```

---

## ~~LRU cache~~

利用一个hashmap和一个doublelinkedlist来处理O（1）的操作

```
class LRUCache {
HashMap<Integer, Node> map;
int cap;
DoubleLinkedList cache;
public LRUCache(int capacity) {
this.cap = capacity;
map = new HashMap<>();
cache = new DoubleLinkedList();
}
public int get(int key) {
    if(!map.containsKey(key)) return -1;
    int val = map.get(key).val;
    put(key, val);
    return val;
}

public void put(int key, int value) {
    Node newnode = new Node(key, value);
    if(map.containsKey(key)) {
       cache.delete(map.get(key));
        cache.addFirst(newnode);
        map.put(key, newnode);
    }
    else{
        if(map.size() == cap) {
            int k = cache.deleteLast();
            map.remove(k);
        }
        cache.addFirst(newnode);
        map.put(key, newnode);
  
  
  
    }
}


class DoubleLinkedList{
    Node head;
    Node tail;
    public DoubleLinkedList(){
        head = new Node(0, 0);
        tail = new Node(0, 0);
        head.next = tail;
        tail.prev = head;
    }
  
    public void addFirst(Node newnode) {
        newnode.next = head.next;
        newnode.prev = head;
        head.next.prev = newnode;
        head.next = newnode;
    }
  
    public int delete(Node n) {
        int key = n.key;
        n.prev.next = n.next;
        n.next.prev = n.prev;
        return key;
    }
    public int deleteLast() {
        if(head.next == tail) return -1;
        int key = delete(tail.prev);
        return key;
    }
  
  
}



class Node{
    int val;
    int key;
    Node prev;
    Node next;
    public Node(int key, int val) {
        this.val = val;
        this.key = key;
    }
  
  
}
```

}

~~394 decode string~~
-----------------

可以利用递归，但是熟练掌握了使用一个stack的写法，当遇到】的时候pop并且处理直到【前的字符串，处理后重新push进stack

```
return new String(res);
}}
         }
  
}
    else{
        stack.push(s.charAt(i));
    }
}


char[] res = new char[stack.size()];
for(int i = res.length - 1; i >= 0; i--) {
    res[i] = stack.pop();

}class Solution {
public String decodeString(String s) {
Stack`<Character>` stack = new Stack<>();
for(int i = 0; i < s.length(); i++) {
if(s.charAt(i) == ']') {
ArrayList`<Character>` decodedString = new ArrayList<>();
while(!stack.isEmpty() && stack.peek() != '[') {
decodedString.add(stack.pop());
}
//pop left bracket
stack.pop();
//deal w/ number
int base = 1;
int k = 0;
while(!stack.isEmpty() && Character.isDigit(stack.peek())) {
k = k + (stack.pop() - '0') * base;
base *= 10;
}
//we have the number
while(k > 0) {
for(int j = decodedString.size() - 1; j >= 0; j--) {
stack.push(decodedString.get(j));
}
k--;
         }
  
}
    else{
        stack.push(s.charAt(i));
    }
}


char[] res = new char[stack.size()];
for(int i = res.length - 1; i >= 0; i--) {
    res[i] = stack.pop();

}
return new String(res);
}}
```

## ~~402 remove k digits~~

维护一个单调递增的stack

```
public String removeKdigits(String num, int k) {
    LinkedList<Character> stack = new LinkedList<Character>();
      
    for(char digit : num.toCharArray()) {
      while(stack.size() > 0 && k > 0 && stack.peekLast() > digit) {
        stack.removeLast();
        k -= 1;
      }
      stack.addLast(digit);
    }
      
    /* remove the remaining digits from the tail. */
    for(int i=0; i<k; ++i) {
      stack.removeLast();
    }
      
    // build the final string, while removing the leading zeros.
    StringBuilder ret = new StringBuilder();
    boolean leadingZero = true;
    for(char digit: stack) {
      if(leadingZero && digit == '0') continue;
      leadingZero = false;
      ret.append(digit);
    }
      
    /* return the final string  */
    if (ret.length() == 0) return "0";
    return ret.toString();
  }
```

## ~~653 1 two sum~~变种

i. 主要是利用hashmap解决two sum

ii. 当given array为sorted array的时候，利用双指针，low，high来找到index

iii. 设计data structure，利用either sorted array 或者hashmap解决find的问题

iv. bst,利用hashset来记录每个node的值(dfs)

~~198 打家劫舍~~
------------

主要是利用dp思想，dp[i] = max(dp[i - 2] + nums[i], dp[i - 1]) 我们对于这家抢不抢的处理

## ~~2 add two numbers~~

和之前的given two string number类似，given two linked list来计算

```
public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
  
        int carry = 0;
        ListNode head = new ListNode(0);
        ListNode p = head;
        while(l1 != null || l2 != null || carry != 0) {
            int sum = carry;
  
            if(l1 != null) {
                sum += l1.val;
                l1 = l1.next;
            }
            if(l2 != null) {
                sum += l2.val;
                l2 = l2.next;
            }
           ListNode temp = new ListNode(sum % 10);
            p.next = temp;
            p = p.next;
            carry = sum / 10;
        }
        return head.next;
    }
```

## ~~10 Regular expression~~

```
public boolean isMatch(String s, String p) {
        if(p.isEmpty()) return s.isEmpty();
        boolean firstMatch = (s.length() != 0) && ((s.charAt(0) == p.charAt(0) || p.charAt(0) == '.'));
    
        if(p.length() >= 2 && p.charAt(1) == '*' )
            return (firstMatch && isMatch(s.substring(1), p) || isMatch(s, p.substring(2)));
        //more, zero preceeding character
        else
            return firstMatch && isMatch(s.substring(1), p.substring(1));
    }
```

## ~~37 sudoku solver~~

```
public void solveSudoku(char[][] board) {
        backtrack(board, 0, 0);
    }
  
    private boolean backtrack(char[][] board, int i, int j) {
        if(j == 9)  return backtrack(board, i + 1, 0);
        if(i == 9)  return true;
    
        if(board[i][j] != '.')
            return backtrack(board, i, j + 1);
    
    
        for(char ch = '1'; ch <= '9'; ch++) {
            if(!isValid(board, i, j, ch)) continue;
            board[i][j] = ch;
            if(backtrack(board, i, j + 1)) return true;
            board[i][j] = '.';
        }
        return false;
    }
    public boolean isValid(char[][] board, int r, int c, char ch) {
        for(int i = 0; i < 9; i++) {
            if(board[i][c] == ch) return false;
            if(board[r][i] == ch) return false;
            if(board[(r/3) * 3+ i / 3][(c/3) * 3 + i % 3] == ch) return false;
        }
        return true;
    }
```

## ~~46 permuation i~~

```
List<List<Integer>> res;
    public List<List<Integer>> permute(int[] nums) {
        res = new ArrayList<>();
        if(nums.length == 0) return res;
        List<Integer> path = new ArrayList<>();
        backtrack(nums, path);
        return res;
    }
  
    public void backtrack(int[] nums, List<Integer> path) {
        if(path.size() == nums.length) {
            res.add(new ArrayList<>(path));
            return;
        }
        for(int i =0; i < nums.length; i++) {
            if(path.contains(nums[i])) continue;
            path.add(nums[i]);
            backtrack(nums, path);
            path.remove(path.size() - 1);
        }
    
    }
```

## ~~47 Permutation ii~~

建立visited 来判断我们是否访问过此节点，去重方法为如果遇到相邻两点值相等，continue

```
List<List<Integer>> res;
    HashSet<List<Integer>> ans = new HashSet<>();
    public List<List<Integer>> permuteUnique(int[] nums) {
        if(nums.length == 0) return res;
        List<Integer> path = new ArrayList<>();
        boolean[] visited = new boolean[nums.length];
        Arrays.sort(nums);
        backtrack(nums, path, visited);
        res = new ArrayList<>(ans);
        return res;
    }
  
    private void backtrack(int[] nums, List<Integer> path, boolean[] visited) {
        //System.out.println(path);
        if(path.size() == nums.length) {
            ans.add(new ArrayList<>(path));
            return;
        }
        for(int i = 0; i < nums.length; i++) {

            if(visited[i] || (i >= 1 && !visited[i - 1] && nums[i - 1] == nums[i])) continue;
            path.add(nums[i]);
            visited[i] = true;
            backtrack(nums, path, visited);
            path.remove(path.size() - 1);
            visited[i] = false;
        }
    }
```

## ~~236 lowest common ancestor变种~~

主要是利用递归寻找左右两边有没有与p，q值相同的node，有就返回，当左右两边都不为null时说明此点是p和q的公共祖先。当左没有时，right既是，右边同理。

public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
if(root == null) return null;
if(root.val == p.val || root.val == q.val) return root;
TreeNode left = lowestCommonAncestor(root.left, p, q);
TreeNode right = lowestCommonAncestor(root.right, p, q);
if(left != null && right != null)
return root;
if(left == null) return right;
if(right == null) return left;
return null;
}

~~347 top k frequent~~ ood
----------------------

主要是利用heap，构建一个node 含有val和freq，然后利用priorityqueue来进行处理，最后pop出前几位的

## ~~692 top k frequent words~~

维护一个map用来存放freq，用一个size 为k的优先队列来存放string，需要重写compare

```
 public List<String> topKFrequent(String[] words, int k) {
        List<String> res = new ArrayList<>();
        Map<String, Integer> map = new HashMap<>();
        for(String s : words) {
            if(map.containsKey(s))
                map.put(s, map.get(s) + 1);
            else
                map.put(s, 1);
        }
        PriorityQueue<Map.Entry<String,Integer>> pq = new PriorityQueue<>(
        (a, b) -> a.getValue() == b.getValue() ? b.getKey().compareTo(a.getKey()) : a.getValue() - b.getValue());
        for(Map.Entry<String, Integer> entry : map.entrySet()) {
            pq.offer(entry);
            if(pq.size() > k)
                pq.poll();
        }
        while(!pq.isEmpty())
            res.add(0, pq.poll().getKey());
        return res;
    }
```

## ~~253 meeting room变形~~

首先将given array sort（根据开始时间大小)， 然后判断前一个的结束时间是不是大于后一个的开始时间

```
public boolean canAttendMeetings(int[][] intervals) {
   
        Arrays.sort(intervals, (a,b) -> Integer.compare(a[0],b[0]));
        for(int i =0;i<intervals.length -1;i++){
            if(intervals[i][1] > intervals[i+1][0])
                return false;
        }
        return true;
    }



```

```
 public int minMeetingRooms(int[][] intervals) {
       if(intervals == null || intervals.length == 0 ) return 0;
       int n = intervals.length, index = 0;
        int[] begins = new int[n];
        int[] ends = new int[n];
        for(int i =0;i < n;i++) {
            begins[i] = intervals[i][0];
            ends[i] = intervals[i][1];
        }
        Arrays.sort(begins);
        Arrays.sort(ends);
        int rooms = 0, pre = 0;
        for(int i =0;i < n;i ++){
            rooms ++;
            if(begins[i] >= ends[pre]){
                rooms--;
                pre++;
            }
        }
        return rooms;
  

```

关于第二题，我们需要剔出begins和ends时间的数组然后sort。然后建立pre -> 说明的是前一个会议的结束时间，如果for循环中 begin[i] 大于前一个会议的结束时间， 说明我们需要增加会议室。在每次for loop里，会议室++，如果出现以上情况--。

## ~~238 Product of Array Except Self~~

可以使用两个left，right数组，达到乘积和的目的

```
public int[] productExceptSelf(int[] nums) {
        int[] left = new int[nums.length];
        int[] right = new int[nums.length];
        int[] res = new int[nums.length];
        for(int i = 0; i < nums.length; i++) {
            if(i == 0)
                left[0] = 1;
            else
                left[i] = left[i - 1] * nums[i - 1];
        }
  
        for(int i = nums.length - 1; i>= 0; i--) {
            if(i == nums.length - 1)
                right[i] = 1;
            else
                right[i] = right[i + 1] * nums[i + 1];
        }
        for(int i = 0; i < nums.length; i++)
            res[i] = left[i] * right[i];
        return res;
  
    }
```

优化解法：

```
public int[] productExceptSelf(int[] nums) {
        int[] res=  new int[nums.length];
        res[0] = 1;
        for(int i = 1; i < nums.length; i++)
            res[i] = res[i - 1] * nums[i - 1];
        int r = 1;
        for(int i = nums.length - 1; i >= 0; i--) {
            res[i] = res[i] * r;
            r *= nums[i];
        }
        return res;
    }
```

~~237 delete node~~
---------------

将目标node的下一个node的值赋值给给予的node，然后将下一个node删除

design a class that hold collections of expressions
---------------------------------------------------

~~100 same tree~~
-------------

简单的判断p与q是不是同时为null，是不是值相同，然后递归就可以了

```
 boolean flag = true;
    public boolean isSameTree(TreeNode p, TreeNode q) {
        dfs(p, q);
        return flag;
    }
  
    private void dfs(TreeNode p, TreeNode q) {
        if(p == null && q == null) return;
        if(p == null || q == null) {flag = false; return;}
        if(p.val != q.val) {flag = false;}
        dfs(p.left, q.left);
        dfs(p.right, q.right);
  
    }
```

~~75 sort colors~~
--------------

主要是利用两个pointer，left 和right，将num[i] = 0与left交换，将num[i] = 1与right交换，==1的时候i++，注意与left交换时i++

```
public void sortColors(int[] nums) {
        int left = 0, right = nums.length - 1;
        int i = 0;
        while(i <= right) {
            if(nums[i] == 2) {
                swap(nums, right, i);
                right--;
    
            }
            else if(nums[i] == 0) {
                swap(nums, left, i);
                left++;
                i++;
            }
            else 
                i++;
  
        }
    }
  
    private void swap(int[] nums, int i, int j) {
        int temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;
    }
```

## sliding window

~~39 combination sum~~
------------------

```
private List<List<Integer>> res = new ArrayList<>();
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        if(candidates.length == 0) return res;
        List<Integer> path = new ArrayList<>();
        backtrack(candidates, target, path, 0, 0);
        return res;
    }
  
    private void backtrack(int[] candidates, int target, List<Integer> path, int sum, int start) {
        System.out.println(path);
        if(sum == target) {
            res.add(new ArrayList<>(path));
            return;
        }
        else if(sum > target)
            return;
        for(int i = start; i < candidates.length; i++) {
            sum += candidates[i];
        
            path.add(candidates[i]);
            backtrack(candidates, target, path, sum, i);
            path.remove(path.size() - 1);
            sum-= candidates[i];
        }
    
    }
```

## ~~40 combination sum ii~~

```
List<List<Integer>> res = new ArrayList<>();
    public List<List<Integer>> combinationSum2(int[] candidates, int target) {
        if(candidates.length == 0) return res;
        List<Integer> path = new ArrayList<>();
        Arrays.sort(candidates);
        backtrack(candidates, target, 0, path, 0);
    
        return res;
    }
  
    private void backtrack(int[] candidates, int target, int sum, List<Integer> path, int start) {
        if(target == sum) {
            res.add(new ArrayList<>(path));
            return;
        }
        else if(sum > target)
            return;
        for(int i = start; i < candidates.length; i++) {
            if(i > start && candidates[i - 1] == candidates[i]) continue;
        
            path.add(candidates[i]);
            sum += candidates[i];
            backtrack(candidates, target, sum, path, i + 1);
            path.remove(path.size() - 1);
            sum -= candidates[i];
        }
    
    }
```

## ~~77 combinations~~

```
List<List<Integer>> res = new ArrayList<>();
    public List<List<Integer>> combine(int n, int k) {
        List<Integer> path = new ArrayList<>();
        backtrack(n, k, 1, path);
        return res;
    }
  
    private void backtrack(int n, int k, int start, List<Integer> path) {
        if(path.size() == k) {
            res.add(new ArrayList<>(path));
            return;
        }
        if(start > n || path.size() > k) return;
    
        for(int i = start; i <= n; i++) {
            path.add(i);
            backtrack(n, k, i + 1, path);
            path.remove(path.size() - 1);
        }
    }
```

## 126 word ladder ii


## 127 word ladder i

```
 public int ladderLength(String beginWord, String endWord, List<String> wordList) {
        Set<String> wordSet = new HashSet<>(wordList);
        if(wordSet.size() == 0 || !wordSet.contains(endWord)) return 0;
        wordSet.remove(beginWord);
      
        Queue<String> queue = new LinkedList<>();
        queue.offer(beginWord);
        Set<String> visited = new HashSet<>();
        visited.add(beginWord);
      
        int step = 1;
        while(!queue.isEmpty()) {
            int currentSize = queue.size();
            for(int i = 0; i < currentSize; i++) {
                String currentWord = queue.poll();
                if(changeWordEveryoneLetter(currentWord, endWord, queue, visited, wordSet)) 
                    return step + 1;
             
            }
             step ++;
        }
        return 0;
    }
  
    private boolean changeWordEveryoneLetter(String currentWord, String endWord, Queue<String> queue, Set<String> visited, Set<String> wordSet) {
        char[] charArray = currentWord.toCharArray();
        for(int i = 0; i < endWord.length(); i++) {
            char originChar = charArray[i];
            for(char k = 'a'; k <= 'z'; k++) {
                if(k == originChar) continue; //if char is in the original array continue
                charArray[i] = k;
                String nextWord = String.valueOf(charArray);
                if(wordSet.contains(nextWord)) {
                    if(nextWord.equals(endWord)) return true;
                    if(!visited.contains(nextWord)) {
                        queue.add(nextWord);
                        visited.add(nextWord);
                    }
                }
              
            }
            charArray[i] = originChar;
        }
        return false;
    }
```


## ~~155 min stack~~

维护一个arraylist和一个优先队列，就可以了

```
private List<Integer> list;
    private Queue<Integer> queue;
    public MinStack() {
        list = new ArrayList<>();
        queue = new PriorityQueue<Integer>();
    }
  
    public void push(int val) {
        list.add(val);
        queue.add(val);
  
    }
  
    public void pop() {
        int value = list.remove(list.size() - 1);
  
        queue.remove(value);
  
    }
  
    public int top() {
  
        return list.get(list.size() - 1);
    }
  
    public int getMin() {
        int value = queue.peek();
  
        return value;
    }
```

~~2 add two large number~~
----------------------

先转化成int数组，然后将每位相加， 注意index的退位。然后对于进位进行处理，最后转化成char输出

```
public String addStrings(String num1, String num2) {
int len1 = num1.length();
int len2 = num2.length();
// if(len1 < len2)
//     return addStrings(num2, num1);
int[] nums1 = new int[len1];
int[] nums2 = new int[len2];  
for(int i = 0; i < len1; i++)
        nums1[i] = num1.charAt(i) - '0';
    for(int i = 0; i < len2; i++)
        nums2[i] = num2.charAt(i) - '0';
    //always num1 > num2
    int[] res = new int[Math.max(len1, len2) + 1];
    int index1 = len1 - 1, index2 = len2 - 1;
    int index = res.length - 1;
    while(index1 >= 0 || index2 >= 0) {
        if(index1 < 0)
            res[index--] = nums2[index2--];
        else if(index2 < 0)
            res[index--] = nums1[index1--];
        else {
            res[index--] = nums1[index1--] + nums2[index2--];
        }
    }
    index = res.length - 1;
  
    while(index >= 0) {
        if(index!= 0 && res[index] >= 10) {
  
            int temp = res[index];
            System.out.println(temp);
            res[index] = temp % 10;
            res[index - 1] = res[index - 1] + temp / 10;
        }
        index--;
    }
  
    StringBuilder ans = new StringBuilder("");
    for(int i = 0; i < res.length; i++) {
        if(i == 0 && res[i] == 0) continue;
        ans.append(res[i]);
    }
    return ans.toString();
}
```

~~139 Word break~~
--------------

```
HashMap<String, Boolean> map = new HashMap<>();
    public boolean wordBreak(String s, List<String> wordDict) {
      
        boolean[] dp = new boolean[s.length() + 1];
        for(String temp : wordDict)
            map.put(temp, true);
        dp[0] = true;
        for(int i = 1; i <= s.length(); i++) {
            for(int j = i - 1; j >= 0; j--) {
                dp[i] = dp[j] && check(s.substring(j, i));
                if(dp[i]) break;
            }
        }
        return dp[s.length()];
    }
  
    public boolean check(String temp) {
        return map.getOrDefault(temp, false);
    }
```

140 Word break
--------------

~~151Reverse words in a string~~
----------------------------

很简单，用split分开得到单独的单词然后逆序append到stringbuilder返回

```
 public String reverseWords(String s) {
        if(s == null) return s;
  
  
        String[] splitted = s.split("\\s+");
        StringBuilder sb = new StringBuilder();
        for(int i = splitted.length - 1; i >= 0; i--) {
            if(!splitted[i].isEmpty())
                sb.append(splitted[i]).append(" ");
  
        }
   
        return sb.toString().trim();
    }
```

~~137 single number~~
-----------------

很简单，使用hashmap即可，hashset应该也可以

```
public int singleNumber(int[] nums) {
        HashMap<Integer, Integer> map = new HashMap<>();
        for(int i = 0; i < nums.length; i++) {
            map.put(nums[i], map.getOrDefault(nums[i], 0) + 1);
        }
        for(int num : nums) {
            if(map.get(num) == 1) return num;
        }
        return 0;
    }
```

797 All paths from source to target
-----------------------------------

回溯算法

```
List<List<Integer>> res; 
    int last_index;
    public List<List<Integer>> allPathsSourceTarget(int[][] graph) {
        res = new ArrayList<>();
        last_index = graph.length - 1;
        LinkedList<Integer> path = new LinkedList<>();
        path.addLast(0);
        backtrack(graph, path, 0);
        return res;
    }
  
    public void backtrack(int[][] graph, LinkedList<Integer> path, int index) {
        if(index == last_index){
            res.add(new ArrayList<>(path));
            return;
        }
        for(int i : graph[index]) {
            path.addLast(i);
            backtrack(graph, path, i);
            path.removeLast();
        }
    }
```

29 divide two integers
----------------------

因为溢出的问题，我们需要将正数转化为负数再做计算。利用指数级增长来计算除数

```
public int divide(int dividend, int divisor) {
        // O(log(dividend))
        if(dividend == 0)   return 0;
        int sign = 1;
        if(dividend == Integer.MIN_VALUE && divisor == -1) return Integer.MAX_VALUE;
        //negative
        if((dividend > 0 && divisor < 0)  || (dividend < 0 && divisor > 0))
            sign = -1;
        //avoid overflow
        dividend = dividend > 0 ? -dividend : dividend;
        divisor = divisor > 0 ? -divisor : divisor;
        return sign * helper(dividend, divisor);
  
    }
  
    public int helper(int a, int b) {
        // a = -1, b = -5
        if(a >= b) return a > b? 0:1;
        int count = 1;
        int res = 0;
        int tb = b;
        while(a <= tb && tb < 0) {
            a -= tb;
            res += count;
            tb += tb;
            count += count;
        }
        return res + helper(a, b);
    }
```

~~49 group anagrams~~
-----------------

```
 public List<List<String>> groupAnagrams(String[] strs) {
        if(strs == null || strs.length == 0)
            return new ArrayList();
        HashMap<String, List> map = new HashMap<>();
        for(String s : strs) {
            char[] chars = s.toCharArray();
            Arrays.sort(chars);
            String key = String.valueOf(chars);
          
            if(!map.containsKey(key))
                map.put(key, new ArrayList());
            map.get(key).add(s);
          
        }
        return new ArrayList(map.values());
    }
```

79 word search i 212 word search ii
-----------------------------------

206 reverse linkedlist
----------------------

273 Integer to english words
----------------------------

138 copy list with random pointer
---------------------------------

## ~~242 valid anagram~~

```
public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) {
        return false;
    }
        int[] alpha = new int[26];
        for(int i = 0 ; i< s.length(); i++)
            alpha[s.charAt(i) - 'a']++;
        for(int i = 0; i < t.length(); i++){
            alpha[t.charAt(i) - 'a']--;
            if(alpha[t.charAt(i) - 'a'] < 0)
                return false;
        }
            return true;
    }
```

295 find median from data stream变形
------------------------------------

## sentence里边两个word的最短距离

## ~~200 Number of island~~

dfs查询，建立两个for循环来遍历grid，如果遇到1，就进行dfs将这个岛的1全部改成0

```
void dfs(char[][] grid, int row, int col){
        int rowMax=grid.length;
        int colMax=grid[0].length;
        if(row<0||col<0||row>=rowMax||col>=colMax||grid[row][col]=='0'){
            return;
        }
        grid[row][col]='0';
        dfs(grid,row-1,col);
        dfs(grid,row+1,col);
        dfs(grid,row,col-1);
        dfs(grid,row,col+1);
    }
  
  
     public int numIslands(char[][] grid) {
        if(grid==null||grid.length==0)
            return 0;
         int rowMax=grid.length;
         int colMax=grid[0].length;
         int num_islands=0;
         for(int row=0;row<rowMax;row++){
             for(int col=0;col<colMax;col++){
                 if(grid[row][col]=='1'){
                     num_islands++;
                     dfs(grid,row,col);
                 }
             }
         }
         return num_islands;
    }
```

进步做法，union find

```
class UnionFind {
int count; // # of connected components
int[] parent;
int[] rank;
public UnionFind(char[][] grid) { // for problem 200
  count = 0;
  int m = grid.length;
  int n = grid[0].length;
  parent = new int[m * n];
  rank = new int[m * n];
  for (int i = 0; i < m; ++i) {
    for (int j = 0; j < n; ++j) {
      if (grid[i][j] == '1') {
        parent[i * n + j] = i * n + j;
        ++count;
      }
      rank[i * n + j] = 0;
    }
  }
}

public int find(int i) { // path compression
  if (parent[i] != i) parent[i] = find(parent[i]);
  return parent[i];
}

public void union(int x, int y) { // union with rank
  int rootx = find(x);
  int rooty = find(y);
  if (rootx != rooty) {
    if (rank[rootx] > rank[rooty]) {
      parent[rooty] = rootx;
    } else if (rank[rootx] < rank[rooty]) {
      parent[rootx] = rooty;
    } else {
      parent[rooty] = rootx; rank[rootx] += 1;
    }
    --count;
  }
}

public int getCount() {
  return count;
}
```

```

}
}}

public int numIslands(char[][] grid) {
if (grid == null || grid.length == 0) {
return 0;
}
int nr = grid.length;
int nc = grid[0].length;
int num_islands = 0;
UnionFind uf = new UnionFind(grid);
for (int r = 0; r < nr; ++r) {
  for (int c = 0; c < nc; ++c) {
    if (grid[r][c] == '1') {
      grid[r][c] = '0';
      if (r - 1 >= 0 && grid[r-1][c] == '1') {
        uf.union(r * nc + c, (r-1) * nc + c);
      }
      if (r + 1 < nr && grid[r+1][c] == '1') {
        uf.union(r * nc + c, (r+1) * nc + c);
      }
      if (c - 1 >= 0 && grid[r][c-1] == '1') {
        uf.union(r * nc + c, r * nc + c - 1);
      }
      if (c + 1 < nc && grid[r][c+1] == '1') {
        uf.union(r * nc + c, r * nc + c + 1);
      }
    }
  }
}

return uf.getCount();
}
```

## ~~994 rotting oranges~~

bfs

```
 int rowMax;
    int colMax;
  
    public int orangesRotting(int[][] grid) {
        if(grid == null || grid[0].length == 0) return -1;
        int count_fresh = 0;
        Queue<Pair<Integer, Integer>> queue = new LinkedList<>();
        rowMax = grid.length;
        colMax = grid[0].length;
        for(int row = 0; row < rowMax; row++) {
            for(int col = 0; col < colMax; col++) {
                if(grid[row][col] == 2) queue.offer(new Pair(row, col));
                else if(grid[row][col] == 1) count_fresh++;
            }
        }
        if(count_fresh == 0) return 0;
        int count = 0;
        int[][] dir = new int[][]{{-1, 0}, {1, 0}, {0, 1}, {0, -1}};
        while(!queue.isEmpty()) {
            count++;
            int size = queue.size();
            for(int i = 0; i < size; i++) {
                Pair<Integer, Integer> pair = queue.poll();
                int row = pair.getKey();
                int col = pair.getValue();
                for(int[] d : dir) {
                    int r = row + d[0];
                    int c = col + d[1];
                    if(r<0 || r>=rowMax || c<0 || c>=colMax || grid[r][c] == 0 || grid[r][c] == 2) continue;
              
                    grid[r][c] = 2;
                    queue.add(new Pair(r, c));
                    count_fresh--;
                }
            }
        }
        return count_fresh == 0? count - 1 : -1;
    }
```

4 median of two sorted array
----------------------------

49 give a sentence and find anagram in it
-----------------------------------------

## 763 partition labels

首先记录不同字母最后出现的位置

利用index，将字符遍历到它出现的最远的位置，然后break，就可以partition了

```
  public List<Integer> partitionLabels(String s) {
        int[] last = new int[26];
        for(int i = 0; i < s.length(); i++) {
            last[s.charAt(i) - 'a'] = i;
        }
  
        List<Integer> res = new ArrayList<>();
        int j = 0, anchor = 0;
        for (int i = 0; i < s.length(); ++i) {
            j = Math.max(j, last[s.charAt(i) - 'a']);
            if (i == j) {
                res.add(i - anchor + 1);
                anchor = i + 1;
            }
        }
        return res;
    }
```

## ~~股票买卖~~

主要是利用三/两/一维 dp （维度视可允许操作数来看）来进行动态规划，

dp[ink0] = Math.max(dp[i - 1 nk 0], dp[i - 1 nk 1] + prices[i - 1])

dp[ink1] = Math.max(dp[i - 1nk 1], dp[i - 1 nk - 1 0] - prices[i - 1])

nk是可交易数

## ~~316 remove duplicate characters~~

单调栈，要确保字典序，我们需要不断判断谁的开头asc码最小，如果有更小的弹出之前的

```
public String removeDuplicateLetters(String s) {
        Stack<Character> stack = new Stack<>();
        HashSet<Character> visited = new HashSet<>();
        HashMap<Character, Integer> last_index = new HashMap<>();
        for(int i = 0; i < s.length(); i++) last_index.put(s.charAt(i), i);
        for(int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if(!visited.contains(c)) {
                //if the letter in the solution
                while(!stack.isEmpty() && c < stack.peek() && last_index.get(stack.peek()) > i) {
                    visited.remove(stack.pop());
                }
                visited.add(c);
                stack.push(c);
            }
        }
        StringBuilder sb = new StringBuilder();
        for(Character c : stack) sb.append(c.charValue());
        return sb.toString();
    }
```

## ~~215 kth largest element in the array~~

利用快速排序的原理，我们返回的j值即为第x大的元素位置。

主要难度在parition， 大的while loop都是true，小的即为  --/++x

```
public int findKthLargest(int[] nums, int k) {
        int targetIndex = nums.length - k;
        int low = 0, high = nums.length - 1;
        while(true){
            int partitionIndex = partition(nums, low, high);
            if(partitionIndex == targetIndex)
                return nums[targetIndex];
            else if(partitionIndex < targetIndex)
                low = partitionIndex + 1;
            else
                high = partitionIndex - 1;
        }
    }
  
    public int partition(int[] nums, int low, int high) {
        if(low == high) return low;
        int i = low, j = high + 1;
        int cmp = nums[i];
        while(true) {
            while(nums[++i] < cmp) {
                if(i == high) break;
            }
            while(nums[--j] > cmp) {
                if(j == low) break;
            }
            if(i >= j) break;
            exch(nums, i, j);
        }
        exch(nums, j, low);
        return j;
    }
  
    private void exch(int[] nums, int i, int j) {
        int temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;
    }
```

## ~~56 Merge Intervals~~

首先sort given array，然后建立list来接受新的merged intervals，和meeting room类似，当我们的前一个的结束时间比下一个的开始时间晚的话，我们需要merge这两个interval，用math max来获得最晚的结束时间，如果没有overlap，就将此interval加入list，然后返回

```
public int[][] merge(int[][] intervals) {
        Arrays.sort(intervals, (a, b) -> Integer.compare(a[0] , b[0]));
        List<int[]> list = new ArrayList<>();
        int start = intervals[0][0], end = intervals[0][1];
        for(int i = 1; i < intervals.length; i++) {
            if(intervals[i][0] <= end) {
                //overlap
                end = Math.max(intervals[i][1], end);
    
            }
            else{
                list.add(new int[]{start, end});
                start = intervals[i][0];
                end = intervals[i][1];
            }
        }
        list.add(new int[]{start, end});
        int[][] res = new int[list.size()][2];
        for(int i = 0; i < list.size(); i++) {
            res[i] = list.get(i);
        }
        return res;
  
    }
```

## ~~20 Valid parentheses~~

很简单，使用stack，遇到【{（就push】}），当我们将左侧括号都push进去后开始pop，如果遇到pop！=c，说明不valid，最后return stack.isempty，因为如果stack不空，说明多了一个括号。

```
public boolean isValid(String s) {
        if(s == null) return false;
        Stack<Character> stack = new Stack<>();
        for(int i = 0; i < s.length(); i++) {
            if(s.charAt(i) == '(') stack.push(')');
            else if(s.charAt(i) == '[') stack.push(']');
            else if(s.charAt(i) == '{') stack.push('}');
            else if(stack.isEmpty() || s.charAt(i) != stack.pop()) return false;
        }
        return stack.isEmpty();
    }
```

## ~~210 207 Course schedule~~

拓扑排序

当课程构成环时我们就无法满足条件完成课程。使用dfs查看是否有环

hashmap存对应课程和它的先修课， 维护一个visited的set，如果出现二次访问，说明出现环

```
public boolean canFinish(int numCourses, int[][] prerequisites) {
        //build graph 
        //in-degree map
        //pre -> course
        List<Integer>[] graph = new ArrayList[numCourses];
        int[] inDegree = new int[numCourses];
        for(int i = 0; i < numCourses; i++) {
            graph[i] = new ArrayList();
        }
        //build graph
        for(int[] pair : prerequisites) {
            int pre = pair[1];
            int cur = pair[0];
            graph[pre].add(cur);
            inDegree[cur]++;
        }
        //bfs topo
        int visited = 0;
        Queue<Integer> queue = new LinkedList<>();
        for(int i = 0; i < numCourses; i++) {
            if(inDegree[i] == 0)
                queue.add(i);
        }
  
        while(!queue.isEmpty()) {
            int cur = queue.remove();
            visited++;
            for(Integer child : graph[cur]) {
                inDegree[child]--;
                if(inDegree[child] == 0)
                    queue.add(child);
            }
        }
  
        return visited == numCourses;
    }
```

## ~~11 container with most water~~

双指针，left right不停压缩，利用math max找到最大的container

```
public int maxArea(int[] height) {
        if(height.length == 0 || height == null) return 0;
        int len = height.length;
        int left = 0, right = len - 1;
        int res = 0;
        while(left < right) {
            if(height[left] < height[right]) {
                res = Math.max(res, (right - left) * height[left]);
                left++;
            }
            else {
                res = Math.max(res, (right - left) * height[right]);
                right--;
            }
        }
        return res;
    }
```

## ~~1539 kth missing positive number~~

还可以用binary search, 一个缺失元素的递增数组，会有arr[i]> i + 1的情况。所以arr[i] - 1 - i > 0，以此类推，当缺失k个的时候即为 arr[i] - 1 - i = k

```
public int findKthPositive(int[] arr, int k) {
        int left = 0, right = arr.length - 1 , mid = 0;
        while(left <= right) {
            mid = left + (right-left) /2;
            if(arr[mid] - mid >=k + 1) {
                right = mid - 1;
            }
            else{
                left = mid + 1;
            }
        }
        return k + left;
    }
```

```
public int findKthPositive(int[] arr, int k) {
        int i = 0, p = 1;
        while(i < arr.length) {
  
            if(p != arr[i]) {
                k--;
                if(k == 0)
                    return p;
            }
            else{
                i++;
            }
            p++;
        }
        return p - 1 + k;
  
    }
```

## ~~937 reorder data in log files~~

```
public String[] reorderLogFiles(String[] logs) {
        List<String> alpha = new ArrayList<>();
        List<String> nums = new ArrayList<>();
        for(int i = 0; i < logs.length; i++) {
            String cur = logs[i];
            int pos = cur.indexOf(" ");
            if(Character.isDigit(cur.charAt(pos + 1)))
                nums.add(cur);
            else
                alpha.add(cur);
        }
        alpha.sort(new Comparator<String>() {
            public int compare(String o1, String o2) {
                int pos1 = o1.indexOf(" ");
                int pos2 = o2.indexOf(" ");
                String str1 = o1.substring(pos1 + 1);
                String str2 = o2.substring(pos2 + 1);
                int cmp = str1.compareTo(str2);
                if(cmp == 0) {
                    return o1.substring(0, pos1).compareTo(o2.substring(0, pos2));
                }
                else
                    return cmp;
            }
  
        } );
        String[] res=  new String[logs.length];
        int index = 0;
        for(int i = 0; i < logs.length; i++) {
            if(i < alpha.size())
                res[index++] = alpha.get(i);
            else
                res[index++] = nums.get(i - alpha.size());
        }
        return res;
    }
```

# OOD

## Design parking lot

```

public enum VehicleSize { Motorcycle, Compact,Large }
  
public abstract class Vehicle
{
      protected ArrayList<ParkingSpot> parkingSpots =
                           new ArrayList<ParkingSpot>();
      protected String licensePlate;
      protected int spotsNeeded;
      protected VehicleSize size;
  
      public int getSpotsNeeded()
      {
          return spotsNeeded;
      }
      public VehicleSize getSize()
      {
          return size;
      }
  
      /* Park vehicle in this spot (among others,
         potentially) */
      public void parkinSpot(ParkingSpot s)
      {
          parkingSpots.add(s);
      }
  
  
      /* Remove vehicle from spot, and notify spot
         that it's gone */
      public void clearSpots() { ... }
  
      /* Checks if the spot is big enough for the
         vehicle (and is available).
         This * compares the SIZE only.It does not
        check if it has enough spots. */
      public abstract boolean canFitinSpot(ParkingSpot spot);
}
  
public class Bus extends Vehicle
{
    public Bus()
    {
        spotsNeeded = 5;
        size = VehicleSize.Large;
    }
  
    /* Checks if the spot is a Large. Doesn't check
     num of spots */
    public boolean canFitinSpot(ParkingSpot spot) 
    {... }
}
  
public class Car extends Vehicle
{
    public Car()
    {
        spotsNeeded = 1;
        size = VehicleSize.Compact;
    }
  
    /* Checks if the spot is a Compact or a Large. */
    public boolean canFitinSpot(ParkingSpot spot) 
    { ... }
}
  
public class Motorcycle extends Vehicle
{
    public Motorcycle()
    {
        spotsNeeded = 1;
        size = VehicleSize.Motorcycle;
    }
    public boolean canFitinSpot(ParkingSpot spot) 
    { ... }
}

public class ParkingSpot
{
    private Vehicle vehicle;
    private VehicleSize spotSize;
    private int row;
    private int spotNumber;
    private Level level;
  
    public ParkingSpot(Level lvl, int r, int n,
                         VehicleSize s)
    { ... }
  
    public boolean isAvailable()
    {
        return vehicle == null;
    }
  
    /* Check if the spot is big enough and is available */
    public boolean canFitVehicle(Vehicle vehicle) { ... }
  
    /* Park vehicle in this spot. */
    public boolean park(Vehicle v) {..}
  
    public int getRow()
    {
        return row;
    }
    public int getSpotNumber()
    {
        return spotNumber;
    }
  
    /* Remove vehicle from spot, and notify
      level that a new spot is available */
    public void removeVehicle() { ... }
}

```

## 1472 design broswer history

## Design locker system

```
User.java
public class User {
  private String name;
  private Address address;
  private String email;
  private String phone;
}
Account.java
public class Account {
  private String accountId;
  private String password;
  private AccountStatus status; //Prime, Not a prime, 
  private User user;

  public boolean resetPassword() { ... };
  public boolean packageRetrieved(PackageId packageId) {...};
  public boolean packageRefunded(PackageId packageId, Date date){ ... };
  public Locker searchForLockerNearYou(String address, Date date){ ... };
  public DeliveryStatus getNotifications(){...};
  public boolean updateDeliveryMode(Delivery delivery) {...};
  public boolean updateDeliveryDateForParticularPackage(Delivery delivery, Date date) {...};
}
Package.java
public class Package {
  String packageId;
  int height;
  int weight;
  int width;
  int breadth;
 
  public LockerSize findLockerSizeForPackage(String packageId, int height, int width, int breadth){...}
}
Order.java
public class Order {
  String OrderId;
  Date orderCreationDate;
  List<Packages> listOfPackages;
  
  public void updateOrder(){...};
  public void cancelOrder(){...};
}
Locker.java
public class Locker {
  
  private LockerId lockerId;
  private LockerSize lockerSize;
  private String address;
  private int totalCapacity;
}
LockerSlot.java
public class LockerSlot {
  private List<LockerSlot> listOfSlots;
  private String lockerSlotId;
  private LockerId lockerId;
  private Date lastOccupied;
  private LockerStatus lockerStatus;

  public boolean isOccupied() {...};
  //total available locker slots for a particular date
  public List<LockerSlot> getTotalAvailableLockerSlot(LockerId lockerId, Date date) { ... }
}
Delivery.java
public class Delivery {
  private DeliveryStatus deliveryStatus;
  private DeliveryMode deliveryMode;
  private Date expectedDeliveryDate;
  private DeliveryVehicle deliveryVehicle
  
  // ability to send OTP
  public void sendOTP() {...}
  
}
Notification.java
public class Notification {
	String notificationId;
	NotificationMode notificationMode;
	NotificationStatus notificationStatus;
}
Payment.java
public class Payment {
	String paymentId;
	PaymentMode paymentMode;
	PaymentStatus paymentStatus;

	boolean makeTransaction() {...}
}
```

## Airline management system

```
Airport.java
public class Airport {

	String airportName; // for eg: SeaTac, Sky Harbor, Charles Douglas;
	String address;
	String uniqueAirportId; // for each airport

}
Airline.java
public class Airline {
	String airlineName; //Alaska, American, Delta
	String airlineCode; //1,2,3
}
Aircraft.java
public class Aircraft {
	String manufacturer; //boeing, airbus
	String model; //737, A300
	String yearsInService;
	String lastService;
	String manufacturingDate;

}
Flight.java
public class Flight {
	String flightNumber;
	String source;
	String destination;
	String departureTime;
	String expectedArrivalTime;
	Aircraft assignedAircraft; //each flight will be an instance so a flight from seattle to london at a paricular time is 1 instance of flight
	Airport airport;

	boolean addFlightSchedule() {...} //information like source destination date time etc.
	void updateStatus(FlightStatus flightStatus) {...} //update the status of the flight
	boolean cancel() {...} // cancel the flight.

}
FlightReservation.java
To pull out the reservation of the entire flight

/*To pull out the reservation of the entire flight*/
public class FlightReservation {

		Flight flight;
		String reservationNumber;
		Map<Passenger, Seat> seatMap;
		ReservationStatus reservationStatus;

		public List<Passenger> getPassengers() {...}
		public FlightReservation getFlightReservation(String reservationNumber) {...}

}
Seat.java
Class to assign seats to passengers for a particular flight instance.

/*Class to assign seats to passengers for a particular flight instance.*/
public class Seat {
	String seatFare;
	String seatType;
	String seatNumber;

	public float getFare() {...}
}
Itinerary.java
Both the customer and front-desk can use the itinerary class to book/ cancel/ update the reservation.

/*
Both the customer and front-desk can use the itinerary class to book/ cancel/ update the reservation.
*/
public class Itinerary {
	String customerId;
  	Airport startingAirport;
  	Airport finalAirport;
  	Date creationDate;
  	List<FlightReservation> reservations;

  	public List<FlightReservation> getReservations();
  	public boolean makeReservation();
  	public boolean makePayment();

}
Payment.java
public class Payment {
	String paymentId;
	PaymentMode paymentMode;
	PaymentStatus paymentStatus;

	boolean makeTransaction() {...}
}
Notification.java
public class Notification {
	String notificationId;
	NotificationMode notificationMode;
	NotificationStatus notificationStatus;
}
```

## Online book store

```
Book.java
  private String ISBN;
  private String title;
  private String subject;
  private String publisher;
  private String language;
  private int numberOfPages;
  private List<Author> authors;
BookItem.java
One unit of a Book is a BookItem.

  private String barcode;
  private boolean isReferenceOnly;
  private Date borrowed;
  private Date dueDate;
  private double price;
  private BookStatus status;

  public boolean checkout(String memberId) {...}
User.java
public class User {
  private String name;
  private Address address;
  private String email;
  private String phone;
}
Account.java
public abstract class Account {
  private String accountId;
  private String password;
  private AccountStatus status; //Prime, Not a prime, 
  private User user;

  public boolean resetPassword() { ... };
  //total number of books that the account current has leased; 
  public int getTotalBooksCheckedout() {...};
  public void setTotalBooksCheckedout() {...};
  
  //account reserving books that are currently out of stock.
  public boolean reserveBookItem(BookItem bookItem) {...};
  //account reserving books that are currently out of stock.
  public boolean returnBookIten(BookItem bookItem) {...};
  //account reserving books that are currently out of stock.
  public boolean renewBookItem(BookItem bookItem) {...};
  //check for fine.
  void checkForFine(String bookItemBarcode) { ... }
}
BookReservation.java
public class BookReservation {  
  private Date creationDate;
  private ReservationStatus status;
  private String bookItemBarcode;
  private String memberId;

  public static BookReservation fetchReservationDetails(String barcode) {...};
}
BookLeasing.java
public class BookLeasing {
  private Date creationDate;
  private Date dueDate;
  private Date returnDate;
  private String bookItemBarcode;
  private String accountId;
  private boolean isAvailable;

  // lend the book to a particular accountId
  public static void lendBook(String barcode, String accountId) { ... };
  public static BookLeasing fetchLeasingDetails(String barcode);
 //check if a particular book that is selected is available.
  public boolean isBookAvailableForLease(String barcode);
}
Catalog.java
This class will be used by the user to search respective books based on title and author or genre.

  private HashMap<String, List<Book>> bookTitles;
  private HashMap<String, List<Book>> bookAuthors;
  private HashMap<String, List<Book>> bookGenre;
  private HashMap<String, List<Book>> bookPublicationDates;

  public List<Book> searchByTitle(String query) {
    // return all books containing the string query in their title.
    return bookTitles.get(query);
  }

  public List<Book> searchByAuthor(String query) {
    // return all books containing the string query in their author's name.
    return bookAuthors.get(query);
  }

  public List<Book> searchByGenre(String query) {
    // return all books containing the string query in their author's name.
    return bookGenre.get(query);
  }
  //update the catalog for a particular book if it is leased.
  public int updateCatalog(Book book) {...};
  
  //notify all the account if a particular book become available.
  public List<AccountId> notifyAccounts() { ... };
  
Fine.java
  private Date creationDate;
  private double bookItemBarcode;
  private String memberId;

  public static void collectFine(String accountId, long days) { ... }
Payment.java
public class Payment {
	String paymentId;
	PaymentMode paymentMode;
	PaymentStatus paymentStatus;

	boolean makeTransaction() {...}
}
Notification.java
public class Notification {
	String notificationId;
	NotificationMode notificationMode;
	NotificationStatus notificationStatus;
}
```

# Behavior questions

Think long term, put the customer in the center of our universe and invent.

you can't invent beyond customers

follow STAR rule:

Situation：事情是在什么情况下发生
Task：你是如何明确你的任务的
Action：针对这样的情况分析，你采用了什么行动方式
Result：结果怎样，在这样的情况下你学习到了什么

ADL Algorithm

The project was a year-long project, it was issued by a company called Inovnoics(the company is a wireless sensor provider, they have different devices installed in senior living....) who wanted to know if it was possible to use machine learning method to forecast future warnings based on feed data. By warnings, it means unsual body index like low blood pressure, low blood oxygen, etc. The company wanted to see if it is possible to forecase such sympotoms after we feed the data to the model. And for the whole project, we pretty much start from the scarth, in terms of we have to crate data on our own since it would be a violation if the company gave us user data without permission which they haven't get even after I left.

So our group had a meeting with the sponsor who is the tech officer of the company, and we discussed the goal and requirements of the project. After that we had our group meeting to discuss the detailed implementation. We have splitted the project into two parts, create data, and we do the machine learning part.

We start with the data part where the sponsor gave us a list of activities of one of the users. These activities were daily basis, each day contains few activities with some body indices like blood pressure, blood oxygen, pulse pressure, etc.  And locations were also provided to us, its more like during 830-900, john was at kitchen and these were his body indices.

## Tell me about a time you failed/ The biggest mistake you made

→ 对应的是 earn trust, customer obsession
错误不能是致命伤,突出的是为了customer坚持了什么，没有customer的换成老师同学小组都可以。

I think it has to be that insisted on using bigquery as our database instead of other services like heroku since we in the end deployed our web app on heroku. Bigquery is more like data warehouse designed to help you for big data/ machine learning related projects. but we wanted to use bigquery as our database and it was extremely wired to use since we are developing locally and we have to generate data locally and push it to the bigquery, and get through bunch of autentication and used not up to date bigquery api to get data. Most importantly, heroku doesn't support the most current bigquery api so we have to use the oldest one and do lots of data preprocessing before we put the data into the model. But the reason why I insisted on using bigquery is that my sponsor didnt want me to use other services since they have paid quite a lot to purchase the service and they wanted to keep it up. Although they said they could afford heroku database serivce, but I thought we could do that using bigquery without costing more. With such difficulties, we managed to find a way to push /retrieve the data and deployed on heroku with not really intuitive ways.

## Take a risk, or do not have much time, to make a decision/ Tell me about a time when you had to work on a project with unclear responsibilities.

→ 对应的是 Bias for action, Ownership.
是行动优先，而且是要突出当仁不让，有责任自己能顶上的意识。比如customer找不到人刚好你在，你能主动做些事。

So when I was developing the ADL algorithm project, in the start the whole development group was a mess, although we had our goal and we had planned something ahead. But each one of the group members was just coding on their own, there was no communication, no code review at that time. So I decided to become the connector bewteen the group members and gradually I started to own the project in terms of I was literally at every meeting and code review session, like I just said we had members focus on creating data and some members were focusing on create web app(and that was one of my responsibilities). I was in both, so when the project was delivered, I knew the every part of the code that we pushed. I held the weekly meeting with the group and the sponsor to discuss the process and updated requirements although it was not my responsibilities to do these things, but I thought I have to carry the whole team when none of the team member wanted to take that responsibility.

## Challenging client-facing situation/ Disagree with teammate or manager/ Tell me a time when you did something without asking approval from you manager

→ 对应的是earn trust
这个很多人没对准，记住不是强行说服或者没什么理由的顺应别人, 为了customer或者最重要目的所以不同意别人。都是好说辞，和事佬的说法是偏题。
介绍背景，说出分歧。然后说自己怎么做，可以是讨论trade off, 可以是坚持高标准..等 结局一定说最后的选择是对的。 It proved to work well.

So for our adl project, in the start everyone including the sponsor wanted to only testify if we can create a model to forecast and analyze the data and generate warings, which means that probably in the end the only thing we had was just a python notebook and some csv files. I thought it was kind of weird to have these two things called project and let alone we have to push our work to the company. Also considering of if this could really work, the tech staff in the company would have to develop some applications using our python notebook code. So I thought we should develop some valid staff to allow future implementation and usage. Then I decided to develop a web app which would allow user to recieve warnings, check data, etc. My idea was not supported by my team members and the sponsor as well. my team member wanted smaller workload and my manager wanted me to focus on the model itself. But I decided to work on my own to develop the web app and I integrated it the model and data after few months, then I deployed it on the Heroku, suppported by bigquery database. Meanwhile, I helped the team to finish the model which could generate warnings and forecast future warnings. And when we finally presented our project to the manager, he was really happy about the output and invited me to do another one w/ the company's president who was also satisfied about the web app since it could be really working. So it proved to work well in the end.

## Most challenging/proudest project/Tell me a time you solved a complex problem

→ 对应的是highest standards, think big
要讲自己怎么走出comfort zone, 当然舒适区本身也是一道题。
扣题，怎么复杂，是deadline 紧，还是技术复杂，你怎么做的，学习了新技术，use my priavte time to work on it 等等 最后说结果或者说通过这个process 你学到了什么

So we had a machine learning project just due few weeks ago which we were going to use crypto prices to predict bitcoin price in the next hour.  It was my first time doing project related to machine learning. At that time we were really confused about how did we feed the data to our model so it can predict the bitcoin prices in the next hour, also if we only feed the data of bitcoin that was definitely not enough, since we only had 2 features after we tested the rest of features using heatmap. So I kind of jumped out of my comfort zone at that time in term of starting to reading some academic paper seriously and looking at mathmateical formulas. Until one day I found a paper talking about they found out the the high correlation between different types of cryptos to bitcoin, and inspired by that paper, we decided to run several test to find out the corelation between litecoin, tezos, eth and bitcoin. After drawing few plots, we have decided to use litecoin, tezos and eth as our features to predict bitoin price. And another paper was talking about they were using different lagging timestamps to predict meat prices at an area. So we decided to use lagging crypto prices to predict the bitcoin price in the next hour, with the help of LSTM which is the nerual network. Altough our result was highly influenced by the external factors, but when the external factors are small enough to not shock the market, the model performance meets our expectation.

## Miss deadline  对应的是customer obsession, Deliver Results.

要突出怎么让影响最小, 让customer不受影响。讲你自己的影响就偏题了。
解释为何会miss 你是怎么把损失降到最低的，最后结果是好的，影响不是很大

So in the end of my internship, when I was going to finish my web app and push it to the workflow then leave, the tech department had a meeting w/ me that they wanted to change the frontend from react js to angular since the whole company's web products were written in angular. And it would be really hard for them to do the further development after I leave. So it was only 3 days left before the last day I can work there. To make sure that the product could be esaily develop and for the convience of other staff. I started to learning angular and rewirte everything I had. On the third day, I was still working on the furnishing the web page though most of the base functions were finished at that time. The angular web app was working although it was really simple at that time. But It was easy to take from there for the other tech staff since the part where I couldn't finish was similar to any other angular frontend design. I did miss the deadline that I didnt finish the web app completely, but the parts I finished were enough to make the web app functional.

## Tell me a time when you received negative feedback

先介绍背景,别人对你哪里不满意了, 简单说以下就行, 不要说很多别人如何对你不满, 也不要sugar coat 说自己其实没错。重点放在自己怎么解决这个问题，以及学到了什么。结果一定是好结果

So when I was doing movietracker project, when we were in the middle of the development, we were interviewed by a ta who told me that your ood design was really bad and "it was shit". Since we didnt off hook the data part with the other part of the backend, which is a design pattern called DAO(data access object) that is used to separate low level data accessing api or operations from high level business services. So we googled that design pattern and started to working on the code. We have created several dao classes to retrieve the data from the database and send it to other high level classes if needed. One thing I learned from this interview was when we are designing the backend, we need to off hook the data accessor with other high level classes, to isolate the application layer from the persistence layer. I used the same design in the future development, like adl algorithm and other backend I have developed.

## Tell me about a time when you gave a simple solution to a complex problem/ Find a new way to do something

这个问题一定要让面试官信服你说的例子。先说一般的方法很耗时，自己找到一个方法很快就完成并且Del‍‌‍‌‍‌‌‌‌‌‍‌‍‍‍‌‍‍‌‍iver 了，而且很稳定，没出过问题，结果要是好的。

So when I was in the internship for Inovonics they wanted me to use angular for the frontend of the web app. So I have to integrated everything and one of the things I needed to rewrite is data retrieving part. Since it would be great if we could use some api to get json file and push it to the frontend in angular framework, I spent a lots of time on looking for a way to figure out how to do that but it seems really hard since it requires some autentication part and other factors. Since the company insisted on using angular and bigquery services, I needed to find a way to do that ,even a detour. So I decided to use flask to get bigquery data then trim the data and then  we pushed the data to the frontned, angular will have an function to recieve the data and push it to the component where it needed. It took me a day to test the data pusher and recivever on angular and then the function was pretty much done.

# Leading Principles

顾客至上：永远站在顾客的视角上看待问题
领导视角：目光长远, 相对于完成短期工作任务，更关注对于公司的长期收益
创造优化：不断创新，并且精简工作中不必要的流程
洞察预判, 挑战自己：用直觉为公司做判断
不断学习：做一台没有感情的学习机器
选择最优：总裁养成计划：会用人也会培养人
坚持最高标准：完美主义+强迫症: 对自己对团队最高要求， 从长计议，长期收益永远高于短期收益
大智慧全局观:想的多、想的远、想的“骚”(揽客思路要骚)
行动是第一生产力: 敢冒险勇担责
勤俭持家从我做起：doing more with less
获取信任：与用户、同事、上司建立信任关系
注重细节：细节决定效率和成败
保持不同观点：希望听见不同的声音和可取的建议，一旦下了决定就会绝不言弃
结果导向：为最终的目标而努力


## Customer Obsession

Leaders start with the customer and work backwards. They work vigorously to earn and keep customer trust. Although leaders pay attention to competitors, they obsess over customers.

## Ownership

Leaders are owners. They think long term and don’t sacrifice long-term value for short-term results. They act on behalf of the entire company, beyond just their own team. They never say “that’s not my job."

## Invent and Simplify

Leaders expect and require innovation and invention from their teams and always find ways to simplify. They are externally aware, look for new ideas from everywhere, and are not limited by “not invented here." As we do new things, we accept that we may be misunderstood for long periods of time.

## Are Right, A Lot

Leaders are right a lot. They have strong judgment and good instincts. They seek diverse perspectives and work to disconfirm their beliefs.

## Learn and Be Curious

Leaders are never done learning and always seek to improve themselves. They are curious about new possibilities and act to explore them.

## Hire and Develop the Best

Leaders raise the performance bar with every hire and promotion. They recognize exceptional talent, and willingly move them throughout the organization. Leaders develop leaders and take seriously their role in coaching others. We work on behalf of our people to invent mechanisms for development like Career Choice.

## Insist on the Highest Standards

Leaders have relentlessly high standards — many people may think these standards are unreasonably high. Leaders are continually raising the bar and drive their teams to deliver high quality products, services, and processes. Leaders ensure that defects do not get sent down the line and that problems are fixed so they stay fixed.

## Think Big

Thinking small is a self-fulfilling prophecy. Leaders create and communicate a bold direction that inspires results. They think differently and look around corners for ways to serve customers.

## Bias for Action

Speed matters in business. Many decisions and actions are reversible and do not need extensive study. We value calculated risk taking.

## Frugality

Accomplish more with less. Constraints breed resourcefulness, self-sufficiency, and invention. There are no extra points for growing headcount, budget size, or fixed expense.

## Earn Trust

Leaders listen attentively, speak candidly, and treat others respectfully. They are vocally self-critical, even when doing so is awkward or embarrassing. Leaders do not believe their or their team’s body odor smells of perfume. They benchmark themselves and their teams against the best.

## Dive Deep

Leaders operate at all levels, stay connected to the details, audit frequently, and are skeptical when metrics and anecdote differ. No task is beneath them.

## Have Backbone; Disagree and Commit

Leaders are obligated to respectfully challenge decisions when they disagree, even when doing so is uncomfortable or exhausting. Leaders have conviction and are tenacious. They do not compromise for the sake of social cohesion. Once a decision is determined, they commit wholly.

## Deliver Results

Leaders focus on the key inputs for their business and deliver them with the right quality and in a timely fashion. Despite setbacks, they rise to the occasion and never settle.

## Strive to be Earth's Best Employer

Leaders work every day to create a safer, more productive, higher performing, more diverse, and more just work environment. They lead with empathy, have fun at work, and make it easy for others to have fun. Leaders ask themselves: Are my fellow employees growing? Are they empowered? Are they ready for what's next? Leaders have a vision for and commitment to their employees' personal success, whether that be at Amazon or elsewhere.

## Success and Scale Bring Broad Responsibility

We started in a garage, but we're not there anymore. We are big, we impact the world, and we are far from perfect. We must be humble and thoughtful about even the secondary effects of our actions. Our local communities, planet, and future generations need us to be better every day. We must begin each day with a determination to make better, do better, and be better for our customers, our employees, our partners, and the world at large. And we must end every day knowing we can do even more tomorrow. Leaders create more than they consume and always leave things better than how they found them.

# Data Structure

## haspmap 实现原理


put函数大致的思路为：

1. 对key的hashCode()做hash，然后再计算index;
2. 如果没碰撞直接放到bucket里；
3. 如果碰撞了，以链表的形式存在buckets后；
4. 如果碰撞导致链表过长(大于等于TREEIFY_THRESHOLD)，就把链表转换成红黑树；
5. 如果节点已经存在就替换old value(保证key的唯一性)
6. 如果bucket满了(超过load factor*current capacity)，就要resize。


在理解了put之后，get就很简单了。大致思路如下：

1. bucket里的第一个节点，直接命中；
2. 如果有冲突，则通过key.equals(k)去查找对应的entry
   若为树，则在树中通过key.equals(k)查找，O(logn)；
   若为链表，则在链表中通过key.equals(k)查找，O(n)。


**Array（数组）是基于索引(index)的数据结构，它使用索引在数组中搜索和读取数据是很快的**

**LinkList是一个双链表,在添加和删除元素时具有比ArrayList更好的性能.但在get与set方面弱于ArrayList.当然,这些对比都是指数据量很大或者操作很频繁**


**LinkList是一个双链表，线程不安全**

**基于hash 表的Map 结构，线性表的速度最快**



hashmap 是由hash 表生成的 key-value 集合。

TreeMap 是由红黑树实现的有序的 key-value 集合。

共同点：

Map：在数组中是通过数组下标来对 其内容进行索引的，而Map是通过对象来对 对象进行索引的，用来 索引的对象叫键key，其对应的对象叫值value；

HashMap和TreeMap都不是线程安全的

异同点：

1、HashMap是通过hashcode()对其内容进行快速查找的；HashMap中的元素是没有顺序的；

```
TreeMap中所有的元素都是有某一固定顺序的，如果需要得到一个有序的结果，就应该使用TreeMap
```

2.HashMap：适用于Map插入，删除，定位元素；

TreeMap：适用于按自然顺序或自定义顺序遍历键（key）

3.明确定义了hashcode() 和equals()，保证了键的唯一性，而只是保证了 TreeMap继承SortedMap类；他保持键的有序顺序；
————————————————
版权声明：本文为CSDN博主「thoughtCodes」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/xiamaocheng/article/details/104558505
