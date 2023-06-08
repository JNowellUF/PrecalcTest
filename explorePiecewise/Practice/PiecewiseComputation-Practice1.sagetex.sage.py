## -*- encoding: utf-8 -*-

# This file was *autogenerated* from the file PiecewiseComputation-Practice1.sagetex.sage
from sage.all_cmdline import *   # import sage library

_sage_const_3 = Integer(3); _sage_const_2 = Integer(2); _sage_const_1 = Integer(1); _sage_const_0 = Integer(0); _sage_const_7 = Integer(7); _sage_const_6 = Integer(6); _sage_const_5 = Integer(5); _sage_const_4 = Integer(4); _sage_const_43 = Integer(43); _sage_const_9 = Integer(9); _sage_const_8 = Integer(8); _sage_const_243 = Integer(243); _sage_const_201 = Integer(201); _sage_const_266 = Integer(266); _sage_const_203 = Integer(203); _sage_const_29 = Integer(29); _sage_const_23 = Integer(23); _sage_const_22 = Integer(22); _sage_const_207 = Integer(207); _sage_const_20 = Integer(20); _sage_const_21 = Integer(21); _sage_const_26 = Integer(26); _sage_const_27 = Integer(27); _sage_const_24 = Integer(24); _sage_const_25 = Integer(25); _sage_const_40 = Integer(40); _sage_const_41 = Integer(41); _sage_const_42 = Integer(42); _sage_const_32 = Integer(32); _sage_const_44 = Integer(44); _sage_const_249 = Integer(249); _sage_const_46 = Integer(46); _sage_const_47 = Integer(47); _sage_const_48 = Integer(48); _sage_const_49 = Integer(49); _sage_const_54 = Integer(54); _sage_const_52 = Integer(52); _sage_const_202 = Integer(202); _sage_const_50 = Integer(50); _sage_const_51 = Integer(51); _sage_const_33 = Integer(33); _sage_const_245 = Integer(245); _sage_const_244 = Integer(244); _sage_const_45 = Integer(45); _sage_const_270 = Integer(270); _sage_const_194 = Integer(194); _sage_const_53 = Integer(53); _sage_const_265 = Integer(265); _sage_const_264 = Integer(264); _sage_const_13 = Integer(13); _sage_const_12 = Integer(12); _sage_const_11 = Integer(11); _sage_const_10 = Integer(10); _sage_const_17 = Integer(17); _sage_const_16 = Integer(16); _sage_const_15 = Integer(15); _sage_const_14 = Integer(14); _sage_const_31 = Integer(31); _sage_const_30 = Integer(30); _sage_const_19 = Integer(19); _sage_const_18 = Integer(18); _sage_const_35 = Integer(35); _sage_const_34 = Integer(34); _sage_const_37 = Integer(37); _sage_const_36 = Integer(36); _sage_const_39 = Integer(39); _sage_const_38 = Integer(38); _sage_const_286 = Integer(286); _sage_const_287 = Integer(287); _sage_const_28 = Integer(28); _sage_const_285 = Integer(285); _sage_const_228 = Integer(228); _sage_const_291 = Integer(291); _sage_const_224 = Integer(224); _sage_const_223 = Integer(223); _sage_const_222 = Integer(222)## This file (PiecewiseComputation-Practice1.sagetex.sage) was *autogenerated* from PiecewiseComputation-Practice1.tex with sagetex.sty version 2015/08/26 v3.0-92d9f7a.
import sagetex
_st_ = sagetex.SageTeXProcessor('PiecewiseComputation-Practice1', version='2015/08/26 v3.0-92d9f7a', version_check=True)
_st_.current_tex_line = _sage_const_10 
_st_.blockbegin()
try:
 ##### Useful Macros
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
 
 funcvec = [x,x**_sage_const_2 ,x**_sage_const_3 ,sqrt(abs(x)),ln(abs(x)+_sage_const_1 ),e**x]
 
 ###############
 #### Problem p1
 p1f1pick = RandInt(_sage_const_0 ,_sage_const_5 )
 p1f2pick = RandInt(_sage_const_0 ,_sage_const_5 )
 p1f3pick = RandInt(_sage_const_0 ,_sage_const_5 )
 
 ### Build each of the functions.
 p1f1 = NonZeroInt(-_sage_const_5 ,_sage_const_5 )*funcvec[p1f1pick](x=(x-RandInt(-_sage_const_5 ,_sage_const_5 ))) + RandInt(-_sage_const_5 ,_sage_const_5 )
 p1f2 = NonZeroInt(-_sage_const_5 ,_sage_const_5 )*funcvec[p1f2pick](x=(x-RandInt(-_sage_const_5 ,_sage_const_5 ))) + RandInt(-_sage_const_5 ,_sage_const_5 )
 p1f3 = NonZeroInt(-_sage_const_5 ,_sage_const_5 )*funcvec[p1f3pick](x=(x-RandInt(-_sage_const_5 ,_sage_const_5 ))) + RandInt(-_sage_const_5 ,_sage_const_5 )
 
 ### Build the left and right endpoints for the functions.
 p1l1 = RandInt(-_sage_const_15 ,_sage_const_15 )
 p1r1 = p1l1 + RandInt(_sage_const_1 ,_sage_const_7 )
 p1r2 = p1r1 + RandInt(_sage_const_1 ,_sage_const_7 )
 p1r3 = p1r2 + RandInt(_sage_const_1 ,_sage_const_7 )
 
 ## Now to pick a point to evaluate; and then evaluate it:
 p1eval = RandInt(p1l1,p1r3)
 
 if p1eval < p1r1+_sage_const_1 :
     p1ans = p1f1(x=p1eval)
 elif p1eval < p1r2+_sage_const_1 :
     p1ans = p1f2(x=p1eval)
 else:
     p1ans = p1f3(x=p1eval)
 
 
 ##### End of problem p1
 
 
 
 
 ###############
 #### Problem p2
 p2f1pick = RandInt(_sage_const_0 ,_sage_const_5 )
 p2f2pick = RandInt(_sage_const_0 ,_sage_const_5 )
 p2f3pick = RandInt(_sage_const_0 ,_sage_const_5 )
 
 ### Build each of the functions.
 p2f1 = NonZeroInt(-_sage_const_5 ,_sage_const_5 )*funcvec[p2f1pick](x=(x-RandInt(-_sage_const_5 ,_sage_const_5 ))) + RandInt(-_sage_const_5 ,_sage_const_5 )
 p2f2 = NonZeroInt(-_sage_const_5 ,_sage_const_5 )*funcvec[p2f2pick](x=(x-RandInt(-_sage_const_5 ,_sage_const_5 ))) + RandInt(-_sage_const_5 ,_sage_const_5 )
 p2f3 = NonZeroInt(-_sage_const_5 ,_sage_const_5 )*funcvec[p2f3pick](x=(x-RandInt(-_sage_const_5 ,_sage_const_5 ))) + RandInt(-_sage_const_5 ,_sage_const_5 )
 
 ### Build the left and right endpoints for the functions.
 p2l1 = RandInt(-_sage_const_15 ,_sage_const_15 )
 p2r1 = p2l1 + RandInt(_sage_const_1 ,_sage_const_7 )
 p2r2 = p2r1 + RandInt(_sage_const_1 ,_sage_const_7 )
 p2r3 = p2r2 + RandInt(_sage_const_1 ,_sage_const_7 )
 
 ## Now to pick a point to evaluate; and then evaluate it:
 p2eval = RandInt(p2l1,p2r3)
 
 if p2eval < p2r1+_sage_const_1 :
     p2ans = p2f1(x=p2eval)
 elif p2eval < p2r2+_sage_const_1 :
     p2ans = p2f2(x=p2eval)
 else:
     p2ans = p2f3(x=p2eval)
 
 
 ##### End of problem p2
 
 
 
 
 ###############
 #### Problem p3
 p3f1pick = RandInt(_sage_const_0 ,_sage_const_5 )
 p3f2pick = RandInt(_sage_const_0 ,_sage_const_5 )
 p3f3pick = RandInt(_sage_const_0 ,_sage_const_5 )
 
 ### Build each of the functions.
 p3f1 = NonZeroInt(-_sage_const_5 ,_sage_const_5 )*funcvec[p3f1pick](x=(x-RandInt(-_sage_const_5 ,_sage_const_5 ))) + RandInt(-_sage_const_5 ,_sage_const_5 )
 p3f2 = NonZeroInt(-_sage_const_5 ,_sage_const_5 )*funcvec[p3f2pick](x=(x-RandInt(-_sage_const_5 ,_sage_const_5 ))) + RandInt(-_sage_const_5 ,_sage_const_5 )
 p3f3 = NonZeroInt(-_sage_const_5 ,_sage_const_5 )*funcvec[p3f3pick](x=(x-RandInt(-_sage_const_5 ,_sage_const_5 ))) + RandInt(-_sage_const_5 ,_sage_const_5 )
 
 ### Build the left and right endpoints for the functions.
 p3l1 = RandInt(-_sage_const_15 ,_sage_const_15 )
 p3r1 = p3l1 + RandInt(_sage_const_1 ,_sage_const_7 )
 p3r2 = p3r1 + RandInt(_sage_const_1 ,_sage_const_7 )
 p3r3 = p3r2 + RandInt(_sage_const_1 ,_sage_const_7 )
 
 ## Now to pick a point to evaluate; and then evaluate it:
 p3eval = RandInt(p3l1,p3r3)
 
 if p3eval < p3r1+_sage_const_1 :
     p3ans = p3f1(x=p3eval)
 elif p3eval < p3r2+_sage_const_1 :
     p3ans = p3f2(x=p3eval)
 else:
     p3ans = p3f3(x=p3eval)
 
 
 ##### End of problem p3
 
 
 
 
 ###############
 #### Problem p4
 p4f1pick = RandInt(_sage_const_0 ,_sage_const_5 )
 p4f2pick = RandInt(_sage_const_0 ,_sage_const_5 )
 p4f3pick = RandInt(_sage_const_0 ,_sage_const_5 )
 
 ### Build each of the functions.
 p4f1 = NonZeroInt(-_sage_const_5 ,_sage_const_5 )*funcvec[p4f1pick](x=(x-RandInt(-_sage_const_5 ,_sage_const_5 ))) + RandInt(-_sage_const_5 ,_sage_const_5 )
 p4f2 = NonZeroInt(-_sage_const_5 ,_sage_const_5 )*funcvec[p4f2pick](x=(x-RandInt(-_sage_const_5 ,_sage_const_5 ))) + RandInt(-_sage_const_5 ,_sage_const_5 )
 p4f3 = NonZeroInt(-_sage_const_5 ,_sage_const_5 )*funcvec[p4f3pick](x=(x-RandInt(-_sage_const_5 ,_sage_const_5 ))) + RandInt(-_sage_const_5 ,_sage_const_5 )
 
 ### Build the left and right endpoints for the functions.
 p4l1 = RandInt(-_sage_const_15 ,_sage_const_15 )
 p4r1 = p4l1 + RandInt(_sage_const_1 ,_sage_const_7 )
 p4r2 = p4r1 + RandInt(_sage_const_1 ,_sage_const_7 )
 p4r3 = p4r2 + RandInt(_sage_const_1 ,_sage_const_7 )
 
 ## Now to pick a point to evaluate; and then evaluate it:
 p4eval = RandInt(p4l1,p4r3)
 
 if p4eval < p4r1+_sage_const_1 :
     p4ans = p4f1(x=p4eval)
 elif p4eval < p4r2+_sage_const_1 :
     p4ans = p4f2(x=p4eval)
 else:
     p4ans = p4f3(x=p4eval)
 
 
 ##### End of problem p4
 
 
 
 
 ###############
 #### Problem p5
 p5f1pick = RandInt(_sage_const_0 ,_sage_const_5 )
 p5f2pick = RandInt(_sage_const_0 ,_sage_const_5 )
 p5f3pick = RandInt(_sage_const_0 ,_sage_const_5 )
 
 ### Build each of the functions.
 p5f1 = NonZeroInt(-_sage_const_5 ,_sage_const_5 )*funcvec[p5f1pick](x=(x-RandInt(-_sage_const_5 ,_sage_const_5 ))) + RandInt(-_sage_const_5 ,_sage_const_5 )
 p5f2 = NonZeroInt(-_sage_const_5 ,_sage_const_5 )*funcvec[p5f2pick](x=(x-RandInt(-_sage_const_5 ,_sage_const_5 ))) + RandInt(-_sage_const_5 ,_sage_const_5 )
 p5f3 = NonZeroInt(-_sage_const_5 ,_sage_const_5 )*funcvec[p5f3pick](x=(x-RandInt(-_sage_const_5 ,_sage_const_5 ))) + RandInt(-_sage_const_5 ,_sage_const_5 )
 
 ### Build the left and right endpoints for the functions.
 p5l1 = RandInt(-_sage_const_15 ,_sage_const_15 )
 p5r1 = p5l1 + RandInt(_sage_const_1 ,_sage_const_7 )
 p5r2 = p5r1 + RandInt(_sage_const_1 ,_sage_const_7 )
 p5r3 = p5r2 + RandInt(_sage_const_1 ,_sage_const_7 )
 
 ## Now to pick a point to evaluate; and then evaluate it:
 p5eval = RandInt(p5l1,p5r3)
 
 if p5eval < p5r1+_sage_const_1 :
     p5ans = p5f1(x=p5eval)
 elif p5eval < p5r2+_sage_const_1 :
     p5ans = p5f2(x=p5eval)
 else:
     p5ans = p5f3(x=p5eval)
 
 
 ##### End of problem p5
 
 
 
 
except:
 _st_.goboom(_sage_const_194 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_201 
 _st_.inline(_sage_const_0 , latex(p1f1))
except:
 _st_.goboom(_sage_const_201 )
try:
 _st_.current_tex_line = _sage_const_201 
 _st_.inline(_sage_const_1 , latex(p1l1))
except:
 _st_.goboom(_sage_const_201 )
try:
 _st_.current_tex_line = _sage_const_201 
 _st_.inline(_sage_const_2 , latex(p1r1))
except:
 _st_.goboom(_sage_const_201 )
try:
 _st_.current_tex_line = _sage_const_202 
 _st_.inline(_sage_const_3 , latex(p1f2))
except:
 _st_.goboom(_sage_const_202 )
try:
 _st_.current_tex_line = _sage_const_202 
 _st_.inline(_sage_const_4 , latex(p1r1))
except:
 _st_.goboom(_sage_const_202 )
try:
 _st_.current_tex_line = _sage_const_202 
 _st_.inline(_sage_const_5 , latex(p1r2))
except:
 _st_.goboom(_sage_const_202 )
try:
 _st_.current_tex_line = _sage_const_203 
 _st_.inline(_sage_const_6 , latex(p1f3))
except:
 _st_.goboom(_sage_const_203 )
try:
 _st_.current_tex_line = _sage_const_203 
 _st_.inline(_sage_const_7 , latex(p1r2))
except:
 _st_.goboom(_sage_const_203 )
try:
 _st_.current_tex_line = _sage_const_203 
 _st_.inline(_sage_const_8 , latex(p1r3))
except:
 _st_.goboom(_sage_const_203 )
try:
 _st_.current_tex_line = _sage_const_207 
 _st_.inline(_sage_const_9 , latex(p1eval))
except:
 _st_.goboom(_sage_const_207 )
try:
 _st_.current_tex_line = _sage_const_207 
 _st_.inline(_sage_const_10 , latex(p1ans))
except:
 _st_.goboom(_sage_const_207 )
try:
 _st_.current_tex_line = _sage_const_222 
 _st_.inline(_sage_const_11 , latex(p2f1))
except:
 _st_.goboom(_sage_const_222 )
try:
 _st_.current_tex_line = _sage_const_222 
 _st_.inline(_sage_const_12 , latex(p2l1))
except:
 _st_.goboom(_sage_const_222 )
try:
 _st_.current_tex_line = _sage_const_222 
 _st_.inline(_sage_const_13 , latex(p2r1))
except:
 _st_.goboom(_sage_const_222 )
try:
 _st_.current_tex_line = _sage_const_223 
 _st_.inline(_sage_const_14 , latex(p2f2))
except:
 _st_.goboom(_sage_const_223 )
try:
 _st_.current_tex_line = _sage_const_223 
 _st_.inline(_sage_const_15 , latex(p2r1))
except:
 _st_.goboom(_sage_const_223 )
try:
 _st_.current_tex_line = _sage_const_223 
 _st_.inline(_sage_const_16 , latex(p2r2))
except:
 _st_.goboom(_sage_const_223 )
try:
 _st_.current_tex_line = _sage_const_224 
 _st_.inline(_sage_const_17 , latex(p2f3))
except:
 _st_.goboom(_sage_const_224 )
try:
 _st_.current_tex_line = _sage_const_224 
 _st_.inline(_sage_const_18 , latex(p2r2))
except:
 _st_.goboom(_sage_const_224 )
try:
 _st_.current_tex_line = _sage_const_224 
 _st_.inline(_sage_const_19 , latex(p2r3))
except:
 _st_.goboom(_sage_const_224 )
try:
 _st_.current_tex_line = _sage_const_228 
 _st_.inline(_sage_const_20 , latex(p2eval))
except:
 _st_.goboom(_sage_const_228 )
try:
 _st_.current_tex_line = _sage_const_228 
 _st_.inline(_sage_const_21 , latex(p2ans))
except:
 _st_.goboom(_sage_const_228 )
try:
 _st_.current_tex_line = _sage_const_243 
 _st_.inline(_sage_const_22 , latex(p3f1))
except:
 _st_.goboom(_sage_const_243 )
try:
 _st_.current_tex_line = _sage_const_243 
 _st_.inline(_sage_const_23 , latex(p3l1))
except:
 _st_.goboom(_sage_const_243 )
try:
 _st_.current_tex_line = _sage_const_243 
 _st_.inline(_sage_const_24 , latex(p3r1))
except:
 _st_.goboom(_sage_const_243 )
try:
 _st_.current_tex_line = _sage_const_244 
 _st_.inline(_sage_const_25 , latex(p3f2))
except:
 _st_.goboom(_sage_const_244 )
try:
 _st_.current_tex_line = _sage_const_244 
 _st_.inline(_sage_const_26 , latex(p3r1))
except:
 _st_.goboom(_sage_const_244 )
try:
 _st_.current_tex_line = _sage_const_244 
 _st_.inline(_sage_const_27 , latex(p3r2))
except:
 _st_.goboom(_sage_const_244 )
try:
 _st_.current_tex_line = _sage_const_245 
 _st_.inline(_sage_const_28 , latex(p3f3))
except:
 _st_.goboom(_sage_const_245 )
try:
 _st_.current_tex_line = _sage_const_245 
 _st_.inline(_sage_const_29 , latex(p3r2))
except:
 _st_.goboom(_sage_const_245 )
try:
 _st_.current_tex_line = _sage_const_245 
 _st_.inline(_sage_const_30 , latex(p3r3))
except:
 _st_.goboom(_sage_const_245 )
try:
 _st_.current_tex_line = _sage_const_249 
 _st_.inline(_sage_const_31 , latex(p3eval))
except:
 _st_.goboom(_sage_const_249 )
try:
 _st_.current_tex_line = _sage_const_249 
 _st_.inline(_sage_const_32 , latex(p3ans))
except:
 _st_.goboom(_sage_const_249 )
try:
 _st_.current_tex_line = _sage_const_264 
 _st_.inline(_sage_const_33 , latex(p4f1))
except:
 _st_.goboom(_sage_const_264 )
try:
 _st_.current_tex_line = _sage_const_264 
 _st_.inline(_sage_const_34 , latex(p4l1))
except:
 _st_.goboom(_sage_const_264 )
try:
 _st_.current_tex_line = _sage_const_264 
 _st_.inline(_sage_const_35 , latex(p4r1))
except:
 _st_.goboom(_sage_const_264 )
try:
 _st_.current_tex_line = _sage_const_265 
 _st_.inline(_sage_const_36 , latex(p4f2))
except:
 _st_.goboom(_sage_const_265 )
try:
 _st_.current_tex_line = _sage_const_265 
 _st_.inline(_sage_const_37 , latex(p4r1))
except:
 _st_.goboom(_sage_const_265 )
try:
 _st_.current_tex_line = _sage_const_265 
 _st_.inline(_sage_const_38 , latex(p4r2))
except:
 _st_.goboom(_sage_const_265 )
try:
 _st_.current_tex_line = _sage_const_266 
 _st_.inline(_sage_const_39 , latex(p4f3))
except:
 _st_.goboom(_sage_const_266 )
try:
 _st_.current_tex_line = _sage_const_266 
 _st_.inline(_sage_const_40 , latex(p4r2))
except:
 _st_.goboom(_sage_const_266 )
try:
 _st_.current_tex_line = _sage_const_266 
 _st_.inline(_sage_const_41 , latex(p4r3))
except:
 _st_.goboom(_sage_const_266 )
try:
 _st_.current_tex_line = _sage_const_270 
 _st_.inline(_sage_const_42 , latex(p4eval))
except:
 _st_.goboom(_sage_const_270 )
try:
 _st_.current_tex_line = _sage_const_270 
 _st_.inline(_sage_const_43 , latex(p4ans))
except:
 _st_.goboom(_sage_const_270 )
try:
 _st_.current_tex_line = _sage_const_285 
 _st_.inline(_sage_const_44 , latex(p5f1))
except:
 _st_.goboom(_sage_const_285 )
try:
 _st_.current_tex_line = _sage_const_285 
 _st_.inline(_sage_const_45 , latex(p5l1))
except:
 _st_.goboom(_sage_const_285 )
try:
 _st_.current_tex_line = _sage_const_285 
 _st_.inline(_sage_const_46 , latex(p5r1))
except:
 _st_.goboom(_sage_const_285 )
try:
 _st_.current_tex_line = _sage_const_286 
 _st_.inline(_sage_const_47 , latex(p5f2))
except:
 _st_.goboom(_sage_const_286 )
try:
 _st_.current_tex_line = _sage_const_286 
 _st_.inline(_sage_const_48 , latex(p5r1))
except:
 _st_.goboom(_sage_const_286 )
try:
 _st_.current_tex_line = _sage_const_286 
 _st_.inline(_sage_const_49 , latex(p5r2))
except:
 _st_.goboom(_sage_const_286 )
try:
 _st_.current_tex_line = _sage_const_287 
 _st_.inline(_sage_const_50 , latex(p5f3))
except:
 _st_.goboom(_sage_const_287 )
try:
 _st_.current_tex_line = _sage_const_287 
 _st_.inline(_sage_const_51 , latex(p5r2))
except:
 _st_.goboom(_sage_const_287 )
try:
 _st_.current_tex_line = _sage_const_287 
 _st_.inline(_sage_const_52 , latex(p5r3))
except:
 _st_.goboom(_sage_const_287 )
try:
 _st_.current_tex_line = _sage_const_291 
 _st_.inline(_sage_const_53 , latex(p5eval))
except:
 _st_.goboom(_sage_const_291 )
try:
 _st_.current_tex_line = _sage_const_291 
 _st_.inline(_sage_const_54 , latex(p5ans))
except:
 _st_.goboom(_sage_const_291 )
_st_.endofdoc()

