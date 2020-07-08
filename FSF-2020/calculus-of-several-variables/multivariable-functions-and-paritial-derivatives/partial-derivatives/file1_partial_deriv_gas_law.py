from manimlib.imports import *

class GasLaw(Scene):
    def construct(self):
        gas_law = TextMobject(r"$P$", r"$V$", r"=", r"$n$", r"$R$", r"$T$").scale(1.5)
        gas_law[0].set_color(BLUE_C)
        gas_law[1].set_color(GREEN_C)
        gas_law[3].set_color(RED_C)
        gas_law[4].set_color(ORANGE)
        gas_law[5].set_color(YELLOW_C)

        gas_law_trans = TexMobject("V", "=", "{n", "R", "T", "\\over", "P}").scale(1.5)
        gas_law_trans[0].set_color(GREEN_C)
        gas_law_trans[2].set_color(RED_C)
        gas_law_trans[3].set_color(ORANGE)
        gas_law_trans[4].set_color(YELLOW_C)
        gas_law_trans[6].set_color(BLUE_C)

        gas_law_func = TexMobject("V", "=", "f(", "n", ",", "T", ",", "P", ")").scale(1.5)
        gas_law_func[0].set_color(GREEN_C)
        gas_law_func[2].set_color(ORANGE)
        gas_law_func[3].set_color(RED_C)
        gas_law_func[5].set_color(YELLOW_C)
        gas_law_func[7].set_color(BLUE_C)
        gas_law_func[8].set_color(ORANGE)

        partial_gas_law_func = TexMobject("{\\partial", "V","\\over", "\\partial", "P}", r"=", "{\\partial", "\\over", "\\partial", "P}", "f(", r"n", ",", r"T", ",", r"P", r")").scale(1.5)
        partial_gas_law_func.set_color_by_tex("\\partial", PINK)
        partial_gas_law_func.set_color_by_tex("P}", BLUE_C)

        partial_gas_law_func[1].set_color(GREEN_C)
        partial_gas_law_func[10].set_color(ORANGE)
        partial_gas_law_func[11].set_color(RED_C)
        partial_gas_law_func[13].set_color(YELLOW_C)
        partial_gas_law_func[15].set_color(BLUE_C)
        partial_gas_law_func[16].set_color(ORANGE)

        partial_gas_law_trans = TexMobject("{\\partial", "V","\\over", "\\partial", "P}", r"=", "{\\partial", "\\over", "\\partial", "P}", "{n", "R", "T", "\\over", "P}").scale(1.5)
        partial_gas_law_trans.set_color_by_tex("\\partial", PINK)
        partial_gas_law_trans.set_color_by_tex("P}", BLUE_C)

        partial_gas_law_trans[1].set_color(GREEN_C)
        partial_gas_law_trans[10].set_color(RED_C)
        partial_gas_law_trans[11].set_color(ORANGE)
        partial_gas_law_trans[12].set_color(YELLOW_C)

        partial_gas_law_trans2 = TexMobject("{\\partial", "V","\\over", "\\partial", "P}", r"=", "n", "R", "T", "{\\partial", "\\over", "\\partial", "P}", "P^{-1}",).scale(1.5)
        partial_gas_law_trans2.set_color_by_tex("\\partial", PINK)
        partial_gas_law_trans2.set_color_by_tex("P}", BLUE_C)

        partial_gas_law_trans2[1].set_color(GREEN_C)
        partial_gas_law_trans2[6].set_color(RED_C)
        partial_gas_law_trans2[7].set_color(ORANGE)
        partial_gas_law_trans2[8].set_color(YELLOW_C)
        partial_gas_law_trans2[-1].set_color(BLUE_C)

        partial_gas_law_trans3 = TexMobject("{\\partial", "V","\\over", "\\partial", "P}", r"=", "n", "R", "T", "P^{-2}",).scale(1.5)
        partial_gas_law_trans3.set_color_by_tex("\\partial", PINK)
        partial_gas_law_trans3.set_color_by_tex("P}", BLUE_C)

        partial_gas_law_trans3[1].set_color(GREEN_C)
        partial_gas_law_trans3[6].set_color(RED_C)
        partial_gas_law_trans3[7].set_color(ORANGE)
        partial_gas_law_trans3[8].set_color(YELLOW_C)
        partial_gas_law_trans3[9].set_color(BLUE_C)

        framebox = SurroundingRectangle(partial_gas_law_trans3, color = PURPLE, buff = 0.3)



        self.play(Write(gas_law))
        self.wait()
        self.play(Transform(gas_law, gas_law_trans))
        self.wait()
        self.play(Transform(gas_law, gas_law_func))
        self.wait()
        self.play(Transform(gas_law, gas_law_trans))
        self.wait()
        self.play(Transform(gas_law, partial_gas_law_func))
        self.wait()
        self.play(Transform(gas_law, partial_gas_law_trans))
        self.wait()
        self.play(Transform(gas_law, partial_gas_law_trans2))
        self.wait()
        self.play(Transform(gas_law, partial_gas_law_trans3))
        self.wait()
        self.play(ShowCreation(framebox))
        self.wait()