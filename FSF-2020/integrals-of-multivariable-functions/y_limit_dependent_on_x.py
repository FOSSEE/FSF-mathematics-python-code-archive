from manimlib.imports import *

class AreaUnderCurve(GraphScene):
    CONFIG = {
        "x_min" : 0,
        "x_max" : 1,
        "y_min" : 0,
        "y_max" : 2, 
        "x_tick_frequency" : 1,
        "y_tick_frequency" : 1,
        "x_labeled_nums": list(np.arange(0,2)),
        "y_labeled_nums": list(np.arange(0 ,3)),
        "x_axis_width": 3.5,
        "y_axis_height": 6,
        "graph_origin": ORIGIN+2.5*LEFT+3*DOWN,    
    }

    def construct(self):
        X = RIGHT*self.x_axis_width/(self.x_max- self.x_min)
        Y = UP*self.y_axis_height/(self.y_max- self.y_min)
        
        self.setup_axes(animate=False)
        
        line= self.get_graph(
            lambda x : 2-2*x ,
            x_min = 0,
            x_max = 1,
            color = RED)
        line_eqn=TextMobject("2x+y=0").move_to(self.graph_origin+.8*X+Y).rotate(np.arctan(-2))
        self.line=line
        
        caption=TextMobject(r"See the value of $y$ \\ is changing with $x$").move_to(self.graph_origin+1.2*X+1.8*Y)
        self.play(ShowCreation(line),Write(line_eqn))
   #     self.show_area()
        self.show_rects()
        self.play(Write(caption))
        self.show_y_values_at_different_x()

        self.wait(2)
        
  ###################         
    def show_area(self):
        area = self.get_riemann_rectangles(
            self.line, 
            x_min = 0,
            x_max = 1,
            dx =.0001,
            start_color = BLUE,
            end_color = BLUE,
            fill_opacity = 1,
            stroke_width = 0,
        )
        self.play(ShowCreation(area))
  #      self.transform_between_riemann_rects(self.rects,area)
        self.area = area
                
    def show_rects(self):
        rects = self.get_riemann_rectangles(
            self.line, 
            x_min = 0,
            x_max = 1,
            dx =.02,
            start_color = BLUE,
            end_color = BLUE,
            fill_opacity = 0.75,
            stroke_width = 0,
        )
     #   self.play(ShowCreation(rects))
     #   self.transform_between_riemann_rects(self.area,rects)
        self.rects=rects 
        
    def show_y_values_at_different_x(self):
        rects=self.rects
        rect = rects[len(rects)*1//10]
        dx_brace = Brace(rect, DOWN, buff = 0)
        dx_label = dx_brace.get_text("$dx$", buff = SMALL_BUFF)
        dx_brace_group = VGroup(dx_brace,dx_label)
        rp=int(len(rects)/10)
        rects_subset = self.rects[3*rp:5*rp]

        last_rect = None
        for rect in rects_subset:
            brace = Brace(rect, LEFT, buff = 0)
            y = TexMobject("y=2-2x")
            y.next_to(brace, LEFT, SMALL_BUFF)
            anims = [
                rect.set_fill, YELLOW, 1,
                dx_brace_group.next_to, rect, DOWN, SMALL_BUFF
            ]
            if last_rect is not None:
                anims += [
                    last_rect.set_fill, None, 0,
       #             last_rect.set_fill, BLUE, .75,
                    ReplacementTransform(last_brace, brace),
                    ReplacementTransform(last_y, y),
                ]
            else:
                anims += [
                    GrowFromCenter(brace),
                    Write(y)
                ]
            self.play(*anims)
           # self.wait(.2)

            last_rect = rect
            last_brace = brace
            last_y = y

        y = last_y
        y_brace = last_brace
        
        
