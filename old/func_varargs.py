def total(a=5,*nums,**phone):
    print('a',a)    

    for n in nums:
        print("item",n)

    for k,v in phone.items():
        print(k,v)


total(5,1,2,3,A=1,B=2,C=3)
