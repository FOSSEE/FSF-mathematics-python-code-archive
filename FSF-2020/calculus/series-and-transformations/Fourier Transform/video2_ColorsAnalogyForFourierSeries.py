from manimlib.imports import*
import numpy as np

def func(t,n1,n2):
    s=0
    for i in range(n1,n2+1):
        s+=((-2/(i*np.pi))*((-1)**i)*np.sin(2*np.pi*i*t))
    return s

class divideColors(GraphScene):
    CONFIG = {
        "x_min": -2,
        "x_max": 2,
        "y_min": -1,
        "y_max": 1,
        "graph_origin": ORIGIN,
        "function_color": RED,
        "axes_color": BLUE,
        "x_axis_label": "$t$",
        "y_axis_label": "$y$",
        "x_labeled_nums": range(-1, 2, 1),
        "x_axis_width": 3,
        "y_axis_height": 2
    }
    def construct(self):
        text1a=TextMobject("Consider dividing a","mixture of colors")
        text1b=TextMobject("into its","components")
        text1a.scale(0.8)
        text1b.scale(0.8)
        text1a.shift(UP)
        text1b.shift(0.3*UP)
        text1a.set_color_by_tex_to_color_map({"mixture of colors":[GREEN,RED,BLUE,YELLOW]})
        text1b.set_color_by_tex_to_color_map({"components":GREEN})
        self.play(Write(text1a))
        self.play(FadeIn(text1b))
        self.wait(0.8)

        self.play(FadeOut(text1a),FadeOut(text1b))

        mainCircle=Circle(radius=1.4,color=BLACK,fill_color=[PURPLE_E,PURPLE_D,RED_B,ORANGE,YELLOW_B,YELLOW_D,GREEN_A,GREEN_C],fill_opacity=0.8)
        self.play(ShowCreation(mainCircle))
        self.wait(1)
        mainCirclea=Circle(radius=1.4,color=BLACK,fill_color=[RED_B,ORANGE,YELLOW_B,YELLOW_D,GREEN_A,GREEN_C],fill_opacity=0.8)
        mainCircleb=Circle(radius=1.4,color=BLACK,fill_color=[YELLOW_B,YELLOW_D,GREEN_A,GREEN_C],fill_opacity=0.8)
        mainCirclec=Circle(radius=1.4,color=BLACK,fill_color=[GREEN_A,GREEN_C],fill_opacity=0.8)
        mainCircled=Circle(radius=1.4,color=BLACK,fill_color=[],fill_opacity=0.8)
        
        c1=Circle(radius=0.5,color=PURPLE_E,fill_color=PURPLE_E,fill_opacity=0.8)
        c2=Circle(radius=0.5,color=PURPLE_D,fill_color=PURPLE_D,fill_opacity=0.8)
        c3=Circle(radius=0.5,color=RED_D,fill_color=RED_B,fill_opacity=0.8)
        c4=Circle(radius=0.5,color=ORANGE,fill_color=ORANGE,fill_opacity=0.8)
        c5=Circle(radius=0.5,color=YELLOW_B,fill_color=YELLOW_B,fill_opacity=0.8)
        c6=Circle(radius=0.5,color=YELLOW_D,fill_color=YELLOW_D,fill_opacity=0.8)
        c7=Circle(radius=0.5,color=GREEN_A,fill_color=GREEN_A,fill_opacity=0.8)
        c8=Circle(radius=0.5,color=GREEN_C,fill_color=GREEN_C,fill_opacity=0.8)

        self.play(ApplyMethod(c1.shift,3*UP+LEFT),ApplyMethod(c2.shift,3*UP+RIGHT),ReplacementTransform(mainCircle,mainCirclea))
        self.wait(0.8)

        self.play(ApplyMethod(c3.shift,UP+3*LEFT),ApplyMethod(c4.shift,DOWN+3*LEFT),ReplacementTransform(mainCirclea,mainCircleb))
        self.wait(0.8)

        self.play(ApplyMethod(c5.shift,3*DOWN+LEFT),ApplyMethod(c6.shift,3*DOWN+RIGHT),ReplacementTransform(mainCircleb,mainCirclec))
        self.wait(0.8)

        self.play(ApplyMethod(c7.shift,3*RIGHT+UP),ApplyMethod(c8.shift,3*RIGHT+DOWN),ReplacementTransform(mainCirclec,mainCircled))
        self.wait(1)

        text2=TextMobject("Similarly,").scale(0.8).shift(UP).set_color(RED)

        self.play(FadeOut(c1),FadeOut(c2),FadeOut(c3),FadeOut(c4),FadeOut(c5),FadeOut(c6),FadeOut(c7),FadeOut(c8))
        self.play(Write(text2))
        self.wait(0.8)
        self.play(FadeOut(text2))
        

        coeff=[
            TextMobject("$\\frac { -2 }{ \pi  } \sum _{ n=1 }^{ 24 }{ \\frac { { -1 }^{ n } }{ n } sin(2\pi nt) }$").scale(0.2).shift(RIGHT+UP),
            TextMobject("$\\frac { 2 }{ \pi } sin(2\pi t)$").scale(0.3).shift(RIGHT+UP+4*LEFT+UP),
            TextMobject("$\\frac { -2 }{ \pi  } \sum _{ n=2 }^{ 24 }{ \\frac { { -1 }^{ n } }{ n } sin(2\pi nt) }$").scale(0.2).shift(RIGHT+UP),
            TextMobject("$\\frac { -1 }{ \pi  } sin(4\pi t)$").scale(0.3).shift(RIGHT+UP+4*RIGHT+UP),
            TextMobject("$\\frac { -2 }{ \pi  } \sum _{ n=3 }^{ 24 }{ \\frac { { -1 }^{ n } }{ n } sin(2\pi nt) }$").scale(0.2).shift(RIGHT+UP),
            TextMobject("$\\frac { 2 }{ 3\pi  } sin(6\pi t)$").scale(0.3).shift(RIGHT+UP+4*LEFT+2*DOWN),
            TextMobject("$\\frac { -2 }{ \pi  } \sum _{ n=4 }^{ 24 }{ \\frac { { -1 }^{ n } }{ n } sin(2\pi nt) }$").scale(0.2).shift(RIGHT+UP),
            TextMobject("$\\frac { -1 }{ 2\pi  } sin(8\pi t)$").scale(0.3).shift(RIGHT+UP+4*RIGHT+2*DOWN),
            TextMobject("$\\frac { -2 }{ \pi  } \sum _{ n=5 }^{ 24 }{ \\frac { { -1 }^{ n } }{ n } sin(2\pi nt) }$").scale(0.2).shift(RIGHT+UP),
            TextMobject("$\\frac { 2 }{ 5\pi  } sin(10\pi t)$").scale(0.3).shift(RIGHT+UP+2.5*UP),
            TextMobject("$\\frac { -2 }{ \pi  } \sum _{ n=6 }^{ 24 }{ \\frac { { -1 }^{ n } }{ n } sin(2\pi nt) }$").scale(0.2).shift(RIGHT+UP),
            TextMobject("$\\frac { -1 }{ 3\pi  } sin(12\pi t)$").scale(0.3).shift(RIGHT+UP+2.5*DOWN),
            TextMobject("$\\frac { -2 }{ \pi  } \sum _{ n=7 }^{ 24 }{ \\frac { { -1 }^{ n } }{ n } sin(2\pi nt) }$").scale(0.2).shift(RIGHT+UP),
        ]

        axes=[]
        self.setup_axes(scalee=1)
        axes.append(self.axes)
        graphs=[self.get_graph(lambda x:func(x,1,24),x_min=-1,x_max=1).set_color([DARK_BROWN,GREEN_E,GREEN_C,GOLD_E,GOLD_C,ORANGE,RED_C]),
                self.get_graph(lambda x:func(x,2,24),x_min=-1,x_max=1).set_color([DARK_BROWN,GREEN_C,GOLD_E,GOLD_C,ORANGE,RED_C]),
                self.get_graph(lambda x:func(x,3,24),x_min=-1,x_max=1).set_color([DARK_BROWN,GOLD_E,GOLD_C,ORANGE,RED_C]),
                self.get_graph(lambda x:func(x,4,24),x_min=-1,x_max=1).set_color([DARK_BROWN,GOLD_C,ORANGE,RED_C]),
                self.get_graph(lambda x:func(x,5,24),x_min=-1,x_max=1).set_color([DARK_BROWN,ORANGE,RED_C]),
                self.get_graph(lambda x:func(x,6,24),x_min=-1,x_max=1).set_color([DARK_BROWN,RED_C]),
                self.get_graph(lambda x:func(x,7,24),x_min=-1,x_max=1).set_color(DARK_BROWN)
                ]
        #self.y_axis_label="$\\frac { 2 }{ \pi } sin(2\pi t)$"
        self.setup_axes(scalee=1)
        axes.append(self.axes)
        graph1=self.get_graph(lambda x:func(x,1,1),x_min=-1,x_max=1,color=GREEN_E)
        #self.y_axis_label="$\\frac { -1 }{ \pi  } sin(4\pi t)$"
        self.setup_axes(scalee=1)
        axes.append(self.axes)
        graph2=self.get_graph(lambda x:func(x,2,2),x_min=-1,x_max=1,color=GREEN_C)
        #self.y_axis_label="$\\frac { 2 }{ 3\pi  } sin(6\pi t)$"
        self.setup_axes(scalee=1)
        axes.append(self.axes)
        graph3=self.get_graph(lambda x:func(x,3,3),x_min=-1,x_max=1,color=GOLD_E)
        #self.y_axis_label="$\\frac { -1 }{ 2\pi  } sin(8\pi t)$"
        self.setup_axes(scalee=1)
        axes.append(self.axes)
        graph4=self.get_graph(lambda x:func(x,4,4),x_min=-1,x_max=1,color=GOLD_C)
        #self.y_axis_label="$\\frac { 2 }{ 5\pi  } sin(10\pi t)$"
        self.setup_axes(scalee=1)
        axes.append(self.axes)
        graph5=self.get_graph(lambda x:func(x,5,5),x_min=-1,x_max=1,color=ORANGE)
        #self.y_axis_label="$\\frac { -1 }{ 3\pi  } sin(12\pi t)$"
        self.setup_axes(scalee=1)
        axes.append(self.axes)
        graph6=self.get_graph(lambda x:func(x,6,6),x_min=-1,x_max=1,color=RED_C)

        groups=[VGroup(axes[1],graph1),VGroup(axes[2],graph2),VGroup(axes[3],graph3),VGroup(axes[4],graph4),
        VGroup(axes[5],graph5),VGroup(axes[6],graph6)]

        self.play(ShowCreation(graphs[0]))
        self.play(Write(coeff[0]))
        self.wait(1)
        # self.play(ApplyMethod(axes[0].scale,0.4),ApplyMethod(graphs[0].scale,0.4),ApplyMethod(axes[1].scale,0.4),
        #         ApplyMethod(axes[2].scale,0.4),ApplyMethod(axes[3].scale,0.4),
        #         ApplyMethod(axes[4].scale,0.4),ApplyMethod(axes[5].scale,0.4),ApplyMethod(axes[6].scale,0.4))
        self.play(ReplacementTransform(graphs[0],graphs[1]),ApplyMethod(groups[0].shift,4*LEFT+UP),ReplacementTransform(coeff[0],coeff[2]),FadeIn(coeff[1]))
        self.play(ReplacementTransform(graphs[1],graphs[2]),ApplyMethod(groups[1].shift,4*RIGHT+UP),ReplacementTransform(coeff[2],coeff[4]),FadeIn(coeff[3]))
        self.play(ReplacementTransform(graphs[2],graphs[3]),ApplyMethod(groups[2].shift,4*LEFT+2*DOWN),ReplacementTransform(coeff[4],coeff[6]),FadeIn(coeff[5]))
        self.play(ReplacementTransform(graphs[3],graphs[4]),ApplyMethod(groups[3].shift,4*RIGHT+2*DOWN),ReplacementTransform(coeff[6],coeff[8]),FadeIn(coeff[7]))
        self.play(ReplacementTransform(graphs[4],graphs[5]),ApplyMethod(groups[4].shift,2.5*UP),ReplacementTransform(coeff[8],coeff[10]),FadeIn(coeff[9]))
        self.play(ReplacementTransform(graphs[5],graphs[6]),ApplyMethod(groups[5].shift,2.5*DOWN),ReplacementTransform(coeff[10],coeff[12]),FadeIn(coeff[11]))

        # self.play(ReplacementTransform(graphs[0],graphs[1]),ApplyMethod(groups[0].shift,3*LEFT))
        # self.play(ReplacementTransform(graphs[0],graphs[1]),)
        # self.play(ReplacementTransform(graphs[0],graphs[1]),)
        # self.play(ReplacementTransform(graphs[0],graphs[1]),)
        # self.play(ReplacementTransform(graphs[0],graphs[1]),)
        # self.play(ReplacementTransform(graphs[0],graphs[1]),)

        

        self.wait(2)
        # self.play(ReplacementTransform(function,const))
        # self.play(ShowCreation(sinx),ShowCreation(cosx))
        # self.play(ShowCreation(sin2x),ShowCreation(cos2x))
        # self.play(ShowCreation(sin3x),ShowCreation(cos3x))
        # self.play(ShowCreation(sin4x),ShowCreation(cos4x))
        # sintext=TextMobject("Infinite","sines").shift(5*RIGHT).set_color_by_tex_to_color_map({"Infinite":[YELLOW,RED],"sines":BLUE})
        # costext=TextMobject("Infinite","cosines").shift(5*LEFT).set_color_by_tex_to_color_map({"Infinite":[YELLOW,RED],"cosines":BLUE})
        # sintext.scale(0.6)
        # costext.scale(0.6)
        # self.play(FadeIn(sintext),FadeIn(costext))
        # self.wait(2)        