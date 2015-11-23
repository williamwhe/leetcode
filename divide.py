def divide(numerator, denominator):
	if numerator%denominator==0:
		return str(numerator/denominator)
	ipart=numerator/denominator
	fpart=numerator%denominator*10
	m={}
	idx=0
	retstr=str(ipart+".")
	remind=""
	while True:
		if fpart%denominator==0:
			remind+=str(fpart/denominator)
			break
		if fpart in s:
			remind+=str(fpart/denominator)
			break
		m[fpart]=idx
		idx+=1
		remind+=str(fpart/denominator)
		fpart=fpart%denominator*10
	return retstr+remind

print divide(1,2)
print divide(2,1)
print divide(2,3)