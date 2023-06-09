## -*- encoding: utf-8 -*-
## This file (absoluteValueAnalyticViewpoint-Practice1.sagetex.sage) was *autogenerated* from absoluteValueAnalyticViewpoint-Practice1.tex with sagetex.sty version 2015/08/26 v3.0-92d9f7a.
import sagetex
_st_ = sagetex.SageTeXProcessor('absoluteValueAnalyticViewpoint-Practice1', version='2015/08/26 v3.0-92d9f7a', version_check=True)
_st_.current_tex_line = 1
_st_.blockbegin()
try:
 
 ######  Define a function to convert a sage number into a saved counter number.
 
 #####Define default Sage variables.
 #Default function variables
 var('x,y,z,X,Y,Z')
 #Default function names
 var('f,g,h,dx,dy,dz,dh,df')
 #Default Wild cards
 w0 = SR.wild(0)
 
 def higherRoot(rootVal,rootArg):
     # Note that this returns a String version of the latex higher root in root form, rather than exponential form.
     rootString = LatexExpr(r'\sqrt[' + rootVal.str() + ']{' + rootArg.str() +'}')
     return rootString
 
 
 def DispSign(b):
     """ Returns the string of the 'signed' version of `b`, e.g. 3 -> "+3", -3 -> "-3", 0 -> "".
     """
     if b == 0:
         return ""
     elif b > 0:
         return "+" + str(b)
     elif b < 0:
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
     for i in range(0, length):
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
         sinh(w0) : (exp(w0) - exp(-w0))/2,
         cosh(w0) : (exp(w0) + exp(-w0))/2,
         tanh(w0) : (exp(w0) - exp(-w0))/(exp(w0) + exp(-w0)),
         sech(w0) : 2/(exp(w0) + exp(-w0)),                      # This seems to work, but Nowell said it didn't at one point.
         csch(w0) : 2/(exp(w0) - exp(-w0)),                      # This seems to work, but Nowell said it didn't at one point.
         coth(w0) : (exp(w0) + exp(-w0))/(exp(w0) - exp(-w0)),   # This seems to work, but Nowell said it didn't at one point.
         arcsinh(w0) :       ln( w0 + sqrt((w0)^2 + 1) ),
         arccosh(w0) :       ln( w0 + sqrt((w0)^2 - 1) ),
         arctanh(w0) : 1/2 * ln( (1 + w0) / (1 - w0) ),
         arccsch(w0) :       ln( (1 + sqrt((w0)^2 + 1))/w0 ),
         arcsech(w0) :       ln( (1 + sqrt(1 - (w0)^2))/w0 ),
         arccoth(w0) : 1/2 * ln( (1 + w0) / (w0 - 1) )
     }
     g = f.substitute(subsDict)
     return simplify(g)
 
 def RandInt(a,b):
     """ Returns a random integer in [`a`,`b`]. Note that `a` and `b` should be integers themselves to avoid unexpected behavior.
     """
     return QQ(randint(int(a),int(b)))
     # return choice(range(a,b+1))
 
 def NonZeroInt(b,c, avoid = [0]):
     """ Returns a random integer in [`b`,`c`] which is not in `av`.
         If `av` is not specified, defaults to a non-zero integer.
     """
     while True:
         a = RandInt(b,c)
         if a not in avoid:
             return a
 
 def RandVector(b, c, avoid=[], rep=1):
     """ Returns essentially a multiset permutation of ([b,c]-av) * rep.
         That is, a vector which contains each integer in [`b`,`c`] which is not in `av` a total of `rep` number of times.
         Example:
         sage: RandVector(1,3, [2], 2)
         [3, 1, 1, 3]
     """
     oneVec = [val for val in range(b,c+1) if val not in avoid]
     vec = oneVec * rep
     shuffle(vec)
     return vec
 
 
 def fudge(b):
     up = b+RandInt(2,5)/10
     down = b-RandInt(2,5)/10
     fudgebup = round(up,1)
     fudgebdown = round(down,1)
     fudgedb = [fudgebdown,fudgebup]
     return fudgedb
 
 def disjointCheck(checkvec):
     if len(uniq(checkvec)) < len(checkvec):
         return 1
     else:
         return 0
 
 def disjointIntervals(IntStart,IntEnd,CheckVal):
     if IntStart < CheckVal and CheckVal < IntEnd:
         return 1
     else:
         return 0
 
 def IntervalVecCheck(checkVec):
     veclen = len(checkVec)
     returnval = 0
     for i in range(veclen):
         for j in range(veclen):
             if (disjointIntervals(checkVec[j][0],checkVec[j][1],checkVec[i][0]) + disjointIntervals(checkVec[j][0],checkVec[j][1],checkVec[i][1])) > 0:
                 returnval = returnval + 1
     if returnval > 0:
         return 1
     else:
         return 0
 
 
 
 
except:
 _st_.goboom(136)
_st_.blockend()
_st_.current_tex_line = 11
_st_.blockbegin()
try:
 #### Problem p1
 p1c1 = NonZeroInt(-5,5)
 p1c2 = RandInt(-5,5)
 p1c3 = RandInt(-5,5)
 p1c4 = RandInt(-5,5)
 
 p1f1 = p1c1*x - p1c2
 p1f2 = p1c3*x - p1c4
 
 if p1c1 > 0:
     p1ans1 = -p1f1 + p1f2
     p1ans2 = p1f1 + p1f2
 else:
     p1ans1 = p1f1 + p1f2
     p1ans2 = -p1f1 + p1f2
 p1ans3 = p1c2/p1c1
 
 
 #### Problem p2
 p2c1 = NonZeroInt(-5,5)
 p2c2 = RandInt(-5,5)
 p2c3 = RandInt(-5,5)
 p2c4 = RandInt(-5,5)
 
 p2f1 = p2c1*x - p2c2
 p2f2 = p2c3*x - p2c4
 
 if p2c1 > 0:
     p2ans1 = -p2f1 + p2f2
     p2ans2 = p2f1 + p2f2
 else:
     p2ans1 = p2f1 + p2f2
     p2ans2 = -p2f1 + p2f2
 p2ans3 = p2c2/p2c1
 
 
 #### Problem p3
 p3c1 = NonZeroInt(-5,5)
 p3c2 = RandInt(-5,5)
 p3c3 = RandInt(-5,5)
 p3c4 = RandInt(-5,5)
 
 p3f1 = p3c1*x - p3c2
 p3f2 = p3c3*x - p3c4
 
 if p3c1 > 0:
     p3ans1 = -p3f1 + p3f2
     p3ans2 = p3f1 + p3f2
 else:
     p3ans1 = p3f1 + p3f2
     p3ans2 = -p3f1 + p3f2
 p3ans3 = p3c2/p3c1
 
 
 #### Problem p4
 p4c1 = NonZeroInt(-5,5)
 p4c2 = RandInt(-5,5)
 p4c3 = RandInt(-5,5)
 p4c4 = RandInt(-5,5)
 
 p4f1 = p4c1*x - p4c2
 p4f2 = p4c3*x - p4c4
 
 if p4c1 > 0:
     p4ans1 = -p4f1 + p4f2
     p4ans2 = p4f1 + p4f2
 else:
     p4ans1 = p4f1 + p4f2
     p4ans2 = -p4f1 + p4f2
 p4ans3 = p4c2/p4c1
 
 
except:
 _st_.goboom(84)
_st_.blockend()
try:
 _st_.current_tex_line = 89
 _st_.inline(0, latex(p1f1))
except:
 _st_.goboom(89)
try:
 _st_.current_tex_line = 89
 _st_.inline(1, latex(p1f2))
except:
 _st_.goboom(89)
try:
 _st_.current_tex_line = 95
 _st_.inline(2, latex(p1f1))
except:
 _st_.goboom(95)
try:
 _st_.current_tex_line = 95
 _st_.inline(3, latex(p1f2))
except:
 _st_.goboom(95)
try:
 _st_.current_tex_line = 97
 _st_.inline(4, latex(p1ans1))
except:
 _st_.goboom(97)
try:
 _st_.current_tex_line = 97
 _st_.inline(5, latex(p1ans3))
except:
 _st_.goboom(97)
try:
 _st_.current_tex_line = 98
 _st_.inline(6, latex(p1ans2))
except:
 _st_.goboom(98)
try:
 _st_.current_tex_line = 98
 _st_.inline(7, latex(p1ans3))
except:
 _st_.goboom(98)
try:
 _st_.current_tex_line = 102
 _st_.inline(8, latex(p1f1))
except:
 _st_.goboom(102)
try:
 _st_.current_tex_line = 113
 _st_.inline(9, latex(p2f1))
except:
 _st_.goboom(113)
try:
 _st_.current_tex_line = 113
 _st_.inline(10, latex(p2f2))
except:
 _st_.goboom(113)
try:
 _st_.current_tex_line = 119
 _st_.inline(11, latex(p2f1))
except:
 _st_.goboom(119)
try:
 _st_.current_tex_line = 119
 _st_.inline(12, latex(p2f2))
except:
 _st_.goboom(119)
try:
 _st_.current_tex_line = 121
 _st_.inline(13, latex(p2ans1))
except:
 _st_.goboom(121)
try:
 _st_.current_tex_line = 121
 _st_.inline(14, latex(p2ans3))
except:
 _st_.goboom(121)
try:
 _st_.current_tex_line = 122
 _st_.inline(15, latex(p2ans2))
except:
 _st_.goboom(122)
try:
 _st_.current_tex_line = 122
 _st_.inline(16, latex(p2ans3))
except:
 _st_.goboom(122)
try:
 _st_.current_tex_line = 127
 _st_.inline(17, latex(p2f1))
except:
 _st_.goboom(127)
try:
 _st_.current_tex_line = 138
 _st_.inline(18, latex(p3f1))
except:
 _st_.goboom(138)
try:
 _st_.current_tex_line = 138
 _st_.inline(19, latex(p3f2))
except:
 _st_.goboom(138)
try:
 _st_.current_tex_line = 144
 _st_.inline(20, latex(p3f1))
except:
 _st_.goboom(144)
try:
 _st_.current_tex_line = 144
 _st_.inline(21, latex(p3f2))
except:
 _st_.goboom(144)
try:
 _st_.current_tex_line = 146
 _st_.inline(22, latex(p3ans1))
except:
 _st_.goboom(146)
try:
 _st_.current_tex_line = 146
 _st_.inline(23, latex(p3ans3))
except:
 _st_.goboom(146)
try:
 _st_.current_tex_line = 147
 _st_.inline(24, latex(p3ans2))
except:
 _st_.goboom(147)
try:
 _st_.current_tex_line = 147
 _st_.inline(25, latex(p3ans3))
except:
 _st_.goboom(147)
try:
 _st_.current_tex_line = 152
 _st_.inline(26, latex(p3f1))
except:
 _st_.goboom(152)
try:
 _st_.current_tex_line = 163
 _st_.inline(27, latex(p4f1))
except:
 _st_.goboom(163)
try:
 _st_.current_tex_line = 163
 _st_.inline(28, latex(p4f2))
except:
 _st_.goboom(163)
try:
 _st_.current_tex_line = 169
 _st_.inline(29, latex(p4f1))
except:
 _st_.goboom(169)
try:
 _st_.current_tex_line = 169
 _st_.inline(30, latex(p4f2))
except:
 _st_.goboom(169)
try:
 _st_.current_tex_line = 171
 _st_.inline(31, latex(p4ans1))
except:
 _st_.goboom(171)
try:
 _st_.current_tex_line = 171
 _st_.inline(32, latex(p4ans3))
except:
 _st_.goboom(171)
try:
 _st_.current_tex_line = 172
 _st_.inline(33, latex(p4ans2))
except:
 _st_.goboom(172)
try:
 _st_.current_tex_line = 172
 _st_.inline(34, latex(p4ans3))
except:
 _st_.goboom(172)
try:
 _st_.current_tex_line = 177
 _st_.inline(35, latex(p4f1))
except:
 _st_.goboom(177)
_st_.endofdoc()
