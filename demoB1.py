from manim import *

class CaroGridWithLines(Scene):
    def construct(self):
        grid_size = 5
        square_size = 1
        grid_half_size = grid_size * square_size / 2

        vertical_lines = []
        horizontal_lines = []

        # Create vertical lines
        for i in range(grid_size + 1):
            line = Line(
                start=np.array(
                    [-grid_half_size + i * square_size, -grid_half_size, 0]),
                end=np.array(
                    [-grid_half_size + i * square_size, grid_half_size, 0]),
                color=WHITE
            )
            vertical_lines.append(line)

        # Create horizontal lines
        for j in range(grid_size + 1):
            line = Line(
                start=np.array(
                    [-grid_half_size, -grid_half_size + j * square_size, 0]),
                end=np.array(
                    [grid_half_size, -grid_half_size + j * square_size, 0]),
                color=WHITE
            )
            horizontal_lines.append(line)

        # Animate all lines simultaneously
        self.play(
            AnimationGroup(
                *[Create(line) for line in vertical_lines + horizontal_lines],
                lag_ratio=0.1
            )
        )

        # Create a paragraph
        paragraph = Paragraph(
            'This is an awesome', 'paragraph',
            'With \nNewlines', '\tWith Tabs',
            '  With Spaces', 'With Alignments',
            'center', 'left', 'right',
            alignment="center"
        ).scale(0.5)

        # Move the paragraph to a suitable position
        paragraph.move_to(3 * UP)

        # Add the paragraph to the scene
        self.add(paragraph)

        # Optionally animate something if needed (this is just an example)
        self.play(Create(paragraph))

        self.wait()
