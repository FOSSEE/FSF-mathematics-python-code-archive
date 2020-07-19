from manimlib.imports import*
import math

def formFormula(coeff_list,variable_list):
    coeff_list=[TextMobject("${ a }_{ 0 }$"),TextMobject("${ a }_{ 1 }$"),TextMobject("${ a }_{ 2 }$")]
    variable_list=[TextMobject("+"),TextMobject("${ x }$+"),TextMobject("${ x }^{ 2 }$")]
    coeff_list[0].shift(2.2*UP+1.6*LEFT)    
    for i in range(0,3):
        coeff_list[i].set_color(GOLD_A)
        variable_list[i].next_to(coeff_list[i],buff=0.1)
        if i!=2:
            coeff_list[i+1].next_to(variable_list[i],buff=0.1)
    dots=TextMobject("...")
    dots.next_to(variable_list[2])
    expansion=VGroup(coeff_list[0],coeff_list[1],coeff_list[2],variable_list[0],variable_list[1],variable_list[2],dots)
    #expansion.scale(0.7)
    return expansion,coeff_list

class intro(Scene):
    def construct(self):
        equation=TextMobject("$f(x)=$","${ e }^{ -x^{ 2 } }$")
        equation.scale(2)
        equation.set_color_by_tex_to_color_map({"${ e }^{ -x^{ 2 } }$":RED})
        text=TextMobject("let $a=0$")
        text.scale(0.7)
        text.shift(DOWN)

        self.play(Write(equation))
        self.wait(0.5)
        self.play(FadeIn(text))
        self.wait(0.7)
        self.play(FadeOut(equation),FadeOut(text))

class graphScene(GraphScene,MovingCameraScene):
    CONFIG = {
        "x_min": -8,
        "x_max": 8,
        "y_min": -8,
        "y_max": 8,
        "graph_origin": ORIGIN,
        "function_color": RED,
        "axes_color": GREEN,
        "x_axis_label": "$x$",
        "y_axis_label": "$y$",
        "exclude_zero_label": True,
        "x_labeled_nums": range(-8, 8, 1),
    }
    def setup(self):
        GraphScene.setup(self)
        MovingCameraScene.setup(self)
    def construct(self):
        x_each_unit = self.x_axis_width / (self.x_max - self.x_min)
        y_each_unit = self.y_axis_height / (self.y_max - self.y_min)   

        equation=TextMobject("$f(x)=$","${ e }^{ -x^{ 2 } }$")
        equation.scale(0.55)
        equation.set_color_by_tex_to_color_map({"${ e }^{ -x^{ 2 } }$":RED})
        text=TextMobject("$a=0$")
        text.scale(0.55)

        equation.shift(3.39*UP+5*LEFT)
        text.shift(2.9*UP+5*LEFT)

        self.add(equation)
        self.add(text)

        generalized_eq_coeff=[]
        variables_eq=[]
        eq,generalized_eq_coeff=formFormula(generalized_eq_coeff,variables_eq)
        trText1=TextMobject("let $T_{ n }(x)$:=")
        eq.next_to(trText1)
        trTextGrup=VGroup(trText1,eq)
        trTextGrup.scale(0.5)
        trTextGrup.to_corner(UP+RIGHT)
        self.play(Write(trTextGrup))
        self.setup_axes(animate=True,scalee=1)
        
        fx=TextMobject("${ e }^{ -x^{ 2 } }$")
        fx.scale(0.5)
        fx.shift(ORIGIN+x_each_unit*7.5*RIGHT+y_each_unit*0.5*UP)
        mainfunction=self.get_graph(lambda x:math.exp(-1*pow(x,2)),color=RED,x_min=-8,x_max=8)
        self.play(ShowCreation(mainfunction))
        self.play(FadeIn(fx))
        self.wait(1)

        coeff=[TextMobject("$1$"),TextMobject("$f'(x)$"),TextMobject("$\\frac { f''(x) }{ 2! } $")]
        coeff[0].shift(3.39*UP+4.88*RIGHT)
        coeff[0].scale(0.5)
        coeff[1].shift(3.39*UP+5.4*RIGHT)
        coeff[1].scale(0.275)
        coeff[2].shift(3.39*UP+6*RIGHT)
        coeff[2].scale(0.28)

        for obj in coeff:
            obj.set_color(GOLD_A)
        group=VGroup(coeff[0],coeff[1],coeff[2])


        firstApprox=[self.get_graph(lambda x:1,color=BLUE)]
        secondApprox=[self.get_graph(lambda x:1,color=BLUE),
                    self.get_graph(lambda x:x+1,color=BLUE),
                    self.get_graph(lambda x:-x+1,color=BLUE)]
        thirdApprox=[self.get_graph(lambda x:1-2*math.pow(x,2),color=BLUE),
                    self.get_graph(lambda x:1-0.1*math.pow(x,2),color=BLUE),
                    self.get_graph(lambda x:1,color=BLUE),
                    self.get_graph(lambda x:1+0.1*math.pow(x,2),color=BLUE),
                    self.get_graph(lambda x:1+math.pow(x,2),color=BLUE)]
                    
        firstGraph=self.get_graph(lambda x:1,color=BLUE)
        secondGraph=self.get_graph(lambda x:1-math.pow(x,2),color=BLUE)

        bottomText1=TextMobject("The polynomial should","satisfy","the function at $x=0$")
        bottomText2=TextMobject("This gives","$a_{ 0 }=1$")
        bottomText3=TextMobject("Now it could be of","any slope!")
        #show graphs of second approx
        bottomText4=TextMobject("Hence the","slopes","should","even match")
        #final graph
        bottomText5=TextMobject("This gives","$a_{ 1 }=0$")
        bottomText6=TextMobject("Since the rate of change of this slope","could vary")
        #show third approx graphs
        bottomText7=TextMobject("Hence the","rate of change of these slopes","should also be","same!")
        #final graph
        bottomText8=TextMobject("This gives","$a_{ 2 }=-1$")

        bottomText1.set_color_by_tex_to_color_map({"satisfy":YELLOW})
        bottomText2.set_color_by_tex_to_color_map({"$a_{ 0 }=1$":BLUE})
        bottomText3.set_color_by_tex_to_color_map({"any slope!":YELLOW})
        bottomText4.set_color_by_tex_to_color_map({"slopes":BLUE,"even match":YELLOW})
        bottomText5.set_color_by_tex_to_color_map({"$a_{ 1 }=0$":BLUE})
        bottomText6.set_color_by_tex_to_color_map({"could vary":YELLOW})
        bottomText7.set_color_by_tex_to_color_map({"rate of change of these slopes":BLUE,"same!":YELLOW})
        bottomText8.set_color_by_tex_to_color_map({"$a_{ 2 }=-1$":BLUE})

        bottomText1.scale(0.4)
        bottomText2.scale(0.5)
        bottomText3.scale(0.4)
        bottomText4.scale(0.4)
        bottomText5.scale(0.5)
        bottomText6.scale(0.4)
        bottomText7.scale(0.4)
        bottomText8.scale(0.5)

        bottomText1.shift(4.5*RIGHT+2.5*DOWN)
        bottomText2.shift(3*RIGHT*x_each_unit+2.5*DOWN*y_each_unit)
        bottomText3.shift(3*RIGHT*x_each_unit+2.5*DOWN*y_each_unit)
        bottomText4.shift(3*RIGHT*x_each_unit+2.5*DOWN*y_each_unit)
        bottomText5.shift(3*RIGHT*x_each_unit+2.5*DOWN*y_each_unit)
        bottomText6.shift(3.7*RIGHT*x_each_unit+2.5*DOWN*y_each_unit)
        bottomText7.shift(3.7*RIGHT*x_each_unit+2.5*DOWN*y_each_unit)
        bottomText8.shift(3.7*RIGHT*x_each_unit+2.5*DOWN*y_each_unit)

        bottomText2.scale(0.7)
        bottomText3.scale(0.7)
        bottomText4.scale(0.7)
        bottomText5.scale(0.7)
        bottomText6.scale(0.7)
        bottomText7.scale(0.7)
        bottomText8.scale(0.7)

        self.play(Write(bottomText1))
        self.wait(0.8)
        #self.activate_zooming(animate=True)
        self.camera_frame.save_state()
        group.move_to(4*y_each_unit*UP+4.6*RIGHT*x_each_unit).scale(0.7)
        self.play(self.camera_frame.set_width, 8,
                self.camera_frame.move_to, x_each_unit*UP,
                ApplyMethod(trTextGrup.move_to,4*y_each_unit*UP+4.1*RIGHT*x_each_unit),
                ApplyMethod(bottomText1.move_to,3.4*RIGHT*x_each_unit+2.5*DOWN*y_each_unit),
                ApplyMethod(equation.shift,1.39*DOWN+2*RIGHT),
                ApplyMethod(text.shift,1.39*DOWN+2*RIGHT),)
        self.play(ApplyMethod(text.scale,0.5),ApplyMethod(equation.scale,0.5),ApplyMethod(bottomText1.scale,0.6),ApplyMethod(trTextGrup.scale,0.7))
        self.play(ApplyMethod(text.shift,0.3*UP))
        self.wait(0.6)
        
        self.play(ShowCreation(firstApprox[0]),ReplacementTransform(bottomText1,bottomText2))
        #change coeff in tn(x)
        self.play(ReplacementTransform(generalized_eq_coeff[0],coeff[0]))
        self.wait(1.5)
        self.play(ReplacementTransform(bottomText2,bottomText3))
        self.wait(0.5)
        self.play(ReplacementTransform(firstApprox[0],secondApprox[1]))
        self.wait(0.5)
        self.play(ReplacementTransform(secondApprox[1],secondApprox[0]))
        self.wait(0.5)
        self.play(ReplacementTransform(secondApprox[0],secondApprox[2]))
        self.wait(1)
        self.play(ReplacementTransform(bottomText3,bottomText4),FadeOut(secondApprox[2]))
        self.wait(1)
        self.play(Write(firstGraph),ReplacementTransform(bottomText4,bottomText5))
        #change a1 coeff
        self.play(ReplacementTransform(generalized_eq_coeff[1],coeff[1]))
        self.wait(1.5)
        self.play(ReplacementTransform(bottomText5,bottomText6))
        self.play(ReplacementTransform(firstGraph,thirdApprox[0]))
        self.wait(0.6)
        self.play(ReplacementTransform(thirdApprox[0],thirdApprox[1]))
        self.wait(0.6)
        self.play(ReplacementTransform(thirdApprox[1],thirdApprox[2]))
        self.wait(0.6)
        self.play(ReplacementTransform(thirdApprox[2],thirdApprox[3]))
        self.wait(0.6)
        self.play(ReplacementTransform(thirdApprox[3],thirdApprox[4]))       
        self.wait(1.5)
        self.play(ReplacementTransform(bottomText6,bottomText7))
        self.wait(1.5)
        self.play(ReplacementTransform(bottomText7,bottomText8),ReplacementTransform(thirdApprox[4],secondGraph))
        self.play(ReplacementTransform(generalized_eq_coeff[2],coeff[2]))
        self.wait(2)

        textFinal=TextMobject("And so on..!")
        textFinal.scale(0.35)
        textFinal.shift(3.7*RIGHT*x_each_unit+2.5*DOWN*y_each_unit)
        self.play(ReplacementTransform(bottomText8,textFinal))
        self.wait(1)
        self.play(FadeOut(equation),FadeOut(text))
        self.play(self.camera_frame.set_width, 15)

        finalFormula=TextMobject("Hence","$T_{ n }(x)$","=","$f(0)+f'(0)x+\\frac { f''(0) }{ 2! }x^2+..+\\frac { { f }^{ n }(0) }{ n! } { x }^{ n }$")
        finalFormula.scale(0.8)
        finalFormula.set_color_by_tex_to_color_map({"$T_{ n }(x)$":GREEN,"$f(0)+f'(0)x+\\frac { f''(0) }{ 2! }x^2+..+\\frac { { f }^{ n }(0) }{ n! } { x }^{ n }$":RED})        

        self.play(FadeOut(self.axes),FadeOut(textFinal),FadeOut(secondGraph),FadeOut(trTextGrup),FadeOut(mainfunction),FadeOut(fx),FadeOut(coeff[0]),FadeOut(coeff[1]),FadeOut(coeff[2]))
        self.play(Write(finalFormula))
        self.wait(2)
  




