import GPM as LP


### Test 3 (нечеткая слабо несогласованная МПС 5x5)
##L = [[1, 1, 4, 3, 2], [1/5, 1, 1/6, 1/7, 3], [1/8, 2, 1, 1/4, 1/7], [1/7, 3, 1, 1, 1], [1/6,1/7,3,1/5,1]]
##U = [[1, 5, 8, 7, 6], [  1, 1, 1/2, 1/3, 7], [1/4, 6, 1,   1, 1/3], [1/3, 7, 4, 1, 5], [1/2,1/3,7,  1,1]]
##print( LP.gpm(L,U) )



# Test 4 (четкая слабо несогласованная МПС_4 5x5)
##D = [[[1,1], [1,1], [2,2], [4,4], [1/2,1/2]], [[1,1], [1,1], [2,2], [4,4], [8,8]], [[1/2,1/2],[1/2,1/2],[1,1],[2,2], [4,4]], [[1/4,1/4],[1/4,1/4],[1/2,1/2],[1,1],[2,2]], [[2,2],[1/8,1/8],[1/4,1/4],[1/2,1/2],[1,1]]]
##L = [[1,1,2,4,1/2], [1,1,2,4,8], [1/2,1/2,1,2,4], [1/4,1/4,1/2,1,2], [2,1/8,1/4,1/2,1]]
##U = [[1,1,2,4,1/2], [1,1,2,4,8], [1/2,1/2,1,2,4], [1/4,1/4,1/2,1,2], [2,1/8,1/4,1/2,1]]
##print( LP.gpm(L,U) )



# Test А1_1 (четкая полностью согласованная МПС 5x5)
##D = [[[1,1], [1,1], [2,2], [4,4], [8,8]], [[1,1], [1,1], [2,2], [4,4], [8,8]], [[1/2,1/2],[1/2,1/2],[1,1],[2,2], [4,4]], [[1/4,1/4],[1/4,1/4],[1/2,1/2],[1,1],[2,2]], [[2,2],[1/8,1/8],[1/4,1/4],[1/2,1/2],[1,1]]]
##L = [[1,1,2,4,8], [1,1,2,4,8], [1/2,1/2,1,2,4], [1/4,1/4,1/2,1,2], [1/8,1/8,1/4,1/2,1]]
##U = [[1,1,2,4,8], [1,1,2,4,8], [1/2,1/2,1,2,4], [1/4,1/4,1/2,1,2], [1/8,1/8,1/4,1/2,1]]
##print( LP.gpm(L,U) )



# Test А3_1 (четкая слабо несогласованная МПС_4 5x5)
##D = [[[1,1], [1,1], [2,2], [4,4], [1/2,1/2]], [[1,1], [1,1], [2,2], [4,4], [8,8]], [[1/2,1/2],[1/2,1/2],[1,1],[2,2], [4,4]], [[1/4,1/4],[1/4,1/4],[1/2,1/2],[1,1],[2,2]], [[2,2],[1/8,1/8],[1/4,1/4],[1/2,1/2],[1,1]]]
##L = [[1,1,2,4,1/2], [1,1,2,4,8], [1/2,1/2,1,2,4], [1/4,1/4,1/2,1,2], [2,1/8,1/4,1/2,1]]
##U = [[1,1,2,4,1/2], [1,1,2,4,8], [1/2,1/2,1,2,4], [1/4,1/4,1/2,1,2], [2,1/8,1/4,1/2,1]]
##print( LP.gpm(L,U) )


# Test А3_2 (четкая слабо несогласованная МПС_4 5x5)
##D = [[[1,1], [1,1], [2,2], [4,4], [1/2,1/2]], [[1,1], [1,1], [2,2], [4,4], [8,8]], [[1/2,1/2],[1/2,1/2],[1,1],[2,2], [4,4]], [[1/4,1/4],[1/4,1/4],[1/2,1/2],[1,1],[2,2]], [[2,2],[1/8,1/8],[1/4,1/4],[1/2,1/2],[1,1]]]
##L = [[1,1,2,4,1/2], [1,1,2,4,8], [1/2,1/2,1,2,4], [1/4,1/4,1/2,1,2], [2,1/8,1/4,1/2,1]]
##U = [[1,1,2,4,1/2], [1,1,2,4,8], [1/2,1/2,1,2,4], [1/4,1/4,1/2,1,2], [2,1/8,1/4,1/2,1]]
##print( LP.gpm(L,U) )


#Test A4 (нечеткая слабо согласованная МПС)

##PCM = [[[1,1], [1,3], [3,5], [5,7], [5,9]], [[1/3,1], [1,1], [1,4], [1,5], [1,4]], [[1/5,1/3],[1/4,1],[1,1],[1/5,5], [2,4]], [[1/7,1/5],[1/5,1],[1/5,5],[1,1],[1,2]], [[1/9,1/5],[1/4,1],[1/4,1/2],[1/2,1],[1,1]]]
##L = [[1, 1, 3, 5, 5], [1/3, 1, 1, 1, 1], [1/5,1/4,1,1/5,2], [1/7,1/5,1/5,1,1], [1/9,1/4,1/4,1/2,1] ]
##U = [[1, 3, 5, 7, 9], [  1, 1, 4, 5, 4], [1/3,  1,1,  5,4], [1/5,  1,  5,1,2], [1/5,  1,1/2,  1,1] ]
##print( LP.gpm(L,U) )



#Test A4 (нечеткая слабо согласованная МПС)

##PCM = [[[1,1], [1,3], [3,5], [5,7], [5,9]], [[1/3,1], [1,1], [1,4], [1,5], [1,4]], [[1/5,1/3],[1/4,1],[1,1],[1/5,5], [2,4]], [[1/7,1/5],[1/5,1],[1/5,5],[1,1],[1,2]], [[1/9,1/5],[1/4,1],[1/4,1/2],[1/2,1],[1,1]]]
##L = [[1, 1, 3, 5, 5], [1/3, 1, 1, 1, 1], [1/5,1/4,1,1/5,2], [1/7,1/5,1/5,1,1], [1/9,1/4,1/4,1/2,1] ]
##U = [[1, 3, 5, 7, 9], [  1, 1, 4, 5, 4], [1/3,  1,1,  5,4], [1/5,  1,  5,1,2], [1/5,  1,1/2,  1,1] ]
##print( LP.gpm(L,U) )



# Test 5 (четкая слабо несогласованная МПС_3 5x5)
##D = [[[1,1], [2,2], [3,3], [5,5], [7,7]], [[1/2,1/2], [1,1], [2,2], [2,2], [4,4]], [[1/3,1/3],[1/2,1/2],[1,1],[1,1], [2,2]], [[1/5,1/5],[1/2,1/2],[1,1],[1,1],[9,9]], [[1/7,1/7],[1/4,1/4],[1/2,1/2],[1/9,1/9],[1,1]]]
##L = [[1, 2, 3, 5, 7], [1/2, 1, 2, 2, 4], [1/3, 1/2, 1, 1, 2], [1/5, 1/2, 1, 1, 9], [1/7, 1/4, 1/2, 1/9, 1]]
##U = [[1, 2, 3, 5, 7], [1/2, 1, 2, 2, 4], [1/3, 1/2, 1, 1, 2], [1/5, 1/2, 1, 1, 9], [1/7, 1/4, 1/2, 1/9, 1]]
##print( LP.gpm(L,U) )



##Test 5 (четкая слабо несогласованная МПС_3 5x5)
##D = [[[1,1], [2,2], [3,3], [5,5], [7,7]], [[1/2,1/2], [1,1], [2,2], [2,2], [4,4]], [[1/3,1/3],[1/2,1/2],[1,1],[1,1], [2,2]], [[1/5,1/5],[1/2,1/2],[1,1],[1,1],[9,9]], [[1/7,1/7],[1/4,1/4],[1/2,1/2],[1/9,1/9],[1,1]]]
##L = [[1, 2, 3, 5, 7], [1/2, 1, 2, 2, 4], [1/3, 1/2, 1, 1, 2], [1/5, 1/2, 1, 1, 9], [1/7, 1/4, 1/2, 1/9, 1]]
##U = [[1, 2, 3, 5, 7], [1/2, 1, 2, 2, 4], [1/3, 1/2, 1, 1, 2], [1/5, 1/2, 1, 1, 9], [1/7, 1/4, 1/2, 1/9, 1]]
##print( LP.gpm(L,U) )


#Test 8 (нечеткая слабо согласованная МПС 5x5)
##D = [[[1,1], [1/3,1], [1/4,1/2], [1/7,1/5], [1/3,1]], [[1,3], [1,1], [3,5], [4,6], [1,3]], [[2,4],[1/5,1/3],[1,1],[1/3,1], [1/5,1/3]], [[5,7],[1/6,1/4],[1,3],[1,1],[1/4,1/2]], [[1,3],[1/3,1],[3,5],[2,4],[1,1]]]
##L = [[1, 1/3, 1/4, 1/7, 1/3], [1, 1, 3, 4, 1], [2,1/5,1,1/3,1/5], [5,1/6,1,1,1/4], [1,1/3,3,2,1]]
##U = [[1,   1, 1/2, 1/5,   1], [3, 1, 5, 6, 3], [4,1/3,1,  1,1/3], [7,1/4,3,1,1/2], [3,  1,5,4,1]]
##print( LP.gpm(L,U) )



#Test 9 (нечеткая согласованная МПС 3x3)
##D = [ [[1,1], [1,3], [3,5]], [[1/3,1], [1,1], [1,3]], [[1/5,1/3],[1/3,1],[1,1]] ]
##L = [ [1, 1, 3], [1/3, 1, 1], [1/5, 1/3, 1] ]
##U = [ [1, 3, 5], [  1, 1, 3], [1/3,   1, 1] ]
##print( LP.gpm(L,U) )


#Test A5 (interval PCM, weak inconsistent)
##L = [ [1, 1/3, 1/6, 1/8, 1/9], [1, 1, 1/3, 1/4, 1/5], [4, 1, 1, 1, 1/3], [6, 2, 1/3, 1, 1], [8, 3, 1, 1, 1] ]
##U = [ [1,   1, 1/4, 1/6, 1/8], [3, 1,   1, 1/2, 1/3], [6, 3, 1, 3,   1], [8, 4,   1, 1, 1], [9, 5, 3, 1, 1] ]
##print( LP.gpm(L,U) )


#Test corrected A5 (interval PCM, weak consistent)
##L = [ [1, 1/3, 1/6, 1/8, 1/9], [1, 1, 1/3, 1/4, 1/5], [4, 1, 1, 1/3, 1/3], [6, 2, 1, 1, 1], [8, 3, 1, 1, 1] ]
##U = [ [1,   1, 1/4, 1/6, 1/8], [3, 1,   1, 1/2, 1/3], [6, 3, 1,   1,   1], [8, 4, 3, 1, 1], [9, 5, 3, 1, 1] ]
####print( LP.gpm(L,U) )



#Test A6 (interval PCM, weak inconsistent)
##L = [ [1, 1/7, 1, 1/7, 1/9], [5, 1, 2, 1/3, 1], [1, 1/4, 1, 1/9, 1/5], [5, 1, 8, 1, 1/3], [7, 1/3, 3, 1, 1] ]
##U = [ [1, 1/5, 1, 1/5, 1/7], [7, 1, 4,   1, 3], [1, 1/2, 1, 1/8, 1/3], [7, 3, 9, 1,   1], [9,   1, 5, 3, 1] ]
##print( LP.gpm(L,U) )



#Test corrected A6 (interval PCM, weak consistent)
##L = [ [1, 1/7, 1, 1/7, 1/9], [5, 1, 2, 1/3, 1/3], [1, 1/4, 1, 1/9, 1/5], [5, 1, 8, 1, 1/3], [7, 1, 3, 1, 1] ]
##U = [ [1, 1/5, 1, 1/5, 1/7], [7, 1, 4,   1,   1], [1, 1/2, 1, 1/8, 1/3], [7, 3, 9, 1,   1], [9, 3, 5, 3, 1] ]
##print( LP.gpm(L,U) )

#Test A7 (interval PCM, weak inconsistent)
##L = [ [1, 1, 2, 4, 6], [1/3, 1, 1, 1/3, 3], [1/4, 1/3, 1, 1, 1], [1/6, 1, 1/3, 1, 8], [1/8, 1/5, 1/3, 1/10, 1] ]
##U = [ [1, 3, 4, 6, 8], [  1, 1, 3,   1, 5], [1/2,   1, 1, 3, 3], [1/4, 3,   1, 1,10], [1/6, 1/3,   1, 1/8,  1] ]
##print( LP.gpm(L,U) )



#Test corrected A7 (interval PCM, weak inconsistent)
L = [ [1, 1, 2, 4, 6], [1/3, 1, 1, 1, 3], [1/4, 1/3, 1, 1, 1], [1/6, 1/3, 1/3, 1, 8], [1/8, 1/5, 1/3, 1/10, 1] ]
U = [ [1, 3, 4, 6, 8], [  1, 1, 3, 3, 5], [1/2,   1, 1, 3, 3], [1/4,   1,   1, 1,10], [1/6, 1/3,   1, 1/8,  1] ]
print( LP.gpm(L,U) )


