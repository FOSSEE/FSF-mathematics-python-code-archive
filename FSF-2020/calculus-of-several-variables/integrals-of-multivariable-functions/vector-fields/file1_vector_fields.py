from manimlib.imports import *

class VectorFields(ThreeDScene):

    CONFIG = {
        "axes_config": {
            "x_min": -4,
            "x_max": 4,
            "y_min": -4,
            "y_max": 4,
            "z_min": -3,
            "z_max": 3,
            "a":-4 ,"b": 4, "c":-4 , "d":4,
            "axes_shift": ORIGIN+2*LEFT,
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
            "num_axis_pieces": 10,
        },
        "default_graph_style": {
            "stroke_width": 2,
            "stroke_color": WHITE,
        },
        "default_vector_field_config": {
            "delta_x": .5,
            "delta_y": .5,
            "x_min": -3,
            "x_max": 3, 
            "y_min": -3,
            "y_max": 3,
            "min_magnitude": 0,
            "max_magnitude": 4,
            "colors": [BLUE,GREEN,ORANGE,RED],
            "length_func": lambda norm : .45*sigmoid(norm),
            "opacity": 1.0,
            "vector_config": {
                "stroke_width":3.5,
                "max_tip_length_to_length_ratio": 0.35,
                "max_stroke_width_to_length_ratio": 8,
            },
        },
        
    }


    def construct(self):

        self.setup_axes()
        axes=self.axes
        
        self.set_camera_orientation(distance=35,
            phi=0 * DEGREES,
            theta=-90 * DEGREES,
        )
        self.move_camera(frame_center=axes.c2p(0,0,0))
        
        self.show_2d_field()
        self.wait(3)
        
        self.show_3d_field()
        self.begin_ambient_camera_rotation(rate=-.3,)
        self.wait(1.5)
        axes.x_axis.rotate(
                    -90 * DEGREES, LEFT,
                    about_point=axes.c2p(0, 0, 0),
                ),
        axes.y_axis.rotate(
                90 * DEGREES, UP,
                about_point=axes.c2p(0, 0, 0),
                ),
        self.move_camera(
          #  distance=20,
            phi=85 * DEGREES,
            rate_func=linear,
            run_time=8
        )
        self.wait(5)
    
    
    def show_2d_field(self): 
        d2_field_text=TexMobject(
            r"\vec F(x,y)=-y\hat i+x\hat j",
            stroke_width=1.5
            ).set_color_by_gradient(
            *self.default_vector_field_config["colors"]
        )
        d2_field_text.to_corner(UR,buff=.5)
        
        d2_field = self.get_vector_field(
            lambda v: np.array([
            -v[1],
            v[0],
            0
            ]),
        )
        self.add_fixed_in_frame_mobjects(d2_field_text)
     #   self.add(d2_field)
        self.play(Write(d2_field_text))
        self.play(FadeIn(d2_field))
        
        self.d2_field=d2_field
        self.d2_field_text=d2_field_text
        
    def show_3d_field(self):
        d3_field_text=TexMobject(
            r"\vec F(x,y,z)=-y\hat i+x\hat j+0 \hat k",
            stroke_width=1.5
            ).set_color_by_gradient(
            *self.default_vector_field_config["colors"]
        )
        d3_field_text.to_corner(UR,buff=.5)
        
        d3_field= self.get_vector_field(
            lambda v: np.array([
            -v[1],
            v[0],
            0
       #     v[0]*v[2]
            ]),
            z_min=-2,
            z_max= 2,
            delta_x= 1,
            delta_y= 1,
            delta_z= 1,
            length_func=lambda norm : .5*sigmoid(norm),
            opacity= 1,
            ThreeD=True
        )
        
        self.remove(self.d2_field,self.d2_field_text)
        self.add_fixed_in_frame_mobjects(d3_field_text)
    #    self.add(d3_field)
        self.play(Write(d3_field_text))
        self.play(FadeIn(d3_field))
    
    def get_vector_field(self,func,ThreeD=False,**kwargs):
        config = dict()
        config.update(self.default_vector_field_config)
        config.update(kwargs)
        if ThreeD:
            vector_field= VectorField3D(func,**config)
        else:
            vector_field= VectorField(func,**config)
        
        vector_field.move_to(self.axes.c2p(0,0,0))
        self.vector_field=vector_field
            
        return vector_field
 
   

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
            -0 * DEGREES, LEFT,
            about_point=axes.c2p(0, 0, 0),
        )
        axes.y_axis.rotate(
            0 * DEGREES, UP,
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
        
#-----------------------------------------------------------
   
class VectorField3D(VGroup):
    CONFIG = {
        "delta_x": 1,
        "delta_y": 1,
        "delta_z": 1,
        "x_min": int(np.floor(-FRAME_WIDTH / 2)),
        "x_max": int(np.ceil(FRAME_WIDTH / 2)),
        "y_min": int(np.floor(-FRAME_HEIGHT / 2)),
        "y_max": int(np.ceil(FRAME_HEIGHT / 2)),
        "z_min":-1,
        "z_max": 1,
        "min_magnitude": 0,
        "max_magnitude": 4,
        "colors": DEFAULT_SCALAR_FIELD_COLORS,
        # Takes in actual norm, spits out displayed norm
        "length_func": lambda norm: 0.45 * sigmoid(norm),
        "opacity": 1.0,
        "vector_config": {},
    }
    '''Position of the tip of vector to be fixed'''
    def __init__(self, func, **kwargs):
        VGroup.__init__(self, **kwargs)
        self.func = func
        self.rgb_gradient_function = get_rgb_gradient_function(
            self.min_magnitude,
            self.max_magnitude,
            self.colors,
            flip_alphas=False
        )
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
        z_range = np.arange(
            self.z_min,
            self.z_max + self.delta_z,
            self.delta_z
        )
        for x, y, z in it.product(x_range, y_range, z_range):
            point = x * RIGHT + y * UP + z * OUT
        #    print(point)
            self.add(self.get_vector(point))
        self.set_opacity(self.opacity)

    def get_vector(self, point, **kwargs):
        output = np.array(self.func(point))
        norm = get_norm(output)
        if norm == 0:
            output *= 0
        else:
            output *= self.length_func(norm) / norm
      #  norm=np.linalg.norm(output)
        vector_config = dict(self.vector_config)
        vector_config.update(kwargs)
        
        vect = Vector(
            output,
            **vector_config
        )
        vect_perp=vect.copy().rotate(PI/2, axis=output)
        vect= VGroup(vect,vect_perp)
     #   vect= self.position_vector(vect,point,output,norm)
        vect.shift(point)
        fill_color = rgb_to_color(
            self.rgb_gradient_function(np.array([norm]))[0]
        )
        vect.set_color(fill_color)
        return vect
        
    '''def position_vector(self,vect,point,output,norm):
        theta,phi=self.get_theta_phi(output,norm)
        vect.rotate(PI-phi, axis=RIGHT)
        vect.rotate(theta, axis=IN)
    # or apply rotation matrix?
        return vect
        
    def get_theta_phi(self,output,norm):
        if norm==0:
            phi,theta=0,0
        else:
            phi= np.arccos(output[-1]/norm)
            if output[0]!=0:
                theta= np.arccos(output[0]/(norm*np.sin(phi)))
            else:
                theta= 0
        return phi,theta'''
        
        
        
  #uploaded by Somnath Pandit. FSF2020_Vector_fields
  
  
  
