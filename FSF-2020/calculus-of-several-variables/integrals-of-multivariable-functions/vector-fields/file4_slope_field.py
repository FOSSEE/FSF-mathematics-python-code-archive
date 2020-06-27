from manimlib.imports import *


class SlopeFields(GraphScene):
    CONFIG = {
        "x_min" : -2,
        "x_max" : 2,
        "y_min" : -2,
        "y_max" : 2,
        "graph_origin": ORIGIN+2.5*LEFT,
        "x_axis_width": 7,
        "y_axis_height": 7,
        "x_tick_frequency": 1,
        "y_tick_frequency": 1,
        "default_slope_field_config": {
            "delta_x": .2,
            "delta_y": .2,
            "opacity": 1,
            "color": BLUE_A,
            "slope_length_factor": .2,
            "line_config": {
                "stroke_width":2.5,
            },
        },
        
        "a":-1.9 ,"b": 2, "c": -1.9 ,"d": 2,
    }  

    def construct(self):
        X = RIGHT*self.x_axis_width/(self.x_max- self.x_min)
        Y = UP*self.y_axis_height/(self.y_max- self.y_min)
        self.X=X ;self.Y=Y
        
        self.setup_axes(animate=False)
        
        slope_field=self.get_slope_field(
            lambda x,y:-2.0*(x-self.graph_origin[0])*(y-self.graph_origin[1]),
            x_min=self.graph_origin[0]+self.a,
            x_max=self.graph_origin[0]+self.b,
            y_min=self.graph_origin[1]+self.c,
            y_max=self.graph_origin[1]+self.d,
            color= GREEN_B
        )
        
        self.show_points()
        self.wait(.5)
        self.show_func_machine()
        self.wait(1)
        self.produce_slopes(slope_field)
      #  self.add(slope_field)
        self.glimpse_of_solutions()
        self.wait(2)
    
    
    
        
    def show_points(self):
        dn=1.0/5
        x_vals=np.arange(self.a,self.b,dn)
        y_vals=np.arange(self.c,self.d,dn)
        dots=VGroup()
        for x_val in x_vals:
          for y_val in y_vals:
            dot=Dot(
                self.coords_to_point(x_val,y_val),
                radius=.04,
                color=TEAL,
            )
            dots.add(dot)
        self.play(ShowCreation(dots, run_time=1))
        self.dots=dots  
    
    def show_func_machine(self):
        machine=RoundedRectangle(
            height=3,
            width=4,
            color=PURPLE,
            stroke_width=8
        ).to_edge(RIGHT, buff=.4)
        
        machine_label=TextMobject(
            r"Line segment\\ with slope\\"," $y'=-2xy$",
            stroke_width=1.2,
            color=BLUE
        ).next_to(machine,IN)
        machine_label[1].set_color(GREEN)
        machine=VGroup(machine, machine_label)
        self.play(FadeIn(machine))
        
        self.func_machine = machine
        
    
    def produce_slopes(self,slope_field):
        count,i=3,0
        self.run_time=1
        for dot in self.dots:
            if i==count:
                self.run_time=.05
            position=dot.get_center()
            line= slope_field.get_slope(position)
            self.go_to_machine(dot)
            self.take_line_from_machine(line,position)
            i+=1
            
    def go_to_machine(self,dot):
        if self.run_time>.5:
         self.play(ApplyMethod(
                dot.next_to,
                self.func_machine,4*UP,
                ),
         run_time=self.run_time
         )
        self.dot=dot
        
    def take_line_from_machine(self,vect,position):
        
        if self.run_time>.5:
          vect.next_to(self.func_machine,DOWN,buff=.1)
          self.play(
            ApplyMethod(
            self.dot.shift,DOWN,
            run_time=self.run_time
          )),
          self.play(
            FadeOut(self.dot),
            run_time=.2
          )
          self.play(
            FadeIn(vect),
            run_time=.4
          )
          self.play(
            ApplyMethod(
            vect.move_to,position
            ),
            run_time=self.run_time
        )
        else:
            self.remove(self.dot)
            self.add(vect)
            vect.move_to(position)
        
        
    def get_slope_field(self,func,**kwargs):
        config = dict()
        config.update(self.default_slope_field_config)
        config.update(kwargs)
        slope_field= SlopeField(func,**config)
        
        return slope_field
        
    def glimpse_of_solutions(self):
        sol_text= TextMobject(
            r"The solution curves\\ seem to be like...", 
            color= BLUE, 
            stroke_width=1.2
        )
        sol_text.to_corner(UR, buff=1)
        condition_text= TextMobject(
            r"for different\\ initial conditions", 
            color= GOLD, 
            stroke_width=1.1
        )
        condition_text.next_to(sol_text,DOWN,buff=1)
        solution1 = self.get_graph(
            lambda x : np.exp(-x**2),
            x_min = self.a,
            x_max = self.b,
            color = PINK)
        solution2 = self.get_graph(
            lambda x : .5*np.exp(-x**2),
            x_min = self.a,
            x_max = self.b,
            color = YELLOW)
        solution3 = self.get_graph(
            lambda x : 1.5*np.exp(-x**2),
            x_min = self.a,
            x_max = self.b,
            color = BLUE)
        solution4 = self.get_graph(
            lambda x : -np.exp(-x**2),
            x_min = self.a,
            x_max = self.b,
            color = RED_E)
            
        self.play(FadeOut(self.func_machine))
        self.play(Write(sol_text))
        self.wait(.6)
        self.play(ShowCreation(solution1))
        self.play(Write(condition_text))
        self.play(ShowCreation(solution2))
        self.wait(.5)
        self.play(ShowCreation(solution3))
        self.wait(.5)
        self.play(ShowCreation(solution4))
        
         
class SlopeField(VGroup):
    CONFIG = {
        "delta_x": 0.5,
        "delta_y": 0.5,
        "x_min": int(np.floor(-FRAME_WIDTH / 2)),
        "x_max": int(np.ceil(FRAME_WIDTH / 2)),
        "y_min": int(np.floor(-FRAME_HEIGHT / 2)),
        "y_max": int(np.ceil(FRAME_HEIGHT / 2)),
        "opacity": 1.0,
        "color": WHITE,
        "slope_length_factor": .25,
        "line_config": {},
    }

    def __init__(self, func, **kwargs):
        VGroup.__init__(self, **kwargs)
        self.func = func
        
        x_range = np.arange(
            self.x_min,
            self.x_max + self.delta_x,
            self.delta_x
        )
        y_range = np.arange(
            self.y_min,
            self.y_max + self.delta_y,
            self.delta_y
        )
        for x, y in it.product(x_range, y_range):
            point = x * RIGHT + y * UP
            self.add(self.get_slope(point))
        self.set_opacity(self.opacity)

    def get_slope(self, point, **kwargs):
        slope = self.func(*point[:2])
        line_config = dict(self.line_config)
        line_config.update(kwargs)
        line = Line(ORIGIN,self.slope_length_factor*RIGHT, **line_config)
        line.move_to(point).rotate(np.arctan(slope/3.2))
        
        line.set_color(self.color)
        return line
 
        
        
        
#uploaded by Somnath Pandit. FSF2020_Vector_fields


       
