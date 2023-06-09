## -*- encoding: utf-8 -*-

# This file was *autogenerated* from the file typeOneRadicals-Practice2.sagetex.sage
from sage.all_cmdline import *   # import sage library

_sage_const_3 = Integer(3); _sage_const_2 = Integer(2); _sage_const_1 = Integer(1); _sage_const_0 = Integer(0); _sage_const_7 = Integer(7); _sage_const_6 = Integer(6); _sage_const_5 = Integer(5); _sage_const_473 = Integer(473); _sage_const_43 = Integer(43); _sage_const_9 = Integer(9); _sage_const_8 = Integer(8); _sage_const_500 = Integer(500); _sage_const_479 = Integer(479); _sage_const_28 = Integer(28); _sage_const_29 = Integer(29); _sage_const_22 = Integer(22); _sage_const_23 = Integer(23); _sage_const_20 = Integer(20); _sage_const_21 = Integer(21); _sage_const_26 = Integer(26); _sage_const_27 = Integer(27); _sage_const_24 = Integer(24); _sage_const_25 = Integer(25); _sage_const_40 = Integer(40); _sage_const_41 = Integer(41); _sage_const_42 = Integer(42); _sage_const_32 = Integer(32); _sage_const_44 = Integer(44); _sage_const_45 = Integer(45); _sage_const_46 = Integer(46); _sage_const_47 = Integer(47); _sage_const_48 = Integer(48); _sage_const_49 = Integer(49); _sage_const_54 = Integer(54); _sage_const_4 = Integer(4); _sage_const_52 = Integer(52); _sage_const_33 = Integer(33); _sage_const_51 = Integer(51); _sage_const_50 = Integer(50); _sage_const_522 = Integer(522); _sage_const_489 = Integer(489); _sage_const_53 = Integer(53); _sage_const_511 = Integer(511); _sage_const_13 = Integer(13); _sage_const_12 = Integer(12); _sage_const_11 = Integer(11); _sage_const_10 = Integer(10); _sage_const_17 = Integer(17); _sage_const_16 = Integer(16); _sage_const_15 = Integer(15); _sage_const_14 = Integer(14); _sage_const_31 = Integer(31); _sage_const_30 = Integer(30); _sage_const_19 = Integer(19); _sage_const_18 = Integer(18); _sage_const_35 = Integer(35); _sage_const_34 = Integer(34); _sage_const_37 = Integer(37); _sage_const_36 = Integer(36); _sage_const_39 = Integer(39); _sage_const_38 = Integer(38)## This file (typeOneRadicals-Practice2.sagetex.sage) was *autogenerated* from typeOneRadicals-Practice2.tex with sagetex.sty version 2015/08/26 v3.0-92d9f7a.
import sagetex
_st_ = sagetex.SageTeXProcessor('typeOneRadicals-Practice2', version='2015/08/26 v3.0-92d9f7a', version_check=True)
_st_.current_tex_line = _sage_const_8 
_st_.blockbegin()
try:
 var('x')
 
 def RandInt(a,b):
     """ Returns a random integer in [`a`,`b`]. Note that `a` and `b` should be integers themselves to avoid unexpected behavior.
     """
     return QQ(randint(int(a),int(b)))
     # return choice(range(a,b+1))
 
 def NonZeroInt(b,c, avoid = [_sage_const_0 ]):
     """ Returns a random integer in [`b`,`c`] which is not in `av`.
         If `av` is not specified, defaults to a non-zero integer.
     """
     while True:
         a = RandInt(b,c)
         if a not in avoid:
             return a
 
 
 #### Note: Because Sage does everything in the complex plane,
 #           it cannot be trusted to simplify radicals in any sane way for a precalc student.
 #           Thus we will need to manually build out the correct answer.
 
 ###### Problem p1
 ### Decide on the root value.
 p1rootVal = RandInt(_sage_const_2 ,_sage_const_9 )
 
 ### Build coefficients. In order to avoid crazy leading coefficients it is useful to ensure that there are no common factors.
 p1c1 = _sage_const_2 
 p1c2 = _sage_const_2 
 p1c3 = _sage_const_2 
 p1c4 = _sage_const_2 
 p1c5 = _sage_const_2 
 p1c6 = _sage_const_2 
 p1c7 = _sage_const_2 
 p1c8 = _sage_const_2 
 while abs(p1c2/p1c1)==abs(p1c4/p1c3) or abs(p1c2/p1c1)==abs(p1c6/p1c5) or abs(p1c2/p1c1)==abs(p1c8/p1c7) or abs(p1c4/p1c3)==abs(p1c6/p1c5) or abs(p1c4/p1c3)==abs(p1c8/p1c7) or abs(p1c6/p1c5)==abs(p1c8/p1c7):
     p1c1 = _sage_const_2 
     p1c2 = _sage_const_2 
     p1c3 = _sage_const_2 
     p1c4 = _sage_const_2 
     p1c5 = _sage_const_2 
     p1c6 = _sage_const_2 
     p1c7 = _sage_const_2 
     p1c8 = _sage_const_2 
     while gcd(p1c1,p1c2)>_sage_const_1 :
         p1c1 = RandInt(_sage_const_1 ,_sage_const_5 )
         p1c2 = RandInt(-_sage_const_10 ,_sage_const_10 )
     while gcd(p1c3,p1c4)>_sage_const_1 :
         p1c3 = RandInt(_sage_const_1 ,_sage_const_5 )
         p1c4 = RandInt(-_sage_const_10 ,_sage_const_10 )
     while gcd(p1c5,p1c6)>_sage_const_1 :
         p1c5 = RandInt(_sage_const_1 ,_sage_const_5 )
         p1c6 = RandInt(-_sage_const_10 ,_sage_const_10 )
     while gcd(p1c7,p1c8)>_sage_const_1 :
         p1c7 = RandInt(_sage_const_1 ,_sage_const_5 )
         p1c8 = RandInt(-_sage_const_10 ,_sage_const_10 )
 
 ### Choose the remainder power for each factor; the part that remains in radicand after simplifying.
 p1f1remainPwr = RandInt(_sage_const_0 ,p1rootVal-_sage_const_1 )
 p1f2remainPwr = RandInt(_sage_const_0 ,p1rootVal-_sage_const_1 )
 p1f3remainPwr = RandInt(_sage_const_0 ,p1rootVal-_sage_const_1 )
 p1f4remainPwr = RandInt(_sage_const_0 ,p1rootVal-_sage_const_1 )
 
 ### Choose the factorable power; the part that will be removed from the radicand during simplifying.
 p1f1factorPwr = RandInt(_sage_const_0 ,_sage_const_5 )
 p1f2factorPwr = RandInt(_sage_const_0 ,_sage_const_5 )
 p1f3factorPwr = RandInt(_sage_const_0 ,_sage_const_5 )
 p1f4factorPwr = RandInt(_sage_const_0 ,_sage_const_5 )
 
 ### Build individual function elements.
 p1f1remain = (p1c1*x-p1c2)**p1f1remainPwr
 p1f2remain = (p1c3*x-p1c4)**p1f2remainPwr
 p1f3remain = (p1c5*x-p1c6)**p1f3remainPwr
 p1f4remain = (p1c7*x-p1c8)**p1f4remainPwr
 
 p1f1total = (p1c1*x-p1c2)**(p1f1remainPwr+p1f1factorPwr*p1rootVal)
 p1f2total = (p1c3*x-p1c4)**(p1f2remainPwr+p1f2factorPwr*p1rootVal)
 p1f3total = (p1c5*x-p1c6)**(p1f3remainPwr+p1f3factorPwr*p1rootVal)
 p1f4total = (p1c7*x-p1c8)**(p1f4remainPwr+p1f4factorPwr*p1rootVal)
 
 p1fDisp = p1f1total*p1f2total*p1f3total*p1f4total
 
 p1fRemainder = p1f1remain*p1f2remain*p1f3remain*p1f4remain
 
 ### The fun part; writing out the factored piece, which depends on things like if they need absolute value or not.
 if p1rootVal%_sage_const_2 ==_sage_const_0 :
     if p1f1factorPwr%_sage_const_2 ==_sage_const_0 :
         p1f1factored = (p1c1*x-p1c2)**p1f1factorPwr
     else:
         p1f1factored = abs(p1c1*x-p1c2)**p1f1factorPwr
     if p1f2factorPwr%_sage_const_2 ==_sage_const_0 :
         p1f2factored = (p1c3*x-p1c4)**p1f2factorPwr
     else:
         p1f2factored = abs(p1c3*x-p1c4)**p1f2factorPwr
     if p1f3factorPwr%_sage_const_2 ==_sage_const_0 :
         p1f3factored = (p1c5*x-p1c6)**p1f3factorPwr
     else:
         p1f3factored = abs(p1c5*x-p1c6)**p1f3factorPwr
     if p1f4factorPwr%_sage_const_2 ==_sage_const_0 :
         p1f4factored = (p1c7*x-p1c8)**p1f4factorPwr
     else:
         p1f4factored = abs(p1c7*x-p1c8)**p1f4factorPwr
     p1fFactored = p1f1factored*p1f2factored*p1f3factored*p1f4factored
 else:
     p1fFactored = (p1c1*x-p1c2)**p1f1factorPwr*(p1c3*x-p1c4)**p1f2factorPwr*(p1c5*x-p1c6)**p1f3factorPwr*(p1c7*x-p1c8)**p1f4factorPwr
 
 
 
 
 
 
 ###### Problem p2
 ### Decide on the root value.
 p2rootVal = RandInt(_sage_const_2 ,_sage_const_9 )
 
 ### Build coefficients. In order to avoid crazy leading coefficients it is useful to ensure that there are no common factors.
 p2c1 = _sage_const_2 
 p2c2 = _sage_const_2 
 p2c3 = _sage_const_2 
 p2c4 = _sage_const_2 
 p2c5 = _sage_const_2 
 p2c6 = _sage_const_2 
 p2c7 = _sage_const_2 
 p2c8 = _sage_const_2 
 while abs(p2c2/p2c1)==abs(p2c4/p2c3) or abs(p2c2/p2c1)==abs(p2c6/p2c5) or abs(p2c2/p2c1)==abs(p2c8/p2c7) or abs(p2c4/p2c3)==abs(p2c6/p2c5) or abs(p2c4/p2c3)==abs(p2c8/p2c7) or abs(p2c6/p2c5)==abs(p2c8/p2c7):
     p2c1 = _sage_const_2 
     p2c2 = _sage_const_2 
     p2c3 = _sage_const_2 
     p2c4 = _sage_const_2 
     p2c5 = _sage_const_2 
     p2c6 = _sage_const_2 
     p2c7 = _sage_const_2 
     p2c8 = _sage_const_2 
     while gcd(p2c1,p2c2)>_sage_const_1 :
         p2c1 = RandInt(_sage_const_1 ,_sage_const_5 )
         p2c2 = RandInt(-_sage_const_10 ,_sage_const_10 )
     while gcd(p2c3,p2c4)>_sage_const_1 :
         p2c3 = RandInt(_sage_const_1 ,_sage_const_5 )
         p2c4 = RandInt(-_sage_const_10 ,_sage_const_10 )
     while gcd(p2c5,p2c6)>_sage_const_1 :
         p2c5 = RandInt(_sage_const_1 ,_sage_const_5 )
         p2c6 = RandInt(-_sage_const_10 ,_sage_const_10 )
     while gcd(p2c7,p2c8)>_sage_const_1 :
         p2c7 = RandInt(_sage_const_1 ,_sage_const_5 )
         p2c8 = RandInt(-_sage_const_10 ,_sage_const_10 )
 
 ### Choose the remainder power for each factor; the part that remains in radicand after simplifying.
 p2f1remainPwr = RandInt(_sage_const_0 ,p2rootVal-_sage_const_1 )
 p2f2remainPwr = RandInt(_sage_const_0 ,p2rootVal-_sage_const_1 )
 p2f3remainPwr = RandInt(_sage_const_0 ,p2rootVal-_sage_const_1 )
 p2f4remainPwr = RandInt(_sage_const_0 ,p2rootVal-_sage_const_1 )
 
 ### Choose the factorable power; the part that will be removed from the radicand during simplifying.
 p2f1factorPwr = RandInt(_sage_const_0 ,_sage_const_5 )
 p2f2factorPwr = RandInt(_sage_const_0 ,_sage_const_5 )
 p2f3factorPwr = RandInt(_sage_const_0 ,_sage_const_5 )
 p2f4factorPwr = RandInt(_sage_const_0 ,_sage_const_5 )
 
 ### Build individual function elements.
 p2f1remain = (p2c1*x-p2c2)**p2f1remainPwr
 p2f2remain = (p2c3*x-p2c4)**p2f2remainPwr
 p2f3remain = (p2c5*x-p2c6)**p2f3remainPwr
 p2f4remain = (p2c7*x-p2c8)**p2f4remainPwr
 
 p2f1total = (p2c1*x-p2c2)**(p2f1remainPwr+p2f1factorPwr*p2rootVal)
 p2f2total = (p2c3*x-p2c4)**(p2f2remainPwr+p2f2factorPwr*p2rootVal)
 p2f3total = (p2c5*x-p2c6)**(p2f3remainPwr+p2f3factorPwr*p2rootVal)
 p2f4total = (p2c7*x-p2c8)**(p2f4remainPwr+p2f4factorPwr*p2rootVal)
 
 p2fDisp = p2f1total*p2f2total*p2f3total*p2f4total
 
 p2fRemainder = p2f1remain*p2f2remain*p2f3remain*p2f4remain
 
 ### The fun part; writing out the factored piece, which depends on things like if they need absolute value or not.
 if p2rootVal%_sage_const_2 ==_sage_const_0 :
     if p2f1factorPwr%_sage_const_2 ==_sage_const_0 :
         p2f1factored = (p2c1*x-p2c2)**p2f1factorPwr
     else:
         p2f1factored = abs(p2c1*x-p2c2)**p2f1factorPwr
     if p2f2factorPwr%_sage_const_2 ==_sage_const_0 :
         p2f2factored = (p2c3*x-p2c4)**p2f2factorPwr
     else:
         p2f2factored = abs(p2c3*x-p2c4)**p2f2factorPwr
     if p2f3factorPwr%_sage_const_2 ==_sage_const_0 :
         p2f3factored = (p2c5*x-p2c6)**p2f3factorPwr
     else:
         p2f3factored = abs(p2c5*x-p2c6)**p2f3factorPwr
     if p2f4factorPwr%_sage_const_2 ==_sage_const_0 :
         p2f4factored = (p2c7*x-p2c8)**p2f4factorPwr
     else:
         p2f4factored = abs(p2c7*x-p2c8)**p2f4factorPwr
     p2fFactored = p2f1factored*p2f2factored*p2f3factored*p2f4factored
 else:
     p2fFactored = (p2c1*x-p2c2)**p2f1factorPwr*(p2c3*x-p2c4)**p2f2factorPwr*(p2c5*x-p2c6)**p2f3factorPwr*(p2c7*x-p2c8)**p2f4factorPwr
 
 
 
 
 
 ###### Problem p3
 ### Decide on the root value.
 p3rootVal = RandInt(_sage_const_2 ,_sage_const_9 )
 
 ### Build coefficients. In order to avoid crazy leading coefficients it is useful to ensure that there are no common factors.
 p3c1 = _sage_const_2 
 p3c2 = _sage_const_2 
 p3c3 = _sage_const_2 
 p3c4 = _sage_const_2 
 p3c5 = _sage_const_2 
 p3c6 = _sage_const_2 
 p3c7 = _sage_const_2 
 p3c8 = _sage_const_2 
 while abs(p3c2/p3c1)==abs(p3c4/p3c3) or abs(p3c2/p3c1)==abs(p3c6/p3c5) or abs(p3c2/p3c1)==abs(p3c8/p3c7) or abs(p3c4/p3c3)==abs(p3c6/p3c5) or abs(p3c4/p3c3)==abs(p3c8/p3c7) or abs(p3c6/p3c5)==abs(p3c8/p3c7):
     p3c1 = _sage_const_2 
     p3c2 = _sage_const_2 
     p3c3 = _sage_const_2 
     p3c4 = _sage_const_2 
     p3c5 = _sage_const_2 
     p3c6 = _sage_const_2 
     p3c7 = _sage_const_2 
     p3c8 = _sage_const_2 
     while gcd(p3c1,p3c2)>_sage_const_1 :
         p3c1 = RandInt(_sage_const_1 ,_sage_const_5 )
         p3c2 = RandInt(-_sage_const_10 ,_sage_const_10 )
     while gcd(p3c3,p3c4)>_sage_const_1 :
         p3c3 = RandInt(_sage_const_1 ,_sage_const_5 )
         p3c4 = RandInt(-_sage_const_10 ,_sage_const_10 )
     while gcd(p3c5,p3c6)>_sage_const_1 :
         p3c5 = RandInt(_sage_const_1 ,_sage_const_5 )
         p3c6 = RandInt(-_sage_const_10 ,_sage_const_10 )
     while gcd(p3c7,p3c8)>_sage_const_1 :
         p3c7 = RandInt(_sage_const_1 ,_sage_const_5 )
         p3c8 = RandInt(-_sage_const_10 ,_sage_const_10 )
 
 ### Choose the remainder power for each factor; the part that remains in radicand after simplifying.
 p3f1remainPwr = RandInt(_sage_const_0 ,p3rootVal-_sage_const_1 )
 p3f2remainPwr = RandInt(_sage_const_0 ,p3rootVal-_sage_const_1 )
 p3f3remainPwr = RandInt(_sage_const_0 ,p3rootVal-_sage_const_1 )
 p3f4remainPwr = RandInt(_sage_const_0 ,p3rootVal-_sage_const_1 )
 
 ### Choose the factorable power; the part that will be removed from the radicand during simplifying.
 p3f1factorPwr = RandInt(_sage_const_0 ,_sage_const_5 )
 p3f2factorPwr = RandInt(_sage_const_0 ,_sage_const_5 )
 p3f3factorPwr = RandInt(_sage_const_0 ,_sage_const_5 )
 p3f4factorPwr = RandInt(_sage_const_0 ,_sage_const_5 )
 
 ### Build individual function elements.
 p3f1remain = (p3c1*x-p3c2)**p3f1remainPwr
 p3f2remain = (p3c3*x-p3c4)**p3f2remainPwr
 p3f3remain = (p3c5*x-p3c6)**p3f3remainPwr
 p3f4remain = (p3c7*x-p3c8)**p3f4remainPwr
 
 p3f1total = (p3c1*x-p3c2)**(p3f1remainPwr+p3f1factorPwr*p3rootVal)
 p3f2total = (p3c3*x-p3c4)**(p3f2remainPwr+p3f2factorPwr*p3rootVal)
 p3f3total = (p3c5*x-p3c6)**(p3f3remainPwr+p3f3factorPwr*p3rootVal)
 p3f4total = (p3c7*x-p3c8)**(p3f4remainPwr+p3f4factorPwr*p3rootVal)
 
 p3fDisp = p3f1total*p3f2total*p3f3total*p3f4total
 
 p3fRemainder = p3f1remain*p3f2remain*p3f3remain*p3f4remain
 
 ### The fun part; writing out the factored piece, which depends on things like if they need absolute value or not.
 if p3rootVal%_sage_const_2 ==_sage_const_0 :
     if p3f1factorPwr%_sage_const_2 ==_sage_const_0 :
         p3f1factored = (p3c1*x-p3c2)**p3f1factorPwr
     else:
         p3f1factored = abs(p3c1*x-p3c2)**p3f1factorPwr
     if p3f2factorPwr%_sage_const_2 ==_sage_const_0 :
         p3f2factored = (p3c3*x-p3c4)**p3f2factorPwr
     else:
         p3f2factored = abs(p3c3*x-p3c4)**p3f2factorPwr
     if p3f3factorPwr%_sage_const_2 ==_sage_const_0 :
         p3f3factored = (p3c5*x-p3c6)**p3f3factorPwr
     else:
         p3f3factored = abs(p3c5*x-p3c6)**p3f3factorPwr
     if p3f4factorPwr%_sage_const_2 ==_sage_const_0 :
         p3f4factored = (p3c7*x-p3c8)**p3f4factorPwr
     else:
         p3f4factored = abs(p3c7*x-p3c8)**p3f4factorPwr
     p3fFactored = p3f1factored*p3f2factored*p3f3factored*p3f4factored
 else:
     p3fFactored = (p3c1*x-p3c2)**p3f1factorPwr*(p3c3*x-p3c4)**p3f2factorPwr*(p3c5*x-p3c6)**p3f3factorPwr*(p3c7*x-p3c8)**p3f4factorPwr
 
 
 
 
 
 ###### Problem p4
 ### Decide on the root value.
 p4rootVal = RandInt(_sage_const_2 ,_sage_const_9 )
 
 ### Build coefficients. In order to avoid crazy leading coefficients it is useful to ensure that there are no common factors.
 p4c1 = _sage_const_2 
 p4c2 = _sage_const_2 
 p4c3 = _sage_const_2 
 p4c4 = _sage_const_2 
 p4c5 = _sage_const_2 
 p4c6 = _sage_const_2 
 p4c7 = _sage_const_2 
 p4c8 = _sage_const_2 
 while abs(p4c2/p4c1)==abs(p4c4/p4c3) or abs(p4c2/p4c1)==abs(p4c6/p4c5) or abs(p4c2/p4c1)==abs(p4c8/p4c7) or abs(p4c4/p4c3)==abs(p4c6/p4c5) or abs(p4c4/p4c3)==abs(p4c8/p4c7) or abs(p4c6/p4c5)==abs(p4c8/p4c7):
     p4c1 = _sage_const_2 
     p4c2 = _sage_const_2 
     p4c3 = _sage_const_2 
     p4c4 = _sage_const_2 
     p4c5 = _sage_const_2 
     p4c6 = _sage_const_2 
     p4c7 = _sage_const_2 
     p4c8 = _sage_const_2 
     while gcd(p4c1,p4c2)>_sage_const_1 :
         p4c1 = RandInt(_sage_const_1 ,_sage_const_5 )
         p4c2 = RandInt(-_sage_const_10 ,_sage_const_10 )
     while gcd(p4c3,p4c4)>_sage_const_1 :
         p4c3 = RandInt(_sage_const_1 ,_sage_const_5 )
         p4c4 = RandInt(-_sage_const_10 ,_sage_const_10 )
     while gcd(p4c5,p4c6)>_sage_const_1 :
         p4c5 = RandInt(_sage_const_1 ,_sage_const_5 )
         p4c6 = RandInt(-_sage_const_10 ,_sage_const_10 )
     while gcd(p4c7,p4c8)>_sage_const_1 :
         p4c7 = RandInt(_sage_const_1 ,_sage_const_5 )
         p4c8 = RandInt(-_sage_const_10 ,_sage_const_10 )
 
 ### Choose the remainder power for each factor; the part that remains in radicand after simplifying.
 p4f1remainPwr = RandInt(_sage_const_0 ,p4rootVal-_sage_const_1 )
 p4f2remainPwr = RandInt(_sage_const_0 ,p4rootVal-_sage_const_1 )
 p4f3remainPwr = RandInt(_sage_const_0 ,p4rootVal-_sage_const_1 )
 p4f4remainPwr = RandInt(_sage_const_0 ,p4rootVal-_sage_const_1 )
 
 ### Choose the factorable power; the part that will be removed from the radicand during simplifying.
 p4f1factorPwr = RandInt(_sage_const_0 ,_sage_const_5 )
 p4f2factorPwr = RandInt(_sage_const_0 ,_sage_const_5 )
 p4f3factorPwr = RandInt(_sage_const_0 ,_sage_const_5 )
 p4f4factorPwr = RandInt(_sage_const_0 ,_sage_const_5 )
 
 ### Build individual function elements.
 p4f1remain = (p4c1*x-p4c2)**p4f1remainPwr
 p4f2remain = (p4c3*x-p4c4)**p4f2remainPwr
 p4f3remain = (p4c5*x-p4c6)**p4f3remainPwr
 p4f4remain = (p4c7*x-p4c8)**p4f4remainPwr
 
 p4f1total = (p4c1*x-p4c2)**(p4f1remainPwr+p4f1factorPwr*p4rootVal)
 p4f2total = (p4c3*x-p4c4)**(p4f2remainPwr+p4f2factorPwr*p4rootVal)
 p4f3total = (p4c5*x-p4c6)**(p4f3remainPwr+p4f3factorPwr*p4rootVal)
 p4f4total = (p4c7*x-p4c8)**(p4f4remainPwr+p4f4factorPwr*p4rootVal)
 
 p4fDisp = p4f1total*p4f2total*p4f3total*p4f4total
 
 p4fRemainder = p4f1remain*p4f2remain*p4f3remain*p4f4remain
 
 ### The fun part; writing out the factored piece, which depends on things like if they need absolute value or not.
 if p4rootVal%_sage_const_2 ==_sage_const_0 :
     if p4f1factorPwr%_sage_const_2 ==_sage_const_0 :
         p4f1factored = (p4c1*x-p4c2)**p4f1factorPwr
     else:
         p4f1factored = abs(p4c1*x-p4c2)**p4f1factorPwr
     if p4f2factorPwr%_sage_const_2 ==_sage_const_0 :
         p4f2factored = (p4c3*x-p4c4)**p4f2factorPwr
     else:
         p4f2factored = abs(p4c3*x-p4c4)**p4f2factorPwr
     if p4f3factorPwr%_sage_const_2 ==_sage_const_0 :
         p4f3factored = (p4c5*x-p4c6)**p4f3factorPwr
     else:
         p4f3factored = abs(p4c5*x-p4c6)**p4f3factorPwr
     if p4f4factorPwr%_sage_const_2 ==_sage_const_0 :
         p4f4factored = (p4c7*x-p4c8)**p4f4factorPwr
     else:
         p4f4factored = abs(p4c7*x-p4c8)**p4f4factorPwr
     p4fFactored = p4f1factored*p4f2factored*p4f3factored*p4f4factored
 else:
     p4fFactored = (p4c1*x-p4c2)**p4f1factorPwr*(p4c3*x-p4c4)**p4f2factorPwr*(p4c5*x-p4c6)**p4f3factorPwr*(p4c7*x-p4c8)**p4f4factorPwr
 
 
 
 
 
 ###### Problem p5
 ### Decide on the root value.
 p5rootVal = RandInt(_sage_const_2 ,_sage_const_9 )
 
 ### Build coefficients. In order to avoid crazy leading coefficients it is useful to ensure that there are no common factors.
 p5c1 = _sage_const_2 
 p5c2 = _sage_const_2 
 p5c3 = _sage_const_2 
 p5c4 = _sage_const_2 
 p5c5 = _sage_const_2 
 p5c6 = _sage_const_2 
 p5c7 = _sage_const_2 
 p5c8 = _sage_const_2 
 while abs(p5c2/p5c1)==abs(p5c4/p5c3) or abs(p5c2/p5c1)==abs(p5c6/p5c5) or abs(p5c2/p5c1)==abs(p5c8/p5c7) or abs(p5c4/p5c3)==abs(p5c6/p5c5) or abs(p5c4/p5c3)==abs(p5c8/p5c7) or abs(p5c6/p5c5)==abs(p5c8/p5c7):
     p5c1 = _sage_const_2 
     p5c2 = _sage_const_2 
     p5c3 = _sage_const_2 
     p5c4 = _sage_const_2 
     p5c5 = _sage_const_2 
     p5c6 = _sage_const_2 
     p5c7 = _sage_const_2 
     p5c8 = _sage_const_2 
     while gcd(p5c1,p5c2)>_sage_const_1 :
         p5c1 = RandInt(_sage_const_1 ,_sage_const_5 )
         p5c2 = RandInt(-_sage_const_10 ,_sage_const_10 )
     while gcd(p5c3,p5c4)>_sage_const_1 :
         p5c3 = RandInt(_sage_const_1 ,_sage_const_5 )
         p5c4 = RandInt(-_sage_const_10 ,_sage_const_10 )
     while gcd(p5c5,p5c6)>_sage_const_1 :
         p5c5 = RandInt(_sage_const_1 ,_sage_const_5 )
         p5c6 = RandInt(-_sage_const_10 ,_sage_const_10 )
     while gcd(p5c7,p5c8)>_sage_const_1 :
         p5c7 = RandInt(_sage_const_1 ,_sage_const_5 )
         p5c8 = RandInt(-_sage_const_10 ,_sage_const_10 )
 
 ### Choose the remainder power for each factor; the part that remains in radicand after simplifying.
 p5f1remainPwr = RandInt(_sage_const_0 ,p5rootVal-_sage_const_1 )
 p5f2remainPwr = RandInt(_sage_const_0 ,p5rootVal-_sage_const_1 )
 p5f3remainPwr = RandInt(_sage_const_0 ,p5rootVal-_sage_const_1 )
 p5f4remainPwr = RandInt(_sage_const_0 ,p5rootVal-_sage_const_1 )
 
 ### Choose the factorable power; the part that will be removed from the radicand during simplifying.
 p5f1factorPwr = RandInt(_sage_const_0 ,_sage_const_5 )
 p5f2factorPwr = RandInt(_sage_const_0 ,_sage_const_5 )
 p5f3factorPwr = RandInt(_sage_const_0 ,_sage_const_5 )
 p5f4factorPwr = RandInt(_sage_const_0 ,_sage_const_5 )
 
 ### Build individual function elements.
 p5f1remain = (p5c1*x-p5c2)**p5f1remainPwr
 p5f2remain = (p5c3*x-p5c4)**p5f2remainPwr
 p5f3remain = (p5c5*x-p5c6)**p5f3remainPwr
 p5f4remain = (p5c7*x-p5c8)**p5f4remainPwr
 
 p5f1total = (p5c1*x-p5c2)**(p5f1remainPwr+p5f1factorPwr*p5rootVal)
 p5f2total = (p5c3*x-p5c4)**(p5f2remainPwr+p5f2factorPwr*p5rootVal)
 p5f3total = (p5c5*x-p5c6)**(p5f3remainPwr+p5f3factorPwr*p5rootVal)
 p5f4total = (p5c7*x-p5c8)**(p5f4remainPwr+p5f4factorPwr*p5rootVal)
 
 p5fDisp = p5f1total*p5f2total*p5f3total*p5f4total
 
 p5fRemainder = p5f1remain*p5f2remain*p5f3remain*p5f4remain
 
 ### The fun part; writing out the factored piece, which depends on things like if they need absolute value or not.
 if p5rootVal%_sage_const_2 ==_sage_const_0 :
     if p5f1factorPwr%_sage_const_2 ==_sage_const_0 :
         p5f1factored = (p5c1*x-p5c2)**p5f1factorPwr
     else:
         p5f1factored = abs(p5c1*x-p5c2)**p5f1factorPwr
     if p5f2factorPwr%_sage_const_2 ==_sage_const_0 :
         p5f2factored = (p5c3*x-p5c4)**p5f2factorPwr
     else:
         p5f2factored = abs(p5c3*x-p5c4)**p5f2factorPwr
     if p5f3factorPwr%_sage_const_2 ==_sage_const_0 :
         p5f3factored = (p5c5*x-p5c6)**p5f3factorPwr
     else:
         p5f3factored = abs(p5c5*x-p5c6)**p5f3factorPwr
     if p5f4factorPwr%_sage_const_2 ==_sage_const_0 :
         p5f4factored = (p5c7*x-p5c8)**p5f4factorPwr
     else:
         p5f4factored = abs(p5c7*x-p5c8)**p5f4factorPwr
     p5fFactored = p5f1factored*p5f2factored*p5f3factored*p5f4factored
 else:
     p5fFactored = (p5c1*x-p5c2)**p5f1factorPwr*(p5c3*x-p5c4)**p5f2factorPwr*(p5c5*x-p5c6)**p5f3factorPwr*(p5c7*x-p5c8)**p5f4factorPwr
 
 
 
 
 
 
except:
 _st_.goboom(_sage_const_473 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_479 
 _st_.inline(_sage_const_0 , latex(p1rootVal))
except:
 _st_.goboom(_sage_const_479 )
try:
 _st_.current_tex_line = _sage_const_479 
 _st_.inline(_sage_const_1 , latex(p1fDisp))
except:
 _st_.goboom(_sage_const_479 )
try:
 _st_.current_tex_line = _sage_const_479 
 _st_.inline(_sage_const_2 , latex(p1fDisp))
except:
 _st_.goboom(_sage_const_479 )
try:
 _st_.current_tex_line = _sage_const_479 
 _st_.inline(_sage_const_3 , latex(p1fDisp))
except:
 _st_.goboom(_sage_const_479 )
try:
 _st_.current_tex_line = _sage_const_479 
 _st_.inline(_sage_const_4 , latex(p1fDisp))
except:
 _st_.goboom(_sage_const_479 )
try:
 _st_.current_tex_line = _sage_const_479 
 _st_.inline(_sage_const_5 , latex(p1fFactored))
except:
 _st_.goboom(_sage_const_479 )
try:
 _st_.current_tex_line = _sage_const_479 
 _st_.inline(_sage_const_6 , latex(p1rootVal))
except:
 _st_.goboom(_sage_const_479 )
try:
 _st_.current_tex_line = _sage_const_479 
 _st_.inline(_sage_const_7 , latex(p1fRemainder))
except:
 _st_.goboom(_sage_const_479 )
try:
 _st_.current_tex_line = _sage_const_479 
 _st_.inline(_sage_const_8 , latex(p1fRemainder))
except:
 _st_.goboom(_sage_const_479 )
try:
 _st_.current_tex_line = _sage_const_479 
 _st_.inline(_sage_const_9 , latex(p1fRemainder))
except:
 _st_.goboom(_sage_const_479 )
try:
 _st_.current_tex_line = _sage_const_479 
 _st_.inline(_sage_const_10 , latex(p1fRemainder))
except:
 _st_.goboom(_sage_const_479 )
try:
 _st_.current_tex_line = _sage_const_489 
 _st_.inline(_sage_const_11 , latex(p2rootVal))
except:
 _st_.goboom(_sage_const_489 )
try:
 _st_.current_tex_line = _sage_const_489 
 _st_.inline(_sage_const_12 , latex(p2fDisp))
except:
 _st_.goboom(_sage_const_489 )
try:
 _st_.current_tex_line = _sage_const_489 
 _st_.inline(_sage_const_13 , latex(p2fDisp))
except:
 _st_.goboom(_sage_const_489 )
try:
 _st_.current_tex_line = _sage_const_489 
 _st_.inline(_sage_const_14 , latex(p2fDisp))
except:
 _st_.goboom(_sage_const_489 )
try:
 _st_.current_tex_line = _sage_const_489 
 _st_.inline(_sage_const_15 , latex(p2fDisp))
except:
 _st_.goboom(_sage_const_489 )
try:
 _st_.current_tex_line = _sage_const_489 
 _st_.inline(_sage_const_16 , latex(p2fFactored))
except:
 _st_.goboom(_sage_const_489 )
try:
 _st_.current_tex_line = _sage_const_489 
 _st_.inline(_sage_const_17 , latex(p2rootVal))
except:
 _st_.goboom(_sage_const_489 )
try:
 _st_.current_tex_line = _sage_const_489 
 _st_.inline(_sage_const_18 , latex(p2fRemainder))
except:
 _st_.goboom(_sage_const_489 )
try:
 _st_.current_tex_line = _sage_const_489 
 _st_.inline(_sage_const_19 , latex(p2fRemainder))
except:
 _st_.goboom(_sage_const_489 )
try:
 _st_.current_tex_line = _sage_const_489 
 _st_.inline(_sage_const_20 , latex(p2fRemainder))
except:
 _st_.goboom(_sage_const_489 )
try:
 _st_.current_tex_line = _sage_const_489 
 _st_.inline(_sage_const_21 , latex(p2fRemainder))
except:
 _st_.goboom(_sage_const_489 )
try:
 _st_.current_tex_line = _sage_const_500 
 _st_.inline(_sage_const_22 , latex(p3rootVal))
except:
 _st_.goboom(_sage_const_500 )
try:
 _st_.current_tex_line = _sage_const_500 
 _st_.inline(_sage_const_23 , latex(p3fDisp))
except:
 _st_.goboom(_sage_const_500 )
try:
 _st_.current_tex_line = _sage_const_500 
 _st_.inline(_sage_const_24 , latex(p3fDisp))
except:
 _st_.goboom(_sage_const_500 )
try:
 _st_.current_tex_line = _sage_const_500 
 _st_.inline(_sage_const_25 , latex(p3fDisp))
except:
 _st_.goboom(_sage_const_500 )
try:
 _st_.current_tex_line = _sage_const_500 
 _st_.inline(_sage_const_26 , latex(p3fDisp))
except:
 _st_.goboom(_sage_const_500 )
try:
 _st_.current_tex_line = _sage_const_500 
 _st_.inline(_sage_const_27 , latex(p3fFactored))
except:
 _st_.goboom(_sage_const_500 )
try:
 _st_.current_tex_line = _sage_const_500 
 _st_.inline(_sage_const_28 , latex(p3rootVal))
except:
 _st_.goboom(_sage_const_500 )
try:
 _st_.current_tex_line = _sage_const_500 
 _st_.inline(_sage_const_29 , latex(p3fRemainder))
except:
 _st_.goboom(_sage_const_500 )
try:
 _st_.current_tex_line = _sage_const_500 
 _st_.inline(_sage_const_30 , latex(p3fRemainder))
except:
 _st_.goboom(_sage_const_500 )
try:
 _st_.current_tex_line = _sage_const_500 
 _st_.inline(_sage_const_31 , latex(p3fRemainder))
except:
 _st_.goboom(_sage_const_500 )
try:
 _st_.current_tex_line = _sage_const_500 
 _st_.inline(_sage_const_32 , latex(p3fRemainder))
except:
 _st_.goboom(_sage_const_500 )
try:
 _st_.current_tex_line = _sage_const_511 
 _st_.inline(_sage_const_33 , latex(p4rootVal))
except:
 _st_.goboom(_sage_const_511 )
try:
 _st_.current_tex_line = _sage_const_511 
 _st_.inline(_sage_const_34 , latex(p4fDisp))
except:
 _st_.goboom(_sage_const_511 )
try:
 _st_.current_tex_line = _sage_const_511 
 _st_.inline(_sage_const_35 , latex(p4fDisp))
except:
 _st_.goboom(_sage_const_511 )
try:
 _st_.current_tex_line = _sage_const_511 
 _st_.inline(_sage_const_36 , latex(p4fDisp))
except:
 _st_.goboom(_sage_const_511 )
try:
 _st_.current_tex_line = _sage_const_511 
 _st_.inline(_sage_const_37 , latex(p4fDisp))
except:
 _st_.goboom(_sage_const_511 )
try:
 _st_.current_tex_line = _sage_const_511 
 _st_.inline(_sage_const_38 , latex(p4fFactored))
except:
 _st_.goboom(_sage_const_511 )
try:
 _st_.current_tex_line = _sage_const_511 
 _st_.inline(_sage_const_39 , latex(p4rootVal))
except:
 _st_.goboom(_sage_const_511 )
try:
 _st_.current_tex_line = _sage_const_511 
 _st_.inline(_sage_const_40 , latex(p4fRemainder))
except:
 _st_.goboom(_sage_const_511 )
try:
 _st_.current_tex_line = _sage_const_511 
 _st_.inline(_sage_const_41 , latex(p4fRemainder))
except:
 _st_.goboom(_sage_const_511 )
try:
 _st_.current_tex_line = _sage_const_511 
 _st_.inline(_sage_const_42 , latex(p4fRemainder))
except:
 _st_.goboom(_sage_const_511 )
try:
 _st_.current_tex_line = _sage_const_511 
 _st_.inline(_sage_const_43 , latex(p4fRemainder))
except:
 _st_.goboom(_sage_const_511 )
try:
 _st_.current_tex_line = _sage_const_522 
 _st_.inline(_sage_const_44 , latex(p5rootVal))
except:
 _st_.goboom(_sage_const_522 )
try:
 _st_.current_tex_line = _sage_const_522 
 _st_.inline(_sage_const_45 , latex(p5fDisp))
except:
 _st_.goboom(_sage_const_522 )
try:
 _st_.current_tex_line = _sage_const_522 
 _st_.inline(_sage_const_46 , latex(p5fDisp))
except:
 _st_.goboom(_sage_const_522 )
try:
 _st_.current_tex_line = _sage_const_522 
 _st_.inline(_sage_const_47 , latex(p5fDisp))
except:
 _st_.goboom(_sage_const_522 )
try:
 _st_.current_tex_line = _sage_const_522 
 _st_.inline(_sage_const_48 , latex(p5fDisp))
except:
 _st_.goboom(_sage_const_522 )
try:
 _st_.current_tex_line = _sage_const_522 
 _st_.inline(_sage_const_49 , latex(p5fFactored))
except:
 _st_.goboom(_sage_const_522 )
try:
 _st_.current_tex_line = _sage_const_522 
 _st_.inline(_sage_const_50 , latex(p5rootVal))
except:
 _st_.goboom(_sage_const_522 )
try:
 _st_.current_tex_line = _sage_const_522 
 _st_.inline(_sage_const_51 , latex(p5fRemainder))
except:
 _st_.goboom(_sage_const_522 )
try:
 _st_.current_tex_line = _sage_const_522 
 _st_.inline(_sage_const_52 , latex(p5fRemainder))
except:
 _st_.goboom(_sage_const_522 )
try:
 _st_.current_tex_line = _sage_const_522 
 _st_.inline(_sage_const_53 , latex(p5fRemainder))
except:
 _st_.goboom(_sage_const_522 )
try:
 _st_.current_tex_line = _sage_const_522 
 _st_.inline(_sage_const_54 , latex(p5fRemainder))
except:
 _st_.goboom(_sage_const_522 )
_st_.endofdoc()

