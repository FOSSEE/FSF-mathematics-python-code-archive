from manimlib.imports import *

class Left_Null_Space(Scene):
    def construct(self):

        A = TextMobject(r"Left Null Space of A")
        A.move_to(3*UP)
        defn = TextMobject(r"It is a vector space that consists of all the solution $x$ to the equation $A^{T}x=0$")
        defn.move_to(2*UP)
        defn.scale(0.75)
        eqn1 = TextMobject(r"$A^{T}x=0 \cdots (i)$")
        eqn1.move_to(UP)
        self.play(Write(A), Write(defn), Write(eqn1),run_time=1)
        statement = TextMobject(r"Taking transpose of eqn $(i)$")
        eqn = TextMobject(r"$(A^{T}x)^{T}=0$")
        eqn.move_to(DOWN)
        eqn2 = TextMobject(r"$x^{T}(A^{T})^{T}=0$")
        eqn2.move_to(DOWN)
        eqn3 = TextMobject(r"$x^{T}A=0$")
        eqn3.move_to(DOWN)
        self.play(Write(statement),Write(eqn),run_time=1)
        self.wait(0.5)
        self.play(Transform(eqn,eqn2),run_time=1)
        self.wait(0.5)
        self.play(Transform(eqn,eqn3),run_time=1)
        self.wait(0.5)