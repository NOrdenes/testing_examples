from mydot import dot

import pytest

#@ = decoration symbol. transforms the inmediately next function.
@pytest.mark.parametrize("a,b,expected",[
	([0,0],[0,0],0),
	([1,0],[0,1],0),
	([1,2],[2,-1],0),
])
def test_asser_equal(a,b,expected):
	assert dot(a,b) == expected

@pytest.mark.parametrize("a,b",[
	([1,2],[1,2,3]),
	([1,2,3],[42,7]),
])
def test_a_lessthan_b(a,b):
	a = [1,2]
	b = [1,2,3]

	with pytest.raises(AssertionError):
		dot(a,b)
