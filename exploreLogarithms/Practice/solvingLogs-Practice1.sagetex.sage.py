## -*- encoding: utf-8 -*-

# This file was *autogenerated* from the file solvingLogs-Practice1.sagetex.sage
from sage.all_cmdline import *   # import sage library

_sage_const_3 = Integer(3); _sage_const_2 = Integer(2); _sage_const_1 = Integer(1); _sage_const_0 = Integer(0); _sage_const_7 = Integer(7); _sage_const_6 = Integer(6); _sage_const_5 = Integer(5); _sage_const_4 = Integer(4); _sage_const_9 = Integer(9); _sage_const_8 = Integer(8); _sage_const_96 = Integer(96); _sage_const_28 = Integer(28); _sage_const_29 = Integer(29); _sage_const_22 = Integer(22); _sage_const_23 = Integer(23); _sage_const_20 = Integer(20); _sage_const_21 = Integer(21); _sage_const_26 = Integer(26); _sage_const_27 = Integer(27); _sage_const_24 = Integer(24); _sage_const_25 = Integer(25); _sage_const_65 = Integer(65); _sage_const_60 = Integer(60); _sage_const_81 = Integer(81); _sage_const_68 = Integer(68); _sage_const_83 = Integer(83); _sage_const_33 = Integer(33); _sage_const_39 = Integer(39); _sage_const_107 = Integer(107); _sage_const_32 = Integer(32); _sage_const_13 = Integer(13); _sage_const_12 = Integer(12); _sage_const_11 = Integer(11); _sage_const_136 = Integer(136); _sage_const_17 = Integer(17); _sage_const_16 = Integer(16); _sage_const_15 = Integer(15); _sage_const_14 = Integer(14); _sage_const_31 = Integer(31); _sage_const_30 = Integer(30); _sage_const_19 = Integer(19); _sage_const_18 = Integer(18); _sage_const_35 = Integer(35); _sage_const_34 = Integer(34); _sage_const_37 = Integer(37); _sage_const_36 = Integer(36); _sage_const_109 = Integer(109); _sage_const_70 = Integer(70); _sage_const_38 = Integer(38); _sage_const_91 = Integer(91); _sage_const_104 = Integer(104); _sage_const_78 = Integer(78); _sage_const_94 = Integer(94); _sage_const_10 = Integer(10)## This file (solvingLogs-Practice1.sagetex.sage) was *autogenerated* from solvingLogs-Practice1.tex with sagetex.sty version 2015/08/26 v3.0-92d9f7a.
import sagetex
_st_ = sagetex.SageTeXProcessor('solvingLogs-Practice1', version='2015/08/26 v3.0-92d9f7a', version_check=True)
_st_.current_tex_line = _sage_const_1 
_st_.blockbegin()
try:
 
 ######  Define a function to convert a sage number into a saved counter number.
 
 #####Define default Sage variables.
 #Default function variables
 var('x,y,z,X,Y,Z')
 #Default function names
 var('f,g,h,dx,dy,dz,dh,df')
 #Default Wild cards
 w0 = SR.wild(_sage_const_0 )
 
 def higherRoot(rootVal,rootArg):
     # Note that this returns a String version of the latex higher root in root form, rather than exponential form.
     rootString = LatexExpr(r'\sqrt[' + rootVal.str() + ']{' + rootArg.str() +'}')
     return rootString
 
 
 def DispSign(b):
     """ Returns the string of the 'signed' version of `b`, e.g. 3 -> "+3", -3 -> "-3", 0 -> "".
     """
     if b == _sage_const_0 :
         return ""
     elif b > _sage_const_0 :
         return "+" + str(b)
     elif b < _sage_const_0 :
         return str(b)
     else:
         # If we're here, then something has gone wrong.
         raise ValueError
 
 def ISP(b):
     return DispSign(b)
 
 def NoEval(f, c):
     # TODO
     """ Returns a non-evaluted version of the result f(c).
     """
     cStr = str(c)
     # fLatex = latex(f)
     fString = latex(f)
     fStrList = list(fString)
     length = len(fStrList)
     fStrList2 = range(length)
     for i in range(_sage_const_0 , length):
         if fStrList[i] == "x":
             fStrList2[i] = "("+cstr+")"
         else:
             fStrList2[i] = fStrList[i]
     f2 = join(fStrList2,"")
     return LatexExpr(f2)
 
 def HyperSimp(f):
     """ Returns the expression `f` without hyperbolic expressions.
     """
     subsDict = {
         sinh(w0) : (exp(w0) - exp(-w0))/_sage_const_2 ,
         cosh(w0) : (exp(w0) + exp(-w0))/_sage_const_2 ,
         tanh(w0) : (exp(w0) - exp(-w0))/(exp(w0) + exp(-w0)),
         sech(w0) : _sage_const_2 /(exp(w0) + exp(-w0)),                      # This seems to work, but Nowell said it didn't at one point.
         csch(w0) : _sage_const_2 /(exp(w0) - exp(-w0)),                      # This seems to work, but Nowell said it didn't at one point.
         coth(w0) : (exp(w0) + exp(-w0))/(exp(w0) - exp(-w0)),   # This seems to work, but Nowell said it didn't at one point.
         arcsinh(w0) :       ln( w0 + sqrt((w0)**_sage_const_2  + _sage_const_1 ) ),
         arccosh(w0) :       ln( w0 + sqrt((w0)**_sage_const_2  - _sage_const_1 ) ),
         arctanh(w0) : _sage_const_1 /_sage_const_2  * ln( (_sage_const_1  + w0) / (_sage_const_1  - w0) ),
         arccsch(w0) :       ln( (_sage_const_1  + sqrt((w0)**_sage_const_2  + _sage_const_1 ))/w0 ),
         arcsech(w0) :       ln( (_sage_const_1  + sqrt(_sage_const_1  - (w0)**_sage_const_2 ))/w0 ),
         arccoth(w0) : _sage_const_1 /_sage_const_2  * ln( (_sage_const_1  + w0) / (w0 - _sage_const_1 ) )
     }
     g = f.substitute(subsDict)
     return simplify(g)
 
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
 
 def RandVector(b, c, avoid=[], rep=_sage_const_1 ):
     """ Returns essentially a multiset permutation of ([b,c]-av) * rep.
         That is, a vector which contains each integer in [`b`,`c`] which is not in `av` a total of `rep` number of times.
         Example:
         sage: RandVector(1,3, [2], 2)
         [3, 1, 1, 3]
     """
     oneVec = [val for val in range(b,c+_sage_const_1 ) if val not in avoid]
     vec = oneVec * rep
     shuffle(vec)
     return vec
 
 
 def fudge(b):
     up = b+RandInt(_sage_const_2 ,_sage_const_5 )/_sage_const_10 
     down = b-RandInt(_sage_const_2 ,_sage_const_5 )/_sage_const_10 
     fudgebup = round(up,_sage_const_1 )
     fudgebdown = round(down,_sage_const_1 )
     fudgedb = [fudgebdown,fudgebup]
     return fudgedb
 
 def disjointCheck(checkvec):
     if len(uniq(checkvec)) < len(checkvec):
         return _sage_const_1 
     else:
         return _sage_const_0 
 
 def disjointIntervals(IntStart,IntEnd,CheckVal):
     if IntStart < CheckVal and CheckVal < IntEnd:
         return _sage_const_1 
     else:
         return _sage_const_0 
 
 def IntervalVecCheck(checkVec):
     veclen = len(checkVec)
     returnval = _sage_const_0 
     for i in range(veclen):
         for j in range(veclen):
             if (disjointIntervals(checkVec[j][_sage_const_0 ],checkVec[j][_sage_const_1 ],checkVec[i][_sage_const_0 ]) + disjointIntervals(checkVec[j][_sage_const_0 ],checkVec[j][_sage_const_1 ],checkVec[i][_sage_const_1 ])) > _sage_const_0 :
                 returnval = returnval + _sage_const_1 
     if returnval > _sage_const_0 :
         return _sage_const_1 
     else:
         return _sage_const_0 
 
 
 
 
except:
 _st_.goboom(_sage_const_136 )
_st_.blockend()
_st_.current_tex_line = _sage_const_9 
_st_.blockbegin()
try:
 
 ###### Problem p1
 p1b1 = RandInt(_sage_const_2 ,_sage_const_7 )
 
 p1c1 = NonZeroInt(-_sage_const_5 ,_sage_const_5 )
 p1c2 = RandInt(-_sage_const_5 ,_sage_const_5 )
 p1c3 = RandInt(-_sage_const_5 ,_sage_const_5 )
 
 p1f1 = p1c1*x + p1c2
 
 p1ans1 = (p1b1**p1c3-p1c2)/p1c1
 
 
 ###### Problem p2
 p2b1 = RandInt(_sage_const_2 ,_sage_const_7 )
 
 p2c1 = NonZeroInt(-_sage_const_5 ,_sage_const_5 )
 p2c2 = RandInt(-_sage_const_5 ,_sage_const_5 )
 p2c3 = RandInt(-_sage_const_5 ,_sage_const_5 )
 
 p2f1 = p2c1*x + p2c2
 
 p2ans1 = (p2b1**p2c3-p2c2)/p2c1
 
 
 ###### Problem p3
 p3b1 = RandInt(_sage_const_2 ,_sage_const_7 )
 
 p3c1 = NonZeroInt(-_sage_const_5 ,_sage_const_5 )
 p3c2 = RandInt(-_sage_const_5 ,_sage_const_5 )
 p3c3 = RandInt(-_sage_const_5 ,_sage_const_5 )
 
 p3f1 = p3c1*x + p3c2
 
 p3ans1 = (p3b1**p3c3-p3c2)/p3c1
 
 
 ###### Problem p4
 p4b1 = RandInt(_sage_const_2 ,_sage_const_7 )
 
 p4c1 = NonZeroInt(-_sage_const_5 ,_sage_const_5 )
 p4c2 = RandInt(-_sage_const_5 ,_sage_const_5 )
 p4c3 = RandInt(-_sage_const_5 ,_sage_const_5 )
 
 p4f1 = p4c1*x + p4c2
 
 p4ans1 = (p4b1**p4c3-p4c2)/p4c1
 
 
 
except:
 _st_.goboom(_sage_const_60 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_65 
 _st_.inline(_sage_const_0 , latex(p1b1))
except:
 _st_.goboom(_sage_const_65 )
try:
 _st_.current_tex_line = _sage_const_65 
 _st_.inline(_sage_const_1 , latex(p1f1))
except:
 _st_.goboom(_sage_const_65 )
try:
 _st_.current_tex_line = _sage_const_65 
 _st_.inline(_sage_const_2 , latex(p1c3))
except:
 _st_.goboom(_sage_const_65 )
try:
 _st_.current_tex_line = _sage_const_68 
 _st_.inline(_sage_const_3 , latex(p1ans1))
except:
 _st_.goboom(_sage_const_68 )
try:
 _st_.current_tex_line = _sage_const_70 
 _st_.inline(_sage_const_4 , latex(p1b1))
except:
 _st_.goboom(_sage_const_70 )
try:
 _st_.current_tex_line = _sage_const_70 
 _st_.inline(_sage_const_5 , latex(p1f1))
except:
 _st_.goboom(_sage_const_70 )
try:
 _st_.current_tex_line = _sage_const_70 
 _st_.inline(_sage_const_6 , latex(p1c3))
except:
 _st_.goboom(_sage_const_70 )
try:
 _st_.current_tex_line = _sage_const_70 
 _st_.inline(_sage_const_7 , latex(p1f1))
except:
 _st_.goboom(_sage_const_70 )
try:
 _st_.current_tex_line = _sage_const_70 
 _st_.inline(_sage_const_8 , latex(p1b1))
except:
 _st_.goboom(_sage_const_70 )
try:
 _st_.current_tex_line = _sage_const_70 
 _st_.inline(_sage_const_9 , latex(p1c3))
except:
 _st_.goboom(_sage_const_70 )
try:
 _st_.current_tex_line = _sage_const_78 
 _st_.inline(_sage_const_10 , latex(p2b1))
except:
 _st_.goboom(_sage_const_78 )
try:
 _st_.current_tex_line = _sage_const_78 
 _st_.inline(_sage_const_11 , latex(p2f1))
except:
 _st_.goboom(_sage_const_78 )
try:
 _st_.current_tex_line = _sage_const_78 
 _st_.inline(_sage_const_12 , latex(p2c3))
except:
 _st_.goboom(_sage_const_78 )
try:
 _st_.current_tex_line = _sage_const_81 
 _st_.inline(_sage_const_13 , latex(p2ans1))
except:
 _st_.goboom(_sage_const_81 )
try:
 _st_.current_tex_line = _sage_const_83 
 _st_.inline(_sage_const_14 , latex(p2b1))
except:
 _st_.goboom(_sage_const_83 )
try:
 _st_.current_tex_line = _sage_const_83 
 _st_.inline(_sage_const_15 , latex(p2f1))
except:
 _st_.goboom(_sage_const_83 )
try:
 _st_.current_tex_line = _sage_const_83 
 _st_.inline(_sage_const_16 , latex(p2c3))
except:
 _st_.goboom(_sage_const_83 )
try:
 _st_.current_tex_line = _sage_const_83 
 _st_.inline(_sage_const_17 , latex(p2f1))
except:
 _st_.goboom(_sage_const_83 )
try:
 _st_.current_tex_line = _sage_const_83 
 _st_.inline(_sage_const_18 , latex(p2b1))
except:
 _st_.goboom(_sage_const_83 )
try:
 _st_.current_tex_line = _sage_const_83 
 _st_.inline(_sage_const_19 , latex(p2c3))
except:
 _st_.goboom(_sage_const_83 )
try:
 _st_.current_tex_line = _sage_const_91 
 _st_.inline(_sage_const_20 , latex(p3b1))
except:
 _st_.goboom(_sage_const_91 )
try:
 _st_.current_tex_line = _sage_const_91 
 _st_.inline(_sage_const_21 , latex(p3f1))
except:
 _st_.goboom(_sage_const_91 )
try:
 _st_.current_tex_line = _sage_const_91 
 _st_.inline(_sage_const_22 , latex(p3c3))
except:
 _st_.goboom(_sage_const_91 )
try:
 _st_.current_tex_line = _sage_const_94 
 _st_.inline(_sage_const_23 , latex(p3ans1))
except:
 _st_.goboom(_sage_const_94 )
try:
 _st_.current_tex_line = _sage_const_96 
 _st_.inline(_sage_const_24 , latex(p3b1))
except:
 _st_.goboom(_sage_const_96 )
try:
 _st_.current_tex_line = _sage_const_96 
 _st_.inline(_sage_const_25 , latex(p3f1))
except:
 _st_.goboom(_sage_const_96 )
try:
 _st_.current_tex_line = _sage_const_96 
 _st_.inline(_sage_const_26 , latex(p3c3))
except:
 _st_.goboom(_sage_const_96 )
try:
 _st_.current_tex_line = _sage_const_96 
 _st_.inline(_sage_const_27 , latex(p3f1))
except:
 _st_.goboom(_sage_const_96 )
try:
 _st_.current_tex_line = _sage_const_96 
 _st_.inline(_sage_const_28 , latex(p3b1))
except:
 _st_.goboom(_sage_const_96 )
try:
 _st_.current_tex_line = _sage_const_96 
 _st_.inline(_sage_const_29 , latex(p3c3))
except:
 _st_.goboom(_sage_const_96 )
try:
 _st_.current_tex_line = _sage_const_104 
 _st_.inline(_sage_const_30 , latex(p4b1))
except:
 _st_.goboom(_sage_const_104 )
try:
 _st_.current_tex_line = _sage_const_104 
 _st_.inline(_sage_const_31 , latex(p4f1))
except:
 _st_.goboom(_sage_const_104 )
try:
 _st_.current_tex_line = _sage_const_104 
 _st_.inline(_sage_const_32 , latex(p4c3))
except:
 _st_.goboom(_sage_const_104 )
try:
 _st_.current_tex_line = _sage_const_107 
 _st_.inline(_sage_const_33 , latex(p4ans1))
except:
 _st_.goboom(_sage_const_107 )
try:
 _st_.current_tex_line = _sage_const_109 
 _st_.inline(_sage_const_34 , latex(p4b1))
except:
 _st_.goboom(_sage_const_109 )
try:
 _st_.current_tex_line = _sage_const_109 
 _st_.inline(_sage_const_35 , latex(p4f1))
except:
 _st_.goboom(_sage_const_109 )
try:
 _st_.current_tex_line = _sage_const_109 
 _st_.inline(_sage_const_36 , latex(p4c3))
except:
 _st_.goboom(_sage_const_109 )
try:
 _st_.current_tex_line = _sage_const_109 
 _st_.inline(_sage_const_37 , latex(p4f1))
except:
 _st_.goboom(_sage_const_109 )
try:
 _st_.current_tex_line = _sage_const_109 
 _st_.inline(_sage_const_38 , latex(p4b1))
except:
 _st_.goboom(_sage_const_109 )
try:
 _st_.current_tex_line = _sage_const_109 
 _st_.inline(_sage_const_39 , latex(p4c3))
except:
 _st_.goboom(_sage_const_109 )
_st_.endofdoc()

