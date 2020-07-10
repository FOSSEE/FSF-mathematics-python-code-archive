from manimlib.imports import *


class VectorFields(GraphScene):
    CONFIG = {
        "x_min" : -4,
        "x_max" : 4,
        "y_min" : -4,
        "y_max" : 4,
        "graph_origin": ORIGIN+2.5*LEFT,
        "x_axis_width": 7,
        "y_axis_height": 7,
        "x_tick_frequency": 1,
        "y_tick_frequency": 1,
        "default_vector_field_config": {
            "delta_x": .5,
            "delta_y": .5,
            "min_magnitude": 0,
            "max_magnitude": 4,
            "colors": [GREEN,GREEN,YELLOW,RED],
            "length_func": lambda n: n/2.5,
            "opacity": .75,
            "vector_config": {
                "stroke_width":6,
                "max_stroke_width_to_length_ratio":4
            },
        },
        
        "a":-3.5 ,"b": 4, "c": -3.5 ,"d": 4,
    }  

    def construct(self):
        X = RIGHT*self.x_axis_width/(self.x_max- self.x_min)
        Y = UP*self.y_axis_height/(self.y_max- self.y_min)
        self.X=X ;self.Y=Y
        
        self.setup_axes(animate=False)
        vector_function = lambda v: np.array([
            (v[0]-self.graph_origin[0])*(v[1]-self.graph_origin[1]),  
            -(v[0]-self.graph_origin[0]),  
            0,
            ])
            
        vector_field=self.get_vector_field(
            vector_function,
            colors= [GREEN]
        )
        
        self.show_points()
        self.wait(.5)
        self.show_func_machine()
        self.wait(1)
        self.produce_vectors(vector_field)
        self.wait(.5)
        self.scale_down_vectors(vector_function)
        self.wait(2)
    
    
    
    def show_points(self):
        dn=1
        x_vals=np.arange(self.a,self.b,dn)
        y_vals=np.arange(self.c,self.d,dn)
        dots=VGroup()
        for x_val in x_vals:
          for y_val in y_vals:
            dot=Dot(
                self.coords_to_point(x_val,y_val),
                radius=.05,
                color=TEAL,
            )
            dots.add(dot)
        self.play(ShowCreation(dots, run_time=1))
        self.dots=dots  
    
    def show_func_machine(self):
        machine=RoundedRectangle(
            height=2,
            width=3.5,
            color=PURPLE,
            stroke_width=8
        ).to_edge(RIGHT, buff=.4)
        
        machine_label=TexMobject(
            r"\vec F=xy\hat i-x\hat j",
            stroke_width=1.5,
        ).set_color_by_gradient(
            *self.default_vector_field_config["colors"]
        ).next_to(machine,IN)
        
        machine=VGroup(machine,machine_label)
        self.add(machine)
        
        self.func_machine=machine
        
    
    def produce_vectors(self,vector_field):
        count,i=3,0
        self.run_time=1
        non_scaled_vectors=VGroup()
        for dot in self.dots:
            if i==count:
                self.run_time=.05
            position=dot.get_center()
            vect= vector_field.get_vector(position)
            self.go_to_machine(dot)
            self.take_vec_from_machine(vect,position)
            non_scaled_vectors.add(vect)
            i+=1
            
        self.non_scaled_vectors=non_scaled_vectors
                
    def go_to_machine(self,dot):
        if self.run_time>.5:
         self.play(ApplyMethod(
                dot.next_to,
                self.func_machine,4*UP,
                ),
         run_time=self.run_time
         )
        self.dot=dot
        
    def take_vec_from_machine(self,vect,position):
        vect.next_to(self.func_machine,DOWN,buff=.1)
        
        if self.run_time>.5:
          point_coord=TexMobject(
            "(x_i,y_i)"
          ).next_to(self.dot,RIGHT,buff= .01).scale(.75)
          input_point=VGroup(point_coord, self.dot)
          self.play(
            ApplyMethod(
            input_point.shift,DOWN,
            run_time=self.run_time
          )),
          self.play(
            FadeOut(input_point),
            run_time=.2
          )
          self.play(
            FadeIn(vect),
            run_time=.4
          )
        else:
            self.remove(self.dot)
            self.add(vect)
            self.wait(1.0/15)
 
        self.play(
            vect.move_to,position,
            run_time=self.run_time
        )
    
    def scale_down_vectors(self,vector_function):
        scale_down_text=TextMobject(
            r"Vectors are rescaled\\ for clarity\\ and \\",
            r"colors are used to \\ indicate magnitudes",
            stroke_width=1.2
        )
        scale_down_text[0][:7].set_color(BLUE)
        scale_down_text[1].set_color_by_gradient(
            *self.default_vector_field_config["colors"]
        )
        scale_down_text.to_corner(UR).shift(DOWN)
        scaled_vector_field= self.get_vector_field(
            vector_function,
            length_func= lambda norm : .75*sigmoid(norm)
        )
        for vector in self.non_scaled_vectors:
            scaled_vect= scaled_vector_field.get_vector(vector.get_center())
            vector.target= scaled_vect
            
        self.play(FadeOut(self.func_machine))
        self.play(Write(scale_down_text))
        self.wait(1.2) 
        self.play(LaggedStartMap(
            MoveToTarget, self.non_scaled_vectors,
            run_time=3
        ))   
            
    def get_vector_field(self,func,**kwargs):
        config = dict()
        config.update(self.default_vector_field_config)
        config.update(kwargs)
        vector_field= VectorField(func,**config)
        
        return vector_field   

 
        
        
        
#uploaded by Somnath Pandit. FSF2020_Vector_fields


       
