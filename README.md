<html>

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
</body>
</html>
