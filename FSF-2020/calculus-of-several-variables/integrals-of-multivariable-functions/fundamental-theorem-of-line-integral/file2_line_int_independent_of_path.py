from manimlib.imports import *


class LineIntegration(GraphScene):
    CONFIG = {
        "x_min" : -5,
        "x_max" : 5,
        "y_min" : -5,
        "y_max" : 5,
        "axes_color":BLACK,
        "graph_origin": ORIGIN+1.2*DOWN,
        "x_axis_width": 10,
        "y_axis_height": 10 ,
        "x_axis_label": "",
        "y_axis_label": "",
        "x_tick_frequency": 1,
        "y_tick_frequency": 1,
        "default_vector_field_config": {
            "delta_x": .6,
            "delta_y": .6,
            "min_magnitude": 0,
            "max_magnitude": .5,
            "colors": [GREEN,BLUE,BLUE,TEAL],
            "length_func": lambda norm : .45*sigmoid(norm),
            "opacity": .75,
            "vector_config": {
                "stroke_width":1.5
            },
        },
        
        "a": .45,"b": 2, 
        "path_color": PURPLE
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
            "\\vec F(x,y)","=y\hat i+x\hat j",
            stroke_width=1.5
            ).to_edge(TOP,buff=.2)
            
        vector_field_text[0][0:2].set_color(TEAL)
        
        grad_f=TexMobject(
            "\\vec\\nabla f(x,y)",
            stroke_width=1.5
        )
        grad_f[0][2].set_color(LIGHT_BROWN)
        grad_f.move_to(vector_field_text[0])
        
        self.add(vector_field,)
        self.play(Write(vector_field_text))
        self.wait()
        self.play(
            ReplacementTransform(
                vector_field_text[0],grad_f
            )
        )
        self.get_endpoints_of_curve()
        self.wait(.6)
        vector_field.set_fill(opacity=.4)
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
        points=[[-3,0],[2,2]]
        point_labels= ["P_f","P_i"]
        for point,label in zip(points,point_labels):
            dot=Dot(self.coords_to_point(*point)).set_color(RED)
            dot_label=TexMobject(label)
            dot_label.next_to(dot,DR,buff=.2)
            self.play(FadeIn(VGroup(dot,dot_label)))
            self.wait(.2)
            
        self.end_points=points
        
    def show_line_integral(self):
        int_text=TexMobject(
            r"\int_{P_i}^{P_f}\vec F \cdot d\vec r",
            stroke_width=1.5,
        ).scale(1.2)
        int_text[0][0].set_color(self.path_color)
        int_text[0][5:7].set_color(TEAL)
        int_text.to_edge(RIGHT+UP,buff=1)
        
        int_value= TexMobject(r"=f(P_i)-f(P_f)",
            stroke_width=1.5
        ).next_to(int_text,DOWN)
        VGroup(int_value[0][1],
            int_value[0][7]
        ).set_color(LIGHT_BROWN)
        
        path_indepent_text=TextMobject(
            r"Value of the Line Integral is\\ independent of Path",color=GOLD,stroke_width=2,).to_corner(DR,buff=1)
        
        path_indepent_text[0][-4:].set_color(self.path_color)
        
        
        self.play(Write(VGroup(
            int_text,int_value
            )),
            run_time=2
        )
        self.wait(1.5)
       
        
        self.show_path([[0,1],[-1,2],[1,3]])
        self.play(Indicate(int_value))
        self.play(Uncreate(self.path))
        
        self.show_path([[0,1]])
        self.play(Indicate(int_value))
        self.play(Uncreate(self.path))
        
        self.show_path([[-1,1],[-1,-2],[-5,0],[-2,3.5],[1,1]])
        self.play(Indicate(int_value),run_time=2)
        self.wait(.6)
        
        self.play(Write(path_indepent_text))
  
       
        
    def show_path(self,points):
        points=[self.end_points[0]]+points+[self.end_points[1]]
        
        path= VMobject()
        path.set_points_smoothly([
            self.coords_to_point(*point)
                for point in points
        ])
        path.set_color(self.path_color)
        self.play(ShowCreation(path),run_time=1.5)
    
        self.path=path     
    
 
        
        
        
#uploaded by Somnath Pandit. FSF2020_Fundamental_Theorem_of_Line_Integrals


       
