# IMC 录视频 VO

## Version 1
1. describe your favorite project and your contribution and why you like this project? (15s 准备，1分钟答题）
   1. 1. My best work achievement was my last job at Inovonics. The main content of this work is to develop a daily-worn sensor for the elderly that reports abnormal data by monitoring daily activitie
   2. The reason it is my best work achievementis that when my group and I started this work, we only had a handbook with data requirements and how to monitor abnormal data, without a single line of code. Therefore, we have to start from scratch with data creation, software development, abnormal activity monitoring, testing.
   3. Of course, there were many, many problems. For example, in a task plan meeting, I was assigned to work on website development, but I had no experience with website development before. This caused me to miss software development deadlines. However, our team members helped me in time, and with their help, I successfully completed my part of the work.
   4. Through this experience, I learned not to try to solve the problem alone when encountering difficulties, but to communicate more with others and try to get a solution to the problem.
   5. In the end, our group successfully completed the project half a month before the deadline, and won great feedback from our mentor.
   
2. describe a experience which you receive the feedback from others, and how you improve it? (15s准备，1分半答题）
   1. tell me an experience when you received negative feedback
   2. S/T:
      1. When I took User center design class last fall semester, the professor give us an assignment to design the user interface of a mobile phone application. (we don't need to implement this user interface, we just need to draw the user interface and use figma after a few milestones Complete simple prototyping)
      2. My idea is to make a daily calorie calculator, the user can calculate the user's calorie intake for the day by entering what he eats each day.
      3. Since I have no previous experience in designing a user interface for mobile software, I misestimated the complexity of this task and did not think about many details of software design. I only drew 4 user interface diagrams and handed in the assignment.
      4. A few days later, I received feedback from the professor that the design I made was too simple, and misses many details, such as the cooking method of the food, were not clearly written.
   3. A
      1. I realized this problem. Then I scheduled 2 individual meetings with the professor to ask the professor about how to improve my design and record the solutions. Also, I started to download and check out some of the calorie-counting apps already available in the Apple Store. I got some inspiration to perfect my prototyping by watching how their mobile apps design the user interface.
      2. ex: For example, to solve the problem of different calorie caused by different ingredients due to different cooking methods, we allow users to add cooking methods of food after the user selects the ingredients or design some popular food cooking methods (for example, the cooking method of potatoes may have fries or mashed potatoes)
   4. R
      1. I learned the importance of project evaluation and timely communication. In the end I got a good grade on this assignment and got an A in the grade for this class
   
3. immutable data models are always thread safe?（15s 准备，30s答题）
   1. immutable objects are always thread-safe, but its references may not be.
   2. Thread-safe simply means that two or more threads must work in coordination on the shared resource or object. They shouldn't over-ride the changes done by any other thread.
   3. To make their references thread-safe, we may need to access them from synchronized blocks/methods.


   
4. quick sort is always the most efficient/fastest sorting algorithm？（15s 准备，30s答题）
   
5. hashmap/hashtable is always more efficient (faster) than linear search?（15s 准备，30s答题）
   1. Searching in a hash table is not always constant-time in reality. If the hash function is a poor match for the data, you can have a lot of collisions, and in the extreme case that every data item has the same hash value, the result looks much like linear search. 
   
6.  Is it better to run one thread on one task or multithread on one task?（15s 准备，30s答题）
   2. Multiple threads might allow you to do things in parallel, if your CPU has more than one core available, so it is faster.
   3. If you start more threads as cores are available, the thread management of your OS will spend more and more time in Thread-Switches and in such your effiency using your CPU(s) becomes worse.


7.  time complexity：is O(n^2) always slower than O(n)?（15s 准备，30s答题）
   4. big O是worst case
   5. n is the dataset
   
8.  how did you find out this job opportunity and why are you interested in applying

## Version 2
1. Describe a situation where you need to adapt your personal style to work with other people/teams.
2. receive critical feedback。如何改进的(Same with Version 1)
3. What do you look for in a workplace?
4-9：
5. Is the total number of distinct unsigned 32-bit integers different from the total number of signed 32-bit integers?
   1. In 32-bit integers, an unsigned integer has a range of 0 to 2^32-1 
   2. The signed version goes from -2^31-1 to 2^31
   3. The range is the same, but it is shifted on the number line. 
   4. an unsigned int cannot represent a negative number.


一样的
6. Is a task on 2 threads always faster than a task running on one thread?
7. How would you explain HashMap to a non-technical person? ( More than one minute was g‍‍‌‌‌‍‌‍‍‌‍‌‌‍‍‍‌‍‍‌iven to prepare and 2 minutes to answer for this one)
   1. hashmap has a bunch of numbered “buckets” where it puts stuff. It probably has more buckets than it will contain items.

8. Do same hash keys have same hashcodes
   可能会有，hash collision
9.  Can all recursive functions be implemented iteratively?
    1.  The essence of recursion is to push the stack, and the stack operation is added to the loop.
    2.  

## Version 3
1. What are the important qualities in the work environment for you?
2. Describe a situation where you need to adapt your personal style to work with other people/teams. What is the challenge?
3. Tell me a critical feedback you received and how you are improving over time (the steps you took, etc.).
4. Any recursive implemented algorithm can be altered to an iterative implemented algorithm.
   
5. Running a task on 1 thread can be faster than running it on 2 threads.
   如果切换耗时特别大时，可能1个线程比2个线程快，比如在IO上操作相关的，
6. An algorithm implemented with O‍‍‌‌‌‍‌‍‍‌‍‌‌‍‍‍‌‍‍‌(1) time can not be improved faster.
   可以，比如有100，可以通过优化，减少遍历次数，但仍然是O1
7. A signed 32 bits integer and an unsigned 32 bits integer can express the same number of distinct integers.
8. In HashMap, two different keys will always have different hashcodes.
9.  Describe the difference between stack and queue to a non-technology person, including one or more real-world examples.
    1.  Stack: Stack of pancakes
    2.  Queue: like to purchase coffee



