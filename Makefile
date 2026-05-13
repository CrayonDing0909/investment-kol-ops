.PHONY: dashboard open-dashboard help

help:
	@echo "Targets:"
	@echo "  make dashboard       - rebuild ops/dashboard.html + ops/current.md from data"
	@echo "  make open-dashboard  - rebuild and open the dashboard in your default browser"

dashboard:
	@python3 ops/build_dashboard.py

open-dashboard: dashboard
	@open ops/dashboard.html
