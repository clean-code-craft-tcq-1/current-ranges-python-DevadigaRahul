
def getpreviousitem(mylist,myitem):#Given a list and an item, return previous item in list
    for position, item in enumerate(mylist):
        if item == myitem:
            # First item has no previous item
            if position == 0:
                return None
            # Return previous item    
            return mylist[position-1]

def get_ranges_list(input_list):#Given a sorted list of numbers, return a list of ranges
    new_list=list(set(input_list))
    rangelist = []
    inrange = False
    for item in new_list:
        previousitem = getpreviousitem(new_list,item)
        if previousitem == item - 1:
            # We're in a range
            if inrange == True:
                # It's an existing range - change the end to the current item
                newrange[1] = item
            else:    
                # We've found a new range.
                newrange = [item-1, item]
            # Update to show we are now in a range
            inrange = True    
        else:   
            # We were in a range but now it just ended
            if inrange == True:
                # Save the old range
                rangelist.append(newrange)
            # Update to show we're no longer in a range
            inrange = False 
    # Add the final range found to our list
    if inrange == True:
        rangelist.append(newrange)
    return rangelist

def range_list_to_range_dict_list(range_list):
    range_disct_list=[]
    for each_range in range_list:
        new_dict= {'lowerLimit':min(each_range), 'upperLimit': max(each_range), 'Count':0}
        range_disct_list.append(new_dict)
    return range_disct_list

def with_in_range(value, lowerLimit, upperLimit):
  return ((value >= lowerLimit) and (value <= upperLimit))

def ranges_with_most_often_occurences(readings):
  if(readings!=None):
    range_list=get_ranges_list(readings)
    range_dict_list=range_list_to_range_dict_list(range_list)
    for each_reading in readings:
      for each_range_dict in range_dict_list:
        if with_in_range(each_reading, each_range_dict['lowerLimit'], each_range_dict['upperLimit']):
          each_range_dict['Count']=each_range_dict['Count']+1
    return range_dict_list
  return None
  
def display_ranges_with_most_often_occurences(list_result):
  if(len(list_result)!=0):
    print ("Range, Readings")
    for result in list_result:
      print(result['lowerLimit'],"-",result['upperLimit'],",",result['Count'])

def charging_current_log(readings):
  range_dict_list =  ranges_with_most_often_occurences(readings)
  if(range_dict_list!=None):
    display_ranges_with_most_often_occurences(range_dict_list)


