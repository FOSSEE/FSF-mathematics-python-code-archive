from manimlib.imports import *

class GradOfScalar(ThreeDScene):

    CONFIG = {
        "axes_config": {
            "x_min": -3,
            "x_max": 3,
            "y_min": -3,
            "y_max": 3,
            "z_min": 0,
            "z_max": 3,
            "a":-3 ,"b": 3, "c":-3 , "d":3,
            "axes_shift": ORIGIN+IN,
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
            "num_axis_pieces": 1,
        },
        "default_graph_style": {
            "stroke_width": 2,
            "stroke_color": WHITE,
        },
        "default_vector_field_config": {
            "delta_x": 1,
            "delta_y": 1,
            "x_min": -3,
            "x_max": 3,
            "y_min": -3,
            "y_max": 3,
            "min_magnitude": 0,
            "max_magnitude": 2,
            "colors": [TEAL,GREEN,GREEN,GREEN,YELLOW,RED],
            "length_func": lambda norm : norm*np.exp(-.38*norm)/2,
            "opacity": 1.0,
            "vector_config": {
                "stroke_width":8
            },
        },
        "default_surface_config": {
            "fill_opacity": 0.5,
            "checkerboard_colors": [BLUE_E],
            "stroke_width": .5,
            "stroke_color": WHITE,
            "stroke_opacity": 0.75,
        },
    }


    def construct(self):

        self.setup_axes()
        axes=self.axes
        
        self.set_camera_orientation(distance=35,
            phi=70 * DEGREES,
            theta=-135 * DEGREES,
        )
        
        scalar_fn_text=TexMobject("f(x,y,z)=","xy").set_color(BLUE)
        scalar_fn_text.to_corner(UR,buff=.6)
        
        operator=TexMobject("\\vec\\nabla").next_to(
            scalar_fn_text,LEFT,buff=.2
        ).set_color(GOLD)
        grad_text=TexMobject(r"\dfrac{\partial f}{\partial x} \hat i+\dfrac{\partial f}{\partial y} \hat j+\dfrac{\partial f}{\partial z} \hat k").set_color(GOLD)
        grad_text.next_to(scalar_fn_text,DOWN).scale(.9)
        
        VGroup(grad_text[0][1],grad_text[0][9],grad_text[0][17]).set_color(BLUE)
        VGroup(grad_text[0][5:8],grad_text[0][13:16],grad_text[0][21:23]).set_color(WHITE)
        
        vector_field_text=TexMobject("\\vec F=y\hat i+x\hat j").set_color_by_gradient(*self.default_vector_field_config["colors"])
        vector_field_text.next_to(scalar_fn_text,DOWN)
        
        
        #always generate the scalar field first
        s_field1=self.get_scalar_field(
            func= lambda u ,v : u*v/7
        )
        v_field1=self.get_vector_field(
            lambda v: np.array([
            v[1],  
            v[0],  
            0,
            ]),
            on_surface=True,
        )
        
        self.add_fixed_in_frame_mobjects(scalar_fn_text)    
        
        self.begin_ambient_camera_rotation(rate=.2)
        self.play(Write(s_field1))
        self.wait(1)
        self.stop_ambient_camera_rotation()
        
        self.add_fixed_in_frame_mobjects(operator)
        self.play(Write(operator),FadeOut(scalar_fn_text[1]))
        self.add_fixed_in_frame_mobjects(grad_text)
        self.play(Write(grad_text))
        self.wait(2)
        
        self.play(FadeOut(grad_text))
        self.add_fixed_in_frame_mobjects(vector_field_text)
        show_vec_field=[
            FadeIn(v_field1),
            Write(vector_field_text),
        ]
      
        self.begin_ambient_camera_rotation(rate=.2)
        self.move_camera(
          #  distance=20,
            phi=60 * DEGREES,
            added_anims=show_vec_field,
            run_time=4.5
        )

        self.wait(2)
        self.stop_ambient_camera_rotation()
        
        fadeout= [FadeOut(s_field1)]
        self.move_camera(
          #  distance=20,
            phi=0 * DEGREES,
            theta=-90 * DEGREES,
            added_anims=fadeout,
            run_time=2
        )
        self.wait(2)
            
            
    
        
        
    def get_scalar_field(self,func,**kwargs):
        surface= self.get_surface(
            lambda x , y: 
            func(x,y),
        )
       
        self.surface_points=self.get_points(func)
        return surface
    
    def get_points(self,func):
        axes=self.axes
        dn=.5
        x_vals=np.arange(axes.a,axes.b,dn)
        y_vals=np.arange(axes.c,axes.d,dn)
        points=[]
        for x_val in x_vals:
          for y_val in y_vals:
            points+=[axes.c2p(x_val,y_val,func(x_val,y_val)+.05)]
        return points  
    
    def get_vector_field(self,func,on_surface=True,**kwargs):
        config = dict()
        config.update(self.default_vector_field_config)
        config.update(kwargs)
        vector_field= VectorField(func,**config)
        self.vector_field=vector_field
        
        if on_surface:
            vector_field=self.get_vectors_on_surface()
            
        return vector_field
        
    
        
    def get_vectors_on_surface(self):
        config = dict()
        config.update(self.default_vector_field_config["vector_config"])
        vectors_on_surface = VGroup(*[
            self.vector_field.get_vector(point,**config) 
            for point in self.surface_points
        ])

        return vectors_on_surface
       
        
    def get_surface(self, func, **kwargs):
        axes=self.axes
        config = {
            "u_min": axes.a,
            "u_max": axes.b,
            "v_min": axes.c,
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
       
    
        
#-------------------------------------------------------            
    #customize 3D axes        
    def get_three_d_axes(self, include_labels=True, include_numbers=False, **kwargs):
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
        axes.x_axis.rotate(
            -90 * DEGREES, LEFT,
            about_point=axes.c2p(0, 0, 0),
        )
        axes.y_axis.rotate(
            90 * DEGREES, UP,
            about_point=axes.c2p(0, 0, 0),
        )
        
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
            ("-1", axes.a),
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

        z_label = TextMobject("z")
        z_label.rotate(90 * DEGREES, RIGHT)
        z_label.next_to(axes.z_axis.get_zenith(), LEFT)
        axes.z_axis.label = z_label
        for axis in axes:
            axis.add(axis.label)
        return axes      
        
        
        
  #uploaded by Somnath Pandit. FSF2020_Fundamental_Theorem_of_Line_Integrals
  
  
  
  
