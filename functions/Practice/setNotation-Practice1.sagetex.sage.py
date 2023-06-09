## -*- encoding: utf-8 -*-

# This file was *autogenerated* from the file setNotation-Practice1.sagetex.sage
from sage.all_cmdline import *   # import sage library

_sage_const_180 = Integer(180); _sage_const_181 = Integer(181); _sage_const_182 = Integer(182); _sage_const_183 = Integer(183); _sage_const_119 = Integer(119); _sage_const_118 = Integer(118); _sage_const_89 = Integer(89); _sage_const_80 = Integer(80); _sage_const_116 = Integer(116); _sage_const_82 = Integer(82); _sage_const_114 = Integer(114); _sage_const_13 = Integer(13); _sage_const_12 = Integer(12); _sage_const_11 = Integer(11); _sage_const_10 = Integer(10); _sage_const_17 = Integer(17); _sage_const_16 = Integer(16); _sage_const_15 = Integer(15); _sage_const_14 = Integer(14); _sage_const_19 = Integer(19); _sage_const_18 = Integer(18); _sage_const_99 = Integer(99); _sage_const_98 = Integer(98); _sage_const_100 = Integer(100); _sage_const_101 = Integer(101); _sage_const_102 = Integer(102); _sage_const_103 = Integer(103); _sage_const_97 = Integer(97); _sage_const_95 = Integer(95); _sage_const_104 = Integer(104); _sage_const_134 = Integer(134); _sage_const_137 = Integer(137); _sage_const_136 = Integer(136); _sage_const_62 = Integer(62); _sage_const_60 = Integer(60); _sage_const_61 = Integer(61); _sage_const_139 = Integer(139); _sage_const_138 = Integer(138); _sage_const_122 = Integer(122); _sage_const_123 = Integer(123); _sage_const_77 = Integer(77); _sage_const_121 = Integer(121); _sage_const_71 = Integer(71); _sage_const_127 = Integer(127); _sage_const_79 = Integer(79); _sage_const_78 = Integer(78); _sage_const_117 = Integer(117); _sage_const_81 = Integer(81); _sage_const_83 = Integer(83); _sage_const_40 = Integer(40); _sage_const_41 = Integer(41); _sage_const_42 = Integer(42); _sage_const_43 = Integer(43); _sage_const_44 = Integer(44); _sage_const_45 = Integer(45); _sage_const_46 = Integer(46); _sage_const_47 = Integer(47); _sage_const_48 = Integer(48); _sage_const_49 = Integer(49); _sage_const_157 = Integer(157); _sage_const_156 = Integer(156); _sage_const_155 = Integer(155); _sage_const_153 = Integer(153); _sage_const_159 = Integer(159); _sage_const_158 = Integer(158); _sage_const_74 = Integer(74); _sage_const_120 = Integer(120); _sage_const_76 = Integer(76); _sage_const_59 = Integer(59); _sage_const_58 = Integer(58); _sage_const_57 = Integer(57); _sage_const_56 = Integer(56); _sage_const_55 = Integer(55); _sage_const_54 = Integer(54); _sage_const_53 = Integer(53); _sage_const_52 = Integer(52); _sage_const_51 = Integer(51); _sage_const_50 = Integer(50); _sage_const_140 = Integer(140); _sage_const_141 = Integer(141); _sage_const_142 = Integer(142); _sage_const_143 = Integer(143); _sage_const_3 = Integer(3); _sage_const_2 = Integer(2); _sage_const_1 = Integer(1); _sage_const_0 = Integer(0); _sage_const_7 = Integer(7); _sage_const_6 = Integer(6); _sage_const_5 = Integer(5); _sage_const_4 = Integer(4); _sage_const_9 = Integer(9); _sage_const_8 = Integer(8); _sage_const_28 = Integer(28); _sage_const_29 = Integer(29); _sage_const_22 = Integer(22); _sage_const_23 = Integer(23); _sage_const_20 = Integer(20); _sage_const_21 = Integer(21); _sage_const_26 = Integer(26); _sage_const_27 = Integer(27); _sage_const_24 = Integer(24); _sage_const_25 = Integer(25); _sage_const_174 = Integer(174); _sage_const_177 = Integer(177); _sage_const_176 = Integer(176); _sage_const_179 = Integer(179); _sage_const_178 = Integer(178); _sage_const_39 = Integer(39); _sage_const_38 = Integer(38); _sage_const_31 = Integer(31); _sage_const_30 = Integer(30); _sage_const_33 = Integer(33); _sage_const_32 = Integer(32); _sage_const_35 = Integer(35); _sage_const_34 = Integer(34); _sage_const_37 = Integer(37); _sage_const_36 = Integer(36); _sage_const_167 = Integer(167); _sage_const_162 = Integer(162); _sage_const_160 = Integer(160); _sage_const_161 = Integer(161)## This file (setNotation-Practice1.sagetex.sage) was *autogenerated* from setNotation-Practice1.tex with sagetex.sty version 2015/08/26 v3.0-92d9f7a.
import sagetex
_st_ = sagetex.SageTeXProcessor('setNotation-Practice1', version='2015/08/26 v3.0-92d9f7a', version_check=True)
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
_st_.current_tex_line = _sage_const_8 
_st_.blockbegin()
try:
 p1c1 = NonZeroInt(-_sage_const_10 ,_sage_const_10 )
 p1c2 = -p1c1
 
 p2c1 = NonZeroInt(-_sage_const_10 ,_sage_const_10 )
 p2c2 = -p2c1
 p2rvec = [ 'x' + LatexExpr(r"\leq") + str(p1c1), str(x < p1c1), 'x' + LatexExpr(r"\geq") + str(p1c1), str(x > p1c1) ]
 p2vecfalse = [RealSet.open_closed(-infinity,p2c1), RealSet(-infinity, p2c1), RealSet.closed_open(p2c1,infinity), RealSet(p2c1,infinity),RealSet.open_closed(-infinity,-p2c1), RealSet(-infinity, -p2c1), RealSet.closed_open(-p2c1,infinity), RealSet(-p2c1,infinity)]
 p2vecpick = RandInt(_sage_const_0 ,_sage_const_3 )
 p2relate = p2rvec[p2vecpick]
 p2false = [p2vecfalse[i] for i in range(_sage_const_8 ) if abs(i - p2vecpick)>_sage_const_0 ]
 
 p2ans1 = p2false[_sage_const_0 ]
 p2ans2 = p2false[_sage_const_1 ]
 p2ans3 = p2vecfalse[p2vecpick]
 p2ans4 = p2false[_sage_const_2 ]
 p2ans5 = p2false[_sage_const_3 ]
 p2ans6 = p2false[_sage_const_4 ]
 p2ans7 = p2false[_sage_const_5 ]
 p2ans8 = p2false[_sage_const_6 ]
 
 p3c1 = NonZeroInt(-_sage_const_10 ,_sage_const_10 )
 p3c2 = -p3c1
 
 p4c1 = NonZeroInt(-_sage_const_10 ,_sage_const_10 )
 p4c2 = -p4c1
 p4rvec = [ 'x' + LatexExpr(r"\leq") + str(p4c1), str(x < p4c1), 'x' + LatexExpr(r"\geq") + str(p4c1), str(x > p4c1) ]
 p4vecfalse = [RealSet.open_closed(-infinity,p4c1), RealSet(-infinity, p4c1), RealSet.closed_open(p4c1,infinity), RealSet(p4c1,infinity),RealSet.open_closed(-infinity,-p4c1), RealSet(-infinity, -p4c1), RealSet.closed_open(-p4c1,infinity), RealSet(-p4c1,infinity)]
 p4vecpick = RandInt(_sage_const_0 ,_sage_const_3 )
 p4relate = p4rvec[p4vecpick]
 p4false = [p4vecfalse[i] for i in range(_sage_const_8 ) if abs(i - p4vecpick)>_sage_const_0 ]
 
 p4ans1 = p4false[_sage_const_0 ]
 p4ans2 = p4false[_sage_const_1 ]
 p4ans3 = p4vecfalse[p4vecpick]
 p4ans4 = p4false[_sage_const_2 ]
 p4ans5 = p4false[_sage_const_3 ]
 p4ans6 = p4false[_sage_const_4 ]
 p4ans7 = p4false[_sage_const_5 ]
 p4ans8 = p4false[_sage_const_6 ]
 
 p5c1 = NonZeroInt(-_sage_const_10 ,_sage_const_10 )
 p5c2 = -p5c1
 
 p6c1 = NonZeroInt(-_sage_const_10 ,_sage_const_10 )
 p6c2 = -p6c1
 p6rvec = [ 'x' + LatexExpr(r"\leq") + str(p6c1), str(x < p6c1), 'x' + LatexExpr(r"\geq") + str(p6c1), str(x > p6c1) ]
 p6vecfalse = [RealSet.open_closed(-infinity,p6c1), RealSet(-infinity, p6c1), RealSet.closed_open(p6c1,infinity), RealSet(p6c1,infinity),RealSet.open_closed(-infinity,-p6c1), RealSet(-infinity, -p6c1), RealSet.closed_open(-p6c1,infinity), RealSet(-p6c1,infinity)]
 p6vecpick =RandInt(_sage_const_0 ,_sage_const_3 )
 p6relate = p6rvec[p6vecpick]
 p6false = [p6vecfalse[i] for i in range(_sage_const_8 ) if abs(i - p6vecpick)>_sage_const_0 ]
 
 p6ans1 = p6false[_sage_const_0 ]
 p6ans2 = p6false[_sage_const_1 ]
 p6ans3 = p6vecfalse[p6vecpick]
 p6ans4 = p6false[_sage_const_2 ]
 p6ans5 = p6false[_sage_const_3 ]
 p6ans6 = p6false[_sage_const_4 ]
 p6ans7 = p6false[_sage_const_5 ]
 p6ans8 = p6false[_sage_const_6 ]
 
 
 
except:
 _st_.goboom(_sage_const_71 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_74 
 _st_.inline(_sage_const_0 , latex(p1c1))
except:
 _st_.goboom(_sage_const_74 )
try:
 _st_.current_tex_line = _sage_const_76 
 _st_.inline(_sage_const_1 , latex(p1c1))
except:
 _st_.goboom(_sage_const_76 )
try:
 _st_.current_tex_line = _sage_const_77 
 _st_.inline(_sage_const_2 , latex(p1c1))
except:
 _st_.goboom(_sage_const_77 )
try:
 _st_.current_tex_line = _sage_const_78 
 _st_.inline(_sage_const_3 , latex(p1c1))
except:
 _st_.goboom(_sage_const_78 )
try:
 _st_.current_tex_line = _sage_const_79 
 _st_.inline(_sage_const_4 , latex(p1c1))
except:
 _st_.goboom(_sage_const_79 )
try:
 _st_.current_tex_line = _sage_const_80 
 _st_.inline(_sage_const_5 , latex(p1c2))
except:
 _st_.goboom(_sage_const_80 )
try:
 _st_.current_tex_line = _sage_const_81 
 _st_.inline(_sage_const_6 , latex(p1c2))
except:
 _st_.goboom(_sage_const_81 )
try:
 _st_.current_tex_line = _sage_const_82 
 _st_.inline(_sage_const_7 , latex(p1c2))
except:
 _st_.goboom(_sage_const_82 )
try:
 _st_.current_tex_line = _sage_const_83 
 _st_.inline(_sage_const_8 , latex(p1c2))
except:
 _st_.goboom(_sage_const_83 )
try:
 _st_.current_tex_line = _sage_const_89 
 _st_.inline(_sage_const_9 , latex(p1c1))
except:
 _st_.goboom(_sage_const_89 )
try:
 _st_.current_tex_line = _sage_const_89 
 _st_.inline(_sage_const_10 , latex(p1c1))
except:
 _st_.goboom(_sage_const_89 )
try:
 _st_.current_tex_line = _sage_const_89 
 _st_.inline(_sage_const_11 , latex(p1c1))
except:
 _st_.goboom(_sage_const_89 )
try:
 _st_.current_tex_line = _sage_const_95 
 _st_.inline(_sage_const_12 , latex(p2relate))
except:
 _st_.goboom(_sage_const_95 )
try:
 _st_.current_tex_line = _sage_const_97 
 _st_.inline(_sage_const_13 , latex(p2ans1))
except:
 _st_.goboom(_sage_const_97 )
try:
 _st_.current_tex_line = _sage_const_98 
 _st_.inline(_sage_const_14 , latex(p2ans2))
except:
 _st_.goboom(_sage_const_98 )
try:
 _st_.current_tex_line = _sage_const_99 
 _st_.inline(_sage_const_15 , latex(p2ans3))
except:
 _st_.goboom(_sage_const_99 )
try:
 _st_.current_tex_line = _sage_const_100 
 _st_.inline(_sage_const_16 , latex(p2ans4))
except:
 _st_.goboom(_sage_const_100 )
try:
 _st_.current_tex_line = _sage_const_101 
 _st_.inline(_sage_const_17 , latex(p2ans5))
except:
 _st_.goboom(_sage_const_101 )
try:
 _st_.current_tex_line = _sage_const_102 
 _st_.inline(_sage_const_18 , latex(p2ans6))
except:
 _st_.goboom(_sage_const_102 )
try:
 _st_.current_tex_line = _sage_const_103 
 _st_.inline(_sage_const_19 , latex(p2ans7))
except:
 _st_.goboom(_sage_const_103 )
try:
 _st_.current_tex_line = _sage_const_104 
 _st_.inline(_sage_const_20 , latex(p2ans8))
except:
 _st_.goboom(_sage_const_104 )
try:
 _st_.current_tex_line = _sage_const_114 
 _st_.inline(_sage_const_21 , latex(p3c1))
except:
 _st_.goboom(_sage_const_114 )
try:
 _st_.current_tex_line = _sage_const_116 
 _st_.inline(_sage_const_22 , latex(p3c1))
except:
 _st_.goboom(_sage_const_116 )
try:
 _st_.current_tex_line = _sage_const_117 
 _st_.inline(_sage_const_23 , latex(p3c1))
except:
 _st_.goboom(_sage_const_117 )
try:
 _st_.current_tex_line = _sage_const_118 
 _st_.inline(_sage_const_24 , latex(p3c1))
except:
 _st_.goboom(_sage_const_118 )
try:
 _st_.current_tex_line = _sage_const_119 
 _st_.inline(_sage_const_25 , latex(p3c1))
except:
 _st_.goboom(_sage_const_119 )
try:
 _st_.current_tex_line = _sage_const_120 
 _st_.inline(_sage_const_26 , latex(p3c2))
except:
 _st_.goboom(_sage_const_120 )
try:
 _st_.current_tex_line = _sage_const_121 
 _st_.inline(_sage_const_27 , latex(p3c2))
except:
 _st_.goboom(_sage_const_121 )
try:
 _st_.current_tex_line = _sage_const_122 
 _st_.inline(_sage_const_28 , latex(p3c2))
except:
 _st_.goboom(_sage_const_122 )
try:
 _st_.current_tex_line = _sage_const_123 
 _st_.inline(_sage_const_29 , latex(p3c2))
except:
 _st_.goboom(_sage_const_123 )
try:
 _st_.current_tex_line = _sage_const_127 
 _st_.inline(_sage_const_30 , latex(p3c1))
except:
 _st_.goboom(_sage_const_127 )
try:
 _st_.current_tex_line = _sage_const_127 
 _st_.inline(_sage_const_31 , latex(p3c1))
except:
 _st_.goboom(_sage_const_127 )
try:
 _st_.current_tex_line = _sage_const_127 
 _st_.inline(_sage_const_32 , latex(p3c1))
except:
 _st_.goboom(_sage_const_127 )
try:
 _st_.current_tex_line = _sage_const_134 
 _st_.inline(_sage_const_33 , latex(p4relate))
except:
 _st_.goboom(_sage_const_134 )
try:
 _st_.current_tex_line = _sage_const_136 
 _st_.inline(_sage_const_34 , latex(p4ans1))
except:
 _st_.goboom(_sage_const_136 )
try:
 _st_.current_tex_line = _sage_const_137 
 _st_.inline(_sage_const_35 , latex(p4ans2))
except:
 _st_.goboom(_sage_const_137 )
try:
 _st_.current_tex_line = _sage_const_138 
 _st_.inline(_sage_const_36 , latex(p4ans4))
except:
 _st_.goboom(_sage_const_138 )
try:
 _st_.current_tex_line = _sage_const_139 
 _st_.inline(_sage_const_37 , latex(p4ans5))
except:
 _st_.goboom(_sage_const_139 )
try:
 _st_.current_tex_line = _sage_const_140 
 _st_.inline(_sage_const_38 , latex(p4ans6))
except:
 _st_.goboom(_sage_const_140 )
try:
 _st_.current_tex_line = _sage_const_141 
 _st_.inline(_sage_const_39 , latex(p4ans3))
except:
 _st_.goboom(_sage_const_141 )
try:
 _st_.current_tex_line = _sage_const_142 
 _st_.inline(_sage_const_40 , latex(p4ans7))
except:
 _st_.goboom(_sage_const_142 )
try:
 _st_.current_tex_line = _sage_const_143 
 _st_.inline(_sage_const_41 , latex(p4ans8))
except:
 _st_.goboom(_sage_const_143 )
try:
 _st_.current_tex_line = _sage_const_153 
 _st_.inline(_sage_const_42 , latex(p5c1))
except:
 _st_.goboom(_sage_const_153 )
try:
 _st_.current_tex_line = _sage_const_155 
 _st_.inline(_sage_const_43 , latex(p5c1))
except:
 _st_.goboom(_sage_const_155 )
try:
 _st_.current_tex_line = _sage_const_156 
 _st_.inline(_sage_const_44 , latex(p5c1))
except:
 _st_.goboom(_sage_const_156 )
try:
 _st_.current_tex_line = _sage_const_157 
 _st_.inline(_sage_const_45 , latex(p5c1))
except:
 _st_.goboom(_sage_const_157 )
try:
 _st_.current_tex_line = _sage_const_158 
 _st_.inline(_sage_const_46 , latex(p5c1))
except:
 _st_.goboom(_sage_const_158 )
try:
 _st_.current_tex_line = _sage_const_159 
 _st_.inline(_sage_const_47 , latex(p5c2))
except:
 _st_.goboom(_sage_const_159 )
try:
 _st_.current_tex_line = _sage_const_160 
 _st_.inline(_sage_const_48 , latex(p5c2))
except:
 _st_.goboom(_sage_const_160 )
try:
 _st_.current_tex_line = _sage_const_161 
 _st_.inline(_sage_const_49 , latex(p5c2))
except:
 _st_.goboom(_sage_const_161 )
try:
 _st_.current_tex_line = _sage_const_162 
 _st_.inline(_sage_const_50 , latex(p5c2))
except:
 _st_.goboom(_sage_const_162 )
try:
 _st_.current_tex_line = _sage_const_167 
 _st_.inline(_sage_const_51 , latex(p5c1))
except:
 _st_.goboom(_sage_const_167 )
try:
 _st_.current_tex_line = _sage_const_167 
 _st_.inline(_sage_const_52 , latex(p5c1))
except:
 _st_.goboom(_sage_const_167 )
try:
 _st_.current_tex_line = _sage_const_167 
 _st_.inline(_sage_const_53 , latex(p5c1))
except:
 _st_.goboom(_sage_const_167 )
try:
 _st_.current_tex_line = _sage_const_174 
 _st_.inline(_sage_const_54 , latex(p6relate))
except:
 _st_.goboom(_sage_const_174 )
try:
 _st_.current_tex_line = _sage_const_176 
 _st_.inline(_sage_const_55 , latex(p6ans1))
except:
 _st_.goboom(_sage_const_176 )
try:
 _st_.current_tex_line = _sage_const_177 
 _st_.inline(_sage_const_56 , latex(p6ans2))
except:
 _st_.goboom(_sage_const_177 )
try:
 _st_.current_tex_line = _sage_const_178 
 _st_.inline(_sage_const_57 , latex(p6ans4))
except:
 _st_.goboom(_sage_const_178 )
try:
 _st_.current_tex_line = _sage_const_179 
 _st_.inline(_sage_const_58 , latex(p6ans5))
except:
 _st_.goboom(_sage_const_179 )
try:
 _st_.current_tex_line = _sage_const_180 
 _st_.inline(_sage_const_59 , latex(p6ans6))
except:
 _st_.goboom(_sage_const_180 )
try:
 _st_.current_tex_line = _sage_const_181 
 _st_.inline(_sage_const_60 , latex(p6ans7))
except:
 _st_.goboom(_sage_const_181 )
try:
 _st_.current_tex_line = _sage_const_182 
 _st_.inline(_sage_const_61 , latex(p6ans8))
except:
 _st_.goboom(_sage_const_182 )
try:
 _st_.current_tex_line = _sage_const_183 
 _st_.inline(_sage_const_62 , latex(p6ans3))
except:
 _st_.goboom(_sage_const_183 )
_st_.endofdoc()

