def insert_dict(key, value, dict):
    dict[key] = value
    
    # Your code here
    
    

# deleting from dictionary
def del_dict(key, dict):
    dict.pop(key)
    # Your code here
    
    
    
    

# print marks of required name
def print_dict(key, dict):
    for key, value in dict.items():
        print(key, value)
    
    
def main():
    # testcase input
    testcase = int(input())
    
    # looping through testcases
    while(testcase > 0):
        
        n = int(input())
        
        i = 0
        dict = {}
        while i < n:
            flag = False
            delete = False
            query = input().split()
            if(query[0] == 'i'):
                insert_dict(query[1], query[2], dict)
                print ("Inserted")
            
            if(query[0] == 'd'):
                if del_dict(query[1], dict) is False:
                    print ("-1")
                else:
                    print ("Deleted")
            
            if(query[0] == 'p'):
                if(print_dict(query[1], dict) is False):
                    print ("-1")
                    
            i+=1
            
        testcase -= 1


if __name__ == '__main__':
    main()