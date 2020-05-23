from manimlib.imports import *

class ElementaryArea(GraphScene):
    CONFIG = {
        "x_min" : 0,
        "x_max" : 2,
        "y_min" : 0,
        "y_max" : 2, 
        "x_tick_frequency" : 1,
        "y_tick_frequency" : 1,
     #   "x_labeled_nums": list(np.arange(0,3)),
      #  "y_labeled_nums": list(np.arange(0 ,3)),
        "x_axis_width": 6,
        "y_axis_height": 6,
        "graph_origin": ORIGIN+3.5*LEFT+3.5*DOWN,    
    }

    def construct(self):
        X = self.x_axis_width/(self.x_max- self.x_min)
        Y = self.y_axis_height/(self.y_max- self.y_min)
        self.X=X ;self.Y=Y 
        self.setup_axes(animate=False)
        
        caption=TextMobject("The elementary area in ").to_edge(UP)
        rect_text=TextMobject("Cartesian Coordinates").next_to(caption,DOWN,)
        polar_text=TextMobject("Polar Coordinates").next_to(caption,DOWN,) 
        
        self.add(caption)
        self.play(Write(rect_text))
        self.get_rect_element()
    #    self.play(Write(polar_text))
        self.play(ReplacementTransform(rect_text,polar_text),
          FadeOut(VGroup(self.dydx,self.rect_brace_gr)))
        self.get_polar_element()
        
        
        
    def get_rect_element(self):
        rect=Rectangle(
            height=2, width=3,fill_color=BLUE_D,
            fill_opacity=1, color=BLUE_D
            ).scale(.75).move_to(
            self.graph_origin+(RIGHT*self.X+UP*self.Y)
            )
        dx_brace=Brace(rect, DOWN, buff = SMALL_BUFF)
        dx_label=dx_brace.get_text("$dx$", buff = SMALL_BUFF)
        dx_brace_gr=VGroup(dx_brace,dx_label)
        
        dy_brace=Brace(rect,RIGHT, buff = SMALL_BUFF)
        dy_label=dy_brace.get_text("$dy$", buff = SMALL_BUFF)
        dy_brace_gr=VGroup(dy_brace,dy_label)
        
        brace_gr=VGroup(dx_brace_gr,dy_brace_gr)
        
        dydx=TextMobject("$dxdy$",color=BLACK).next_to(rect,IN)

        self.play(FadeIn(rect))
        self.play(GrowFromCenter(brace_gr))
        self.play(GrowFromCenter(dydx))
                 
        self.rect=rect
        self.rect_brace_gr=brace_gr
        self.dydx=dydx
        self.wait(2)
  
        
    def  get_polar_element(self):
        X=self.X ;Y=self.Y 
        theta1=25*DEGREES
        dtheta=TAU/12
        r_in=1.3*X ; r_out=1.9*X
        
        arc=AnnularSector(
        arc_center=self.graph_origin,
        inner_radius=r_in,
        outer_radius=r_out ,
        angle= dtheta,
        start_angle= theta1,
        fill_opacity= 1,
        stroke_width= 0,
        color= BLUE_D, 
        )
        
        
    # # #getting braces
        r_in_theta1=self.graph_origin+r_in*(np.cos(theta1)*RIGHT+np.sin(theta1)*UP)
        dr_line=Line(r_in_theta1,r_in_theta1+RIGHT*(r_out-r_in))
        dr_brace=Brace(dr_line, DOWN, buff = SMALL_BUFF
            ).rotate(theta1, about_point=r_in_theta1
            )
        dr_label=dr_brace.get_text("$dr$", buff = SMALL_BUFF)
        dr_brace_gr=VGroup(dr_brace,dr_label)
        
        theta2=theta1+dtheta
        r_out_theta2=self.graph_origin+r_out*(
            np.cos(theta2)*RIGHT+np.sin(theta2)*UP
            )
        rdt_line=Line(r_out_theta2,r_out_theta2
            +DOWN*(r_out*dtheta)
            )
        rdt_brace=Brace(rdt_line, RIGHT, 
            buff = MED_SMALL_BUFF).rotate(
            theta2-(dtheta/2), about_point=r_out_theta2
            )
        rdt_label=rdt_brace.get_text("$rd\\theta$",buff = SMALL_BUFF)
        rdt_brace_gr=VGroup(rdt_brace,rdt_label)
   
   #getting label r and dtheta 
        r1=DashedLine(self.graph_origin,r_in_theta1).set_color(RED)
        r2=DashedLine(self.graph_origin,r_out_theta2).set_color(RED)   
        r_brace=Brace(r1, DOWN, buff = SMALL_BUFF).rotate(theta1, about_point=self.graph_origin)
        r_label=r_brace.get_text("$r$", buff = SMALL_BUFF)
        r_brace_gr=VGroup(r_brace,r_label)
        
        dtheta_arc=Arc(
        arc_center=self.graph_origin,
        radius=.5*X,
        angle= dtheta,
        start_angle=  theta1,
        )
        dtheta_arc_label=TextMobject("$d\\theta$").move_to(.99*dtheta_arc.get_corner(UR))
        dtheta_label=VGroup(dtheta_arc,dtheta_arc_label)
        
        
        rdrdt=TextMobject("$rdrd\\theta$",color=BLACK).next_to(arc,IN)
        self.play(ReplacementTransform(self.rect,arc))
        self.wait()
        self.play(ShowCreation(r1),
                ShowCreation(r2)
                )
        self.play(ShowCreation(r_brace_gr),
                Write(dtheta_label)
                )
        self.wait()
        self.play(GrowFromCenter(rdt_brace_gr))
        self.wait(.5)
        self.play(GrowFromCenter(dr_brace_gr))
        self.wait(.5)
        self.play(GrowFromCenter(rdrdt))
        
        self.wait(2)
        
        
  #uploaded by Somnath Pandit.FSF2020_Double_Integral
