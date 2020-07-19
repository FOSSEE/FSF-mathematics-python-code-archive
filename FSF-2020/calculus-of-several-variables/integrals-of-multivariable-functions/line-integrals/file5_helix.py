from manimlib.imports import *

class ParametricCurve(ThreeDScene):

    CONFIG = {
        "axes_config": {
            "x_min": 0,
            "x_max": 3,
            "y_min": 0,
            "y_max": 3,
            "z_min": 0,
            "z_max": 4,
            "a":0 ,"b": 2, "c":0 , "d":2,
            "axes_shift":2*IN+1.4*RIGHT+1.4*DOWN,
            "x_axis_config": {
                "tick_frequency": 1,
                "include_tip": False,
            },
            "y_axis_config": {
                "tick_frequency": 1,
                "include_tip": False,
            },
            "z_axis_config": {
                "tick_frequency": 1,
             #   "include_tip": False,
            },
        },
        
    }


    def construct(self):

        self.setup_axes()
        
        self.set_camera_orientation(
            distance=25,
            phi=60 * DEGREES,
            theta=40 * DEGREES,
        )
        
        label=TextMobject("Helix",color=PURPLE).scale(1.6)
        label.to_corner(UR,buff=2)
        self.add_fixed_in_frame_mobjects(label) 
   
        helix=self.get_helix(
            radius=1.5,
            t_min= 0,
            t_max= 4*PI, 
            color=PURPLE 
        )
        parameter_label=TextMobject(
            "Parametric equation: ",
            color=TEAL
            ).next_to(label,DOWN,buff=.3
        )
        parametric_eqn=TextMobject(
            "$x=\cos$ (","t",
            r")\\$y=\sin $(","t",
            r")\\$z$=","t"
        ).next_to(parameter_label,DOWN,buff=.1)  
        parametric_eqn.set_color_by_tex("t",RED)
        self.parametric_eqn=parametric_eqn
        
        parametriztion=VGroup(
            parameter_label,
            parametric_eqn
            )
        
        
        self.play(ShowCreation(helix),run_time=2)
        self.begin_ambient_camera_rotation(.1)
        self.wait(1)
        self.add_fixed_in_frame_mobjects(parametriztion) 
        self.play(Write(parametriztion))
        self.wait(1)
        self.stop_ambient_camera_rotation()
        self.move_camera(
            distance=20,
            phi=85 * DEGREES,
     #       theta=-90 * DEGREES,
            run_time=3
        )
        scale_axes=VGroup(self.axes,helix).scale(1.2)
        self.show_the_parameter()
        self.wait(2)
    
    
    
    def get_helix(self,radius=1, **kwargs):
        config = {
            "t_min": 0,
            "t_max": 2*PI,    
        }
        config.update(kwargs)
        helix= ParametricFunction(
            lambda  t : self.axes.c2p(
                radius*np.cos(t),
                radius*np.sin(t),
                t/4
            ),
            **config
        )
        
        self.helix=helix
        return helix
 
    def show_the_parameter(self):              
        t_tracker = ValueTracker(0)
        t=t_tracker.get_value
 
        t_label = TexMobject(
            "t = ",color=RED
            ).next_to(self.parametric_eqn,DL,buff=.85)
        
        t_text = always_redraw(
            lambda: DecimalNumber(
                t(),
                color=GOLD,
            ).next_to(t_label, RIGHT, MED_SMALL_BUFF)
        )
        t_text.suspend_updating()
        
        dot = Sphere(
                radius= 1.5*DEFAULT_DOT_RADIUS,
                stroke_width= 1,
                fill_opacity= 1.0,
               )
        dot.set_color(GOLD)
        dot.add_updater(lambda v: v.move_to(
            self.helix.get_point_from_function(PI*t())
        ))
        
        pi = TexMobject(
            "\\pi ",
            color=GOLD,
        ).next_to(t_text,RIGHT,buff=-.3)
            
        group = VGroup(t_text,t_label,pi).scale(1.5)

        self.wait(1)
        self.add_fixed_in_frame_mobjects(group)
        t_text.resume_updating()
        self.play(FadeIn(group))
        self.add(dot)
        self.play(
            t_tracker.set_value,2,
            rate_func=linear,
            run_time=5
            )
 
 
#--------------------------------------------------------  
        
    #customize 3D axes        
    def get_three_d_axes(self, include_labels=True, include_numbers=False, **kwargs):
        config = dict(self.axes_config)
        config.update(kwargs)
        axes = ThreeDAxes(**config)
        axes.set_stroke(width=1.5)

        if include_numbers:
            self.add_axes_numbers(axes)

        if include_labels:
            self.add_axes_labels(axes)

        # Adjust axis orientation
        axes.x_axis.rotate(
            90 * DEGREES, LEFT,
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
            label.rotate(180 * DEGREES)
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
        z_label.rotate(90 * DEGREES, LEFT)
        z_label.next_to(axes.z_axis.get_zenith(), LEFT)
        axes.z_axis.label = z_label
        for axis in axes:
            axis.add(axis.label)
        return axes  
        
  #uploaded by Somnath Pandit.FSF2020_Line_integrals
  
  
          
        
    
