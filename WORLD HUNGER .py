import sys


def test(did_pass):
    """ Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
    if did_pass:
        msg = "test at line {0} ok.".format(linenum)
    else:
        msg = ("test at line {0} FAILED.".format(linenum))
    print(msg)
def calc_calo(p,r,c,d):
    calculate = (c - r)* p * d
    if calculate < 0:
        return "your population is deficient by " + str(calculate) + " calories"
    elif calculate > 0:
        return "you wasted your food by " + str(calculate) + " calories"
    else :
        return "you didn't wasted your food or your population did not deficient by " + str(calculate) + " calories "
    
 

  
         



def test_suite():
    test(calc_calo(1, 1500, 1500, 1) == "you didn't wasted your food or your population did not deficient by 0 calories ")
    test(calc_calo(1, 1500, 2500, 1) == "you wasted your food by 1000 calories")
    test(calc_calo(1, 2500, 1500, 1) == "your population is deficient by -1000 calories")
    test(calc_calo(10, 1500, 2500, 1) == "you wasted your food by 10000 calories")
    test(calc_calo(10, 1500, 2500, 10) == "you wasted your food by 100000 calories")
test_suite()   
pop = int(input("What is the population?"))
rec = int(input("what is the recommended number of calories ?"))
cal = int(input("How many calories does the average person eat per day?"))
day = int(input("How many days?"))


print(calc_calo(pop, rec, cal, day))



