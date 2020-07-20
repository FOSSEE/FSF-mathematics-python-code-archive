from manimlib.imports import *
class RiemannRectanglesAnimation(GraphScene):
    CONFIG = {
        "y_max": 5,
        "x_max": 6,
        "x_min": 0,
        "y_min": 0,
        "x_axis_width": 5,
        "y_axis_height": 5,
        "init_dx":0.5,
        "graph_origin": ORIGIN+2*DOWN+6*LEFT,
    }
    def construct(self):
        self.setup_axes()
        def func(x):
            return  0.1*(x)*(x-3)*(x-7)+3

        graph1=self.get_graph(func,x_min=0,x_max=6)
        kwargs = {
            "x_min" : 1.5,
            "x_max" : 5.5,
            "fill_opacity" : 0.75,
            "stroke_width" : 0.25,
            "input_sample_type": "right",
        }
        flat_rectangles1 = self.get_riemann_rectangles(self.get_graph(lambda x : 0),dx=self.init_dx,start_color=invert_color(PURPLE),end_color=invert_color(ORANGE),**kwargs)
        riemann_rectangles_list1 = self.get_riemann_rectangles_list(graph1,6,max_dx=self.init_dx,power_base=2,start_color=PURPLE,end_color=ORANGE,**kwargs)
        self.add(graph1)
        self.graph_origin = ORIGIN+2*DOWN+1*RIGHT
        self.setup_axes()
        graph2=self.get_graph(func,x_min=0,x_max=6)
        kwargs = {
            "x_min" : 1.5,
            "x_max" : 5.5,
            "fill_opacity" : 0.75,
            "stroke_width" : 0.25,
            "input_sample_type": "left",
        }
        flat_rectangles2 = self.get_riemann_rectangles(self.get_graph(lambda x : 0),dx=self.init_dx,start_color=invert_color(PURPLE),end_color=invert_color(ORANGE),**kwargs)
        riemann_rectangles_list2 = self.get_riemann_rectangles_list(graph2,6,max_dx=self.init_dx,power_base=2,start_color=PURPLE,end_color=ORANGE,**kwargs)
        self.add(graph2)
        text1 = TextMobject("Left Riemann sum").move_to(np.array([-3,-2.5,0]))
        text2 = TextMobject("Right Riemann sum").move_to(np.array([4,-2.5,0]))
        grp1 = VGroup(text1, text2)
        text3 = TexMobject(r"n \rightarrow \infty").move_to(np.array([0, -3, 0]))
        text4 = TextMobject("Left and Right Riemann sums are equal").move_to(np.array([0, -3, 0]))
        text5 = TextMobject("Hence function is Riemann integrable and value of integral equals area covered").move_to(np.array([0, -3, 0])).scale(0.6)
        grp2 = VGroup(text1, text2, text3)
        # Show Riemann rectangles
        self.play(ReplacementTransform(flat_rectangles1,riemann_rectangles_list1[0]), ReplacementTransform(flat_rectangles2, riemann_rectangles_list2[0]))
        self.wait()
        self.play(ShowCreation(grp1))
        for r in range(1,len(riemann_rectangles_list1)-3):
            self.transform_between_riemann_rects(riemann_rectangles_list1[r-1],riemann_rectangles_list1[r],replace_mobject_with_target_in_scene = True,)
            self.transform_between_riemann_rects(riemann_rectangles_list2[r-1],riemann_rectangles_list2[r],replace_mobject_with_target_in_scene = True,)
        self.play(ShowCreation(text3))
        for r in range(len(riemann_rectangles_list1)-3,len(riemann_rectangles_list1)):
            self.transform_between_riemann_rects(riemann_rectangles_list1[r-1],riemann_rectangles_list1[r],replace_mobject_with_target_in_scene = True,)
            self.transform_between_riemann_rects(riemann_rectangles_list2[r-1],riemann_rectangles_list2[r],replace_mobject_with_target_in_scene = True,)
        self.wait(2)
        grp3 = VGroup(graph1, riemann_rectangles_list1[5])
        grp4 = VGroup(graph2, riemann_rectangles_list2[5])
        self.play(ReplacementTransform(grp2, text4))
        self.wait(2)
        self.play(ReplacementTransform(text4, text5), ApplyMethod(grp4.shift, 7*LEFT), ApplyMethod(self.axes.shift, 7*LEFT), )
        self.wait(4)