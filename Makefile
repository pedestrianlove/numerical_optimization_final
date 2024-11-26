build:
	manim-slides render -ql presentation.py
	manim-slides convert OptimizationFinal	\
		--to HTML							\
		-ccontrols=true						\
		slides_output/index.html

dev:
	@go run github.com/air-verse/air@latest
