# SPOJ-Crawler
This Software crawls through the Spoj Website to extract various Important Data of a particular Question provided in the Input like:
1)The Problem Description including:
     a)Author
     b)Time Limit
     c)Date
     d)Memory Limit
     
2)Ranking and Status of Code including:
   a)Count of Accepted Solution
   b)Count of Submissions
   c)Count of WA
   d)Count of TLE
   e)Count of CE
   f)Count of RTE
   g)Best Solution Details
   
 3)Status of the User 
    a)If Accepted, then the details of the Accepted Solution
    b)If Not Accepted then the Penalties in a definite order
    
Input: The User Needs to Input Three Things including:
        i)The Link of Spoj Website
        ii)The Name of Problem(Only the Problem Code)
        iii)User Name
        
Output: All the 3 Things Mentioned above with all the descriptions mentioned in detailed and Organised Manner


Tech Used:Python 2.7 + BeautifulSoup Module
  
 Note: SO that the software works properly the user should first ensure that he in logged into his SPOJ account 
