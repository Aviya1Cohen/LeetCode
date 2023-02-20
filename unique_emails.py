""" Given a list of emails address, return the num of unique emails.
- localname@domainname
- localname: ignore "." and "+". everything after "+" will be ignored.

pseudocode:
1. empty set to hold result.
2. for loop: -split email by "@" 
             -empty string for localn
             -loop over the chars in split[0]: if char is not . and not +, add it to string. elif is                 +:break the loop.
             -new varaible mail: localn+@+domain, add it to the result
3. return the length of the result set
"""

def num_unique_emails(emails):
    
    res = set()
    
    for email in emails:
        split_email = email.split("@") #list
        localn = ""
        for char in  split_email[0]:
            if char != "." and char != "+":
                localn += char
            elif char == "+":
                break
        mail = localn +"@" + split_email[1]   
        res.add(mail)
        
    return len(set(res))
        
test1 = ["test.email+alex@leetcode.com", "test.e.mail+bob.cathy@leetcode.com", "testemail+david@lee.tcode.com"]
print(num_unique_emails(test1))   
