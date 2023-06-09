## -*- encoding: utf-8 -*-

# This file was *autogenerated* from the file simplifyingComplexNumbers.sagetex.sage
from sage.all_cmdline import *   # import sage library

_sage_const_3 = Integer(3); _sage_const_2 = Integer(2); _sage_const_1 = Integer(1); _sage_const_0 = Integer(0); _sage_const_7 = Integer(7); _sage_const_6 = Integer(6); _sage_const_5 = Integer(5); _sage_const_4 = Integer(4); _sage_const_9 = Integer(9); _sage_const_8 = Integer(8); _sage_const_201 = Integer(201); _sage_const_187 = Integer(187); _sage_const_116 = Integer(116); _sage_const_173 = Integer(173); _sage_const_176 = Integer(176); _sage_const_159 = Integer(159); _sage_const_190 = Integer(190); _sage_const_13 = Integer(13); _sage_const_12 = Integer(12); _sage_const_11 = Integer(11); _sage_const_10 = Integer(10); _sage_const_17 = Integer(17); _sage_const_16 = Integer(16); _sage_const_15 = Integer(15); _sage_const_14 = Integer(14); _sage_const_19 = Integer(19); _sage_const_18 = Integer(18); _sage_const_204 = Integer(204); _sage_const_162 = Integer(162)## This file (simplifyingComplexNumbers.sagetex.sage) was *autogenerated* from simplifyingComplexNumbers.tex with sagetex.sty version 2015/08/26 v3.0-92d9f7a.
import sagetex
_st_ = sagetex.SageTeXProcessor('simplifyingComplexNumbers', version='2015/08/26 v3.0-92d9f7a', version_check=True)
_st_.current_tex_line = _sage_const_10 
_st_.blockbegin()
try:
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
 
 def cpx(z):
     if z == _sage_const_0 :
         return LatexExpr('0')
     a = z.real()
     b = z.imag()
     if (a == _sage_const_0 ) or (b==_sage_const_0 ) :
         return LatexExpr(latex(z))
     elif b > _sage_const_0 :
       s = '+'
     else:
       s = '-'
     return latex(a) + LatexExpr(s) + latex(abs(b) * i)
 
 
 
 ### Problem p1
 p1c1 = RandInt(-_sage_const_5 ,_sage_const_5 )
 p1c2 = RandInt(-_sage_const_5 ,_sage_const_5 )
 p1c3 = RandInt(-_sage_const_5 ,_sage_const_5 )
 p1c4 = NonZeroInt(-_sage_const_5 ,_sage_const_5 )
 
 p1complex1 = p1c1 + p1c2*i
 p1complex2 = p1c3 + p1c4*i
 
 p1complex1d = cpx(p1c1 + p1c2*i)
 p1complex2d = cpx(p1c3 + p1c4*i)
 
 p1ans1 = (p1complex1/p1complex2).real()
 p1ans2 = (p1complex1/p1complex2).imag()
 
 p1h1 = cpx(p1complex2.conjugate())
 
 
 
 ### Problem p2
 p2c1 = RandInt(-_sage_const_5 ,_sage_const_5 )
 p2c2 = RandInt(-_sage_const_5 ,_sage_const_5 )
 p2c3 = RandInt(-_sage_const_5 ,_sage_const_5 )
 p2c4 = NonZeroInt(-_sage_const_5 ,_sage_const_5 )
 
 p2complex1 = p2c1 + p2c2*i
 p2complex2 = p2c3 + p2c4*i
 
 p2complex1d = cpx(p2c1 + p2c2*i)
 p2complex2d = cpx(p2c3 + p2c4*i)
 
 p2ans1 = (p2complex1/p2complex2).real()
 p2ans2 = (p2complex1/p2complex2).imag()
 
 p2h1 = cpx(p2complex2.conjugate())
 
 
 ### Problem p3
 p3c1 = RandInt(-_sage_const_5 ,_sage_const_5 )
 p3c2 = RandInt(-_sage_const_5 ,_sage_const_5 )
 p3c3 = RandInt(-_sage_const_5 ,_sage_const_5 )
 p3c4 = NonZeroInt(-_sage_const_5 ,_sage_const_5 )
 
 p3complex1 = p3c1 + p3c2*i
 p3complex2 = p3c3 + p3c4*i
 
 p3complex1d = cpx(p3c1 + p3c2*i)
 p3complex2d = cpx(p3c3 + p3c4*i)
 
 p3ans1 = (p3complex1/p3complex2).real()
 p3ans2 = (p3complex1/p3complex2).imag()
 
 p3h1 = cpx(p3complex2.conjugate())
 
 
 ### Problem p4
 p4c1 = RandInt(-_sage_const_5 ,_sage_const_5 )
 p4c2 = RandInt(-_sage_const_5 ,_sage_const_5 )
 p4c3 = RandInt(-_sage_const_5 ,_sage_const_5 )
 p4c4 = NonZeroInt(-_sage_const_5 ,_sage_const_5 )
 
 p4complex1 = p4c1 + p4c2*i
 p4complex2 = p4c3 + p4c4*i
 
 p4complex1d = cpx(p4c1 + p4c2*i)
 p4complex2d = cpx(p4c3 + p4c4*i)
 
 p4ans1 = (p4complex1/p4complex2).real()
 p4ans2 = (p4complex1/p4complex2).imag()
 
 p4h1 = cpx(p4complex2.conjugate())
 
 
 
 
except:
 _st_.goboom(_sage_const_116 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_159 
 _st_.inline(_sage_const_0 , latex(p1complex1d))
except:
 _st_.goboom(_sage_const_159 )
try:
 _st_.current_tex_line = _sage_const_159 
 _st_.inline(_sage_const_1 , latex(p1complex2d))
except:
 _st_.goboom(_sage_const_159 )
try:
 _st_.current_tex_line = _sage_const_159 
 _st_.inline(_sage_const_2 , latex(p1ans1))
except:
 _st_.goboom(_sage_const_159 )
try:
 _st_.current_tex_line = _sage_const_159 
 _st_.inline(_sage_const_3 , latex(p1ans2))
except:
 _st_.goboom(_sage_const_159 )
try:
 _st_.current_tex_line = _sage_const_162 
 _st_.inline(_sage_const_4 , latex(p1h1))
except:
 _st_.goboom(_sage_const_162 )
try:
 _st_.current_tex_line = _sage_const_173 
 _st_.inline(_sage_const_5 , latex(p2complex1d))
except:
 _st_.goboom(_sage_const_173 )
try:
 _st_.current_tex_line = _sage_const_173 
 _st_.inline(_sage_const_6 , latex(p2complex2d))
except:
 _st_.goboom(_sage_const_173 )
try:
 _st_.current_tex_line = _sage_const_173 
 _st_.inline(_sage_const_7 , latex(p2ans1))
except:
 _st_.goboom(_sage_const_173 )
try:
 _st_.current_tex_line = _sage_const_173 
 _st_.inline(_sage_const_8 , latex(p2ans2))
except:
 _st_.goboom(_sage_const_173 )
try:
 _st_.current_tex_line = _sage_const_176 
 _st_.inline(_sage_const_9 , latex(p2h1))
except:
 _st_.goboom(_sage_const_176 )
try:
 _st_.current_tex_line = _sage_const_187 
 _st_.inline(_sage_const_10 , latex(p3complex1d))
except:
 _st_.goboom(_sage_const_187 )
try:
 _st_.current_tex_line = _sage_const_187 
 _st_.inline(_sage_const_11 , latex(p3complex2d))
except:
 _st_.goboom(_sage_const_187 )
try:
 _st_.current_tex_line = _sage_const_187 
 _st_.inline(_sage_const_12 , latex(p3ans1))
except:
 _st_.goboom(_sage_const_187 )
try:
 _st_.current_tex_line = _sage_const_187 
 _st_.inline(_sage_const_13 , latex(p3ans2))
except:
 _st_.goboom(_sage_const_187 )
try:
 _st_.current_tex_line = _sage_const_190 
 _st_.inline(_sage_const_14 , latex(p3h1))
except:
 _st_.goboom(_sage_const_190 )
try:
 _st_.current_tex_line = _sage_const_201 
 _st_.inline(_sage_const_15 , latex(p4complex1d))
except:
 _st_.goboom(_sage_const_201 )
try:
 _st_.current_tex_line = _sage_const_201 
 _st_.inline(_sage_const_16 , latex(p4complex2d))
except:
 _st_.goboom(_sage_const_201 )
try:
 _st_.current_tex_line = _sage_const_201 
 _st_.inline(_sage_const_17 , latex(p4ans1))
except:
 _st_.goboom(_sage_const_201 )
try:
 _st_.current_tex_line = _sage_const_201 
 _st_.inline(_sage_const_18 , latex(p4ans2))
except:
 _st_.goboom(_sage_const_201 )
try:
 _st_.current_tex_line = _sage_const_204 
 _st_.inline(_sage_const_19 , latex(p4h1))
except:
 _st_.goboom(_sage_const_204 )
_st_.endofdoc()

