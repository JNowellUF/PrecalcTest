## -*- encoding: utf-8 -*-
## This file (typeTwoRadicals-Practice1.sagetex.sage) was *autogenerated* from typeTwoRadicals-Practice1.tex with sagetex.sty version 2015/08/26 v3.0-92d9f7a.
import sagetex
_st_ = sagetex.SageTeXProcessor('typeTwoRadicals-Practice1', version='2015/08/26 v3.0-92d9f7a', version_check=True)
_st_.current_tex_line = 9
_st_.blockbegin()
try:
 var('x')
 
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
 
 ###### Problem p1
 p1f1(x) = x + 999999
 while p1f1(x=1)>500 or p1f1(x=-1)>500 or p1f1(x=0)>500:
     p1c1 = RandInt(1,5)
     p1c2 = RandInt(1,5)
     p1c3 = RandInt(1,5)
     p1c4 = RandInt(1,5)
     p1c5 = RandInt(-7,7)
     p1c6 = RandInt(-7,7)
     p1c7 = RandInt(-7,7)
     p1c8 = RandInt(-7,7)
     p1tog1 = RandInt(0,1)
     p1tog2 = RandInt(1-p1tog1,1)
 
     p1f1t = p1c1*x-p1c5
     p1f2t = p1c2*x-p1c6
     p1f3t = (p1c3*x-p1c7)^p1tog1
     p1f4t = (p1c4*x-p1c8)^p1tog2
 
 
     p1f1 = (p1f1t).mul(p1f2t,p1f3t,p1f4t,hold=true)
 
 p1rad = expand(p1f1)
 
 
 ###### Problem p2
 p2f1(x) = x + 999999
 while p2f1(x=1)>500 or p2f1(x=-1)>500 or p2f1(x=0)>500:
     p2c1 = RandInt(1,5)
     p2c2 = RandInt(1,5)
     p2c3 = RandInt(1,5)
     p2c4 = RandInt(1,5)
     p2c5 = RandInt(-7,7)
     p2c6 = RandInt(-7,7)
     p2c7 = RandInt(-7,7)
     p2c8 = RandInt(-7,7)
     p2tog1 = RandInt(0,1)
     p2tog2 = RandInt(0,1)
 
     p2f1t = p2c1*x-p2c5
     p2f2t = p2c2*x-p2c6
     p2f3t = (p2c3*x-p2c7)^p2tog1
     p2f4t = (p2c4*x-p2c8)^p2tog2
 
 
     p2f1 = (p2f1t).mul(p2f2t,p2f3t,p2f4t,hold=true)
 
 p2rad = expand(p2f1)
 
 
 ###### Problem p3
 p3f1(x) = x + 999999
 while p3f1(x=1)>500 or p3f1(x=-1)>500 or p3f1(x=0)>500:
     p3c1 = RandInt(1,5)
     p3c2 = RandInt(1,5)
     p3c3 = RandInt(1,5)
     p3c4 = RandInt(1,5)
     p3c5 = RandInt(-7,7)
     p3c6 = RandInt(-7,7)
     p3c7 = RandInt(-7,7)
     p3c8 = RandInt(-7,7)
     p3tog1 = RandInt(0,1)
     p3tog2 = RandInt(0,1)
 
     p3f1t = p3c1*x-p3c5
     p3f2t = p3c2*x-p3c6
     p3f3t = (p3c3*x-p3c7)^p3tog1
     p3f4t = (p3c4*x-p3c8)^p3tog2
 
 
     p3f1 = (p3f1t).mul(p3f2t,p3f3t,p3f4t,hold=true)
 
 p3rad = expand(p3f1)
 
 
 
 
except:
 _st_.goboom(104)
_st_.blockend()
try:
 _st_.current_tex_line = 155
 _st_.inline(0, latex(p1rad))
except:
 _st_.goboom(155)
try:
 _st_.current_tex_line = 155
 _st_.inline(1, latex(p1f1))
except:
 _st_.goboom(155)
try:
 _st_.current_tex_line = 168
 _st_.inline(2, latex(p2rad))
except:
 _st_.goboom(168)
try:
 _st_.current_tex_line = 168
 _st_.inline(3, latex(p2f1))
except:
 _st_.goboom(168)
try:
 _st_.current_tex_line = 181
 _st_.inline(4, latex(p3rad))
except:
 _st_.goboom(181)
try:
 _st_.current_tex_line = 181
 _st_.inline(5, latex(p3f1))
except:
 _st_.goboom(181)
_st_.endofdoc()
