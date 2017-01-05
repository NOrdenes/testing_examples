def dot(a,b):
	res = 0
	for i in range(len(a)):
		res += a[i]*b[i]
	return res

def test_dot_zeros():
	a = [0,0]
	b = [0,0]
	assert dot(a,b) == 0
