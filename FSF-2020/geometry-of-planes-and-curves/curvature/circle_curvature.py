from manimlib.imports import *

class circleC(GraphScene):
    CONFIG = {
    "x_min": -6,
    "x_max": 6,
    "y_min": -6,
    "y_max": 6,
    "graph_origin": ORIGIN,
    "x_axis_width": 12,
    "y_axis_height": 12
    }
    def construct(self):
        eqn = TextMobject(r'$r(t) = <a\cos{t}, a\sin{t}, 0>$').shift(0.5*UP)
        mid = TextMobject(r'Parametric equation of a circle in the XY plane.').shift(0.2*DOWN)
        prime1 = TextMobject(r'$r\prime(t) = <-a\sin{t}, a\cos{t}, 0>$').shift(0.8*UP)
        prime2 = TextMobject(r'$r\prime\prime(t) = <-a\cos{t}, -a\sin{t}, 0>$')
        crossproduct = TextMobject(r'$r\prime(t) \times r \prime \prime (t) = \begin{bmatrix}\widehat{i} & \widehat{j} & \widehat{k} \\-a\sin{t} & a\cos{t} & 0 \\-a\cos{t} & -a\sin{t} & 0\end{bmatrix}$ \\ $\quad$ \\$\qquad = a^{2}(cos^{2}t + sin^{2}t) = a^{2}$')
        curvature_formula = TextMobject(r'$k(t) = \frac{\left|\left|r\prime(t)\times r\prime\prime(t)\right|\right|}{\left|\left|r\prime(t)\right|\right|^{3}}$').shift(DOWN)
        curvature_result = TextMobject(r'$k(t) = \frac{\left|\left|r\prime(t)\times r\prime\prime(t)\right|\right|}{\left|\left|r\prime(t)\right|\right|^{3}} = \frac{a^{2}}{a^{3}} = \frac{1}{a}$')
        epiphany = TextMobject(r'What does this mean graphically?')
        epiphany2 = TextMobject(r'Driving a vehicle on which of the two paths would be easier?\\The larger path, due to its smaller curvature.')
        outro = TextMobject(r'$k = \frac{1}{a}\equiv$ larger the radius of the circle, lesser its curvature.')
        XTD = self.x_axis_width/(self.x_max- self.x_min)
        YTD = self.y_axis_height/(self.y_max- self.y_min)
        
        circle = Circle(radius = 2, color = BLUE)
        circle2 = Circle(radius = 3, color = GREEN_E)

        self.setup_axes(hideaxes=True)
        self.play(FadeIn(eqn), FadeIn(mid))
        self.wait(2)
        self.play(FadeOut(eqn), FadeOut(mid), FadeIn(self.axes), FadeIn(circle))
        self.wait(2)
        self.play(FadeOut(circle), FadeOut(self.axes))
        self.play(FadeIn(prime1), FadeIn(prime2),FadeIn(curvature_formula))
        self.wait(2)
        self.play(FadeOut(curvature_formula), FadeOut(prime1), FadeOut(prime2), FadeIn(crossproduct))
        self.wait(3)
        self.play(FadeOut(crossproduct), FadeIn(curvature_result))
        self.wait(2)
        self.play(FadeOut(curvature_result), FadeIn(epiphany))
        self.wait(3)
        self.play(FadeOut(epiphany), FadeIn(self.axes), FadeIn(circle), FadeIn(circle2))
        self.wait(2)
        self.play(FadeOut(self.axes), FadeOut(circle), FadeOut(circle2), FadeIn(epiphany2))
        self.wait(2)
        self.play(FadeOut(epiphany2), FadeIn(outro))
        self.wait(2)
        self.play(FadeOut(outro))