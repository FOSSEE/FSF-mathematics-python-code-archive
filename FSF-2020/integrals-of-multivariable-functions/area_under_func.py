from manimlib.imports import *


class AreaUnderIntegral(GraphScene):
    CONFIG = {
        "x_min" : 0,
        "x_max" : 5,
        "y_min" : 0,
        "y_max" : 6,
        "Func":lambda x : 1+x**2*np.exp(-.15*x**2)
    }  

    def construct(self):
        X = RIGHT*self.x_axis_width/(self.x_max- self.x_min)
        Y = UP*self.y_axis_height/(self.y_max- self.y_min)
        
        int_area_sym=TextMobject("$$\int_{a}^b f(x)dx$$").shift(2*UP)
        area_mean_text = TextMobject(r"means area under the curve of $f(x)$ \\ in the region $a\leq x\leq b$").next_to(int_area_sym,DOWN)
        
        opening_text=VGroup(*[int_area_sym,area_mean_text])
        self.play(Write(opening_text),run_time=4)
        self.wait(2)
        self.play(FadeOut(opening_text))

        self.setup_axes(animate=True)
        func= self.get_graph(self.Func, x_min=0,x_max=5)
        self.curve=func 
        
        func_text = TextMobject(r"$y = f(x)$").next_to(func,UP)
        min_lim = self.get_vertical_line_to_graph(1,func,DashedLine,color=YELLOW)
        tick_a=TextMobject(r"$a$").next_to(min_lim,DOWN)
        max_lim = self.get_vertical_line_to_graph(4,func,DashedLine,color=YELLOW)
        tick_b=TextMobject(r"$b$").next_to(max_lim,DOWN)
        
 #       area = self.get_area(func,1,4)

        self.play(ShowCreation(func), ShowCreation(func_text))
	
        self.wait(2)
        self.play(ShowCreation(min_lim),Write(tick_a), ShowCreation(max_lim),Write(tick_b),run_time=0.5)
        
  
        approx_text=TextMobject(r"The area can be approximated as \\ sum of small rectangles").next_to(func,4*Y) 
        self.play(Write(approx_text))
        
        rect_list = self.get_riemann_rectangles_list(
            self.curve, 5, 
            max_dx = 0.25,
            x_min = 1,
            x_max = 4,
        )
        flat_graph = self.get_graph(lambda t : 0)
        rects = self.get_riemann_rectangles( flat_graph, x_min = 1, x_max = 4, dx = 0.5)
        for new_rects in rect_list:
            new_rects.set_fill(opacity = 0.8)
            rects.align_submobjects(new_rects)
            for alt_rect in rects[::2]:
                alt_rect.set_fill(opacity = 0)
            self.play(Transform(
                rects, new_rects,
                run_time = 1.5,
                lag_ratio = 0.5
            ))
        conclude_text=TextMobject(r"Making the rectangles infinitesimally thin \\ we get the real area under the curve.").next_to(func,4*Y) 
        self.play(Transform(approx_text,conclude_text))
        self.wait(3)
        int_area_sym.next_to(self.curve,IN)
        self.play(Transform(conclude_text,int_area_sym))
        
 #       self.play(ShowCreation(area))
        self.wait(3)
        
#uploaded by Somnath Pandit.FSF2020_Double_Integral
