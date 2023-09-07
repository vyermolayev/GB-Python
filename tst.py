def same_by(characteristics, objects):
    filtered = filter(characteristics, objects)
    filteredList = 	list(filtered)		   
    if len(filteredList) == len(objects) or len(filteredList)==0:
    	return True
    return False

values = [0, 2, 10, 6]


if same_by(lambda x: x % 2, values):
	print("same")
else:
	print("different")