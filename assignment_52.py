    largest = None
    smallest = None

while True:
    try:
      num = raw_input("Enter a number: ")
      if num == "done" and largest == None and smallest == None: 
        print "Invalid input"
        continue
      elif num == "done":
            break
      num = int(num)     
    except:
      print "Invalid input"
      num = None
      continue
    
    if smallest is None:
        smallest = num
    if largest is None:
        largest = num 
        
    if num < smallest:
        smallest = num
    if num > largest:
        largest = num
    
print "Maximum is", largest
print "Minimun is", smallest
