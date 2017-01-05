def dot(a,b):
	res = 0
	for i in range(len(a)):
		res += a[i]*b[i]
	return res

def test_dot_zeros():
	a = [0,0]
	b = [0,0]
	assert dot(a,b) == 0

def test_dot_perp():
	a = [0,1]
	b = [1,0]
	assert dot(a,b) == 0

def test_diff_len():
	a = [1,2,3]
	b = [1,1]
	assert dot(a,b) == 3
