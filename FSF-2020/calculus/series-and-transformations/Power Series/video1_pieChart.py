from manimlib.imports import *


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
    expansion.scale(0.7)
    return expansion

class pieChart(Scene):
    def construct(self):
        circle1=Circle(radius=3,color=BLUE)
        powerText=TextMobject("Power Series")
        powerText.scale(0.8)
        self.play(FadeIn(powerText))
        self.play(ShowCreation(circle1))
        self.wait(1)

        powerGroup=VGroup(circle1,powerText)

        self.play(ApplyMethod(powerGroup.scale,0.5))
        self.play(ApplyMethod(powerGroup.move_to,2.2*UP))
        self.wait(0.5)
        expansion_power_coeff=[]
        variables_power=[]
        expansion_power=formFormula(expansion_power_coeff,variables_power)
        self.play(ReplacementTransform(powerText,expansion_power))
        self.wait(1)

        circle2=Circle(radius=1.5)
        circle2.shift(2.2*UP)
        expansion_geo_coeff=[0]*3
        variables_geo=[0]*3
        arrow1_2=Line(start=0.7*UP,end=2.5*LEFT)
        expansion_geo_coeff=[TextMobject("${ a }_{ 0 }$"),TextMobject("${ a }_{ 1 }$"),TextMobject("${ a }_{ 2 }$")]
        for i in range(0,3):
            expansion_geo_coeff[i].set_color(GOLD_A)
        variables_geo=[TextMobject("+"),TextMobject("${ x }$+"),TextMobject("${ x }^{ 2 }$")]
        expansion_geo_coeff[0].shift(2.2*UP+1.6*LEFT)
        for i in range(0,3):
            variables_geo[i].next_to(expansion_geo_coeff[i],buff=0.1)
            if i!=2:
                expansion_geo_coeff[i+1].next_to(variables_geo[i],buff=0.1)
        dots=TextMobject("...")
        dots.next_to(variables_geo[2])
        expansion_geo=VGroup(expansion_geo_coeff[0],expansion_geo_coeff[1],expansion_geo_coeff[2],variables_geo[0],variables_geo[1],variables_geo[2],dots)
        expansion_geo.scale(0.7)

        self.play(ApplyMethod(circle2.shift,4*LEFT+2.5*DOWN),ApplyMethod(expansion_geo.shift,4*LEFT+2.5*DOWN))
        self.add(arrow1_2)
        self.wait(1)

        ones=[TextMobject("1"),TextMobject("1"),TextMobject("1")]
        for i in range(0,3):
            ones[i].set_color(GOLD_A)
        ones[0].shift(0.3*DOWN,5*LEFT)
        ones[1].next_to(ones[0],buff=0.5)
        ones[2].next_to(ones[1],buff=0.7)
        self.play(ReplacementTransform(expansion_geo_coeff[0],ones[0]),ReplacementTransform(expansion_geo_coeff[1],ones[1]),ReplacementTransform(expansion_geo_coeff[2],ones[2]))
        self.wait(1)
        expansion_geo=VGroup(ones[0],ones[1],ones[2],variables_geo[0],variables_geo[1],variables_geo[2],dots)

        expansion_geo_final=TextMobject("$1+x+{ x }^{ 2 }..$")
        expansion_geo_final.scale(0.8)
        expansion_geo_final.shift(0.3*DOWN+4*LEFT)
        self.play(ReplacementTransform(expansion_geo,expansion_geo_final))
        self.wait(1)

        circle3=Circle(radius=1.5,color=GREEN)
        circle3.shift(2.2*UP)
        expansion_taylor_coeff=[0]*3
        variables_taylor=[0]*3
        arrow1_3=Line(start=0.7*UP,end=DOWN*0.3)
        expansion_taylor_coeff=[TextMobject("${ a }_{ 0 }$"),TextMobject("${ a }_{ 1 }$"),TextMobject("${ a }_{ 2 }$")]
        for i in range(0,3):
            expansion_taylor_coeff[i].set_color(GOLD_A)
        variables_taylor=[TextMobject("+"),TextMobject("${ x }$+"),TextMobject("${ x }^{ 2 }$")]
        expansion_taylor_coeff[0].shift(2.2*UP+1.6*LEFT)
        for i in range(0,3):
            variables_taylor[i].next_to(expansion_taylor_coeff[i],buff=0.1)
            if i!=2:
                expansion_taylor_coeff[i+1].next_to(variables_taylor[i],buff=0.1)
        dots=TextMobject("...")
        dots.next_to(variables_taylor[2])
        expansion_taylor=VGroup(expansion_taylor_coeff[0],expansion_taylor_coeff[1],expansion_taylor_coeff[2],variables_taylor[0],variables_taylor[1],variables_taylor[2],dots)
        expansion_taylor.scale(0.7)

        self.play(ApplyMethod(circle3.shift,4*DOWN),ApplyMethod(expansion_taylor.shift,4*DOWN))
        self.add(arrow1_3)
        self.wait(1)        

        differentials=[TextMobject("$f(0)$"),TextMobject("${ f'\left( 0 \\right) }$"),TextMobject("$\\frac { f''\left( 0 \\right)  }{ 2! }$")]
        for i in range(0,3):
            differentials[i].set_color(GOLD_A)
        differentials[0].shift(1.8*DOWN+1.15*LEFT)
        differentials[1].shift(1.8*DOWN+0.45*LEFT)
        differentials[2].shift(1.8*DOWN+0.45*RIGHT)
        differentials[0].scale(0.35)
        differentials[1].scale(0.35)
        differentials[2].scale(0.35)
        self.play(ReplacementTransform(expansion_taylor_coeff[0],differentials[0]),ReplacementTransform(expansion_taylor_coeff[1],differentials[1]),ReplacementTransform(expansion_taylor_coeff[2],differentials[2]))
        self.wait(2)
        expansion_taylor_final=VGroup(differentials[0],differentials[1],differentials[2],variables_taylor[0],variables_taylor[1],variables_taylor[2],dots)

        self.play(FadeOut(expansion_geo_final),FadeOut(expansion_taylor_final))
        geoText=TextMobject("Geometric Series")
        geoText.scale(0.7)
        geoText.shift(4*LEFT+0.3*DOWN)
        taylorText=TextMobject("Taylor Series")
        taylorText.scale(0.7)
        taylorText.shift(1.8*DOWN)
        self.play(FadeIn(geoText),FadeIn(taylorText))
        self.wait(1)

        soOntext=TextMobject("So on..!")
        soOntext.shift(4*RIGHT)
        soOntext.scale(0.8)
        self.play(FadeIn(soOntext))
        self.wait(2)
