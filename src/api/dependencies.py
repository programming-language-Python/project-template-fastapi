from repositories import BudgetRepository
from services import BudgetService


def budget_service() -> BudgetService:
    return BudgetService(BudgetRepository)
