from manimlib.imports import *

class IterationMethods(GraphScene):
    CONFIG = {
        "x_min" : 0,
        "x_max" : 1,
        "y_min" : 0,
        "y_max" : 1, 
        "x_tick_frequency" : 1,
        "y_tick_frequency" : 1,
        "x_labeled_nums": list(np.arange(0,2)),
        "y_labeled_nums": list(np.arange(0 ,2)),
        "x_axis_width": 6,
        "y_axis_height": 6,
        "graph_origin": ORIGIN+4*LEFT+3*DOWN,  
        "area_color": PINK ,
        "area_opacity": .6,
    }

    def construct(self):
        X = RIGHT*self.x_axis_width/(self.x_max- self.x_min)
        Y = UP*self.y_axis_height/(self.y_max- self.y_min)
        
      #  self.intro_scene()
        self.setup_axes(animate=True)
        
        
        curve1= self.get_graph(
            lambda x : x**2 ,
            x_min = 0,
            x_max = 1,
            color = ORANGE)
        c1_eqn=self.get_graph_label(
            curve1,
            label="y=x^2",
            x_val=.5,
            direction=RIGHT,
            buff=MED_LARGE_BUFF,
            color=ORANGE,
        )
        
        curve2= self.get_graph(
            lambda x : x ,
            x_min = 0,
            x_max = 1,
            color = YELLOW)
        c2_eqn=self.get_graph_label(
            curve2,
            label="y=x",
            x_val=.5,
            direction=LEFT,
            buff=MED_LARGE_BUFF,
            color=YELLOW,
        )
        self.curve1=curve1
        self.curve2=curve2
        
        caption_y_int=TextMobject(r"Observe the limits\\ of  integration").to_corner(UR)
        int_lim=TextMobject(
            "$$\\int_0^1$$"
            ).next_to(
            caption_y_int,DOWN,buff=.5
            ).align_to(
            caption_y_int,LEFT
            )
            
        self.play(ShowCreation(VGroup(curve1,curve2)),Write(VGroup(c2_eqn,c1_eqn)))
        rects=self.get_rects()
        
        self.play(Write(caption_y_int))
        self.show_integral_values_at_different_x()
        self.wait(1)
        self.add(int_lim)
        self.play(FadeOut(self.brace_group))
        self.play(ApplyMethod(
            self.y_int.next_to,
            int_lim,RIGHT,buff=0))
            
        self.play(ApplyMethod(
            self.dx_label.next_to,
            self.y_int,RIGHT))
        
        self.show_area()

        self.wait(2)
        
  ###################  
    def intro_scene(self):
        text=TextMobject(r"How different orders of \textbf{iterated  integral}\\ works over the same region ?" ) 
        self.play(Write(text),run_time=4)
        self.wait(2)
        self.play(FadeOut(text))
        
         
    def show_area(self):
        area = self.bounded_riemann_rectangles(
            self.curve1, 
            self.curve2, 
            x_min = 0,
            x_max = 1,
            dx =.001,
            start_color = self.area_color,
            end_color = self.area_color,
            fill_opacity = 1,
            stroke_width = 0,
        )
        self.play(ShowCreation(area))
  #      self.transform_between_riemann_rects(self.rects,area)
        self.area = area
                
    def get_rects(self):
        rects = self.bounded_riemann_rectangles(
            self.curve1,
            self.curve2, 
            x_min = 0,
            x_max = 1,
            dx =.01,
            start_color = self.area_color,
            end_color = self.area_color,
            fill_opacity =self.area_opacity,
            stroke_width = 0,
        )
     #   self.transform_between_riemann_rects(self.area,rects)
        self.rects=rects
        return rects 
        
    def show_integral_values_at_different_x(self):
        rects=self.rects
        rect = rects[len(rects)*1//10]
        dx_brace = Brace(rect, DOWN, buff = 0)
        dx_label = dx_brace.get_text("$dx$", buff = SMALL_BUFF)
        dx_brace_group = VGroup(dx_brace,dx_label)
        rp=int(len(rects)/10)
        rects_subset = self.rects[4*rp:5*rp]

        last_rect = None
        for rect in rects_subset:
            brace = Brace(rect, LEFT, buff =.1)
            y_int = TexMobject("\\int_{x^2}^{x}dy")#.rotate(PI/2)
            y_int.next_to(brace, LEFT, MED_SMALL_BUFF)
            anims = [
                rect.set_fill, self.area_color, 1,
                dx_brace_group.next_to, rect, DOWN, SMALL_BUFF
            ]
            if last_rect is not None:
                anims += [
                    last_rect.set_fill, None, 0,
                  #  last_rect.set_fill, self.area_color, self.area_opacity,
                    ReplacementTransform(last_brace, brace),
                    ReplacementTransform(last_y_int, y_int),
                ]
            else:
                anims += [
                    GrowFromCenter(brace),
                    Write(y_int)
                ]
            self.play(*anims)
           # self.wait(.2)

            last_rect = rect
            last_brace = brace
            last_y_int = y_int

        y_int = last_y_int
        y_brace = last_brace
        self.brace_group=VGroup(y_brace,dx_brace,rect)
        self.y_int=y_int
        self.dx_label=dx_label
        
        
    def bounded_riemann_rectangles(
        self,
        graph1,
        graph2,
        x_min=None,
        x_max=None,
        dx=0.01,
        input_sample_type="center",
        stroke_width=1,
        stroke_color=BLACK,
        fill_opacity=1,
        start_color=None,
        end_color=None,
        show_signed_area=True,
        width_scale_factor=1.001
        ):
            x_min = x_min if x_min is not None else self.x_min
            x_max = x_max if x_max is not None else self.x_max
            if start_color is None:
                start_color = self.default_riemann_start_color
            if end_color is None:
                end_color = self.default_riemann_end_color
            rectangles = VGroup()
            x_range = np.arange(x_min, x_max, dx)
            colors = color_gradient([start_color, end_color], len(x_range))
            for x, color in zip(x_range, colors):
                if input_sample_type == "left":
                    sample_input = x
                elif input_sample_type == "right":
                    sample_input = x + dx
                elif input_sample_type == "center":
                    sample_input = x + 0.5 * dx
                else:
                    raise Exception("Invalid input sample type")
                graph1_point = self.input_to_graph_point(sample_input, graph1)
                graph1_point_dx= self.input_to_graph_point(sample_input + width_scale_factor * dx, graph1)
                graph2_point = self.input_to_graph_point(sample_input, graph2)

                points = VGroup(*list(map(VectorizedPoint, [
                    graph1_point,
                    graph1_point_dx,
                    graph2_point
                ])))
                
                rect = Rectangle()
                rect.replace(points, stretch=True)
                if graph1_point[1] < self.graph_origin[1] and show_signed_area:
                    fill_color = invert_color(color)
                else:
                    fill_color = color
                rect.set_fill(fill_color, opacity=fill_opacity)
                rect.set_stroke(stroke_color, width=stroke_width)
                rectangles.add(rect)
            return rectangles
                 
#uploaded by Somnath Pandit.FSF2020_Fubini's_Theorem
