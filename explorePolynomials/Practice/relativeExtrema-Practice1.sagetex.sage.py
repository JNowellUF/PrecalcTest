## -*- encoding: utf-8 -*-

# This file was *autogenerated* from the file relativeExtrema-Practice1.sagetex.sage
from sage.all_cmdline import *   # import sage library

_sage_const_3 = Integer(3); _sage_const_2 = Integer(2); _sage_const_1 = Integer(1); _sage_const_0 = Integer(0); _sage_const_7 = Integer(7); _sage_const_6 = Integer(6); _sage_const_5 = Integer(5); _sage_const_4 = Integer(4); _sage_const_9 = Integer(9); _sage_const_8 = Integer(8); _sage_const_182 = Integer(182); _sage_const_20 = Integer(20); _sage_const_136 = Integer(136); _sage_const_46 = Integer(46); _sage_const_132 = Integer(132); _sage_const_117 = Integer(117); _sage_const_157 = Integer(157); _sage_const_170 = Integer(170); _sage_const_175 = Integer(175); _sage_const_150 = Integer(150); _sage_const_13 = Integer(13); _sage_const_12 = Integer(12); _sage_const_11 = Integer(11); _sage_const_10 = Integer(10); _sage_const_17 = Integer(17); _sage_const_16 = Integer(16); _sage_const_15 = Integer(15); _sage_const_14 = Integer(14); _sage_const_19 = Integer(19); _sage_const_18 = Integer(18); _sage_const_120 = Integer(120); _sage_const_125 = Integer(125); _sage_const_145 = Integer(145)## This file (relativeExtrema-Practice1.sagetex.sage) was *autogenerated* from relativeExtrema-Practice1.tex with sagetex.sty version 2015/08/26 v3.0-92d9f7a.
import sagetex
_st_ = sagetex.SageTeXProcessor('relativeExtrema-Practice1', version='2015/08/26 v3.0-92d9f7a', version_check=True)
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
_st_.current_tex_line = _sage_const_46 
_st_.blockbegin()
try:
 
 #### Problem p1
 p1c1 = NonZeroInt(-_sage_const_10 ,_sage_const_10 )
 p1c2 = NonZeroInt(-_sage_const_10 ,_sage_const_10 ,[_sage_const_0 ,p1c1])
 p1c3 = NonZeroInt(-_sage_const_10 ,_sage_const_10 ,[_sage_const_0 ,p1c1,p1c2])
 p1c4 = NonZeroInt(-_sage_const_10 ,_sage_const_10 ,[_sage_const_0 ,p1c1,p1c2,p1c3])
 
 p1pwr1 = RandInt(_sage_const_1 ,_sage_const_20 )
 p1pwr2 = RandInt(_sage_const_1 ,_sage_const_20 )
 p1pwr3 = RandInt(_sage_const_1 ,_sage_const_20 )
 p1pwr4 = RandInt(_sage_const_1 ,_sage_const_20 )
 
 p1f1 = p1c1*x**p1pwr1
 p1f2 = p1c2*x**p1pwr2
 p1f3 = p1c3*x**p1pwr3
 p1f4 = p1c4*x**p1pwr4
 
 p1temp1 = max(p1pwr1,p1pwr2,p1pwr3,p1pwr4)
 p1ans1 = p1temp1 - _sage_const_1 
 
 p1ans2 = p1ans1%_sage_const_2 
 
 
 #### Problem p2
 p2c1 = NonZeroInt(-_sage_const_10 ,_sage_const_10 )
 p2c2 = NonZeroInt(-_sage_const_10 ,_sage_const_10 ,[_sage_const_0 ,p2c1])
 p2c3 = NonZeroInt(-_sage_const_10 ,_sage_const_10 ,[_sage_const_0 ,p2c1,p2c2])
 p2c4 = NonZeroInt(-_sage_const_10 ,_sage_const_10 ,[_sage_const_0 ,p2c1,p2c2,p2c3])
 
 p2pwr1 = RandInt(_sage_const_1 ,_sage_const_20 )
 p2pwr2 = RandInt(_sage_const_1 ,_sage_const_20 )
 p2pwr3 = RandInt(_sage_const_1 ,_sage_const_20 )
 p2pwr4 = RandInt(_sage_const_1 ,_sage_const_20 )
 
 p2f1 = p2c1*x**p2pwr1
 p2f2 = p2c2*x**p2pwr2
 p2f3 = p2c3*x**p2pwr3
 p2f4 = p2c4*x**p2pwr4
 
 p2temp2 = max(p2pwr1,p2pwr2,p2pwr3,p2pwr4)
 p2ans1 = p2temp2 - _sage_const_1 
 
 p2ans2 = p2ans1%_sage_const_2 
 
 
 #### Problem p3
 p3c1 = NonZeroInt(-_sage_const_10 ,_sage_const_10 )
 p3c2 = NonZeroInt(-_sage_const_10 ,_sage_const_10 ,[_sage_const_0 ,p3c1])
 p3c3 = NonZeroInt(-_sage_const_10 ,_sage_const_10 ,[_sage_const_0 ,p3c1,p3c2])
 p3c4 = NonZeroInt(-_sage_const_10 ,_sage_const_10 ,[_sage_const_0 ,p3c1,p3c2,p3c3])
 
 p3pwr1 = RandInt(_sage_const_1 ,_sage_const_20 )
 p3pwr2 = RandInt(_sage_const_1 ,_sage_const_20 )
 p3pwr3 = RandInt(_sage_const_1 ,_sage_const_20 )
 p3pwr4 = RandInt(_sage_const_1 ,_sage_const_20 )
 
 p3f1 = p3c1*x**p3pwr1
 p3f2 = p3c2*x**p3pwr2
 p3f3 = p3c3*x**p3pwr3
 p3f4 = p3c4*x**p3pwr4
 
 p3temp3 = max(p3pwr1,p3pwr2,p3pwr3,p3pwr4)
 p3ans1 = p3temp3 - _sage_const_1 
 
 p3ans2 = p3ans1%_sage_const_2 
 
 
 
 
 
except:
 _st_.goboom(_sage_const_117 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_120 
 _st_.inline(_sage_const_0 , latex(p1f1))
except:
 _st_.goboom(_sage_const_120 )
try:
 _st_.current_tex_line = _sage_const_120 
 _st_.inline(_sage_const_1 , latex(p1f2))
except:
 _st_.goboom(_sage_const_120 )
try:
 _st_.current_tex_line = _sage_const_120 
 _st_.inline(_sage_const_2 , latex(p1f3))
except:
 _st_.goboom(_sage_const_120 )
try:
 _st_.current_tex_line = _sage_const_120 
 _st_.inline(_sage_const_3 , latex(p1f4))
except:
 _st_.goboom(_sage_const_120 )
try:
 _st_.current_tex_line = _sage_const_120 
 _st_.inline(_sage_const_4 , latex(p1ans1))
except:
 _st_.goboom(_sage_const_120 )
try:
 _st_.current_tex_line = _sage_const_125 
 _st_.inline(_sage_const_5 , latex(p1ans2))
except:
 _st_.goboom(_sage_const_125 )
try:
 _st_.current_tex_line = _sage_const_132 
 _st_.inline(_sage_const_6 , latex(p1ans1))
except:
 _st_.goboom(_sage_const_132 )
try:
 _st_.current_tex_line = _sage_const_145 
 _st_.inline(_sage_const_7 , latex(p2f1))
except:
 _st_.goboom(_sage_const_145 )
try:
 _st_.current_tex_line = _sage_const_145 
 _st_.inline(_sage_const_8 , latex(p2f2))
except:
 _st_.goboom(_sage_const_145 )
try:
 _st_.current_tex_line = _sage_const_145 
 _st_.inline(_sage_const_9 , latex(p2f3))
except:
 _st_.goboom(_sage_const_145 )
try:
 _st_.current_tex_line = _sage_const_145 
 _st_.inline(_sage_const_10 , latex(p2f4))
except:
 _st_.goboom(_sage_const_145 )
try:
 _st_.current_tex_line = _sage_const_145 
 _st_.inline(_sage_const_11 , latex(p2ans1))
except:
 _st_.goboom(_sage_const_145 )
try:
 _st_.current_tex_line = _sage_const_150 
 _st_.inline(_sage_const_12 , latex(p2ans2))
except:
 _st_.goboom(_sage_const_150 )
try:
 _st_.current_tex_line = _sage_const_157 
 _st_.inline(_sage_const_13 , latex(p2ans1))
except:
 _st_.goboom(_sage_const_157 )
try:
 _st_.current_tex_line = _sage_const_170 
 _st_.inline(_sage_const_14 , latex(p3f1))
except:
 _st_.goboom(_sage_const_170 )
try:
 _st_.current_tex_line = _sage_const_170 
 _st_.inline(_sage_const_15 , latex(p3f2))
except:
 _st_.goboom(_sage_const_170 )
try:
 _st_.current_tex_line = _sage_const_170 
 _st_.inline(_sage_const_16 , latex(p3f3))
except:
 _st_.goboom(_sage_const_170 )
try:
 _st_.current_tex_line = _sage_const_170 
 _st_.inline(_sage_const_17 , latex(p3f4))
except:
 _st_.goboom(_sage_const_170 )
try:
 _st_.current_tex_line = _sage_const_170 
 _st_.inline(_sage_const_18 , latex(p3ans1))
except:
 _st_.goboom(_sage_const_170 )
try:
 _st_.current_tex_line = _sage_const_175 
 _st_.inline(_sage_const_19 , latex(p3ans2))
except:
 _st_.goboom(_sage_const_175 )
try:
 _st_.current_tex_line = _sage_const_182 
 _st_.inline(_sage_const_20 , latex(p3ans1))
except:
 _st_.goboom(_sage_const_182 )
_st_.endofdoc()
