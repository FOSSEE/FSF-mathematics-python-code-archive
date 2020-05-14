from manimlib.imports import *

class AreaUnderCurve(GraphScene):
    CONFIG = {
        "x_min" : -1,
        "x_max" : 8,
        "y_min" : -1,
        "y_max" : 6, 
        "y_axis_label": "$y$",
        "x_tick_frequency" : 1,
        "y_tick_frequency" : 1,
        "x_labeled_nums": list(np.arange(-1, 9)),
	    "y_labeled_nums": list(np.arange(-1, 7)),
        "graph_origin": ORIGIN+4*LEFT+2.5*DOWN,    
    }

    def construct(self):
        X = RIGHT*self.x_axis_width/(self.x_max- self.x_min)
        Y = UP*self.y_axis_height/(self.y_max- self.y_min)
        
        sofar_text=TextMobject(r"So far we have integrated  over \\ rectangular regions")
        self.play(Write(sofar_text))
        self.play(sofar_text.to_edge,UP)
        
        self.setup_axes(animate=False)
        
        rect= self.get_graph(
            lambda x : 3,
            x_min = 0,
            x_max = 5,
            color = GREEN)
            
        rect_region = self.get_riemann_rectangles(
            rect, 
            x_min = 0,
            x_max = 5,
            dx =.01,
            start_color = GREEN,
            end_color = GREEN,
            fill_opacity = 0.75,
            stroke_width = 0,
        )
        
        self.play(ShowCreation(rect_region))
        self.wait(.5)
        
        rect_int=TextMobject(r"Here the integration limits are set as").to_edge(UP)
        rect_lim=TextMobject(r"$$\int_{x=0}^{5}\int_{y=0}^{3}$$").next_to(rect_int,DOWN) 
        const_text=TextMobject(r"$\longleftarrow $ \textsf the limits are\\ constant values").next_to(rect_lim,RIGHT)
        
        self.play(ReplacementTransform(sofar_text,rect_int))
        self.wait(1.5)
        self.play(FadeIn(rect_lim))
        self.wait(2)
        self.play(Write(const_text))
        self.wait(2)
        self.play(FadeOut(rect_int), FadeOut(rect_lim),FadeOut(const_text))
        
        
        non_rect_text=TextMobject(r"Now we see how to integrate over \\ non-rectangular regions")
        non_rect_text.to_edge(UP)
        self.play(Write(non_rect_text))
        self.wait(1.5)
        self.play(FadeOut(rect_region))
        
        c1= self.get_graph(
            lambda x : x**2/4,
            x_min = 0,
            x_max = 4,
            color = RED)
            
        c1_region = self.get_riemann_rectangles(
            c1, 
            x_min = 0,
            x_max = 4,
            dx =.01,
            start_color = BLUE,
            end_color = BLUE,
            fill_opacity = 0.75,
            stroke_width = 0,
        )
        self.add(c1,c1_region)
 #       self.wait(2)
        
        c2= self.get_graph(
            lambda x :12-2*x,
            x_min = 4,
            x_max = 6,
            color = RED)
            
        c2_region = self.get_riemann_rectangles(
            c2, 
            x_min = 4,
            x_max = 6,
            dx =.01,
            start_color = BLUE,
            end_color = BLUE,
            fill_opacity = .75,
            stroke_width = 0,
        )
        self.add(c2_region,c2)
        self.wait(1.5)
        c=VGroup(*[c1,c2])
        
        no_func_text=TextMobject(r"The whole region can't be expressed as\\ bounded by a single $f(x)$").next_to(c2,UP,buff=LARGE_BUFF)
        
        self.play(ReplacementTransform(non_rect_text,no_func_text))
        self.wait(1)
        self.play(Indicate(c))
        self.wait(2)
        
        div_region_text=TextMobject(r"So the region is divided into two").next_to(c2,UP,buff=MED_LARGE_BUFF)
        self.play(ReplacementTransform(no_func_text,div_region_text))
        
        c2.set_color(YELLOW)
        self.play(c2_region.set_color,YELLOW)
        c1_text=TextMobject("$\dfrac{x^2}{4}$").next_to(c1,IN)
        c2_text=TextMobject("$12-2x$").next_to(c2,IN+2*X)
        c_text=VGroup(*[c1_text,c2_text])
        
        self.play(FadeIn(c_text))
        self.wait(.4)
        self.play(Indicate(c1),Indicate(c1_text))
        self.play(Indicate(c2),Indicate(c2_text))
        
        easy_text=TextMobject(r"Now the limis can be set easily").next_to(c2,UP,buff=.5)
        self.play(ReplacementTransform(div_region_text,easy_text))
        
        c1_int=TextMobject(r"$$\int_{x=0}^{4}\int_{y=0}^{\dfrac{x^2}{4}}$$").next_to(c1,IN).shift(.5*(-X+1.3*Y))
        c2_int=TextMobject(r"$$\int_{x=4}^{6}\int_{y=0}^{12-2x}$$").next_to(c2,IN+X)
        
        self.play(ReplacementTransform(c1_text,c1_int),ReplacementTransform(c2_text,c2_int))
        self.wait(2)
        
        total_int=TextMobject(r"The total integraton= ").to_edge(UP)
        plus=TextMobject("$$+$$").move_to(self.graph_origin+4*X+5*Y)
        self.play(ReplacementTransform(easy_text,total_int))
        self.play(c2_region.set_color,BLUE)
        self.play(c1_int.next_to,c1,UP,c2_int.next_to,plus,RIGHT, FadeIn(plus))
        
        region=VGroup(*[c1_region,c2_region])
        region.set_color(GREEN)
        self.play(ShowCreation(region))
        self.wait(3)
        
        
	
#uploaded by Somnath Pandit.FSF2020_Double_Integral
        
        
        
        
        
