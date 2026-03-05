from datetime import date
import pytest
from pytest_bdd import scenarios, given, when, then, parsers

from core.expense_service import ExpenseService
from core.in_memory_expense_repository import InMemoryExpenseRepository

scenarios("./expense_management.feature")


@pytest.fixture
def context():
    repo = InMemoryExpenseRepository()
    service = ExpenseService(repo)
    return {"service": service, "db": repo}


@given(parsers.parse("un gestor de gastos vacío"))
def empty_manager(context):
    pass


@given(parsers.parse("un gestor con un gasto de {amount:d} euros"))
def manager_with_one_expense(context, amount):
    context["service"].create_expense(
        title="Gasto inicial", amount=amount, description="", expense_date=date.today()
    )

# Añadido 1
@given(parsers.parse("un gestor con un gasto de {amount:d} euros en {dt}"))
def add_expense_with_date(context, amount, dt):
    year, month, day = map(int, dt.split("-"))
    context["service"].create_expense(
        title="Gasto fecha",
        amount=amount,
        expense_date=date(year, month, day),
    )

# Añadido 4
@given(parsers.parse("un presupuesto de {amount:d} euros"))
def set_budget(context, amount):
    context["budget"] = amount

@when(parsers.parse("añado un gasto de {amount:d} euros llamado {title}"))
def add_expense(context, amount, title):
    context["service"].create_expense(
        title=title, amount=amount, description="", expense_date=date.today()
    )

# Añadido 2
@when(parsers.parse("añado un gasto de {amount:d} euros llamado {title} en {dt}"))
def add_expense_with_specific_date(context, amount, title, dt):
    actual_date = date.fromisoformat(dt)

    context["service"].create_expense(
        title=title, amount=amount, description="", expense_date=actual_date
    )
# Añadido 3
@when(parsers.parse("consulto los totales por mes"))
def get_monthly_totals(context: dict):
    context["totals"] = context["service"].total_by_month()


@when(parsers.parse("elimino el gasto con id {expense_id:d}"))
def remove_expense(context, expense_id):
    context["service"].remove_expense(expense_id)


@then(parsers.parse("el total de dinero gastado debe ser {total:d} euros"))
def check_total(context, total):
    assert context["service"].total_amount() == total


@then(parsers.parse("{month_name} debe sumar {expected_total:d} euros"))
def check_month_total(context: dict, month_name, expected_total):
    clean_month_name = month_name.replace('"', '').replace("'", "").strip()

    totals = context.get("totals", {})
    total_actual = totals.get(clean_month_name, 0)

    assert total_actual == expected_total


@then(parsers.parse("debe haber {expenses:d} gastos registrados"))
def check_expenses_length(context, expenses):
    total = len(context["service"].list_expenses())
    assert expenses == total

# Añadido 5
@then("el total gastado debe ser mayor que el presupuesto")
def check_over_budget(context):
    total = context["service"].total_amount()
    assert total > context["budget"]