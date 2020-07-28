from manimlib.imports import *

class SineVectors(GraphScene):
    CONFIG = {
    "x_min": 0,
    "x_max": 10,
    "y_min": -5,
    "y_max": 5,
    "graph_origin": ORIGIN+4*LEFT,
    "x_axis_width": 7,
    "y_axis_height": 7,
    }
    def construct(self):



        XTD = self.x_axis_width/(self.x_max - self.x_min)
        YTD = self.y_axis_height/(self.y_max - self.y_min)

        self.setup_axes(animate = True)

        sine = self.get_graph(lambda x :  np.pi*np.sin(x), x_min = 0, x_max = 6.3, color = GREEN)


        dot1 = Dot().rotate(PI/2).set_color(RED_C)
        alpha1 = ValueTracker(0)
        vector1 = self.get_vector(alpha1.get_value(),sine)
        dot1.add_updater(lambda m: m.move_to(vector1.get_end()))
        self.play(
            ShowCreation(sine),
            GrowFromCenter(dot1),
            GrowArrow(vector1)
            )
        vector1.add_updater(
            lambda m: m.become(
                    self.get_vector(alpha1.get_value()%1,sine)
                )
            )
        self.add(vector1,dot1)
        self.play(alpha1.increment_value, 1, run_time=5, rate_func=linear)
        

        self.play(FadeOut(vector1), FadeOut(dot1), FadeOut(sine))

        self.wait()


        sine1 = self.get_graph(lambda x :  np.pi*np.sin(x), x_min = 0, x_max = 1.575, color = GREEN_C)

        point1 = Dot().shift(self.graph_origin+np.pi*YTD*UP + 1.575*XTD*RIGHT)
        point1_lab = TextMobject(r"$t = (\frac{\pi}{2})$", color = GREY).scale(0.6).next_to(point1, 0.5*UP) 


        vector1 = Arrow(self.graph_origin, self.graph_origin+np.pi*YTD*UP + 1.575*XTD*RIGHT, buff=0, color = RED_C, tip_length = 0.25)
        vector1_lab = TextMobject(r"$r(\frac{\pi}{2})$", color = RED).scale(0.7).move_to(self.graph_origin+1.5*XTD*RIGHT+ 1.5*YTD*UP) 

        self.play(GrowArrow(vector1),Write(vector1_lab))
        self.play(ShowCreation(point1), Write(point1_lab))
        self.play(ShowCreation(sine1))
        self.wait(1)


        sine2 = self.get_graph(lambda x :  np.pi*np.sin(x), x_min = 1.575, x_max = 3.15, color = GREEN_C)

        point2 = Dot().shift(self.graph_origin+3.15*XTD*RIGHT)
        point2_lab = TextMobject(r"$t = (\pi)$", color = GREY).scale(0.6).next_to(point2, 0.5*UP+0.5*RIGHT) 

        vector2 = Arrow(self.graph_origin, self.graph_origin+3.15*XTD*RIGHT, buff=0, color = BLUE, tip_length = 0.25)
        vector2_lab = TextMobject(r"$r(\pi)$", color = BLUE).scale(0.7).move_to(self.graph_origin+1.5*XTD*RIGHT+ 0.4*YTD*UP) 

        self.play(GrowArrow(vector2),Write(vector2_lab))
        self.play(ShowCreation(point2), Write(point2_lab))
        self.play(ShowCreation(sine2))
        self.wait(1)


        sine3 = self.get_graph(lambda x :  np.pi*np.sin(x), x_min = 3.15, x_max = 4.725, color = GREEN_C)

        point3 = Dot().shift(self.graph_origin+np.pi*YTD*DOWN + 4.725*XTD*RIGHT)
        point3_lab = TextMobject(r"$t = (\frac{3\pi}{2})$", color = GREY).scale(0.6).next_to(point3, 0.5*DOWN) 

        vector3 = Arrow(self.graph_origin, self.graph_origin+np.pi*YTD*DOWN + 4.725*XTD*RIGHT, buff=0, color = YELLOW_C, tip_length = 0.25)
        vector3_lab = TextMobject(r"$r(\frac{3\pi}{2})$", color = YELLOW_C).scale(0.7).move_to(self.graph_origin+2.5*XTD*RIGHT+ 1*YTD*DOWN) 

        self.play(GrowArrow(vector3),Write(vector3_lab))
        self.play(ShowCreation(point3), Write(point3_lab))
        self.play(ShowCreation(sine3))
        self.wait(1)


        sine4 = self.get_graph(lambda x :  np.pi*np.sin(x), x_min = 4.725, x_max = 6.3, color = GREEN_C)

        point4 = Dot().shift(self.graph_origin+6.3*XTD*RIGHT)
        point4_lab = TextMobject(r"$t = (2\pi)$", color = GREY).scale(0.6).next_to(point4, 0.5*UP+0.5*RIGHT) 

        vector4 = Arrow(self.graph_origin, self.graph_origin+6.3*XTD*RIGHT, buff=0, color = PURPLE, tip_length = 0.25)
        vector4_lab = TextMobject(r"$r(2\pi)$", color = PURPLE).scale(0.7).move_to(self.graph_origin+4.5*XTD*RIGHT+ 0.4*YTD*DOWN) 

        self.play(GrowArrow(vector4),Write(vector4_lab))
        self.play(ShowCreation(point4), Write(point4_lab))
        self.play(ShowCreation(sine4))
        self.wait(3)

        self.play(FadeOut(sine1), FadeOut(point1), FadeOut(point1_lab), FadeOut(vector1), FadeOut(vector1_lab),
                  FadeOut(sine2), FadeOut(point2), FadeOut(point2_lab), FadeOut(vector2), FadeOut(vector2_lab),
                  FadeOut(sine3), FadeOut(point3), FadeOut(point3_lab), FadeOut(vector3), FadeOut(vector3_lab),
                  FadeOut(sine4), FadeOut(point4), FadeOut(point4_lab), FadeOut(vector4), FadeOut(vector4_lab))

        

    def get_vector(self, proportion, curve):
        vector = Arrow(np.array([-4,0,0]), curve.point_from_proportion(proportion), color = ORANGE, buff=0, tip_length = 0.25)
        return vector    

