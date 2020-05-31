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
        "graph_origin": ORIGIN+4.5*LEFT+3*DOWN,  
        "area_color": PINK ,
        "area_opacity": .6,
    }

    def construct(self):
        X = RIGHT*self.x_axis_width/(self.x_max- self.x_min)
        Y = UP*self.y_axis_height/(self.y_max- self.y_min)
        
        self.intro_scene()
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
            x_val=.7,
            direction=LEFT,
            buff=MED_LARGE_BUFF,
            color=YELLOW,
        )
        self.curve1=curve1
        self.curve2=curve2
        
        caption_limit=TextMobject(r"Observe the limits\\ of  integration").to_corner(UR)
        int_lim=TextMobject(
            "$$\\int_0^1$$"
            ).next_to(
            caption_limit,DOWN,buff=.5
            ).align_to(
            caption_limit,LEFT
            )
        self.int_lim=int_lim  
        self.play(ShowCreation(VGroup(curve1,curve2)),Write(VGroup(c2_eqn,c1_eqn)))
        
        self.play(Write(caption_limit))
        self.get_rects()
        self.show_integral_values_at_different_x()
        self.wait(1)
        self.integral_setup(int_lim,first_y=True)
        
        
        self.another_method_scene()
        self.remove(self.area)
        self.wait()
        
        c1_eqn_y=self.get_graph_label(
            curve1,
            label="x=\sqrt y",
            x_val=.6,
            direction=RIGHT,
            buff=MED_LARGE_BUFF,
            color=ORANGE,
        )
        c2_eqn_y=self.get_graph_label(
            curve2,
            label="x=y",
            x_val=.7,
            direction=LEFT,
            buff=MED_LARGE_BUFF,
            color=YELLOW,
        )
        self.play(
            ReplacementTransform(c1_eqn,c1_eqn_y),
            ReplacementTransform(c2_eqn,c2_eqn_y)
        )
        self.get_rects(base_y=True)
        self.show_integral_values_at_different_y()
        self.wait(1)
        
        int_lim_y=int_lim.copy()
        int_lim_y.next_to(int_lim,DOWN)
        self.int_lim_y=int_lim_y
        equal=TextMobject("$$=$$").next_to(int_lim_y,LEFT)
        self.add(equal)
        
        self.integral_setup(int_lim_y,first_y=False)

        self.wait(2)
        
  ###################  
    def intro_scene(self):
        text=TextMobject(r"How different orders of \textbf{iterated  integral}\\ works over the same region ?" ) 
        self.play(Write(text),run_time=4)
        self.wait(2)
        self.play(FadeOut(text))
        
    def another_method_scene(self):
        text=TextMobject(r"The other method\\ of iteration")
        text.next_to(self.curve1,UP,buff=-1)
        self.play(GrowFromCenter(text))
        self.wait(2)
        self.play(LaggedStart(FadeOut(text),lag_ratio=2))
    
    def integral_setup(self,ref_object,first_y=True):
        if first_y: 
          area=self.get_area()
          self.area=area
          self.play(FadeOut(self.brace_group))
          self.play(ApplyMethod(
              self.y_int.next_to,
              ref_object,RIGHT,buff=0)
          )
            
          self.play(ApplyMethod(
              self.dx_label.next_to,
              self.y_int,RIGHT),
              ShowCreation(area),
              Write(self.int_lim),run_time=4
          )
        else:
          area=self.get_area(base_y=True)
          self.area=area
          self.play(
              FadeOut(self.y_brace_group),
              Rotate(self.x_int,PI/2)
          )
          self.play(ApplyMethod(
              self.x_int.next_to,
              ref_object,RIGHT,buff=0)
          )
          self.play(ApplyMethod(
              self.dy_label.next_to,
              self.x_int,RIGHT),
              ShowCreation(area),
               Write(self.int_lim_y),run_time=4
          )
            
    def get_area(self,base_y=False):
        if base_y:
          area = self.bounded_riemann_rectangles_y(
            lambda x: x,
            lambda x: np.sqrt(x), 
            y_min = 0,
            y_max = 1,
            dy =.001,
            start_color = self.area_color,
            end_color = self.area_color,
            fill_opacity =self.area_opacity,
            stroke_width = 0,
          )
          self.y_area = area
        else:
          area = self.bounded_riemann_rectangles(
            self.curve1,
            self.curve2,
            x_min = 0,
            x_max = 1,
            dx =.001,
            start_color = self.area_color,
            end_color = self.area_color,
            fill_opacity =self.area_opacity,
            stroke_width = 0,
          )
          self.area = area
        
  #      self.transform_between_riemann_rects(self.rects,area)
        return area
                
    def get_rects(self,base_y=False):
        if base_y:
          rects = self.bounded_riemann_rectangles_y(
            lambda x: x,
            lambda x: np.sqrt(x), 
            y_min = 0,
            y_max = 1,
            dy =.01,
            start_color = self.area_color,
            end_color = self.area_color,
            fill_opacity =self.area_opacity,
            stroke_width = 0,
          )
          self.y_rects=rects
        else:
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
          self.rects=rects
     #   self.transform_between_riemann_rects(self.area,rects)
        
        return rects 
        
    def show_integral_values_at_different_x(self):
        rects=self.rects
        rect = rects[len(rects)*1//10]
        dx_brace = Brace(rect, DOWN, buff = 0)
        dx_label = dx_brace.get_text("$dx$", buff = SMALL_BUFF)
        dx_brace_group = VGroup(dx_brace,dx_label)
        rp=int(len(rects)/20)
        rects_subset = rects[6*rp:7*rp]

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
        
    def show_integral_values_at_different_y(self):
        rects=self.y_rects
        rect = rects[len(rects)*1//10]
        dy_brace = Brace(rect, LEFT, buff = 0)
        dy_label = dy_brace.get_text("$dy$", buff = SMALL_BUFF)
        dy_brace_group = VGroup(dy_brace,dy_label)
        rp=int(len(rects)/20)
        rects_subset = rects[5*rp:6*rp]

        last_rect = None
        for rect in rects_subset:
            brace = Brace(rect, DOWN, buff =.1)
            x_int = TexMobject("\\int_{y}^{\sqrt y}dx").rotate(-PI/2)
            x_int.next_to(brace, DOWN, SMALL_BUFF)
            anims = [
                rect.set_fill, self.area_color, 1,
                dy_brace_group.next_to, rect, LEFT, SMALL_BUFF
            ]
            if last_rect is not None:
                anims += [
                    last_rect.set_fill, None, 0,
                  #  last_rect.set_fill, self.area_color, self.area_opacity,
                    ReplacementTransform(last_brace, brace),
                    ReplacementTransform(last_x_int, x_int),
                ]
            else:
                anims += [
                    GrowFromCenter(brace),
                    Write(x_int)
                ]
            self.play(*anims)
           # self.wait(.2)

            last_rect = rect
            last_brace = brace
            last_x_int = x_int

        x_int = last_x_int
        y_brace = last_brace
        self.y_brace_group=VGroup(y_brace,dy_brace,rect)
        self.x_int=x_int
        self.dy_label=dy_label
        
            
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
     
    def bounded_riemann_rectangles_y(
        self,
        graph1,
        graph2,
        y_min=None,
        y_max=None,
        dy=0.01,
        input_sample_type="center",
        stroke_width=1,
        stroke_color=BLACK,
        fill_opacity=1,
        start_color=None,
        end_color=None,
        show_signed_area=True,
        width_scale_factor=1.001
        ):
            y_min = y_min if y_min is not None else self.y_min
            y_max = y_max if y_max is not None else self.y_max
            if start_color is None:
                start_color = self.default_riemann_start_color
            if end_color is None:
                end_color = self.default_riemann_end_color
            rectangles = VGroup()
            y_range = np.arange(y_min, y_max, dy)
            colors = color_gradient([start_color, end_color], len(y_range))
            for y, color in zip(y_range, colors):
                if input_sample_type == "left":
                    sample_input = y
                elif input_sample_type == "right":
                    sample_input = y + dy
                elif input_sample_type == "center":
                    sample_input = y + 0.5 * dy
                else:
                    raise Exception("Invalid input sample type")
                graph1_point = self.coords_to_point(
                    graph1(sample_input),sample_input
                )
                dy_input=sample_input + width_scale_factor * dy
                graph1_point_dy= self.coords_to_point(
                    graph1(dy_input),dy_input
                )
                graph2_point = self.coords_to_point(
                    graph2(sample_input),sample_input
                )

                points = VGroup(*list(map(VectorizedPoint, [
                    graph1_point,
                    graph1_point_dy,
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
