import numpy as np
from manim import *

class GridRules:
    def anchor_to_grid(self, mobject, container, coords, edge=ORIGIN):
        grid_x, grid_y = coords
        # Use the container's center as the local origin (0,0)
        center = container.get_center()
        
        # Calculate absolute position based on grid spacing
        target_pos = center + np.array([
            grid_x * self.grid_spacing, 
            grid_y * self.grid_spacing, 
            0
        ])
        
        mobject.move_to(target_pos, aligned_edge=edge)
        
        # Only enforce boundaries for content that isn't the primary axis/grid
        if container == self.right_box:
            self.enforce_boundaries(mobject, container)
        return mobject

    def enforce_boundaries(self, mobject, container):
        # Allow a 0.2 cushion so shapes don't touch the box edges
        margin = 0.2
        buff = 0.1
        
        left_limit = container.get_left()[0] + buff
        right_limit = container.get_right()[0] - buff
        top_limit = container.get_top()[1] - buff
        bottom_limit = container.get_bottom()[1] + buff

        if mobject.get_left()[0] < left_limit: mobject.shift(RIGHT * (left_limit - mobject.get_left()[0]))
        if mobject.get_right()[0] > right_limit: mobject.shift(LEFT * (mobject.get_right()[0] - right_limit))
        if mobject.get_top()[1] > top_limit: mobject.shift(DOWN * (mobject.get_top()[1] - top_limit))
        if mobject.get_bottom()[1] < bottom_limit: mobject.shift(UP * (bottom_limit - mobject.get_bottom()[1]))
        
        return mobject

    def snap_shape_to_grid(self, mobject, container, coords):
        # We don't scale automatically here to avoid 'fucking up' your graphs
        # We just move it to the coordinate.
        return self.anchor_to_grid(mobject, container, coords, edge=ORIGIN)

    def setup_graph_in_container(self, container, x_range=[-4, 4], y_range=[-3, 3]):
        # This aligns the Axes perfectly with your grid dots
        x_units = x_range[1] - x_range[0]
        y_units = y_range[1] - y_range[0]
        
        axes = Axes(
            x_range=x_range,
            y_range=y_range,
            x_length=x_units * self.grid_spacing,
            y_length=y_units * self.grid_spacing,
            axis_config={"color": BLACK, "stroke_width": 2, "include_numbers": False},
            tips=False
        )
        axes.move_to(container.get_center())
        return axes
