from manimlib.imports import *

t_offset = 0
c_t = 0

class cycloid(Scene):
    def construct(self):

        cycl = ParametricFunction(
        lambda t: np.array([
        t - np.sin(t),
        1 - np.cos(t),
        0
        ]), t_min = -2.75*np.pi, t_max = 3*np.pi, color = BLUE
        ).shift(0.73*RIGHT)
        wheel_radius = 1
        wheel_function_path = lambda x : 0 + wheel_radius

        line = FunctionGraph(lambda x : 0, color = BLACK)
        wheel_path = FunctionGraph(wheel_function_path)

        velocity_factor = 0.25
        frame_rate = self.camera.frame_rate
        self.dt = 1 / frame_rate

        wheel = Circle(color = BLACK, radius = 1)
        dot = Dot(radius = 0.16, color = RED)
        #dot.move_to(wheel.get_arc_center() + np.array([0,2,0]))

        def update_dot(mob,dt):
            global t_offset,c_t
            if dt == 0 and c_t == 0:
                rate= - velocity_factor * self.dt
                c_t += 1
            else:
                rate = - dt*velocity_factor
            if dt > 0:
                c_t = 0
            mob.move_to(wheel.point_from_proportion(((t_offset + rate))%1))
            t_offset += rate
            #self.add(mob.copy())

        #dot.move_to(wheel.get_arc_center() + np.array([0,2,0]))
        dot.add_updater(update_dot)
        self.add(wheel,dot, line, cycl)
        self.play(MoveAlongPath(wheel, wheel_path, run_time = 9, rate_func = linear))
