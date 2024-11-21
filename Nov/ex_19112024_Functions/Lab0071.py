def pizza(*toppings):
    # args-> list
    print(toppings)
    for i in toppings:
        print(i)


pizza(1,2,3,4,5,6)
pizza("arun",1,"ajay",2)