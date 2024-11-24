build:
	manim-slides render presentation.py
	manim-slides convert OptimizationFinal	\
		slides_output/index.html
