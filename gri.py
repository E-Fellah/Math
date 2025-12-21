from manim import *

class GridSystem:
    def create_coordinate_grid(self, container, spacing=0.5):
        grid = VGroup()
        width, height = container.width * 0.95, container.height * 0.95
        center = container.get_center()
        num_x, num_y = int(width / spacing), int(height / spacing)
        
        for i in range(-num_x//2, num_x//2 + 1):
            grid.add(Line(center + UP*height/2 + RIGHT*i*spacing, center + DOWN*height/2 + RIGHT*i*spacing, 
                         color=GRAY_D, stroke_width=0.8, stroke_opacity=0.15))
        for i in range(-num_y//2, num_y//2 + 1):
            grid.add(Line(center + LEFT*width/2 + UP*i*spacing, center + RIGHT*width/2 + UP*i*spacing, 
                         color=GRAY_D, stroke_width=0.8, stroke_opacity=0.15))
        
        for i in range(-num_x//2, num_x//2 + 1):
            for j in range(-num_y//2, num_y//2 + 1):
                grid.add(Dot(point=center + RIGHT*i*spacing + UP*j*spacing, radius=0.02, color=BLUE_E, fill_opacity=0.4))
        
        grid.add(Line(center + LEFT*width/2, center + RIGHT*width/2, color=RED_D, stroke_width=1.5, stroke_opacity=0.3))
        grid.add(Line(center + DOWN*height/2, center + UP*height/2, color=RED_D, stroke_width=1.5, stroke_opacity=0.3))
        return grid

    def extract_grid_points(self, container, spacing):
        width, height = container.width * 0.95, container.height * 0.95
        center, num_x, num_y = container.get_center(), int(width/spacing), int(height/spacing)
        return [{'coords': (i, j), 'position': center + RIGHT*i*spacing + UP*j*spacing} 
                for i in range(-num_x//2, num_x//2+1) for j in range(-num_y//2, num_y//2+1)]
