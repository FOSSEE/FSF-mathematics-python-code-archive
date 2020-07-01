# Plotting Graphs
from manimlib.imports import *

class PlotGraphs(GraphScene):
    CONFIG = {
    "x_min": -5,
    "x_max": 5,
    "y_min": 0,
    "y_max": 4,
    "graph_origin": ORIGIN + 2.5* DOWN,
    "x_labeled_nums": list(range(-5, 6)),
    "y_labeled_nums": list(range(0, 5)),
    }
    def construct(self):

        topic = TextMobject("Domain and Range")
        topic.scale(2)
        topic.set_color(YELLOW)
        self.play(Write(topic))
        self.play(FadeOut(topic))
        self.wait(1)

        scalar_func_R = TextMobject(r"Scalar Valued Functions in $R$").scale(1.5).set_color_by_gradient(RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE)
        self.play(Write(scalar_func_R))
        self.play(FadeOut(scalar_func_R))
        self.wait(1)


        XTD = self.x_axis_width/(self.x_max- self.x_min)
        YTD = self.y_axis_height/(self.y_max- self.y_min)

        self.setup_axes(animate = True)

        graphobj = self.get_graph(lambda x :  np.sqrt(x + 4), x_min = -4, x_max = 5)
        graph_lab = self.get_graph_label(graphobj, label = r"\sqrt{x + 4}")


        rangeline1 = Arrow(self.graph_origin+2.2*YTD*UP+5*XTD*LEFT, self.graph_origin+4.1*YTD*UP+5*XTD*LEFT)
        rangeline2 = Arrow(self.graph_origin+1.7*YTD*UP+5*XTD*LEFT, self.graph_origin+5*XTD*LEFT)
        rangeline1.set_color(RED)
        rangeline2.set_color(RED)

        rangeMsg = TextMobject(r"Range: $y \geq 0$")
        rangeMsg.move_to(self.graph_origin+2*YTD*UP+5*XTD*LEFT)
        rangeMsg.scale(0.5)
        rangeMsg.set_color(YELLOW)

        domainline1 = Arrow(self.graph_origin+0.6*YTD*DOWN+1.2*XTD*LEFT, self.graph_origin+0.6*YTD*DOWN + 4*XTD*LEFT, buff = 0.1)
        domainline2 = Arrow(self.graph_origin+0.6*YTD*DOWN+1.1*XTD*RIGHT, self.graph_origin+0.6*YTD*DOWN + 5.3*XTD*RIGHT, buff = 0.1)
        domainline1.set_color(PINK)
        domainline2.set_color(PINK)

        domainMsg = TextMobject(r"Domain: $x \geq -4$")
        domainMsg.move_to(self.graph_origin+0.6*YTD*DOWN)
        domainMsg.scale(0.5)
        domainMsg.set_color(GREEN)


    
        
        self.play(ShowCreation(graphobj))
        self.play(ShowCreation(graph_lab))
        self.wait(1)
        self.play(GrowArrow(rangeline1))
        self.play(GrowArrow(rangeline2))
        self.play(Write(rangeMsg))
        self.wait(1)
        self.play(GrowArrow(domainline1))
        self.play(GrowArrow(domainline2))
        self.play(Write(domainMsg))
        self.wait(3)

        self.wait(2)




class PlotSineGraphs(GraphScene):
    CONFIG = {
    "x_min": -8,
    "x_max": 8,
    "y_min": -1,
    "y_max": 1,
    "graph_origin": ORIGIN,
    "x_labeled_nums": list(range(-8, 9)),
    "y_labeled_nums": list(range(-1, 2)),
    }
    def construct(self):
        


        XTD = self.x_axis_width/(self.x_max- self.x_min)
        YTD = self.y_axis_height/(self.y_max- self.y_min)

        self.setup_axes(animate = True)

        sineobj = self.get_graph(lambda x :  np.sin(x), x_min = -7, x_max = 8)
        sine_lab = self.get_graph_label(sineobj, label = "\\sin(x)")


        rangeline1 = Line(8*XTD*LEFT,1*YTD*UP+8*XTD*LEFT)
        rangeline2 = Line(8*XTD*LEFT,1*YTD*DOWN+8*XTD*LEFT)
        rangeline1.set_color(RED)
        rangeline2.set_color(RED)

        rangeMsg = TextMobject(r"Range: $-1 \leq y \leq  1$")
        rangeMsg.move_to(1.1*YTD*UP+8.5*XTD*LEFT)
        rangeMsg.scale(0.5)
        rangeMsg.set_color(YELLOW)


        domainline1 = Arrow(1.1*YTD*DOWN+2*XTD*LEFT, 1.1*YTD*DOWN + 8.5*XTD*LEFT)
        domainline2 = Arrow(1.1*YTD*DOWN+2*XTD*RIGHT, 1.1*YTD*DOWN + 8.5*XTD*RIGHT)
        domainline1.set_color(PINK)
        domainline2.set_color(PINK)

        domainMsg = TextMobject(r"Domain: $[-\infty, \infty]$")
        domainMsg.move_to(1.1*YTD*DOWN)
        domainMsg.scale(0.5)
        domainMsg.set_color(GREEN)



        self.play(ShowCreation(sineobj))
        self.play(ShowCreation(sine_lab))
        self.wait(1)
        self.play(GrowArrow(rangeline1))
        self.play(GrowArrow(rangeline2))
        self.play(Write(rangeMsg))
        self.wait(1)
        self.play(GrowArrow(domainline1))
        self.play(GrowArrow(domainline2))
        self.play(Write(domainMsg))
        self.wait(3)

    

        
class Paraboloid(ThreeDScene):
    def construct(self):

        scalar_func_R2 = TextMobject(r"Scalar Valued Functions in $R^2$").scale(1.5).set_color_by_gradient(RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE)
        self.play(Write(scalar_func_R2))
        self.play(FadeOut(scalar_func_R2))
        self.wait(1)

        axes = ThreeDAxes() 

        paraboloid = ParametricSurface(
            lambda u, v: np.array([
                2*np.sin(u)*np.cos(v),
                2*np.sin(u)*np.sin(v),
                2*2*np.sin(u)*np.sin(u)
            ]),u_min=0,u_max=PI/2,v_min=0,v_max=2*PI,checkerboard_colors=[GREEN_C, GREEN_E],
            resolution=(15, 32)).scale(1)

        domain = Polygon(np.array([-5,-5,0]),np.array([5,-5,0]),np.array([5,5,0]),np.array([-5,5,0]),np.array([-5,-5,0]), color = BLUE_C, fill_color = BLUE_C, fill_opacity = 0.2)
        domain_lab = TextMobject(r"$Domain: R^2$", color = YELLOW_C).scale(0.7).move_to(1*DOWN + 2*LEFT)
        
        rangef = Line(np.array([0, 0,0]), np.array([0, 0,5]), color = RED_C)
        rangef_lab = TextMobject(r"$Range: z \geq 0$", color = RED_C).scale(0.7).move_to(2*UP + 1.5*RIGHT)

        func = TextMobject(r"$z = f(x,y) = x^2+y^2$").scale(0.7).move_to(3*UP + 4*LEFT).set_color_by_gradient(RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE)
        
        self.set_camera_orientation(phi=60 * DEGREES, theta = 0*DEGREES)
        self.begin_ambient_camera_rotation(rate=0.3)

        self.add(axes)

        axis = TextMobject(r"X",r"Y",r"Z")
        axis[0].move_to(6*RIGHT)
        axis[1].move_to(6*UP)
        axis[2].move_to(np.array([0,0,3.7]))

        self.add_fixed_orientation_mobjects(axis[2])
        self.add_fixed_orientation_mobjects(axis[0])
        self.add_fixed_orientation_mobjects(axis[1]) 



        self.add_fixed_in_frame_mobjects(func)
        self.play(Write(paraboloid))
        self.play(ShowCreation(domain))
        self.add_fixed_in_frame_mobjects(domain_lab)
        self.wait()
        self.play(ShowCreation(rangef))
        self.add_fixed_in_frame_mobjects(rangef_lab)
        self.wait(5)

    