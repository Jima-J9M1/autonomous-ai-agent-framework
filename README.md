# Autonomous AI Agent

An autonomous AI agent system built with FastAPI that can decompose goals into tasks, execute them, evaluate results, and handle escalations.

## Features

- **Goal Decomposition**: Breaks down high-level goals into executable tasks
- **Task Execution**: Executes tasks with retry logic and error handling
- **State Management**: Tracks agent state through planning, execution, completion, and failure states
- **Evaluation**: Evaluates task execution results
- **Memory**: Persistent storage for agent state
- **Escalation Handling**: Handles failures and escalates when tasks exceed retry limits
- **Budget Management**: Tracks and manages resource budgets

## Project Structure

```
app/
├── agent/              # Core agent components
│   ├── controller.py          # Main agent orchestrator
│   ├── goal_decomposer.py     # Goal decomposition logic
│   ├── task_executor.py       # Task execution engine
│   ├── state_machine.py       # State management
│   ├── escalation_handler.py  # Failure escalation
│   └── budget_manager.py      # Budget tracking
├── models/             # Data models
│   ├── goal.py
│   ├── task.py
│   ├── state.py
│   ├── budget.py
│   └── escalation.py
├── evaluation/        # Evaluation logic
│   └── step_evaluator.py
├── memory/            # Persistent storage
│   └── persistent_store.py
└── main.py           # FastAPI application entry point
```

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd autonomus-ai-agent
```

2. Create a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r app/requirements.txt
```

## Usage

### Running the API Server

Start the FastAPI server:
```bash
uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000`

### API Endpoints

#### Health Check
```bash
GET /health
```
Returns the health status of the agent.

#### Run Agent
```bash
POST /run
Content-Type: application/json

{
  "goal": "Your goal description here"
}
```

Executes the agent with the given goal. The agent will:
1. Decompose the goal into tasks
2. Execute each task
3. Evaluate results
4. Retry failed tasks (up to 2 retries)
5. Escalate if tasks fail repeatedly

## Development

### Project Components

- **AutonomousAgent**: Main controller that orchestrates all components
- **GoalDecomposer**: Breaks goals into executable tasks
- **TaskExecutor**: Executes tasks and handles retries
- **StateMachine**: Manages agent state transitions
- **StepEvaluator**: Evaluates task execution results
- **PersistentStore**: Saves and loads agent state
- **EscalationHandler**: Handles failures and escalations
- **BudgetManager**: Tracks resource budgets

### State Flow

1. **PLANNING**: Agent decomposes the goal into tasks
2. **EXECUTING**: Tasks are executed sequentially
3. **COMPLETED**: All tasks completed successfully
4. **FAILED**: Agent encountered an unrecoverable error

## Requirements

- Python 3.8+
- FastAPI
- Uvicorn
- Pydantic

