# Define variables for directories
BACKEND_DIR = backend
FRONTEND_DIR = frontend

# Define targets
.PHONY: all backend frontend install-backend install-frontend

all: backend frontend

test_backend:
	@echo "Starting port-forwarding for PostgreSQL..."
	@oc port-forward svc/postgresql 5433:5432 -n dept-coildb &
	@PORT_FORWARD_PID=$!  # Capture the process ID of the port-forward command
	@sleep 3
	@cd $(BACKEND_DIR) && source venv/bin/activate && pytest --cov=. --cov-report=term-missing tests/
	@kill $$PORT_FORWARD_PID  # Terminate the port-forward process after main.py exits

# Run the Python backend
backend:
	@echo "Starting port-forwarding for PostgreSQL..."
	@oc port-forward svc/postgresql 5433:5432 -n dept-coildb &
	@PORT_FORWARD_PID=$!  # Capture the process ID of the port-forward command
	@sleep 3
	@cd $(BACKEND_DIR) && source venv/bin/activate && python main.py
	@kill $$PORT_FORWARD_PID  # Terminate the port-forward process after main.py exits
# Run the React frontend
frontend:
	cd $(FRONTEND_DIR) && npm start

# Install dependencies for the backend
install-backend:
	cd $(BACKEND_DIR) && source venv/bin/activate && pip install -r requirements.txt

# Install dependencies for the frontend
install-frontend:
	cd $(FRONTEND_DIR) && npm install

# Install dependencies for both
install: install-backend install-frontend
