build:
	manim-slides render presentation.py
	manim-slides convert OptimizationFinal	\
		--to HTML							\
		-ccontrols=true						\
		slides_output/index.html
