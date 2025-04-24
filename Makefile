.PHONY: setup clean test lint type-check format refactor
# Variables
PYTHON := python3
VENV := .venv
SRC_DIR := src
TEST_DIR := tests
help:
	@echo "\033[0;36m"
	@echo '  _____                     _          _  ___   ___  '
	@echo ' |__  /___  ___ _ __ ___   | |_ ___   / |/ _ \ / _ \ '
	@echo '   / // _ \/ _ \ __ / _ \  | __/ _ \  | | | | | | | |'
	@echo '  / /|  __/  __/ | | (_) | | || (_) | | | |_| | |_| |'
	@echo ' /____\___|\___|_|  \___/   \__\___/  |_|\___/ \___/ '
	@echo "\033[0m"
	@echo ""
	@echo "\033[1;32m▶ LOCAL COMMANDS:\033[0m"
	@echo "  make setup         - Create virtual environment and install dependencies"
	@echo "  make clean         - Remove virtual environment and cache files"
	@echo " "
	@echo "  make format        - Run format code"
	@echo "  make lint          - Run linter"
	@echo "  make type-check    - Run type checking"
	@echo "  make test          - Run all tests"
	@echo "  make refactor      - Run all checks"
setup: clean
	$(PYTHON) -m pip install --upgrade uv
clean:
	rm -rf $(VENV)
	rm -rf .pytest_cache
	rm -rf .coverage
	rm -rf .mypy_cache
	rm -rf **/__pycache__
test:
	uv run pytest $(TEST_DIR) -vv
lint:
	uv run ruff check $(SRC_DIR) --fix
type-check:
	uv run mypy $(SRC_DIR)
format:
	uv run ruff format $(SRC_DIR) $(TEST_DIR)
refactor: format lint type-check test
