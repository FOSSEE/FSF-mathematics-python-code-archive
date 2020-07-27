from manimlib.imports import *
import numpy as np

def div(coordinate):
	x,y = coordinate[:2]
	return np.array([
			x,
			y,
			0
	])




class Grid(VMobject):
    CONFIG = {
        "height": 6.0,
        "width": 6.0,
    }

    def __init__(self, rows, columns, **kwargs):
        digest_config(self, kwargs, locals())
        VMobject.__init__(self, **kwargs)

    def generate_points(self):
        x_step = self.width / self.columns
        y_step = self.height / self.rows

        for x in np.arange(0, self.width + x_step, x_step):
            self.add(Line(
                [x - self.width / 2., -self.height / 2., 0],
                [x - self.width / 2., self.height / 2., 0],
            ))
        for y in np.arange(0, self.height + y_step, y_step):
            self.add(Line(
                [-self.width / 2., y - self.height / 2., 0],
                [self.width / 2., y - self.height / 2., 0]
            ))


class ScreenGrid(VGroup):
    CONFIG = {
        "rows":8,
        "columns":14,
        "height": FRAME_Y_RADIUS*2,
        "width": 14,
        "grid_stroke":0.5,
        "grid_color":WHITE,
        "axis_color":RED,
        "axis_stroke":2,
        "show_points":False,
        "point_radius":0,
        "labels_scale":0.5,
        "labels_buff":0,
        "number_decimals":2
    }

    def __init__(self,**kwargs):
        VGroup.__init__(self,**kwargs)
        rows=self.rows
        columns=self.columns
        grilla=Grid(width=self.width,height=self.height,rows=rows,columns=columns).set_stroke(self.grid_color,self.grid_stroke)

        vector_ii=ORIGIN+np.array((-self.width/2,-self.height/2,0))
        vector_id=ORIGIN+np.array((self.width/2,-self.height/2,0))
        vector_si=ORIGIN+np.array((-self.width/2,self.height/2,0))
        vector_sd=ORIGIN+np.array((self.width/2,self.height/2,0))

        ejes_x=Line(LEFT*self.width/2,RIGHT*self.width/2)
        ejes_y=Line(DOWN*self.height/2,UP*self.height/2)

        ejes=VGroup(ejes_x,ejes_y).set_stroke(self.axis_color,self.axis_stroke)

        divisiones_x=self.width/columns
        divisiones_y=self.height/rows

        direcciones_buff_x=[UP,DOWN]
        direcciones_buff_y=[RIGHT,LEFT]
        dd_buff=[direcciones_buff_x,direcciones_buff_y]
        vectores_inicio_x=[vector_ii,vector_si]
        vectores_inicio_y=[vector_si,vector_sd]
        vectores_inicio=[vectores_inicio_x,vectores_inicio_y]
        tam_buff=[0,0]
        divisiones=[divisiones_x,divisiones_y]
        orientaciones=[RIGHT,DOWN]
        puntos=VGroup()
        leyendas=VGroup()


        for tipo,division,orientacion,coordenada,vi_c,d_buff in zip([columns,rows],divisiones,orientaciones,[0,1],vectores_inicio,dd_buff):
            for i in range(1,tipo):
                for v_i,direcciones_buff in zip(vi_c,d_buff):
                    ubicacion=v_i+orientacion*division*i
                    punto=Dot(ubicacion,radius=self.point_radius)
                    coord=round(punto.get_center()[coordenada],self.number_decimals)
                    leyenda=TextMobject("%s"%coord).scale(self.labels_scale)
                    leyenda.next_to(punto,direcciones_buff,buff=self.labels_buff)
                    puntos.add(punto)
                    leyendas.add(leyenda)

        self.add(grilla,ejes,leyendas)
        if self.show_points==True:
            self.add(puntos)






class ExpDiv(Scene):
	def construct(self):

		#all the text
		field_text = TexMobject(r"\vec F = P\hat i + Q\hat j").shift(3*UP+5*RIGHT)
		field_text_2 = TexMobject(r"\vec F = 2x\hat i + 2y\hat j").shift(3*UP+5*RIGHT)
		p = TexMobject(r"P = 2x").scale(0.8)
		q = TexMobject(r"Q = 2y").next_to(p, RIGHT).scale(0.8)
		pq = VGroup(p, q)
		pq.next_to(field_text_2, DOWN, buff = SMALL_BUFF)
		dpq = TexMobject(r"\frac{\partial P}{\partial x}", r"   \frac{\partial Q}{\partial y}").scale(0.8).next_to(pq, DOWN, buff = LARGE_BUFF)

		
		dp_dq = TexMobject(r"\frac{\partial P}{\partial x} + \frac{\partial Q}{\partial y}", r" = \textrm{div} \vec F").scale(0.8).next_to(pq, DOWN, buff = LARGE_BUFF)
		#dp_dq1 = TexMobject(r" = \textrm{div} \vec F").scale(0.8)
		#dp_dq1.next_to(dp_dq[0], DOWN, buff = SMALL_BUFF)
		dp_text = TexMobject(r"\frac{\partial P}{\partial x}\textit{: the rate of change of the horizontal component as x increases}").shift(3*DOWN).scale(0.8)
		dq_text = TexMobject(r"\frac{\partial Q}{\partial y}\textit{: the rate of change of the vertical component as y increases}").shift(3*DOWN).scale(0.8)


		vector_field = VectorField(div, x_min = -4, x_max = 4, y_min = -4, y_max = 4).shift(1.5*LEFT)

		x_comps=VGroup()
		y_comps=VGroup()
		for vector in vector_field:
			x = Vector(RIGHT, color = BLUE_E)
			y = Vector(UP, color= YELLOW_E)
			x.put_start_and_end_on(vector.points[0], np.array([vector.get_end()[0],vector.points[0][1],0]))
			y.put_start_and_end_on(vector.points[0], np.array([vector.points[0][0],vector.get_end()[1],0]))
			x_comps.add(x)
			y_comps.add(y)

		line1 = Arrow(4*LEFT, 4*RIGHT).shift(3.5*DOWN+1.5*LEFT)
		line2 = Arrow(4*DOWN, 4*UP).shift(3*RIGHT)




		# f(x) = x**2
		fx = lambda x: x.get_value()/10
		# ValueTrackers definition
		x_value = ValueTracker(-4)
		fx_value = ValueTracker(fx(x_value))
		# DecimalNumber definition
		x_tex = DecimalNumber(x_value.get_value()).add_updater(lambda v: v.set_value(x_value.get_value()))
		fx_tex = DecimalNumber(fx_value.get_value()).add_updater(lambda v: v.set_value(fx(x_value)))
		# TeX labels definition
		x_label = TexMobject("x = ")
		fx_label = TexMobject("P = ")
		# Grouping of labels and numbers
		group = VGroup(x_tex,fx_tex,x_label,fx_label).scale(0.8)
		VGroup(x_tex, fx_tex).arrange_submobjects(DOWN,buff=0.3)
		# Align labels and numbers
		x_label.next_to(x_tex,LEFT, buff=0.1,aligned_edge=x_label.get_bottom())
		fx_label.next_to(fx_tex,LEFT, buff=0.1,aligned_edge=fx_label.get_bottom())


		fy = lambda y: y.get_value()/10
		# ValueTrackers definition
		y_value = ValueTracker(-4)
		fy_value = ValueTracker(fy(y_value))
		# DecimalNumber definition
		y_tex = DecimalNumber(y_value.get_value()).add_updater(lambda v: v.set_value(y_value.get_value()))
		fy_tex = DecimalNumber(fy_value.get_value()).add_updater(lambda v: v.set_value(fy(y_value)))
		# Tey labels definition
		y_label = TexMobject("y = ")
		fy_label = TexMobject("Q = ")
		# Grouping of labels and numbers
		group_2 = VGroup(y_tex,fy_tex,y_label,fy_label).scale(0.8)
		VGroup(y_tex, fy_tex).arrange_submobjects(DOWN,buff=0.3)
		# Align labels and numbers
		y_label.next_to(y_tex,LEFT, buff=0.1,aligned_edge=y_label.get_bottom())
		fy_label.next_to(fy_tex,LEFT, buff=0.1,aligned_edge=fy_label.get_bottom())


		self.play(ShowCreation(field_text))
		self.wait()
		self.play(ShowCreation(vector_field), ReplacementTransform(field_text, field_text_2))
		self.wait()
		self.play(ShowCreation(p), ShowCreation(q), FadeOut(vector_field))
		self.wait()
		self.play(ShowCreation(dpq[0]), ShowCreation(x_comps))
		self.play(Indicate(dpq[0]))
		self.wait()
		self.play(ShowCreation(dp_text))
		self.wait()
		self.play(Uncreate(dp_text))

		self.add(group.move_to(5*RIGHT+3*DOWN))
		self.play(Write(line1),
			x_value.set_value,4,
			rate_func=linear,
			run_time=3
			)
		self.wait(2)
		self.play(FadeOut(group), FadeOut(line1), ApplyFunction(lambda a:a.fade(), x_comps))

		self.play(ShowCreation(dpq[1]), ShowCreation(y_comps))
		self.play(Indicate(dpq[1]))
		self.wait(2)
		self.play(ShowCreation(dq_text))
		self.wait()
		self.play(Uncreate(dq_text))

		self.add(group_2.move_to(5*RIGHT+3*DOWN))
		self.play(Write(line2),
			y_value.set_value,4,
			rate_func=linear,
			run_time=3
			)
		self.wait(2)
		self.play(ReplacementTransform(dpq, dp_dq), FadeOut(line2), ReplacementTransform(x_comps, vector_field), ReplacementTransform(y_comps, vector_field), FadeOut(group_2))

		self.play(Indicate(dp_dq))
		self.wait()

