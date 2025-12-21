from manim import *
from container import ContainerLayout
from grid import GridSystem
from grid_rules import GridRules

# Import examples
from examples.example1_arithmetic import get_arithmetic_chapter
from examples.example2_fractions import get_fractions_chapter
from examples.example3_decimals import get_decimals_chapter

config.background_color, config.stroke_color, config.fill_color = WHITE, BLACK, BLACK

class EngineeringMathWithGrids(Scene, ContainerLayout, GridSystem, GridRules):
    def construct(self):
        # 1. Setup
        self.setup_containers()
        self.grid_spacing = 0.5
        self.commentary_font_size = 24
        self.title_font_size = 20 
        self.math_scale_factor = 0.5 
        self.numbering_font_size = 36
        
        # 2. Intro
        intro_title = Tex(r"\textbf{Basic Engineering Mathematics}", font_size=64, color=BLACK)
        self.play(Write(intro_title))
        self.wait(1.5)
        self.play(
            FadeOut(intro_title), 
            *[Create(b) for b in [self.left_box, self.right_box, self.bottom_left_box, self.bottom_right_box]]
        )

        # 3. Grids
        self.left_grid = self.create_coordinate_grid(self.left_box, self.grid_spacing)
        self.right_grid = self.create_coordinate_grid(self.right_box, self.grid_spacing)
        self.left_grid_points = self.extract_grid_points(self.left_box, self.grid_spacing)
        self.right_grid_points = self.extract_grid_points(self.right_box, self.grid_spacing)
        self.play(FadeIn(self.left_grid, run_time=0.5), FadeIn(self.right_grid, run_time=0.5))

        # 4. Chapters Loop
        chapters_data = [
            get_arithmetic_chapter(), 
            get_fractions_chapter(),
            get_decimals_chapter()
        ]
        
        for i, data in enumerate(chapters_data, 1):
            self.run_chapter(i, len(chapters_data), data)

        self.play(*[FadeOut(m) for m in self.mobjects])

    def run_chapter(self, i, total, data):
        # Title
        chap_title = Text(data["title"], font_size=self.title_font_size, color=BLACK, weight=BOLD)
        self.anchor_to_grid(chap_title, self.left_box, (-6, 5), edge=DL)

        # Math Lines (Left)
        base_font_size = data.get("math_font_size", 40)
        left_mobs = data["left_mobs"]
        start_x, start_y = -6, 4
        
        for index, mob in enumerate(left_mobs):
            mob.set_font_size(base_font_size).scale(self.math_scale_factor)
            self.anchor_to_grid(mob, self.left_box, (start_x, start_y - index), edge=LEFT)

        # Right Box Content (Shapes or Graphs)
        right_mobs = []
        if data.get("is_graph"):
            ax = self.setup_graph_in_container(self.right_box)
            conf = data["graph_config"]
            curve = ax.plot(conf["func"], x_range=conf["x_range"], color=conf["color"])
            right_mobs.extend([ax, curve])
        elif "right_shapes" in data:
            for shape_info in data["right_shapes"]:
                shape = shape_info["obj"]
                coords = shape_info["coords"]
                self.snap_shape_to_grid(shape, self.right_box, coords)
                right_mobs.append(shape)

        # UI
        num_mob = Text(f"{i}/{total}", font_size=self.numbering_font_size, color=BLACK).move_to(self.bottom_left_box)
        expl = VGroup(*[Text(l, color=BLACK, font_size=self.commentary_font_size) for l in data["bottom_text"].split('\n')[:2]])
        expl.arrange(DOWN, aligned_edge=LEFT).move_to(self.bottom_right_box).align_to(self.bottom_right_box.get_left(), LEFT).shift(RIGHT * 0.2)

        # 1. Show UI and Title
        self.play(FadeIn(chap_title), Write(num_mob), FadeIn(expl))
        
        # 2. Show Right Content
        if data.get("is_graph"):
            self.play(Create(right_mobs[0])) # Create Axes
            self.play(Create(right_mobs[1]), run_time=1.5) # Plot Curve
        elif right_mobs:
            self.play(AnimationGroup(*[Create(s) for s in right_mobs], lag_ratio=0.2))

        # 3. UNROLL Math Lines
        for mob in left_mobs:
            self.play(Write(mob), run_time=0.6)
            
        self.wait(2.5)
        self.play(*[FadeOut(m) for m in [chap_title, *left_mobs, *right_mobs, num_mob, expl]])
