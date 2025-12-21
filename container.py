from manim import *

class ContainerLayout:
    def setup_containers(self):
        UPPER_FRACTION, LOWER_FRACTION = 4/5, 1/5
        total_width, total_height = config.frame_width, config.frame_height
        upper_height, lower_height = total_height * UPPER_FRACTION, total_height * LOWER_FRACTION
        upper_box_width = total_width / 2 - 0.1
        
        self.PADDING_FACTOR = 0.95
        self.NUMBER_FRACTION, self.TEXT_FRACTION = 1/8, 7/8
        BOTTOM_GAP = 0.1
        
        bottom_y_center = DOWN * (total_height * (0.5 - LOWER_FRACTION/2))
        upper_y_center = UP * (total_height * (0.5 - UPPER_FRACTION/2))

        self.left_box = Rectangle(
            width=upper_box_width, height=upper_height - 0.1,   
            color=BLUE_A, stroke_color=BLUE_D, fill_opacity=0.05
        ).move_to(upper_y_center + LEFT * total_width / 4)
        
        self.right_box = Rectangle(
            width=upper_box_width, height=upper_height - 0.1,
            color=RED_A, stroke_color=RED_D, fill_opacity=0.05
        ).move_to(upper_y_center + RIGHT * total_width / 4)

        left_edge, right_edge = self.left_box.get_left()[0], self.right_box.get_right()[0]
        avail_width = right_edge - left_edge - BOTTOM_GAP
        
        self.bottom_left_box = Rectangle(
            width=avail_width * self.NUMBER_FRACTION, height=lower_height - 0.1, 
            color=GREEN_A, stroke_color=GREEN_D, fill_opacity=0.1
        ).move_to([left_edge + (avail_width * self.NUMBER_FRACTION / 2), bottom_y_center[1], 0])
        
        self.bottom_right_box = Rectangle(
            width=avail_width * self.TEXT_FRACTION, height=lower_height - 0.1, 
            color=GREEN_A, stroke_color=GREEN_D, fill_opacity=0.05
        ).move_to([right_edge - (avail_width * self.TEXT_FRACTION / 2), bottom_y_center[1], 0])

        self.max_upper_width = self.left_box.width * self.PADDING_FACTOR
        self.max_upper_height = self.left_box.height * self.PADDING_FACTOR
