from manimlib.imports import *


def funk(x,y):
	x,y = coordinate[:2]
	return np.array([
			np.sin(x)**np.cos(y),
			np.sin(y)**np.cos(x),
			0
	])

class Fluid(Scene):
    def construct(self):
        vf = VectorField(funk).fade(0.5)
        self.add(vf)
        self.wait()
        lines = StreamLines(
            funk,
            virtual_time=3,
            min_magnitude=0,
            max_magnitude=2,
        )
        self.add(AnimatedStreamLines(
            lines,
            line_anim_class=ShowPassingFlashWithThinningStrokeWidth
        ))
        self.wait(3)
