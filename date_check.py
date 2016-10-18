import datetime
def answer(x,y,z):
    correctDate = None
    count = 0
    try:
        newDate = datetime.datetime(x,y,z)
        count = count + 1
    except ValueError:
        count = count
    try:
        newDate = datetime.datetime(x,z,y)
        count = count + 1
    except ValueError:
        count = count
    try:
        newDate = datetime.datetime(z,x,y)
        count = count + 1
    except ValueError:
        count = count
    try:
        newDate = datetime.datetime(z,y,x)
        count = count + 1
    except ValueError:
        count = count
    try:
        newDate = datetime.datetime(y,z,x)
        count = count + 1
    except ValueError:
        count = count
    try:
        newDate = datetime.datetime(y,x,z)
        count = count + 1
    except ValueError:
        count = count
    if count > 1:
        print("Ambiguous")
    else:
        print(str(newDate.strftime('%m/%d/%Y')))
  
