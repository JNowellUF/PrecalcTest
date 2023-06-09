## -*- encoding: utf-8 -*-

# This file was *autogenerated* from the file polyTest-Practice1.sagetex.sage
from sage.all_cmdline import *   # import sage library

_sage_const_3 = Integer(3); _sage_const_2 = Integer(2); _sage_const_1 = Integer(1); _sage_const_0 = Integer(0); _sage_const_130 = Integer(130); _sage_const_5 = Integer(5); _sage_const_4 = Integer(4); _sage_const_9 = Integer(9); _sage_const_147 = Integer(147); _sage_const_136 = Integer(136); _sage_const_140 = Integer(140); _sage_const_10 = Integer(10); _sage_const_133 = Integer(133)## This file (polyTest-Practice1.sagetex.sage) was *autogenerated* from polyTest-Practice1.tex with sagetex.sty version 2015/08/26 v3.0-92d9f7a.
import sagetex
_st_ = sagetex.SageTeXProcessor('polyTest-Practice1', version='2015/08/26 v3.0-92d9f7a', version_check=True)
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
 funcvec = [x, x**_sage_const_2 , x**_sage_const_3 , x**_sage_const_4 , x**_sage_const_5 , sqrt(x),e**x, _sage_const_1 /x, _sage_const_1 /x**_sage_const_2 , log(x)]
 
 ###### Problem p1
 p1pick1 = RandInt(_sage_const_0 ,_sage_const_9 )
 p1pick2 = NonZeroInt(_sage_const_0 ,_sage_const_9 ,[p1pick1])
 p1pick3 = NonZeroInt(_sage_const_0 ,_sage_const_9 ,[p1pick1,p1pick2])
 
 p1c1 = NonZeroInt(-_sage_const_5 ,_sage_const_5 )
 p1c2 = NonZeroInt(-_sage_const_5 ,_sage_const_5 )
 p1c3 = NonZeroInt(-_sage_const_5 ,_sage_const_5 )
 
 p1c4 = RandInt(-_sage_const_10 ,_sage_const_10 )
 p1c5 = RandInt(-_sage_const_10 ,_sage_const_10 )
 p1c6 = RandInt(-_sage_const_10 ,_sage_const_10 )
 
 p1ans1 = _sage_const_0 
 p1ans1t = _sage_const_0 
 p1ans2t = _sage_const_0 
 p1ans3t = _sage_const_0 
 
 p1f1t = funcvec[p1pick1]
 p1f2t = funcvec[p1pick2]
 p1f3t = funcvec[p1pick3]
 
 p1f1 = p1c1*p1f1t + p1c4
 p1f2 = p1c2*p1f2t + p1c5
 p1f3 = p1c3*p1f3t + p1c6
 
 p1f4 = p1f1 + p1f2 + p1f3
 
 if p1pick1 > _sage_const_4 :
     p1ans1t = _sage_const_1 
 if p1pick2 > _sage_const_4 :
     p1ans2t = _sage_const_1 
 if p1pick3 > _sage_const_4 :
     p1ans3t = _sage_const_1 
 
 p1ans1 = p1ans1t + p1ans2t + p1ans3t
 
 
 
 ###### Problem p2
 p2pick1 = RandInt(_sage_const_0 ,_sage_const_9 )
 p2pick2 = NonZeroInt(_sage_const_0 ,_sage_const_9 ,[p2pick1])
 p2pick3 = NonZeroInt(_sage_const_0 ,_sage_const_9 ,[p2pick1,p2pick2])
 
 p2c1 = NonZeroInt(-_sage_const_5 ,_sage_const_5 )
 p2c2 = NonZeroInt(-_sage_const_5 ,_sage_const_5 )
 p2c3 = NonZeroInt(-_sage_const_5 ,_sage_const_5 )
 
 p2c4 = RandInt(-_sage_const_10 ,_sage_const_10 )
 p2c5 = RandInt(-_sage_const_10 ,_sage_const_10 )
 p2c6 = RandInt(-_sage_const_10 ,_sage_const_10 )
 
 p2ans1 = _sage_const_0 
 p2ans1t = _sage_const_0 
 p2ans2t = _sage_const_0 
 p2ans3t = _sage_const_0 
 
 p2f1t = funcvec[p2pick1]
 p2f2t = funcvec[p2pick2]
 p2f3t = funcvec[p2pick3]
 
 p2f1 = p2c1*p2f1t + p2c4
 p2f2 = p2c2*p2f2t + p2c5
 p2f3 = p2c3*p2f3t + p2c6
 
 p2f4 = p2f1 + p2f2 + p2f3
 
 if p2pick1 > _sage_const_4 :
     p2ans1t = _sage_const_1 
 if p2pick2 > _sage_const_4 :
     p2ans2t = _sage_const_1 
 if p2pick3 > _sage_const_4 :
     p2ans3t = _sage_const_1 
 
 p2ans1 = p2ans1t + p2ans2t + p2ans3t
 
 
 
 
 ###### Problem p3
 p3pick1 = RandInt(_sage_const_0 ,_sage_const_9 )
 p3pick2 = NonZeroInt(_sage_const_0 ,_sage_const_9 ,[p3pick1])
 p3pick3 = NonZeroInt(_sage_const_0 ,_sage_const_9 ,[p3pick1,p3pick2])
 
 p3c1 = NonZeroInt(-_sage_const_5 ,_sage_const_5 )
 p3c2 = NonZeroInt(-_sage_const_5 ,_sage_const_5 )
 p3c3 = NonZeroInt(-_sage_const_5 ,_sage_const_5 )
 
 p3c4 = RandInt(-_sage_const_10 ,_sage_const_10 )
 p3c5 = RandInt(-_sage_const_10 ,_sage_const_10 )
 p3c6 = RandInt(-_sage_const_10 ,_sage_const_10 )
 
 p3ans1 = _sage_const_0 
 p3ans1t = _sage_const_0 
 p3ans2t = _sage_const_0 
 p3ans3t = _sage_const_0 
 
 p3f1t = funcvec[p3pick1]
 p3f2t = funcvec[p3pick2]
 p3f3t = funcvec[p3pick3]
 
 p3f1 = p3c1*p3f1t + p3c4
 p3f2 = p3c2*p3f2t + p3c5
 p3f3 = p3c3*p3f3t + p3c6
 
 p3f4 = p3f1 + p3f2 + p3f3
 
 if p3pick1 > _sage_const_4 :
     p3ans1t = _sage_const_1 
 if p3pick2 > _sage_const_4 :
     p3ans2t = _sage_const_1 
 if p3pick3 > _sage_const_4 :
     p3ans3t = _sage_const_1 
 
 p3ans1 = p3ans1t + p3ans2t + p3ans3t
 
 
 
except:
 _st_.goboom(_sage_const_130 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_133 
 _st_.inline(_sage_const_0 , latex(p1f4))
except:
 _st_.goboom(_sage_const_133 )
try:
 _st_.current_tex_line = _sage_const_133 
 _st_.inline(_sage_const_1 , latex(p1ans1))
except:
 _st_.goboom(_sage_const_133 )
try:
 _st_.current_tex_line = _sage_const_140 
 _st_.inline(_sage_const_2 , latex(p2f4))
except:
 _st_.goboom(_sage_const_140 )
try:
 _st_.current_tex_line = _sage_const_140 
 _st_.inline(_sage_const_3 , latex(p2ans1))
except:
 _st_.goboom(_sage_const_140 )
try:
 _st_.current_tex_line = _sage_const_147 
 _st_.inline(_sage_const_4 , latex(p3f4))
except:
 _st_.goboom(_sage_const_147 )
try:
 _st_.current_tex_line = _sage_const_147 
 _st_.inline(_sage_const_5 , latex(p3ans1))
except:
 _st_.goboom(_sage_const_147 )
_st_.endofdoc()

