from manimlib.imports import *

class LineIntegrationProcess(GraphScene):

    CONFIG = {
        "x_min" : -0,
        "x_max" : 1,
        "y_min" : -0,
        "y_max" : 1,
        "axes_color":WHITE,
        "graph_origin": ORIGIN+5*LEFT+3*DOWN,
        "x_axis_width": 5,
        "y_axis_height": 5,
        "x_tick_frequency": 1,
        "y_tick_frequency": 1,
        "default_vector_field_config": {
            "delta_x": .5,
            "delta_y": .5,
            "min_magnitude": 0,
            "max_magnitude": 15,
            "colors": [GREEN,YELLOW,RED],
            "length_func": lambda norm : .45*sigmoid(norm),
            "opacity": 1.0,
            "vector_config": {
                "stroke_width":2
            },
        },
        "default_graph_style": {
            "stroke_width": 2,
            "stroke_color": WHITE,
        },
    }


    def construct(self):
        X = RIGHT*self.x_axis_width/(self.x_max- self.x_min)
        Y = UP*self.y_axis_height/(self.y_max- self.y_min)
        self.X=X ;self.Y=Y
        
        self.setup_axes(animate=False)
    
        fn_text=TexMobject(
            r"\vec F = x^2\hat i-xy\hat j"
        ).set_color_by_gradient(
            *self.default_vector_field_config["colors"]
        )
        fn_text.to_corner(UR,buff=.8).shift(DOWN)
        
        origin=self.graph_origin
        v_field=self.get_vector_field(
            lambda v: np.array([
            (v[0]-origin[0])**2,
            -(v[0]-origin[0])*(v[1]-origin[1]),  
            0,
            ]),
            x_min= 0+origin[0],
            x_max= 5+origin[0],
            y_min= -0+origin[1],
            y_max= 5+origin[1],
        )
        
     #   self.play(Write(surface))  
     #   self.play(Write(v_field),Write(fn_text))
        self.add(v_field, fn_text)
        self.get_line_of_int()
        self.get_dot_product_values()
        '''self.get_field_values_on_line()
        self.wait(1.5)
   
        self.remove(surface)
        self.trasform_to_graphs()'''
        self.wait(2)
            
            
    def get_vector_field(self,func,**kwargs):
        config = dict()
        config.update(self.default_vector_field_config)
        config.update(kwargs)
        vector_field= VectorField(func,**config)
        self.vector_field=vector_field
        
        return vector_field
        
    def get_line_of_int(self): 
        line_of_int_text=TextMobject(r"Line of integration is\\","$\\vec r(t)=\cos(t)\hat i+\sin(t)\hat j$")
        line_of_int_text[1].set_color(PINK)
        line_of_int_text.to_edge(TOP,buff=SMALL_BUFF)
        
        
        line_of_int= self.get_graph(
            lambda x : np.sqrt(1-x**2),
            x_min=1,
            x_max=0,
        )
        line_of_int.set_style(
            stroke_width=5,
            stroke_color=BLUE,
        )
        
      #  self.play(Write(line_of_int_text))
        self.wait(.5)
      #  self.play(ShowCreation(line_of_int),run_time=1.5)
        self.add(line_of_int)
        
        self.line_of_int=line_of_int
        self.line_of_int_text=line_of_int_text
    
    def get_dot_product_values(self):    
        self.get_vector_and_tangent()
        self.play(ApplyMethod(
            self.t_tracker.set_value, PI/2,
                rate_func=linear,
                run_time=.5,
            ) 
        )
        
        
    def get_vector_and_tangent(self):
        t_tracker = ValueTracker(0)
        self.t_tracker = t_tracker
        t = t_tracker.get_value
        coord = [np.cos(t()), np.sin(t()), 0]
        self.show_vector(coord)
        self.show_tangent(coord)
        
        
    def show_vector(self,coord):
        vector = self.vector_field.get_vector(coord)
        vector.set_color(ORANGE)
        
        self.add(vector)
       # self.play(Write(vector),run_time=.2)
        
    def show_tangent(self,coord):
        tangent_sym=TextMobject("$\\vec T(x_i,y_i)$",color="#DC75CD").scale(.8)
        angle=self.angle_of_tangent(
             coord[0],
             self.line_of_int, 
             dx=0.01
        )
        vect = Vector().rotate(angle,about_point=coord)
        vect.set_color("#DC75CD")
        tangent=vect.next_to(coord,DR,buff=0)
        tangent_sym.next_to(tangent,DOWN,buff=.1)
        self.play(Write(VGroup(tangent,tangent_sym)))
        
        self.tangent_sym=tangent_sym
         
    def dot_product(self):
        
        dot_sym=Dot().next_to(self.func_val,RIGHT)
        
        self.play(FadeOut(VGroup(
            self.at_any_points_text,
            self.evaluate_text
        )))
        self.play(Write(self.dot_prod_text))
        self.play(
            FadeIn(dot_sym),
            ApplyMethod(
            self.tangent_sym.next_to,
            dot_sym, RIGHT
        ))

        self.dot_sym=dot_sym
    
    

    def get_curve(self,func,on_surface=False ,**kwargs):
        config = dict()
        config.update(self.default_graph_style)
        config.update({
            "t_min": 0,
            "t_max": PI/2,
        })
        config.update(kwargs)
        r=1
        curve=ParametricFunction(
            lambda t: self.coords_to_point(
                r*np.cos(t), 
                r*np.sin(t),
            ),
            **config,
        )
        return curve
        
    
     #-------------------------------------------------------       
    def trasform_to_graphs(self):        
        on_surface_graph=(self.get_graph(
            self.Func,on_surface=True
        ))
        on_surface_graph.set_style(
            stroke_width=5,
            stroke_color=YELLOW,
        ) 
        
        line_graph=(self.get_graph(
            self.Func,on_surface=False
        ))
        line_graph.set_style(
            stroke_width=5,
            stroke_color=PINK,
        )
        
        self.on_surface_graph=on_surface_graph
        self.line_graph=line_graph
        graph_area=self.get_area(graph=True) 
        
        into_graph=[
            ReplacementTransform(
            self.values_on_surface,
            on_surface_graph
            ),
            ReplacementTransform(
            self.line_of_int,
            line_graph
            ),
            ReplacementTransform(
            self.area,
            graph_area
            ),
        ]
        
        self.move_camera(
          #  distance=20,
            phi=90 * DEGREES,
            theta=-90 * DEGREES,
            added_anims=into_graph,
            run_time=2
        )        
    def get_area(self,graph=False):
        axes=self.axes
        if graph:
            on_surface=self.on_surface_graph
            on_base=self.line_graph
        else:
            on_surface=self.values_on_surface
            on_base=self.line_of_int
        area =Polygon(
            *[
            on_surface.get_point_from_function(t)
                for t in np.arange(0,PI,0.01)
            ],
            *[
             on_base.get_point_from_function(t)
                for t in np.arange(PI,0,-0.01)
            ],
            stroke_width=0,
            fill_color=TEAL_A,
            fill_opacity=.6,
        )

        return area
        
    def get_field_values_on_line(self):
        self.remove(self.line_of_int_text)
          
        values_on_line_text=TextMobject("Values"," of"," function","on the ","line")
        values_on_line_text.set_color_by_tex_to_color_map({
            "Values":YELLOW, "function":BLUE,"line":PINK
        })
        values_on_line_text.to_edge(TOP,buff=SMALL_BUFF)
        
        values_on_surface=(self.get_curve(
            self.Func,on_surface=True
        ))
        values_on_surface.set_style(
            stroke_width=5,
            stroke_color=YELLOW,
        ) 
        
        self.add_fixed_in_frame_mobjects(values_on_line_text) 
        self.play(Write(values_on_line_text))
    #    self.wait()
        self.play(ShowCreation(values_on_surface),run_time=3)
     #   self.add(values_on_surface)
        
        self.values_on_surface=values_on_surface
        self.values_on_line_text=values_on_line_text
       
     
    
                    
  #uploaded by Somnath Pandit.FSF2020_Line_Integrals
