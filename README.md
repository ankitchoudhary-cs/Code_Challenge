<html>
<pre>
<h1>Philaland Coin</h1>
<p>
The problem solvers have found a new Island for coding and named it as Philaland.These smart people were given a task to make purchase of items at the Island easier by distributingvarious coins with different value.Manish has come up with a solution that if we make coins category starting from $1 till the maximum price of item present on Island, then we can purchase any item easily. He added
following example to prove his point.
Lets suppose the maximum price of an item is 5$ then we can make coins of {$1, $2, $3, $4, $5}
to purchase any item ranging from $1 till $5.
Now Manisha, being a keen observer suggested that we could actually minimize the number of coins required and gave following distribution {$1, $2, $3}. According to him any item can be purchased one time ranging from $1 to $5. Everyone was impressed with both of them.


</p><p>
Your task is to help Manisha come up with minimum number of denominations for any arbitrary max price in Philaland.
</p><p>
<h3>Constraints</h3>
1<=T<=100
1<=N<=5000
</p><p>
<h3>Input Format</h3>
First line contains an integer T denoting the number of test cases.
Next T lines contains an integer N denoting the maximum price of the item present on Philaland.
</p><p>
<h3>Output</h3>
For each test case print a single line denoting the minimum number of denominations of coins required.
</p><p>
<h3>Test Case</h3>
<h4>Input<h4>
2
10
5
</p><p>
  <h4>Output</h4>
4
3
</p><p>
<h3>Explanation</h3>
</p><p>
For test case 1, N=10.
According to Manish {$1, $2, $3,… $10} must be distributed.
But as per Manisha only {$1, $2, $3, $4} coins are enough to purchase any item ranging from $1 to $10. Hence minimum is 4. Likewise denominations could also be {$1, $2, $3, $5}. Hence answer is still 4.
</p><p>
For test case 2, N=5.
According to Manish {$1, $2, $3, $4, $5} must be distributed.
But as per Manisha only {$1, $2, $3} coins are enough to purchase any item ranging from $1 to $5. Hence minimum is 3. Likewise denominations could also be {$1, $2, $4}. Hence answer is still 3.
</p>
<hr>

<h1>Prime Fibonacci</h1>
<h3>Problem Description</h3>
<pre>
  Given two numbers n1 and n2 1. Find prime numbers between n1 and n2, then 2. Make all possible unique combinations of numbers from the prime numbers list you found in step 
1. 3. From this new list, again find all prime numbers. 
4. Find smallest (a) and largest (b) number from the 2nd generated list, also count of this list. 
5. Consider smallest and largest number as the 1st and 2nd number to generate Fibonacci series respectively till the count (number of primes in the 2nd list). 
6. Print the last number of a Fibonacci series as an output Constraints 2 <= n1, n2 <= 100 n2 - n1 >= 35 
</pre>
<h3>Input</h3>
<p>
  Format One line containing two space separated integers n1 and n2. 
  </p>
  <h3>Output</h3>
  <p>
  Last number of a generated Fibonacci series. 
  </p>
  <h3>Test Case</h3>
  <h4>Example 1 </h4>
  <h5>Input</h5>
  <p>
  2 40 
  </p>
 <h5> Output </h5>
<p>13158006689 </p>
<h5>Explanation </h5>
<pre>
1st prime list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37] 
Combination of all the primes = [23, 25, 27, 211, 213, 217, 219, 223, 229, 231, 32, 35, 37, 311, 313, 319, 323, 329, 331, 337, 52, 53, 57, 511, 513, 517, 519, 523, 529, 531, 537, 72, 73, 75, 711, 713, 717, 719, 723, 729, 731, 737, 112, 113, 115, 117, 1113, 1117, 1119, 1123, 1129, 1131, 1137, 132, 133, 135, 137, 1311, 1317, 1319, 1323, 1329, 1331, 1337, 172, 173, 175, 177, 1711, 1713, 1719, 1723, 1729, 1731, 1737, 192, 193, 195, 197, 1911, 1913, 1917, 1923, 1929, 1931, 1937, 232, 233, 235, 237, 2311, 2313, 2317, 2319, 2329, 2331, 2337, 292, 293, 295, 297, 2911, 2913, 2917, 2919, 2923, 2931, 2937, 312, 315, 317, 3111, 3113, 3117, 3119, 3123, 3129, 3137, 372, 373, 375, 377, 3711, 3713, 3717, 3719, 3723, 3729, 3731] 
2nd prime list=[193, 3137, 197, 2311, 3719, 73, 137, 331, 523, 1931, 719, 337, 211, 23, 1117, 223, 1123, 229, 37, 293, 2917, 1319, 1129, 233, 173, 3119, 113, 53, 373, 311, 313, 1913, 1723, 317] 
smallest (a) = 23 
largest (b) = 3719 
Therefore, the last number of a Fibonacci series i.e. 34th Fibonacci number in the series that has 23 and 3719 as the first 2 numbers is 13158006689
</pre>
<h4>Example 2 </h4>
<h5>Input</h5> 
<p>30 70 </p>
<h5>Output </h5>
<p>2027041 </p>
<h5>Explanation</h5>
<pre>
1st prime list = [31, 37, 41, 43, 47, 53, 59, 61, 67] 
2nd prime list generated form combination of 1st prime list = [3137, 5953, 5347, 6761, 3761, 4337, 6737, 6131, 3767, 4759, 4153, 3167, 4159, 6143] 
smallest prime in 2nd list=3137 largest prime in 2nd list=6761 
Therefore, the last number of a Fibonacci series i.e. 14th Fibonacci number in the series that has 3137 and 6761 as the first 2 numbers is 2027041
</pre>
<hr>
<h1>Collision Course</h1>
 <h3>Problem Description</h3>
 <p>
  On a busy road, multiple cars are passing by. A simulation is run to see what happens if brakes fail for all cars on the road. The only way for them to be safe is if they don't collide and pass by each other. The goal is to identify whether any of the given cars would collide or pass by each other safely around a Roundabout. Think of this as a reference point O ( Origin with coordinates (0,0) ), but instead of going around it, cars pass through it.
  </p>
  <p>
Considering that each car is moving in a straight line towards the origin with individual uniform speed. Cars will continue to travel in that same straight line even after crossing origin. Calculate the number of collisions that will happen in such a scenario.
</p><p>
Note : - Calculate collisions only at origin. Ignore the other collisions. Assume that each car continues on its respective path even after the collision without change of direction or speed for an infinite distance.
</p>
<h3>Constraints</h3>
<pre>
1<=C<=10^5
-10^9 <= x,y <= 10^9
0 < v < 10^9.
</pre>
<h3>Input Format</h3>
<pre>
The first line contains an integer C, denoting the number of cars being considered that are passing by around the origin.
Next C lines contain 3 space delimited values, first two of them being for position coordinates (x,y) in 2D space and the third one for speed (v).
Output
A single integer Q denoting the number of collisions at origin possible for given set of cars.
</pre>
<h2>Test Case</h2>
<h2>Example 1</h2>
<h3>Input</h3>
<pre>
5
5 12 1
16 63 5
-10 24 2
7 24 2
-24 7 2
</pre>
<h3>Output</h3>
<p>
4</p>
<h3>Explanation</h3>
<pre>
Let the 5 cars be A, B, C, D, and E respectively.
4 Collisions are as follows -
1) A & B.
2) A & C.
3) B & C.
4) D & E.
</pre>
</pre>
<hr>
<pre>
<h1>Swayamvar</h1><pre>
<h3>Problem Description</h3>
A ceremony where a Bride chooses her Groom from an array of eligible bachelors is called Swayamvar. But this is a Swayamvar with difference. An array of Bride-to-be will choose from an array of Groom-to-be.
The arrangement at this Swayamvar is as follows
· Brides-to-be are organized such that the most eligible bachelorette will get first chance to choose her Groom. Only then, the next most eligible bachelorette will get a chance to choose her Groom
· If the initial most eligible bachelorette does not get a Groom of her choice, none of the Brides-to-be have any chance at all to get married. So unless a senior bachelorette is out of the “queue”, the junior bachelorette does not get a chance to select her Groom-to-be
· Inital state of Grooms-to-be is such that most eligible bachelor is at the head of the “queue”. The next most eligible bachelor is next in the queue. So on and so forth.
· Now everything hinges on the choice of the bachelorette. The most eligible bachelorette will now meet the most eligible bachelor.
· If bachelorette selects the bachelor, both, the bachelorette and the bachelor are now Bride and Groom respectively and will no longer be a part of the Swayamvar activity. Now, the next most eligible bachelorette will get a chance to choose her Groom. Her first option is the next most eligible bachelor (relative to initial state)
· If the most eligible bachelorette passes the most eligible bachelor, the most eligible bachelor now moves to the end of the queue. The next most eligible bachelor is now considered by the most eligible bachelorette. Selection or Passing over will have the same consequences as explained earlier.
· If most eligible bachelorette reaches the end of bachelor queue, then the Swayamvar is over. Nobody can get married.
· Given a mix of Selection or Passing over, different pairs will get formed.
The selection criteria is as follows
1. Each person either drinks rum or mojito. Bride will choose groom only if he drinks the same drink as her.
Note : There are equal number of brides and grooms for the swayamvar.
Tyrion as the hand of the king wants to know how many pairs will be left unmatched. Can you help Tyrion?
<h3>Constraints</h3>
1<= N <= 10^4
<h3>Input Format</h3>
First line contains one integer N, which denotes the number of brides and grooms taking part in the swayamvar. Second line contains a string in lowercase, of length N containing initial state of brides-to-be. Third line contains a string in lowercase, of length N containing initial state of grooms-to-be. Each string contains only lowercase 'r' and 'm' stating person at that index drinks "rum"(for 'r') or mojito(for 'm').
<h3>Output</h3>
Output a single integer denoting the number of pairs left unmatched.
<h3>Timeout</h3>
1
<h3>Explanation</h3>
<h3>Example 1</h3>
<h3>Input</h3>
4
rrmm mrmr
<h3>Output</h3>
0
<h3>Explanation</h3>
The bride at first place will only marry groom who drinks rum. So the groom at first place will join the end of the queue. Updated groom's queue is "rmrm".
Now the bride at first place will marry the groom at first place. Updated bride's queue is "rmm" and groom's queue is "mrm".
The process continues and at last there are no pairs left. So answer is 0.
<h3>Example 2</h3>
<h3>Input</h3>
4 rmrm mmmr
<h3>Output</h3>
2
<h3>Explanation</h3>
Following the above process 2 pairs will be left unmatched. Remember that bride will not move until she gets a groom of her choice.</pre>
</pre>
<hr>
<pre>
<h1>Digit Pairs</h1>
<pre>
<h3>Problem Description</h3>
Given N three-digit numbers, your task is to find bit score of all N numbers and then print the number of pairs possible based on these calculated bit score.
1. Rule for calculating bit score from three digit number:
From the 3-digit number,
· extract largest digit and multiply by 11 then
· extract smallest digit multiply by 7 then
· add both the result for getting bit pairs.
Note: - Bit score should be of 2-digits, if above results in a 3-digit bit score, simply ignore most significant digit.
Consider following examples:
Say, number is 286
Largest digit is 8 and smallest digit is 2
So, 8*11+2*7 =102 so ignore most significant bit , So bit score = 02.
Say, Number is 123
Largest digit is 3 and smallest digit is 1
So, 3*11+7*1=40, so bit score is 40.
2. Rules for making pairs from above calculated bit scores
Condition for making pairs are
· Both bit scores should be in either odd position or even position to be eligible to form a pair.
· Pairs can be only made if most significant digit are same and at most two pair can be made for a given significant digit.
<h3>Constraints</h3>
N<=500
<h3>Input Format</h3>
First line contains an integer N, denoting the count of numbers.
Second line contains N 3-digit integers delimited by space
<h3>Output</h3>
One integer value denoting the number of bit pairs.
<h3>Timeout</h3>
1
<h3>Explanation</h3>
<h3>Example 1</h3>
Input
8 234 567 321 345 123 110 767 111
<h3>Output</h3>
3
<h3>Explanation</h3>
After getting the most and least significant digits of the numbers and applying the formula given in Rule 1 we get the bit scores of the numbers as:
58 12 40 76 40 11 19 18
No. of pair possible are 3:
40 appears twice at odd-indices 3 and 5 respectively. Hence, this is one pair.
12, 11, 18 are at even-indices. Hence, two pairs are possible from these three-bit scores.
Hence total pairs possible is 3
</pre>
</pre>
<hr>
<pre>
<h1>Dole Out Cadbury</h1>
<h3>Problem Description</h3>
You are a teacher in reputed school. During Celebration Day you were assigned a task to distribute Cadbury such that maximum children get the chocolate. You have a box full of Cadbury with different width and height. You can only distribute largest square shape Cadbury. So if you have a Cadbury of length 10 and width 5, then you need to break Cadbury in 5X5 square and distribute to first child and then remaining 5X5 to next in queue
<h3>Constraints</h3>
0<P<Q<1501
<pre>0<R<S<1501 </pre>

<h3>Input Format</h3>
First line contains an integer P that denotes minimum length of Cadbury in the box
Second line contains an integer Q that denotes maximum length of Cadbury in the box
Third line contains an integer R that denotes minimum width of Cadbury in the box
Fourth line contains an integer S that denotes maximum width of Cadbury in the box
Output
Print total number of children who will get chocolate.
<h3>Timeout</h3>
1
<h3>Explanation</h3>
<h3>Example 1</h3>
<h3>Input</h3>
5
7
3
4
<h3>Output</h3>
24
<h3>Explanation</h3>

Length is in between 5 to 7 and width is in between 3 to 4.
So we have 5X3,5X4,6X3,6X4,7X3,7X4 type of Cadbury in the box.
If we take 5X3 :
First, we can give 3X3 square Cadbury to 1st child .Then we are left with 3X2. Now largest square is 2X2 which will be given to next child. Next, we are left with two  1X1 part of Cadbury which will be given to another two children.
And so on
</pre>
</body>
</html>
