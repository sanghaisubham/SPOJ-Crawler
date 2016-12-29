import requests
from bs4 import BeautifulSoup #HTML is parsed by Beautiful Soup module

def SPOJ(url,probname,username):
    newurl=url+'/'+'problems/'+probname+'/'
    qstninfo(newurl)
    source_code=requests.get(newurl) #Download the Page
    plain_text=source_code.text      #Bcz Webpages are plain text formatted as HTML
    soup=BeautifulSoup(plain_text,"lxml")  #Response Object
    for link in soup.findAll('a',{'class':''}): #Find's All the elements in The HTML with this type of Class Defination
             if link.string=='Ranking':#By this,we will get the link corresponding to the Ranking String in the HTML
                                        # (or the link for which the strig is defined to be Ranking)
                href=url+link.get('href')
                geteverything(href)    #Redirect to the Rncking page
    href1=url+'/status/'+probname+','+username+'/'
    getstatus(href1)
   
    
def getstatus(statusurl):
    print('\n\n\n')
    print('------------------------------------------------------------')
    print('              Your Status For The Problem Is:  ')
    print('------------------------------------------------------------')
   
    source_code=requests.get(statusurl)
    plain_text=source_code.text
    soup=BeautifulSoup(plain_text,"lxml")
    mystatus=[]
    flag=0
    for link in soup.findAll('td',{'class':'statusres text-center'}):
         if (link.get('status')) == "15": #Status 15 stands for AC code
            flag=1
            print('\nYour Solution is Accepted')
            for link1 in soup.findAll('a',{'title':'See the best solutions'}):
                if link1.string is not None:
                    print('\nThe Time Limit of Accepted Solution is:'+str(link1.string.strip()))
                    break
            for link2 in soup.findAll('td',{'class':'smemory statustext text-center'}):
                if link2.string is not None:
                    print('\nThe Memory Limit of Accepted Solution is:'+str(link2.string.strip()))
                    break 
            break
                
         if link.string is not None:
                mystatus.append(link.string.strip())
    if flag==0:
        print('\nYour Solution is Not Accepted')
        print('\nThe Solution Status are: ')
        
        for i in mystatus:
            print(i)
            
def qstninfo(url):
    print('\n\n\n')
    print('------------------------------------------------------------')
    print("              The Problem Information's Are  :  ")
    print('------------------------------------------------------------\n')
  
    count=1
    source_code=requests.get(url)
    plain_text=source_code.text
    soup=BeautifulSoup(plain_text,"lxml")
    probinfo=[]
    for link in soup.findAll('td',{'class':''}): #Refers To the td(table data)
        if link.string is not None:
            probinfo.append(link.string.strip())
            count=count+1
            if count==12:
                break
    #print probinfo[0]
    sz=len(probinfo)
    #for i in range(0,sz,1):
    #    print probinfo[i]
    for i in range(1,sz,2):
       print probinfo[i]+" "+probinfo[i+1]+"\n";
    
    
def geteverything(newurl):
    print('\n\n\n')
    print('------------------------------------------------------------')
    print("         The Problem Ranking and Status  Is  :  ")
    print('------------------------------------------------------------')
   
    source_code=requests.get(newurl)
    plain_text=source_code.text
    soup=BeautifulSoup(plain_text,"lxml")
    text1=[]
    count=1
    for link in soup.findAll('td',{'class':'text-center'}):
        if link.string is not None:
            text1.append(link.string.strip())
            count=count+1
        if count==12:
            break
    print('\nCount of Users accepted is: '+text1[0])
    print('\nCount of Submissions is: '+text1[1])
    print('\nCount of Accepted Solution is: '+text1[2])
    print('\nCount of Wrong Answer is: '+text1[3])
    print('\nCount of Compilation Error is: '+text1[4])
    print('\nCount of RunTimeError is: '+text1[5])
    print('\nCount of Time Limit Exceeded is: '+text1[6])
    print('\nName of the Coder with the Best Solution : '+text1[8])
    print('\nTime Limit of Best Solution: '+text1[9])
    print('\nMemory Limit of Best Solution: '+text1[10])
    

print('Enter The Link of the Online Judge')
link=raw_input()
print('Enter Problem name')
pname=raw_input()
print('Enter User name')
uname=raw_input()

SPOJ('http://www.spoj.com',pname,uname)