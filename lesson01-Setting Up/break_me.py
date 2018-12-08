def cause_NameError():
	doit = 'yay!'
	return done

def cause_TypeError():
	x = 1
	y = 'string'
	return x + y


#def cause_SyntaxError(x):
#	print "Wrong Way to Print"


def cause_AttributeError():
	x = 'string'
	x.is_integer()
	
#cause_NameError()
#cause_TypeError()
cause_AttributeError()