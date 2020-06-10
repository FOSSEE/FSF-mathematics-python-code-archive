from manimlib.imports import *

class IntegrationProcess(SpecialThreeDScene):

    CONFIG = {
        "axes_config": {
            "x_min": 0,
            "x_max": 7,
            "y_min": 0,
            "y_max": 7,
            "z_min": 0,
            "z_max": 4,
            "a":1 ,"b": 6, "c":2 , "d":6,
            "axes_shift":-3*OUT,
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
        "default_surface_config": {
            "fill_opacity": 0.5,
            "checkerboard_colors": [LIGHT_GREY],
            "stroke_width": 0.5,
            "stroke_color": WHITE,
            "stroke_opacity": 0.5,
        },
    "Func": lambda x,y: 2+y/4+np.cos(x/1.4)
    }


    def construct(self):

        self.setup_axes()
        axes=self.axes
        
        self.camera.frame_center.shift(axes.c2p(3,4,1.7))
        self.set_camera_orientation(distance=35,
            phi= 80 * DEGREES,
            theta= -80 * DEGREES,
            gamma = 0 * DEGREES
        )
        
        fn_text=TextMobject("$z=f(x,y)$").set_color(PINK)
        self.add_fixed_in_frame_mobjects(fn_text) 
        
        
        R=TextMobject("R").set_color(BLACK).scale(3)
        R.move_to(axes.input_plane,IN)
        self.add(R)
        
       # get the surface
        surface= self.get_surface(
            axes, lambda x , y: 
            self.Func(x,y)
        )
        surface.set_style(
            fill_opacity=.65,
            fill_color=PINK,
            stroke_width=0.8,
            stroke_color=WHITE,
        )
        fn_text.next_to(surface,UP,buff=MED_LARGE_BUFF)
        slice_curve=(self.get_y_slice_graph(
            axes,self.Func,5,color=YELLOW))
            

        self.begin_ambient_camera_rotation(rate=0.08)
     #   self.play(Write(surface))
        self.add(surface)
        
        self.get_lines()
      
        self.show_process(axes)
        
        self.wait(3)
        
     
    
    def show_process(self,axes):
        y_tracker = ValueTracker(axes.c)
        self.y_tracker=y_tracker
        y=y_tracker.get_value
        
        graph = always_redraw(
            lambda: self.get_y_slice_graph(
                axes, self.Func, y(),
            stroke_color=YELLOW,
            stroke_width=4,
            )
        )
        graph.suspend_updating()
        

        plane = always_redraw(lambda: Polygon(
            *[
            axes.c2p(x,y(),self.Func(x,y())) 
                for x in np.arange(axes.a,axes.b,0.01)
            ],
            *[
             axes.c2p(x, y(), 0)
                for x in [ axes.b, axes.a,]
            ],
            stroke_width=2,
            fill_color=BLUE_D,
            fill_opacity=.4,
        ))
        
        plane_side1 = always_redraw(lambda: Polygon(
            *[
            axes.c2p(axes.a,y,self.Func(axes.a,y)) 
                for y in np.arange(axes.c,y(),0.01)
            ],
            *[
             axes.c2p(axes.a, y, 0)
                for y in [ y(),axes.c, ]
            ],
            stroke_width=2.5,
            fill_color=BLUE_C,
            fill_opacity=.2,
        ))
        plane_side2 = always_redraw(lambda: Polygon(
            *[
            axes.c2p(axes.b,y,self.Func(axes.b,y)) 
                for y in np.arange(axes.c,y(),0.01)
            ],
            *[
             axes.c2p(axes.b, y, 0)
                for y in [y(),axes.c,] 
            ],
            stroke_width=2.5,
            fill_color=BLUE_E,
            fill_opacity=.45,
        ))
        plane.suspend_updating()
        plane_side1.suspend_updating()
        plane_side2.suspend_updating()
        
        self.play(Write(VGroup(graph,plane)),run_time=2)
        self.add(plane.copy(),plane_side1,plane_side2)
        

        plane_side1.resume_updating()
        plane_side2.resume_updating()
        
        self.move_camera(
            distance=30,
            phi= 85 * DEGREES,
            theta= -10 * DEGREES,
            run_time=1.5
        )
        self.play(
            ApplyMethod(
                y_tracker.set_value, axes.d,
                rate_func=linear,
                run_time=6,
            ) 
        )
        plane.suspend_updating()
        plane_side1.suspend_updating()
        plane_side2.suspend_updating()
        
        

    def get_y_slice_graph(self, axes, func, y, **kwargs):
        config = dict()
        config.update(self.default_graph_style)
        config.update({
            "t_min": axes.a,
            "t_max": axes.b,
        })
        config.update(kwargs)
        slice_curve=ParametricFunction(
            lambda x: axes.c2p(
                x, y, func(x, y)
            ),
            **config,
        )
        return slice_curve
  
        
    def get_surface(self,axes, func, **kwargs):
        config = {
            "u_min": axes.a,
            "u_max": axes.b,
            "v_min": axes.c,
            "v_max": axes.d,
            "resolution": (
                (axes.y_max - axes.y_min) // axes.y_axis.tick_frequency,
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
        
    def get_lines(self):
        axes = self.axes
        
        surface_corners=[]
        for x,y,z in self.region_corners:
            surface_corners.append([x,y,self.Func(x,y)])
            
        lines=VGroup()
        for start , end in zip(surface_corners,
        self.region_corners):
            lines.add(self.draw_lines(start,end,"RED"))
        
        labels=[
            (axes.a,0,0), 
            (axes.b,0,0), 
            (0,axes.d,0), 
            (0,axes.c,0)
        ]  
        self.region_corners[-1]=self.region_corners[0]
        for start , end in zip(labels,
        self.region_corners):
            lines.add(self.draw_lines(start,end,"WHITE"))
        self.add(lines)
        
              
    def draw_lines(self,start,end,color):
        start=self.axes.c2p(*start)
        end=self.axes.c2p(*end)
        line=DashedLine(start,end,color=color)
        
        return line
   
   
#------------------------------------------------------------
    #customize 3d axes            
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
            90 * DEGREES, RIGHT,
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
            fill_opacity=0.5,
            fill_color=TEAL,
            stroke_width=0,
            stroke_color=WHITE,
        )

        axes.input_plane = input_plane

        self.region_corners=[ 
        input_plane.get_corner(pos) for pos in (DL,DR,UL,UR)]
        
        return axes
        
        
    def setup_axes(self):
        axes = self.get_three_d_axes(include_labels=True)
        axes.add(axes.input_plane)
        axes.scale(1)
     #   axes.center()
        axes.shift(axes.axes_shift)

        self.add(axes)
        
        self.axes = axes
        
    def add_axes_numbers(self, axes):
        x_axis = axes.x_axis
        y_axis = axes.y_axis
        tex_vals_x = [
            ("a", axes.a),
            ("b", axes.b),
        ]
        tex_vals_y=[
            ("c", axes.c),
            ("d", axes.d)
        ]
        x_labels = VGroup()
        y_labels = VGroup()
        for tex, val in tex_vals_x:
            label = TexMobject(tex)
            label.scale(1)
            label.next_to(x_axis.n2p(val), DOWN)
            x_labels.add(label)
        x_axis.add(x_labels)
        x_axis.numbers = x_labels

        for tex, val in tex_vals_y:
            label = TexMobject(tex)
            label.scale(1.5)
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
        z_label.next_to(axes.z_axis.get_zenith(), RIGHT)
        axes.z_axis.label = z_label
        for axis in axes:
            axis.add(axis.label)
        return axes    
        
        
        
  #uploaded by Somnath Pandit.FSF2020_Double_Integral
