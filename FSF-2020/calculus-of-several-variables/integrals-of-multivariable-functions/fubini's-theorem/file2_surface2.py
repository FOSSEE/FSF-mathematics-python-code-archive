from manimlib.imports import *

class SurfacesAnimation(ThreeDScene):

    CONFIG = {
        "axes_config": {
            "x_min": 0,
            "x_max": 4,
            "y_min": 0,
            "y_max": 4,
            "z_min": -2,
            "z_max": 4,
            "a":0 ,"b": 4, "c":0 , "d":4,
            "axes_shift":IN+2*LEFT+2*DOWN,
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
            "num_axis_pieces": 1,
        },
        "default_graph_style": {
            "stroke_width": 2,
            "stroke_color": WHITE,
        },
        "default_surface_config": {
            "fill_opacity": 0.5,
            "checkerboard_colors": [LIGHT_GREY],
            "stroke_width": 0.5,
            "stroke_color": WHITE,
            "stroke_opacity": 0.5,
        },
    "Func": lambda x,y: x*y/4
    }


    def construct(self):

        self.setup_axes()
        self.set_camera_orientation(
            distance=30,
            phi=75 * DEGREES,
            theta=20 * DEGREES,
        )
        
        fn_text=TextMobject("$z=xy$").set_color(BLUE).scale(1.5)
        fn_text.to_corner(UR,buff=2)
        self.add_fixed_in_frame_mobjects(fn_text) 
        
        
        #get the surface
        surface= self.get_surface(
            self.axes, lambda x , y: 
            self.Func(x,y)
        )
        surface.set_style(
            fill_opacity=.5,
            fill_color=BLUE_E,
            stroke_width=0.2,
            stroke_color=WHITE,
        )
        #get boundary curves
        c1=self.get_curve(
        self.axes, lambda x: x**2/4
        )
        c1_label=TextMobject("$y=x^2$").next_to(c1,IN+OUT).shift(DOWN+RIGHT)
        c1_label.rotate(PI)
        c1_group=VGroup(c1,c1_label).set_color(ORANGE)

        c2=self.get_curve(
        self.axes, lambda x: x
        ).set_color(PINK)
        c2_label=TextMobject("$y=x$").next_to(c2,IN+OUT)
        c2_label.rotate(PI/2,about_point=(c2_label.get_corner(UL)))
        c2_group=VGroup(c2,c2_label).set_color(YELLOW_E)
        
        
        
        self.add(c1,c2,c1_label,c2_label)
        
        self.begin_ambient_camera_rotation(rate=0.4)
        self.get_region(self.axes,c1,c2)
        self.play(Write(surface))
        self.get_lines()
        self.wait(1)
        self.stop_ambient_camera_rotation()
        self.move_camera(
            distance=20,
            phi=10 * DEGREES,
            theta=80 * DEGREES,
            run_time=2.5
        )
        self.wait(2)
    
    
    
    def get_curve(self,axes, func, **kwargs):
        config = {
            "t_min": axes.x_min,
            "t_max": axes.x_max,    
        }
        config.update(kwargs)
        return ParametricFunction(
            lambda  x : axes.c2p(
                x, func(x),0
            ),
            **config
        )
    
    def get_region(self,axes,curve1,curve2,**kwargs):
        x_vals=np.arange(axes.x_min,axes.x_max,.1)
        c1_points=[curve1.get_point_from_function(x) for x in x_vals]
        c2_points=[curve2.get_point_from_function(x) for x in x_vals]
        c2_points.reverse()
        points=c1_points+c2_points
        region=Polygon(*points,
            stroke_width=0,  
            fill_color=PINK,
            fill_opacity=.5
        )
        R=TextMobject("R").set_color(PINK).scale(2).rotate(180*DEGREES , OUT)
        R.move_to(region,IN+RIGHT)
        
        self.play(Write(region))
        self.add(R)
              
    def get_surface(self,axes, func, **kwargs):
        config = {
            "u_min": axes.x_max,
            "u_max": axes.x_min,
            "v_min": axes.y_max,
            "v_max": axes.y_min,
            "resolution": (10,10),
        }
        
        config.update(self.default_surface_config)
        config.update(kwargs)
        return ParametricSurface(
            lambda  x,y : axes.c2p(
                x, y, func(x, y)
            ),
            **config
        )
        
    def get_lines(self):
        axes = self.axes
        labels=[axes.x_axis.n2p(axes.a), axes.x_axis.n2p(axes.b), axes.y_axis.n2p(axes.c),       
            axes.y_axis.n2p(axes.d)]
        
        
        surface_corners=[]
        for x,y,z in self.region_corners:
            surface_corners.append([x,y,self.Func(x,y)])
            
        lines=VGroup()
        for start , end in zip(surface_corners,
        self.region_corners):
            lines.add(self.draw_lines(start,end,"YELLOW"))
            
        for start , end in zip(labels,
        self.region_corners):
         #   lines.add(self.draw_lines(start,end,"BLUE"))
         #   print (start,end)
         pass
        self.play(ShowCreation(lines))
        
             
    def draw_lines(self,start,end,color):
        start=self.axes.c2p(*start)
        end=self.axes.c2p(*end)
        line=DashedLine(start,end,color=color)
        
        return line
        
    #customize 3D axes        
    def get_three_d_axes(self, include_labels=True, include_numbers=True, **kwargs):
        config = dict(self.axes_config)
        config.update(kwargs)
        axes = ThreeDAxes(**config)
        axes.set_stroke(width=2)

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

        # Add xy-plane
        input_plane = self.get_surface(
            axes, lambda x, t: 0
        )
        input_plane.set_style(
            fill_opacity=0.3,
            fill_color=PINK,
            stroke_width=.2,
            stroke_color=WHITE,
        )

        axes.input_plane = input_plane

        self.region_corners=[ 
        input_plane.get_corner(pos) for pos in (DL,DR,UR,UL)]
        
        return axes
        
        
    def setup_axes(self):
        axes = self.get_three_d_axes(include_labels=True)
     #   axes.add(axes.input_plane)
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
        
  #uploaded by Somnath Pandit.FSF2020_Fubini's_Theorem
  
  
