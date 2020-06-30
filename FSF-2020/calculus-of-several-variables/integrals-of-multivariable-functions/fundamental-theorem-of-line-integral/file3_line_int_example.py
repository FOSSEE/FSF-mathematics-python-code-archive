from manimlib.imports import *


class LineIntegration(GraphScene):
    CONFIG = {
        "x_min" : -1,
        "x_max" : 2,
        "y_min" : -1,
        "y_max" : 2,
        "graph_origin": ORIGIN+3*LEFT+1.5*DOWN,
        "x_axis_width": 10,
        "y_axis_height": 10 ,
        "x_tick_frequency": 1,
        "y_tick_frequency": 1,
        "default_vector_field_config": {
            "delta_x": .5,
            "delta_y": .5,
            "min_magnitude": 0,
            "max_magnitude": .5,
            "colors": [GREEN,BLUE,BLUE,TEAL],
            "length_func": lambda norm : .4*sigmoid(norm),
            "opacity": .75,
            "vector_config": {
                "stroke_width":2
            },
        },
        
        "a": .45,"b": 2, 
    }  

    def construct(self):
        X = RIGHT*self.x_axis_width/(self.x_max- self.x_min)
        Y = UP*self.y_axis_height/(self.y_max- self.y_min)
        self.X=X ;self.Y=Y
        
        self.setup_axes(animate=False)
        
        
        
        
        vector_field=self.get_vector_field(
            lambda v: np.array([
            v[1]-self.graph_origin[1],  
            v[0]-self.graph_origin[0],  
            0,
            ])
        ) 
        vector_field_text=TexMobject(
            "\\vec F=y\hat i+x\hat j",
            stroke_width=2
            ).to_corner(UR,buff=.75).scale(1.2)
            
        vector_field_text[0][0:3].set_color(TEAL),
        self.add(vector_field,)
        self.play(Write(vector_field_text))
        self.wait()
        self.get_endpoints_of_curve()
        self.wait(.6)
        self.play(
            vector_field_text.shift,5*LEFT,

        )
        vector_field.set_fill(opacity=.2)
        self.show_line_integral()
        self.wait(2)
    
    
    
    
        
    def get_vector_field(self,func,**kwargs):
        config = dict()
        config.update(self.default_vector_field_config)
        config.update(kwargs)
        vector_field= VectorField(func,**config)
        
        self.vector_field= vector_field
        
        return vector_field   

        
    
    def get_endpoints_of_curve(self):
        points=[[1,1],[0,0]]
        point_labels= ["(1,1)","(0,0)"]
        for point,label in zip(points,point_labels):
            dot=Dot(self.coords_to_point(*point)).set_color(RED)
            dot_label=TexMobject(label)
            dot_label.next_to(dot,DR)
            self.add(dot,dot_label)
        self.end_points=points
        
    def show_line_integral(self):
        int_text=TexMobject(
            "\\int_\\text{\\textbf{path}}\\vec F \\cdot d\\vec r= 1",
            color=BLUE,
            stroke_width=1.5
        ).scale(1.2)
        int_text[0][0].set_color(RED_C)
        int_text[0][5:7].set_color(TEAL)
        int_text.to_edge(RIGHT+UP,buff=1)
        
        close_int=TexMobject("O").set_color(RED).scale(1.3)
        close_int.move_to(int_text[0][0],OUT)
        close_int_val=TexMobject("0",color=BLUE).scale(1.4)
        close_int_val.move_to(int_text[0][-1],OUT)
        
        self.play(Write(int_text))
        
        
        self.show_method([[0,1]])
        self.play(Indicate(int_text))
        self.wait()
  
        self.show_method([[1,0]])
        self.play(Indicate(int_text))
        self.wait()
        self.remove(int_text[0][-1])
        self.add(close_int)
        
        for i in range(2):
            self.play(self.paths[i].rotate,PI)
        self.play(Indicate(close_int))
        self.play(Write(close_int_val))
        self.wait()
       
        
    def show_method(self,points):
        points=points+self.end_points
        paths=[]
        for i in range(-1,len(points)-2):
            path=Arrow(
                  self.coords_to_point(*points[i]),
                  self.coords_to_point(*points[i+1]),
                  buff=0
                ).set_color(BLUE)
            paths+=VGroup(path)
            self.play(GrowArrow(path),run_time=1.5)
    
        self.paths=paths       
    
 
        
        
        
#uploaded by Somnath Pandit. FSF2020_Fundamental_Theorem_of_Line_Integrals


       
