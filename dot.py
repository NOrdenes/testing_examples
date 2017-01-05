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

def test_a_lessthan__b():
	a = [1,2]
	b = [1,2,3]

	with pytest.raises(AssertionError):	
	assert dot(a,b) == 3

def test_b_lessthan_a():
	a = [1,2]
	b = [1,2,3]

	with pytest.raises(Assertion Error):
	assert dot(a,b) == 3
