from manimlib.imports import *

class LineIntegrationProcess(SpecialThreeDScene):

    CONFIG = {
        "axes_config": {
            "x_min": 0,
            "x_max": 4,
            "y_min": 0,
            "y_max": 4,
            "z_min": 0,
            "z_max": 3,
            "a":-3 ,"b": 3, "c":0 , "d":3,
            "axes_shift":IN+2*DL,
            "x_axis_config": {
                "tick_frequency": 1,
               # "include_tip": False,
            },
            "y_axis_config": {
                "tick_frequency": 1,
             #   "include_tip": False,
            },
            "z_axis_config": {
                "tick_frequency": 1,
             #   "include_tip": False,
            },
            "num_axis_pieces": 20,
        },
        "default_vector_field_config": {
            "delta_x": .5,
            "delta_y": .5,
            "x_min": -3,
            "x_max": 2,
            "y_min": -3,
            "y_max": 2,
            "min_magnitude": 0,
            "max_magnitude": 4,
            "colors": [GREEN,YELLOW,RED],
            "length_func": lambda norm : .4*sigmoid(norm),
            "opacity": 1.0,
            "vector_config": {
                "stroke_width":2
            },
        },
        "default_graph_style": {
            "stroke_width": 2,
            "stroke_color": WHITE,
        },

    "Func": lambda x,y: 1+x**2*y/15
    }


    def construct(self):

        self.setup_axes()
        axes=self.axes
        
        self.set_camera_orientation(distance=10,
            phi=0 * DEGREES,
            theta=-90 * DEGREES,
        )
        
        fn_text=TexMobject(
            r"\vec F = x^2\hat i-xy\hat j"
        ).set_color_by_gradient(
            *self.default_vector_field_config["colors"]
        )
        fn_text.to_corner(UR,buff=.8).shift(DOWN)
        
        origin=axes.c2p(0,0,0)
        v_field=self.get_vector_field(
            lambda v: np.array([
            (v[0]-origin[0])**2,
            -(v[0]-origin[0])*(v[1]-origin[1]),  
            0,
            ]),
        )
        
     #   self.play(Write(surface)) 
        self.add_fixed_in_frame_mobjects(fn_text)   
     #   self.play(Write(v_field),Write(fn_text))
        self.add(v_field, fn_text)
        self.get_line_of_int()
      #  self.begin_ambient_camera_rotation(rate=0.04)
        self.get_dot_product_values()
        '''self.get_field_values_on_line()
        self.wait(1.5)
        self.area=self.get_area()
        area_text=TextMobject("Line"," Integral in the",r" scalar field\\"," means this" ,"area")
        area_text.set_color_by_tex_to_color_map({
            "Line": PINK, "scalar":BLUE, "area":TEAL_A
        })
        area_text.to_edge(TOP,buff=MED_SMALL_BUFF)
        
        self.remove(self.values_on_line_text)
        self.add_fixed_in_frame_mobjects(area_text) 
        self.play(Write(area_text))
        self.play(Write(self.area),run_time=2)
        self.play(FadeOut(VGroup(surface,fn_text)))
        self.wait()
        
        self.stop_ambient_camera_rotation()
    #    self.get_lines()
   
        self.remove(axes,surface)
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
        
        
        line_of_int=(self.get_curve(
            self.Func,on_surface=False
        ))
        line_of_int.set_style(
            stroke_width=5,
            stroke_color=PINK,
        )
        
        self.add_fixed_in_frame_mobjects(line_of_int_text) 
        self.play(Write(line_of_int_text))
        self.wait(.5)
        self.play(ShowCreation(line_of_int),run_time=1.5)
      #  self.add(line_of_int)
        
        self.line_of_int=line_of_int
        self.line_of_int_text=line_of_int_text
    
    def get_dot_product_values(self):    
        self.get_vector_and_tangent()
        
        
        
    def get_vector_and_tangent(self):
        dot=self.dots[self.index]
        self.show_specific_vectors(dot)
        self.play(Write(self.func_val))
        self.wait(1)
        self.show_tangent(dot)
        self.play(FadeIn(VGroup(*[
            dot.set_color(ORANGE).scale(1.4)
                for dot in self.dots ]
        )))
        
        
    def show_specific_vectors(self,dots):
        for dot in dots:
            vector=self.vector_field.get_vector(dot.get_center()) 
            vector.set_color(ORANGE)

            self.play(Write(vector),run_time=.2)

        
    def show_tangent(self,dot):
        tangent_sym=TextMobject("$\\vec T(x_i,y_i)$",color="#DC75CD").scale(.8)
        x=dot.get_center()
        angle=self.angle_of_tangent( 
             self.point_to_coords(x)[0],
             self.curve, 
             dx=0.01
        )
        vect = Vector().rotate(angle,about_point=x)
        vect.set_color("#DC75CD")
        tangent=vect.next_to(x,DR,buff=0)
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

    def get_curve(self,func,on_surface=False ,**kwargs):
        config = dict()
        config.update(self.default_graph_style)
        config.update({
            "t_min": 0,
            "t_max": PI/2,
        })
        config.update(kwargs)
        r=abs(self.axes.a)
        curve=ParametricFunction(
            lambda t: self.axes.c2p(
                r*np.cos(t), 
                r*np.sin(t), 
                func(r*np.cos(t), r*np.sin(t))*bool(on_surface)
            ),
            **config,
        )
        return curve
        
        
    def get_surface(self, func, **kwargs):
        axes=self.axes
        config = {
            "u_min": axes.a-.2,
            "u_max": axes.b+.2,
            "v_min": axes.c-.1,
            "v_max": axes.d,
            "resolution": (
                2*(axes.y_max - axes.y_min) // axes.y_axis.tick_frequency,
                (axes.x_max - axes.x_min) // axes.x_axis.tick_frequency,
            ),
        }
        
        config.update(self.default_surface_config)
        config.update(kwargs)
        return ParametricSurface(
            lambda  x,y : axes.c2p(
                x, y, func(x, y)
            ),
            **config
        )
    
    def get_graph(self,func,on_surface=False ,**kwargs):
        config = dict()
        config.update(self.default_graph_style)
        config.update({
            "t_min": 0,
            "t_max": PI,
        })
        config.update(kwargs)
        slice_curve=ParametricFunction(
            lambda t: self.axes.c2p(
                4*np.cos(t), 
                0, 
                2+func(3*np.cos(t), 3*np.sin(t))*bool(on_surface)
            ),
            **config,
        )
        return slice_curve
        
    def get_lines(self):
        pass
        axes = self.axes
        labels=[axes.x_axis.n2p(axes.a), axes.x_axis.n2p(axes.b), axes.y_axis.n2p(axes.c),       
            axes.y_axis.n2p(axes.d)]
        
        
        surface_corners=[]
        for x,y,z in self.region_corners:
            surface_corners.append([x,y,self.Func(x,y)])
            
        lines=VGroup()
        for start , end in zip(surface_corners,
        self.region_corners):
            lines.add(self.draw_lines(start,end,"PINK"))
            
        for start , end in zip(labels,
        self.region_corners):
         #   lines.add(self.draw_lines(start,end,"BLUE"))
         #   print (start,end)
            pass
       # self.play(ShowCreation(lines))
        self.add(lines)
        
              
    def draw_lines(self,start,end,color):
        start=self.axes.c2p(*start)
        end=self.axes.c2p(*end)
        line=DashedLine(start,end,color=color)
        
        return line
        
#-------------------------------------------------------            
    #customize 3D axes        
    def get_three_d_axes(self, include_labels=True, include_numbers=True, **kwargs):
        config = dict(self.axes_config)
        config.update(kwargs)
        axes = ThreeDAxes(**config)
        axes.set_stroke(width=2)
        self.axes=axes
        
        if include_numbers:
            self.add_axes_numbers(axes)

        if include_labels:
            self.add_axes_labels(axes)

        # Adjust axis orientation
        '''axes.x_axis.rotate(
            -90 * DEGREES, LEFT,
            about_point=axes.c2p(0, 0, 0),
        )
        axes.y_axis.rotate(
            90 * DEGREES, UP,
            about_point=axes.c2p(0, 0, 0),
        )'''

        return axes
        
        
    def setup_axes(self):
        axes = self.get_three_d_axes(include_labels=True)
        axes.scale(1)
     #   axes.center()
        axes.shift(axes.axes_shift)

        self.add(axes)
        self.axes = axes
        
    def add_axes_numbers(self, axes):
        x_axis = axes.x_axis
        y_axis = axes.y_axis
        tex_vals_x = [
           
            ("1", axes.b),
        ]
        tex_vals_y=[
           
            ("1", axes.d)
        ]
        x_labels = VGroup()
        y_labels = VGroup()
        for tex, val in tex_vals_x:
            label = TexMobject(tex)
            label.scale(1)
            label.next_to(x_axis.n2p(val), DOWN)
       #     label.rotate(180 * DEGREES)
            x_labels.add(label)
        x_axis.add(x_labels)
        x_axis.numbers = x_labels

        for tex, val in tex_vals_y:
            label = TexMobject(tex)
            label.scale(1)
            label.next_to(y_axis.n2p(val), LEFT)
            label.rotate(90 * DEGREES)
            y_labels.add(label)
            
        y_axis.add(y_labels)
        y_axis.numbers = y_labels
        
        return axes
    
    def add_axes_labels(self, axes):
        x_label = TexMobject("x")
        x_label.next_to(axes.x_axis.get_end(), RIGHT)
        axes.x_axis.label = x_label

        y_label = TextMobject("y")
        y_label.rotate(90 * DEGREES, OUT)
        y_label.next_to(axes.y_axis.get_end(), UP)
        axes.y_axis.label = y_label

        z_label = TexMobject("")
        z_label.rotate(90 * DEGREES, RIGHT)
        z_label.next_to(axes.z_axis.get_zenith(), LEFT)
        axes.z_axis.label = z_label
        for axis in axes:
            axis.add(axis.label)
        return axes      
        
        
        
  #uploaded by Somnath Pandit.FSF2020_Line_Integrals
