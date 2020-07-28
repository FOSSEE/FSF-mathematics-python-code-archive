from manimlib.imports import *
def GetCenters(width,center,n):
	d = width / 4
	list = [center + [0,d,0]]
	if n > 1:
		list.append(center + [-d,-d,0])
	if n > 2:
		list.extend(GetCenters(width / 2, center + [d,-d,0],n-2))
	return list
END_CENTERS = [ORIGIN]
END_CENTERS.extend(GetCenters(3, 3 * RIGHT, 24))
color_list = ['#00931F','#A93226','#D68910','#17A589','#2471A3','#884EA0','#E74C3C','#D4AC0D']
COLORS = [color_list[i % len(color_list)] for i in range(50)]
class RectangleFromSequence(Rectangle):
	CONFIG = {
		"sequence_number": 0,
		"center": ORIGIN
	}
	def __init__(self, **kwargs):
		digest_config(self, kwargs)
		Rectangle.__init__(self,height = 3 * (1/2) ** ((self.sequence_number + 1) // 2),width = 3 * (1/2) ** ((self.sequence_number) // 2),**kwargs)
		if self.sequence_number < 6:
			if self.sequence_number == 0:
				label = TexMobject("1")
			else:
				label = TexMobject("1/",str(2 ** self.sequence_number))
			label.scale(0.8 ** self.sequence_number)
			self.add(label)
			self.label = label
		self.set_fill(COLORS[self.sequence_number],1)
		self.set_stroke(width = 1)
		self.move_to(self.center)
equation = TexMobject("\\sum_{n=0}^\\infty \\frac{1}{2^n} =","1","+","\\frac{1}{2}","+","\\frac{1}{4}","+","\\frac{1}{8}","+","\\frac{1}{16}","+ \\ldots","= 2")
class Proof1(Scene):
	def construct(self):
		equation.to_edge(UL)
		self.play(Write(equation[0:-1]))	
		rects = VGroup(*[RectangleFromSequence(sequence_number = i)for i in range(25)])
		rects.arrange(RIGHT, buff=0.5)
		left_center = 5*LEFT
		rects.shift(left_center-rects[0].get_center())
		for rect in rects:
			rect.shift(DOWN*rect.get_top()+UP*3 / 2)
		for i in range(25):
			rects[i].generate_target()
			rects[i].target.move_to(left_center+END_CENTERS[i])
		self.wait()
		for i in range(5):
			self.play(GrowFromPoint(rects[i] , equation[2*i+1].get_center()))
		self.play(*[GrowFromPoint(rects[i] , equation[-2].get_center())for i in range(5,25)])
		self.wait()
		for i in range(1,8):
			self.play(MoveToTarget(rects[i]))
		self.play(*[MoveToTarget(rects[i]) for i in range(8,25)])
		self.wait(0.5)
		self.play(Write(equation[-1]))
		self.wait(3)