def meanderingArray(unsortedArray):
# //Sort the array - this is crucial for getting largest,smallest vals
  ascendingArr = sorted(unsortedArray)

  meandered = []
#   //While loop for only one element or no elements left
  while len(ascendingArr) > 1:
    meandered += [ascendingArr[-1], ascending[0]] 
    # //Add the first smallest and first largest values
    ascendingArr = ascendingArr[1:-1] 
    # //Remove the smallest,largest vals from the list and update
  
  meandered += ascendingArr 
#   // Add remaining possible element, or nothing perhaps, to the list
  
  return meandered