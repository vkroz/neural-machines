# Python Backend Development Guidelines

## Table of Contents
1. [Project Structure](#project-structure)
2. [Naming Conventions](#naming-conventions)
3. [Code Style](#code-style)
4. [Design Principles](#design-principles)
5. [API Development with FastAPI](#api-development-with-fastapi)
6. [Database Access with SQLAlchemy](#database-access-with-sqlalchemy)
7. [LLM Integration and Chatbot Development](#llm-integration-and-chatbot-development)
8. [QuickBooks Integration](#quickbooks-integration)
9. [Testing Standards](#testing-standards)
10. [Documentation](#documentation)
11. [Version Control](#version-control)

## Project Structure

```
project_root/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── api/
│   ├── core/
│   ├── db/
│   ├── models/
│   ├── schemas/
│   ├── crud/
│   ├── services/
│   ├── integrations/
│   └── utils/
├── tests/
├── alembic/
├── .env
├── .gitignore
├── requirements.txt
├── README.md
└── docker-compose.yml
```

### Root Directory

- `requirements.txt`: Lists all Python dependencies for the project.
- `README.md`: Project documentation and setup instructions.
- `docker-compose.yml`: Docker configuration for setting up the development environment.
- `.env`: Environment variables (not version controlled).
- `.gitignore`: Specifies files and directories that Git should ignore.

### `app/` Directory

This is the main package containing all application code.

- `__init__.py`: Marks the directory as a Python package.
- `main.py`: The entry point of the application, where the FastAPI app is instantiated.

#### `app/api/`

Contains all API-related code.

- `endpoints/`: Directory containing modules for different API endpoints.
    - Potential modules: One per major resource or feature (e.g., user management, financial data, reporting).
- Consider a module for shared API dependencies or middleware.

#### `app/core/`

Core application components.

- Potential modules:
    - Application configuration management
    - Security utilities (e.g., password hashing, JWT handling)
    - Shared constants or enums

#### `app/db/`

Database-related code.

- Potential modules:
    - Base class for SQLAlchemy models
    - Database session management
    - Database initialization and connection handling

#### `app/models/`

SQLAlchemy ORM models representing database tables.

- Potential modules: One per major database entity or closely related group of entities.

#### `app/schemas/`

Pydantic models for request/response serialization and validation.

- Potential modules: Typically correspond to the modules in `models/`, but focused on API representations.

#### `app/crud/`

CRUD (Create, Read, Update, Delete) operations for database entities.

- Potential modules: Usually correspond to the modules in `models/`, containing database operations for each entity.

#### `app/services/`

Business logic and complex operations.

- Potential modules:
    - LLM service for interacting with Language Models
    - Chatbot service for chatbot-specific logic
    - Financial analysis service
    - Reporting service

#### `app/integrations/`

External service integrations.

- `quickbooks/`: QuickBooks integration code.
    - Potential modules:
        - API client for QuickBooks
        - Data models specific to QuickBooks
        - Synchronization logic
- Consider adding subdirectories for other major integrations as needed.

#### `app/utils/`

Utility functions and helper classes.

- Potential modules:
    - Configuration management utilities
    - Logging setup and utilities
    - Date and time helpers
    - Text processing utilities
    - General-purpose helper functions

### `tests/` Directory

Contains all test files.

- Consider mirroring the `app/` directory structure for organized test files.
- Potential subdirectories:
    - `test_api/`: Tests for API endpoints
    - `test_services/`: Tests for service layer
    - `test_integrations/`: Tests for external integrations
    - `test_utils/`: Tests for utility functions

### `alembic/` Directory

Database migration management.

- `env.py`: Alembic environment configuration.
- `versions/`: Directory containing individual migration scripts.

### Key Interactions Between Components

1. `app/main.py` sets up the FastAPI application and includes routers from `app/api/endpoints/`.

2. API endpoints in `app/api/endpoints/` use:
    - Schemas from `app/schemas/` for request/response models.
    - CRUD operations from `app/crud/` for database interactions.
    - Services from `app/services/` for complex business logic.

3. CRUD operations in `app/crud/` interact with SQLAlchemy models defined in `app/models/`.

4. Database sessions are managed through modules in `app/db/`.

5. External integrations in `app/integrations/` are used by services or API endpoints as needed.

6. Utility functions from `app/utils/` are used throughout the application for common tasks.

7. The `alembic/` directory is used for managing database migrations, which affect the models in `app/models/`.

This structure promotes separation of concerns, making the codebase modular and easier to maintain. Each component has a specific responsibility, allowing for easier testing and future expansion of the application. As the project develops, you can add or modify modules within these packages as needed, while maintaining a clear overall structure.


## Naming Conventions

1. Files and Directories: Use snake_case for all file and directory names.
2. Classes: Use PascalCase for class names.
3. Functions and Variables: Use snake_case for function and variable names.
4. Constants: Use UPPER_CASE for constants.
5. Private Methods/Variables: Prefix with a single underscore (_method_name).

## Code Style

1. Follow PEP 8 guidelines (see detailed explanation below).
2. Use 4 spaces for indentation.
3. Maximum line length: 88 characters (as per Black formatter).
4. Use type hints for function arguments and return values.
5. Use docstrings for all public modules, functions, classes, and methods.

### PEP 8 Explanation

PEP 8 is the official style guide for Python code. It provides coding conventions for the Python code comprising the standard library in the main Python distribution. Here are some key points:

- **Indentation**: Use 4 spaces per indentation level.
- **Maximum Line Length**: Limit all lines to a maximum of 79 characters for code and 72 for comments and docstrings.
- **Imports**: Imports should usually be on separate lines and at the top of the file.
- **Whitespace**: Avoid extraneous whitespace in the following situations:
    - Immediately inside parentheses, brackets or braces.
    - Between a trailing comma and a closing parenthesis.
- **Comments**: Comments should be complete sentences and should be used sparingly.
- **Naming Conventions**:
    - Functions, variables, and attributes: `lowercase_with_underscores`
    - Classes and Exceptions: `CapitalizedWords`
    - Protected instance attributes: `_leading_underscore`
    - Private instance attributes: `__double_leading_underscore`

For a complete guide, refer to the [official PEP 8 documentation](https://www.python.org/dev/peps/pep-0008/).

## Design Principles

When developing your Python backend application, adhere to these design principles:

1. **SOLID Principles**:
    - Single Responsibility Principle: Each class should have only one reason to change.
    - Open/Closed Principle: Software entities should be open for extension, but closed for modification.
    - Liskov Substitution Principle: Objects of a superclass should be replaceable with objects of its subclasses without affecting the correctness of the program.
    - Interface Segregation Principle: Many client-specific interfaces are better than one general-purpose interface.
    - Dependency Inversion Principle: Depend upon abstractions, not concretions.

2. **DRY (Don't Repeat Yourself)**: Avoid duplication of code. Extract common functionality into reusable functions or classes.

3. **KISS (Keep It Simple, Stupid)**: Strive for simplicity in your designs. Avoid unnecessary complexity.

4. **YAGNI (You Aren't Gonna Need It)**: Don't add functionality until it's necessary. Avoid implementing features or adding complexity based on speculation about future needs.

5. **Separation of Concerns**: Divide your program into distinct sections, each addressing a separate concern.

6. **Composition Over Inheritance**: Favor composition of objects over inheritance when designing class relationships.

7. **Dependency Injection**: Provide dependencies to a class from the outside rather than having the class create them.

Example applying these principles:

```python
from abc import ABC, abstractmethod

class DataStore(ABC):
    @abstractmethod
    def save(self, data: dict):
        pass

class DatabaseStore(DataStore):
    def save(self, data: dict):
        # Implementation for database storage

class FileStore(DataStore):
    def save(self, data: dict):
        # Implementation for file storage

class UserService:
    def __init__(self, data_store: DataStore):
        self.data_store = data_store

    def create_user(self, user_data: dict):
        # Business logic for user creation
        self.data_store.save(user_data)

# Usage
db_store = DatabaseStore()
user_service = UserService(db_store)
user_service.create_user({"name": "John Doe", "email": "john@example.com"})
```

This example demonstrates:
- Single Responsibility: Each class has a single, well-defined purpose.
- Open/Closed: We can add new storage methods without modifying existing code.
- Dependency Inversion: UserService depends on the abstract DataStore, not concrete implementations.
- Dependency Injection: The specific DataStore is injected into UserService.
- YAGNI: We've only implemented what's necessary, without speculating on future needs.

## API Development with FastAPI

1. Group related endpoints in separate files under `app/api/endpoints/`.
2. Use Pydantic models for request/response schemas in `app/schemas/`.
3. Implement dependency injection for shared logic (e.g., authentication).
4. Use async functions for database operations and external API calls.
5. Implement proper error handling and use HTTPException for API errors.

Example:

```python
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.api import deps
from app.crud import crud_user
from app.schemas import User, UserCreate

router = APIRouter()

@router.post("/users/", response_model=User)
async def create_user(
    user: UserCreate,
    db: Session = Depends(deps.get_db)
):
    db_user = await crud_user.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return await crud_user.create_user(db=db, user=user)
```

## Database Access with SQLAlchemy

1. Define models in `app/models/` using SQLAlchemy declarative base.
2. Use async SQLAlchemy for database operations.
3. Implement CRUD operations in `app/crud/` modules.
4. Use Alembic for database migrations.

Example model:

```python
from sqlalchemy import Column, Integer, String
from app.db.base_class import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    full_name = Column(String)
```

## LLM Integration and Chatbot Development

Our system uses LLMs to implement a conversational interface (chatbot) that provides users with financial analytics and insights from financial data. As the system evolves, we experiment with different LLM versions and vendors. Therefore, we must support various versions of LLMs, which will serve as the foundation for our chatbot.

### LLM Service Architecture

1. Create an abstract base class for LLM services:

```python
from abc import ABC, abstractmethod

class BaseLLMService(ABC):
    @abstractmethod
    async def generate_response(self, prompt: str, context: dict) -> str:
        pass

    @abstractmethod
    async def get_embedding(self, text: str) -> list[float]:
        pass
```

2. Implement concrete classes for each LLM vendor:

```python
class OpenAIService(BaseLLMService):
    def __init__(self, api_key: str, model: str):
        self.client = AsyncOpenAI(api_key=api_key)
        self.model = model

    async def generate_response(self, prompt: str, context: dict) -> str:
        # Implementation for OpenAI

    async def get_embedding(self, text: str) -> list[float]:
        # Implementation for OpenAI embeddings

class AnthropicService(BaseLLMService):
    def __init__(self, api_key: str, model: str):
        self.client = AsyncAnthropicAPI(api_key=api_key)
        self.model = model

    async def generate_response(self, prompt: str, context: dict) -> str:
        # Implementation for Anthropic

    async def get_embedding(self, text: str) -> list[float]:
        # Implementation for Anthropic embeddings
```

3. Use a factory pattern to create LLM services:

```python
class LLMServiceFactory:
    @staticmethod
    def create_service(vendor: str, api_key: str, model: str) -> BaseLLMService:
        if vendor == "openai":
            return OpenAIService(api_key, model)
        elif vendor == "anthropic":
            return AnthropicService(api_key, model)
        else:
            raise ValueError(f"Unsupported LLM vendor: {vendor}")
```

4. Implement a ChatbotService that uses the LLMService:

```python
class ChatbotService:
    def __init__(self, llm_service: BaseLLMService, financial_data_service: FinancialDataService):
        self.llm_service = llm_service
        self.financial_data_service = financial_data_service

    async def process_user_message(self, user_message: str, conversation_history: list[dict]) -> str:
        context = await self.financial_data_service.get_relevant_data(user_message)
        prompt = self.construct_prompt(user_message, conversation_history, context)
        response = await self.llm_service.generate_response(prompt, context)
        return response

    def construct_prompt(self, user_message: str, conversation_history: list[dict], context: dict) -> str:
        # Implement prompt construction logic
        pass
```

### Prompt Engineering Standards

1. Use a consistent prompt structure across all LLM interactions:
   ```
   [System Instructions]
   [Conversation History]
   [Current Context]
   [User Query]
   ```

2. Maintain clear and concise system instructions that define the chatbot's role and capabilities.

3. Include relevant financial data and context in each prompt to ensure accurate responses.

4. Use few-shot examples in system instructions to guide the LLM's response format and style.

5. Implement prompt templates for common financial queries and analyses:

```python
FINANCIAL_ANALYSIS_TEMPLATE = """
Analyze the following financial data and provide insights:
Revenue: {revenue}
Expenses: {expenses}
Profit Margin: {profit_margin}

Please provide a summary of the financial performance and any recommendations for improvement.
"""

def create_financial_analysis_prompt(financial_data: dict) -> str:
    return FINANCIAL_ANALYSIS_TEMPLATE.format(**financial_data)
```

6. Regularly review and refine prompts based on chatbot performance and user feedback.

7. Implement a prompt versioning system to track changes and allow for A/B testing of different prompt strategies.

### LLM Version Management

1. Use configuration files to manage LLM versions and settings:

```yaml
# config/llm_config.yaml
openai:
  default_model: "gpt-4"
  fallback_model: "gpt-3.5-turbo"
  embedding_model: "text-embedding-ada-002"

anthropic:
  default_model: "claude-2"
  fallback_model: "claude-instant-1"
```

2. Implement a configuration manager to load and manage LLM settings:

```python
import yaml

class LLMConfigManager:
    def __init__(self, config_path: str):
        with open(config_path, 'r') as f:
            self.config = yaml.safe_load(f)

    def get_model(self, vendor: str, model_type: str = "default_model") -> str:
        return self.config[vendor][model_type]
```

3. Use feature flags or environment variables to control which LLM vendor and version is used in different environments (development, staging, production).

## QuickBooks Integration

We use QuickBooks to fetch financial data and store it in our database. This data is later used to generate reports and provide information to users through the chatbot.

### QuickBooks Integration Architecture

1. Create an abstract base class for QuickBooks integration:

```python
from abc import ABC, abstractmethod

class BaseQuickBooksIntegration(ABC):
    @abstractmethod
    async def fetch_financial_data(self, start_date: date, end_date: date) -> dict:
        pass

    @abstractmethod
    async def sync_data_to_database(self, data: dict):
        pass
```

2. Implement concrete classes for different QuickBooks applications:

```python
class QuickBooksOnlineIntegration(BaseQuickBooksIntegration):
    def __init__(self, client_id: str, client_secret: str, refresh_token: str):
        # Initialize QuickBooks Online API client

    async def fetch_financial_data(self, start_date: date, end_date: date) -> dict:
        # Implementation for fetching data from QuickBooks Online

    async def sync_data_to_database(self, data: dict):
        # Implementation for syncing data to our database

class QuickBooksDesktopIntegration(BaseQuickBooksIntegration):
    def __init__(self, connection_string: str):
        # Initialize QuickBooks Desktop connection

    async def fetch_financial_data(self, start_date: date, end_date: date) -> dict:
        # Implementation for fetching data from QuickBooks Desktop

    async def sync_data_to_database(self, data: dict):
        # Implementation for syncing data to our database
```

3. Implement a QuickBooks data synchronization service:

```python
class QuickBooksDataSyncService:
    def __init__(self, integration: BaseQuickBooksIntegration, db_session: AsyncSession):
        self.integration = integration
        self.db_session = db_session

    async def sync_financial_data(self, start_date: date, end_date: date):
        data = await self.integration.fetch_financial_data(start_date, end_date)
        await self.integration.sync_data_to_database(data)
        await self.post_process_data(data)

    async def post_process_data(self, data: dict):
        # Implement any necessary post-processing or data transformation
        pass
```

### Best Practices for QuickBooks Integration

1. Use asynchronous programming to handle QuickBooks API requests efficiently.

2. Implement robust error handling and retry mechanisms for API calls.

3. Use rate limiting to avoid exceeding QuickBooks API quotas.

4. Implement a caching layer to reduce unnecessary API calls for frequently accessed data.

5. Use database transactions to ensure data consistency during synchronization.

6. Implement a logging system to track data synchronization activities and errors.

7. Use data validation to ensure the integrity of fetched financial data before storing it in the database.

8. Implement a reconciliation process to periodically verify the consistency between QuickBooks data and your local database.

### Data Model for Financial Data

Create SQLAlchemy models to represent the financial data fetched from QuickBooks:

```python
from sqlalchemy import Column, Integer, String, Date, Numeric
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True)
    date = Column(Date, nullable=False)
    description = Column(String, nullable=False)
    amount = Column(Numeric(10, 2), nullable=False)
    category = Column(String)

class Account(Base):
    __tablename__ = "accounts"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    type = Column(String, nullable=False)
    balance = Column(Numeric(10, 2), nullable=False)

# Add more models as needed
```

### QuickBooks Data Access Layer

Implement a data access layer to interact with the stored financial data:

```python
class FinancialDataService:
    def __init__(self, db_session: AsyncSession):
        self.db_session = db_session

    async def get_transactions(self, start_date: date, end_date: date) -> list[Transaction]:
        query = select(Transaction).where(
            Transaction.date.between(start_date, end_date)
        )
        result = await self.db_session.execute(query)
        return result.scalars().all()

    async def get_account_balances(self) -> list[Account]:
        query = select(Account)
        result = await self.db_session.execute(query)
        return result.scalars().all()

    async def get_relevant_data(self, user_query: str) -> dict:
        # Implement logic to fetch relevant financial data based on the user's query
        pass
```

By implementing these guidelines for LLM integration, chatbot development, and QuickBooks integration, you'll have a solid foundation for building a robust financial analytics system with a conversational interface.


## Testing Standards

1. Use pytest for writing and running tests.
2. Aim for at least 80% test coverage.
3. Write unit tests for all CRUD operations and services.
4. Write integration tests for API endpoints.
5. Use fixtures for database and API clients.

Example test:

```python
import pytest
from httpx import AsyncClient
from sqlalchemy.orm import Session

from app.crud import crud_user
from app.schemas import UserCreate
from app.main import app

@pytest.mark.asyncio
async def test_create_user(client: AsyncClient, db: Session):
    user_data = {"email": "test@example.com", "password": "password123"}
    response = await client.post("/users/", json=user_data)
    assert response.status_code == 200
    data = response.json()
    assert data["email"] == user_data["email"]
    assert "id" in data
```

## Documentation

1. Use docstrings for all public modules, classes, and functions.
2. Follow Google-style docstring format.
3. Keep README.md up-to-date with setup instructions and project overview.
4. Use FastAPI's automatic API documentation (Swagger UI).

### Code Documentation Examples

Here are examples of properly documented code following the Google-style docstring format:

1. Function documentation:

```python
def calculate_discount(price: float, discount_percent: float) -> float:
    """
    Calculate the discounted price of an item.

    This function takes the original price of an item and a discount percentage,
    then returns the price after applying the discount.

    Args:
        price (float): The original price of the item.
        discount_percent (float): The discount percentage, expressed as a float
            between 0 and 100.

    Returns:
        float: The price after applying the discount.

    Raises:
        ValueError: If the discount_percent is not between 0 and 100.

    Example:
        >>> calculate_discount(100, 20)
        80.0
    """
    if not 0 <= discount_percent <= 100:
        raise ValueError("Discount percentage must be between 0 and 100")
    
    discount_amount = price * (discount_percent / 100)
    return price - discount_amount
```

2. Class documentation:

```python
class User:
    """
    Represents a user in the system.

    This class contains basic user information and methods for user operations.

    Attributes:
        id (int): The unique identifier for the user.
        username (str): The user's username.
        email (str): The user's email address.
        is_active (bool): Whether the user account is active.

    """

    def __init__(self, id: int, username: str, email: str):
        """
        Initialize a new User instance.

        Args:
            id (int): The unique identifier for the user.
            username (str): The user's username.
            email (str): The user's email address.
        """
        self.id = id
        self.username = username
        self.email = email
        self.is_active = True

    def deactivate(self):
        """
        Deactivate the user account.

        This method sets the is_active attribute to False.

        Returns:
            None
        """
        self.is_active = False

    def __str__(self) -> str:
        """
        Return a string representation of the User.

        Returns:
            str: A string containing the user's username and email.
        """
        return f"User: {self.username} ({self.email})"
```

3. Module documentation:

```python
"""
User Management Module

This module provides functionality for managing user accounts in the system.
It includes classes and functions for creating, updating, and deleting users,
as well as for user authentication and authorization.

Classes:
    User: Represents a user in the system.
    UserManager: Provides methods for managing user accounts.

Functions:
    create_user(username: str, email: str, password: str) -> User:
        Creates a new user account.
    authenticate_user(username: str, password: str) -> bool:
        Authenticates a user's credentials.

Usage:
    from user_management import User, UserManager, create_user, authenticate_user

    # Create a new user
    new_user = create_user("johndoe", "john@example.com", "securepassword")

    # Authenticate user
    is_valid = authenticate_user("johndoe", "securepassword")

"""

# Rest of the module code follows...
```

## Version Control

We use Git for version control and follow the Git Flow branching model with some specific adaptations for our workflow. Adhering to these guidelines ensures a smooth and consistent development process across the team.

### Git Flow Overview

1. Use Git for version control.
2. Follow the Git Flow branching model with our specific adaptations.
3. Write clear, concise commit messages.
4. Use pull requests for code reviews before merging into the staging branch.

### Branch Structure

- `main`: Production branch. This branch always reflects the production-ready state.
- `staging`: Staging branch. This is the pre-production branch where features are integrated and tested before going to production.
- `feature/*`: Feature branches. All new features and non-emergency fixes should be developed in feature branches.
- `hotfix/*`: Hotfix branches. For critical bugs in production that need immediate attention.

### Branch Naming Conventions

- Feature branches must follow the pattern: `feature/brief-description-of-feature`
  Example: `feature/implement-quickbooks-sync`
- Hotfix branches should follow the pattern: `hotfix/brief-description-of-fix`
  Example: `hotfix/fix-critical-data-leak`


### Development Workflow

1. Create a new feature branch from `staging`:
   ```
   git checkout staging
   git pull origin staging
   git checkout -b feature/your-feature-name
   ```

2. Develop your feature in the feature branch.

3. Commit your changes with clear, descriptive commit messages:
   ```
   git commit -m "Add QuickBooks data synchronization service"
   ```

4. Push your feature branch to the remote repository on GitHub:
   ```
   git push -u origin feature/your-feature-name
   ```

5. Create a Pull Request (PR) on GitHub to merge your feature branch into `staging`.

6. After the PR is approved and merged, delete the feature branch both locally and on GitHub.

### Pull Request (PR) Guidelines

- **Never** submit a PR directly to `main`. All feature development PRs should target the `staging` branch.
- Use GitHub's PR template if available. If not, consider creating one for consistency.
- Before submitting a PR:
    1. Ensure your code passes all tests.
    2. Deploy your feature branch to the development environment on Render.com for testing.
    3. Update the PR description with the Render.com deployment URL for easy reviewing.

- PR titles should be clear and descriptive, summarizing the changes.
- Include a detailed description of the changes, any testing performed, and any potential impacts.
- Use GitHub's features to link relevant issues or tickets in the PR description.
- Assign appropriate reviewers to your PR using GitHub's reviewer assignment feature.
- Add relevant labels to your PR (e.g., "feature", "bugfix", "documentation").

### Code Review Process

1. Reviewers should use GitHub's review feature to provide inline comments and overall feedback.
2. Make use of GitHub's suggestion feature for proposing specific code changes.
3. Address all comments and make necessary changes.
4. Use the "Request changes" or "Approve" options in GitHub to clearly indicate the status of the review.
5. Once approved, the PR can be merged into `staging` using GitHub's merge options (prefer "Squash and merge" for a clean history).

### Staging to Production

1. After features have been merged into `staging` and thoroughly tested:
    - Create a PR on GitHub from `staging` to `main`.
    - This PR should be reviewed by a senior developer or team lead.
    - Provide a summary of all changes included in this release.
    - Use GitHub's draft PR feature if the release is not yet ready for final review.

2. Once approved, merge the PR from `staging` to `main` using GitHub's merge feature.

### Hotfix Process

For critical issues that need to be fixed in production immediately:

1. Create a `hotfix` branch from `main`:
   ```
   git checkout main
   git checkout -b hotfix/critical-bug-fix
   ```

2. Implement the fix and commit the changes.

3. Create a PR on GitHub to merge the hotfix into both `main` and `staging`.

4. After approval, merge into `main` first, then `staging`.

5. Tag the new production release and create a GitHub Release.

### Best Practices

1. Keep commits atomic: Each commit should represent a single logical change.
2. Rebase feature branches on `staging` regularly to keep them up to date.
3. Use `git rebase -i` to clean up commits before submitting a PR.
4. Write meaningful commit messages. Follow the format:
   ```
   Short (50 chars or less) summary of changes

   More detailed explanatory text, if necessary. Wrap it to about 72
   characters or so. In some contexts, the first line is treated as the
   subject of an email and the rest of the text as the body. The blank
   line separating the summary from the body is critical (unless you omit
   the body entirely); tools like rebase can get confused if you run the
   two together.

   Further paragraphs come after blank lines.

   - Bullet points are okay, too
   - Use a hyphen or asterisk for the bullet, followed by a single space
   ```

5. Use `.gitignore` to exclude files that should not be version controlled (e.g., `.env` files, `__pycache__`, etc.).
6. Make use of GitHub Actions for CI/CD pipelines, including running tests and linting on PRs.
7. Utilize GitHub's branch protection rules to enforce review requirements and status checks before merging.
8. Use GitHub's repository settings to manage team access and permissions.

By following these version control guidelines tailored for GitHub, we ensure a consistent and efficient development process, making it easier to manage our codebase, collaborate effectively, and deploy changes safely to production.
