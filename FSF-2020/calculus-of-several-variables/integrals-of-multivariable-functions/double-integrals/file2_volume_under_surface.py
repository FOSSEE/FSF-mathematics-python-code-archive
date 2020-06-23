from manimlib.imports import *

class SurfacesAnimation(ThreeDScene):

    CONFIG = {
        "axes_config": {
            "x_min": 0,
            "x_max": 7,
            "y_min": 0,
            "y_max": 7,
            "z_min": 0,
            "z_max": 5,
            "a":1 ,"b": 6, "c":2 , "d":6,
            "axes_shift":-3*OUT + 5*LEFT,
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
    "Func": lambda x,y: 2+y/4+np.sin(x)
    }


    def construct(self):

        self.setup_axes()
        self.set_camera_orientation(distance=35,
            phi=80 * DEGREES,
            theta=-100 * DEGREES,
        )
        
        fn_text=TextMobject(
            "$z=f(x,y)$",
            color=PINK,
            stroke_width=1.5
        )
        self.add_fixed_in_frame_mobjects(fn_text) 
        fn_text.to_edge(TOP,buff=MED_SMALL_BUFF)
        
        riemann_sum_text=TextMobject(
            r"The volume approximated as\\ sum of cuboids",
            color=BLUE,
            stroke_width=1.5
        )
        riemann_sum_text.to_corner(UR,buff=.2)
        
        R=TextMobject("R").set_color(BLACK).scale(3)
        R.move_to(self.axes.input_plane,IN)
        self.add(R)
        
        #get the surface
        surface= self.get_surface(
            self.axes, lambda x , y: 
            self.Func(x,y)
        )
        surface.set_style(
            fill_opacity=0.8,
            fill_color=PINK,
            stroke_width=0.8,
            stroke_color=WHITE,
        )
        
        
        self.begin_ambient_camera_rotation(rate=0.06)
        self.play(Write(surface))
     #   self.add(surface)
        
        self.get_lines()
        self.wait(1)
        self.add_fixed_in_frame_mobjects(riemann_sum_text)
        self.play(Write(riemann_sum_text))
        
        cuboids1=self.show_the_riemmann_sum(
            lambda x,y : np.array([x,y,self.Func(x,y)]),
            fill_opacity=1,
            dl=.5,
            start_color=BLUE,
            end_color=BLUE_E,
        )
        self.play(ShowCreation(cuboids1),run_time=5)
        self.play(FadeOut(surface))
        
        cuboids2=self.show_the_riemmann_sum(
            lambda x,y : np.array([x,y,self.Func(x,y)]),
            fill_opacity=1,
            dl=.25,
            start_color=BLUE,
            end_color=BLUE_E,
        )
        self.play(ReplacementTransform(
            cuboids1,
            cuboids2
        ))
        
        cuboids3=self.show_the_riemmann_sum(
            lambda x,y : np.array([x,y,self.Func(x,y)]),
            fill_opacity=1,
            dl=.1,
            start_color=BLUE,
            end_color=BLUE_E,
            stroke_width=.1,
        )
        self.play(
            FadeOut(cuboids2),
            ShowCreation(cuboids3),
        )
        
        self.wait(3)
        
        
        
      
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
            lines.add(self.draw_lines(start,end,"#9CDCEB"))
        
        labels=[
            (axes.a,0,0), 
            (axes.b,0,0), 
            (0,axes.d,0), 
            (0,axes.c,0)
        ]  
        self.region_corners[-1]=self.region_corners[0]
        for start , end in zip(labels,self.region_corners):
            lines.add(self.draw_lines(start,end,"WHITE"))
            
       # self.add(lines)
        self.play(ShowCreation(lines))
        
              
    def draw_lines(self,start,end,color):
        start=self.axes.c2p(*start)
        end=self.axes.c2p(*end)
        line=DashedLine(start,end,color=color)
        
        return line
        
        
    def show_the_riemmann_sum(
        self,
        surface,
        x_min=None,
        x_max=None,
        y_min=None,
        y_max=None,
        dl=.5,
        stroke_width=.5,
        stroke_color=BLACK,
        fill_opacity=1,
        start_color=None,
        end_color=None,
        ):
            x_min = x_min if x_min is not None else self.axes.a
            x_max = x_max if x_max is not None else self.axes.b
            y_min = y_min if y_min is not None else self.axes.c
            y_max = y_max if y_max is not None else self.axes.d
            
            if start_color is None:
                start_color = BLUE
            if end_color is None:
                end_color = BLUE
                
            cuboids = VGroup()
            x_range = np.arange(x_min, x_max, dl)
            y_range = np.arange(y_min, y_max, dl)
            colors = color_gradient([start_color, end_color], len(x_range))
            for x, color in zip(x_range, colors):
              for y in y_range:
                  sample_base = np.array([x ,y ,0])
                  sample_base_dl = np.array([x + dl, y + dl,0])
                  sample_input = np.array([x +0.5*dl, y +0.5*dl,0])
                  
                  base_point = self.axes.c2p(*sample_base)
                  base_dx_point = self.axes.c2p(*sample_base_dl) 
                  
                  surface_val= surface(*sample_input[:2])
                  surface_point = self.axes.c2p(*surface_val)
               
                  points = VGroup(*list(map(VectorizedPoint, [
                      base_point,
                      surface_point,
                      base_dx_point
                  ])))
                    
                #  self.add(points)
                  cuboid = Prism(dimensions=[dl,dl,surface_val[-1]])
                  cuboid.replace(points, stretch=True)
             
                  cuboid.set_fill(color, opacity=fill_opacity)
                  cuboid.set_stroke(stroke_color, width=stroke_width)
                  cuboids.add(cuboid)
            
            return cuboids
            
  
#-------------------------------------------------------  
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
        
    
