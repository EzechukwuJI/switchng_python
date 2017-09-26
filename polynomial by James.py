def evaluate_poly(poly, x):
    """
    Computes the polynomial function for a given value x. Returns that value.
    Example:
    >>> poly = (0.0, 0.0, 5.0, 9.3, 7.0)    # f(x) = 7x^4 + 9.3x^3 + 5x^2
    >>> x = -13
    >>> print evaluate_poly(poly, x)  # f(-13) = 7(-13)^4 + 9.3(-13)^3 + 5(-13)^2
    180339.9
    poly: tuple of numbers, length > 0
    x: number
    returns: float
    """
# first obtain the contents of the list supplied
# using the length of the list obtain the index of each element in the list
    equ_val = 0
    for index in range(len(poly)):
        # equ_val += (poly[index] * (x**index))
        element = poly[index]
        equation = element *(x**index)
        equ_val+= equation
    return float(equ_val)
    
# print evaluate_poly((4,5,2,8,),4)

def compute_deriv(poly): 
    ''' Computes the derivative of the polynomial supplied '''
    derivative = ()        
    for index in range(len(poly)):
        if index > 0:
            element = poly[index]
            derivative +=  (float(index*element),)
        elif len(poly)== 1:
            derivative = 0.0,
    return derivative
print compute_deriv((4,5,2,8,))


#compute the root of the polynomial
def compute_root((poly),x_0,epsilon):
    poly = list(poly)
    poly.reverse()
    ''' Compute the root of the equation given
     the coefficients of the equation'''

    num_iter = 1
    guesses = x_0
    polyval_x = evaluate_poly(poly,guesses)
    while abs(polyval_x) > epsilon:
        num_iter += 1
        guesses -= polyval_x /  evaluate_poly(compute_deriv(poly),guesses)
        polyval_x = evaluate_poly(poly,guesses)
    return (guesses,num_iter)

rpoly = (1.0,3.0,17.5,0.0,-13.39)
poly = (-13.39,0.0,17.5,3.0,1.0)



# print compute_root(rpoly,0.1,0.0001)
#compute_root(poly, 0.0, 0.0001)
#print "the value of x: ", guesses, "number of iterations: ", iteration, "and polynomial value: ", polyval_x


















