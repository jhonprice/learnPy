try:
    text = input("enter -->")
except EOFError:
    print('EOF?')
except KeyboardInterrupt:
    print('cancelled operation')
else:
    print('Right{}'.format(text))
 
