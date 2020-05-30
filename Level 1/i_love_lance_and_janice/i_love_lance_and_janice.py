def solution(x):
	y = ""
	for c in x:
	    if(c.islower()):
	        y+=chr(26 - ord(c) + 2*ord("a")-1)
	    else:
	        y+=c	

print(solution("wrw blf hvv ozhg mrtsg'h vkrhlwv?"))
