from manimlib.imports import *

class SigmoidFunc(GraphScene):
    CONFIG = {
    "x_min": -4,
    "x_max": 4,
    "y_min": -1,
    "y_max": 1,
    "graph_origin": ORIGIN + 0.8*DOWN,
    "x_labeled_nums": list(range(-4, 5)),
    "y_labeled_nums": list(range(-1, 2)),
    "y_axis_height": 4.5,
    }
    def construct(self):
        XTD = self.x_axis_width/(self.x_max- self.x_min)
        YTD = self.y_axis_height/(self.y_max- self.y_min)

        topic = TextMobject("Sigmoid Function")
        topic.move_to(3.2*UP)
        topic.set_color_by_gradient(RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE)

        self.setup_axes(animate = True)
        sigmoid_func = self.get_graph(lambda x : (1/(1 + np.exp(-x))), x_min = -4, x_max = 4)
        sigmoid_lab = self.get_graph_label(sigmoid_func, label = r"\frac{1}{1 + e^{-z}}")

        


        self.play(ShowCreation(sigmoid_func),Write(sigmoid_lab))
        self.play(Write(topic))
        self.wait(2)
        self.play(FadeOut(sigmoid_func), FadeOut(sigmoid_lab))
        self.wait(1)
        


class NeuralNet(GraphScene):
    def construct(self):

        sigmoid_exp = TextMobject(r"g(z) = g($\theta^T$ X) = $\frac{1}{1 + e^{-z}}$")
        sigmoid_exp.move_to(3*UP + 4*LEFT)
        sigmoid_exp.scale(0.8)
        sigmoid_exp.set_color(BLUE)
        sigmoid_exp1 = TextMobject(r"Predict: 'y = 1'",r"When g(z) $\geq$ 0.5, z $\geq$ 0, $\theta^T$ X  $\geq$ 0")
        sigmoid_exp2 = TextMobject(r"Predict: 'y = 0'", r"When g(z) $\leq$ 0.5, z $\leq$ 0, $\theta^T$ X  $\leq$ 0")
        sigmoid_exp1.scale(0.5)
        sigmoid_exp2.scale(0.5)
        sigmoid_exp1.set_color(PURPLE)
        sigmoid_exp2.set_color(PURPLE)

        sigmoid_exp1[0].next_to(sigmoid_exp, 1.5*DOWN)
        sigmoid_exp1[1].next_to(sigmoid_exp1[0], DOWN)
        sigmoid_exp2[0].next_to(sigmoid_exp1[1], 1.5*DOWN)
        sigmoid_exp2[1].next_to(sigmoid_exp2[0], DOWN)


        self.play(Write(sigmoid_exp))
        self.play(Write(sigmoid_exp1[0]), Write(sigmoid_exp1[1]))
        self.play(Write(sigmoid_exp2[0]), Write(sigmoid_exp2[1]))
        self.wait(2)


        neuron1 = Circle()
        neuron1.set_fill(YELLOW_A, opacity = 0.5)

        neuron2 = Circle()
        neuron2.set_fill(ORANGE, opacity = 0.5)

        neuron3 = Circle()
        neuron3.set_fill(GREEN_E, opacity = 0.5)

        neuron1.move_to(2*UP+RIGHT)
        neuron2.move_to(2*DOWN+RIGHT)
        neuron3.move_to(4*RIGHT)

        arrow1 = Arrow(neuron1.get_right(),neuron3.get_left(),buff=0.1)
        arrow1.set_color(RED)
        arrow2 = Arrow(neuron2.get_right(),neuron3.get_left(),buff=0.1)
        arrow2.set_color(RED)

        arrow3 = Arrow(neuron3.get_right(),7*RIGHT,buff=0.1)
        arrow3.set_color(RED)


        sign1 = TextMobject("+1")
        sign1.move_to(2*UP+RIGHT)
        sign1.scale(2)
        sign2 = TextMobject(r"$x_1$")
        sign2.move_to(2*DOWN+RIGHT)
        sign2.scale(2)
        sign3 = TextMobject(r"$h_{\theta}(x)$")
        sign3.move_to(6*RIGHT+0.4*DOWN)
        sign3.scale(0.7)
        sign4 = TextMobject(r"$= g(10 - 20x_1)$")
        sign4.next_to(sign3,DOWN)
        sign4.scale(0.5)
        sign5 = TextMobject(r"$= g(10 - 20x_1)$")
        sign5.next_to(sign3,DOWN)
        sign5.scale(0.5)
        sign6 = TextMobject(r"$= g(10 - 20x_1)$")
        sign6.next_to(sign3,DOWN)
        sign6.scale(0.5) 


        weight1 = TextMobject("10")
        weight1.next_to(arrow1,UP)
        weight2 = TextMobject("-20")
        weight2.next_to(arrow2,DOWN)

        gate = TextMobject("NOT GATE")
        gate.set_color_by_gradient(RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE)
        gate.scale(1.5)
        gate.move_to(3*RIGHT+3.5*UP)



        truth_table = TextMobject(r"\begin{displaymath}\begin{array}{|c|c|} x & y\\ \hline 1 & 0 \\0 & 1 \\\end{array}\end{displaymath}")
        truth_table.next_to(sigmoid_exp2[1], 3*DOWN)

        values = TextMobject("1", "0")
        values.scale(2)

        sign4_trans1 = TextMobject(r"$= g(10 - 20(1))$")
        sign4_trans2 = TextMobject(r"$= g(10 - 20(0))$")
        sign4_trans1.next_to(sign3,DOWN)
        sign4_trans2.next_to(sign3,DOWN)
        sign4_trans1.scale(0.5)
        sign4_trans2.scale(0.5)



        output1 = TextMobject("y = 0")
        output2 = TextMobject("y = 1")
        output1.next_to(sign4,DOWN)
        output2.next_to(sign4,DOWN)
        output1.scale(1.5)
        output2.scale(1.5)



        self.play(ShowCreation(neuron1),ShowCreation(neuron2))
        self.play(ShowCreation(neuron3))
        self.play(ShowCreation(sign1),ShowCreation(sign2))
        self.wait(1)

        self.play(GrowArrow(arrow1))
        self.play(GrowArrow(arrow2))
        self.play(ShowCreation(weight1),ShowCreation(weight2))


        
        self.play(GrowArrow(arrow3))
        self.play(Write(sign3),Write(sign4))

        self.play(Write(gate))
        self.play(ShowCreation(truth_table))

        self.play(ApplyMethod(values[0].move_to, 2*DOWN+RIGHT))
        self.play(FadeOut(values[0]))
        self.play(Transform(sign4,sign4_trans1))
        self.play(Write(output1))
        self.wait(1)
        self.play(FadeOut(output1))
        self.play(Transform(sign4, sign5))
        

        self.play(ApplyMethod(values[1].move_to, 2*DOWN+RIGHT))
        self.play(FadeOut(values[1]))
        self.play(Transform(sign4,sign4_trans2))
        self.play(Write(output2))
        self.wait(1)
        self.play(FadeOut(output2))
        self.play(Transform(sign4, sign6))
        
        self.wait(2)


