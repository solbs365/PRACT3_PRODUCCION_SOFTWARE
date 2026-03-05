Feature: Gestión de gastos
  Como estudiante
  Quiero registrar mis gastos
  Para controlar cuánto dinero gasto

  Scenario: Crear un gasto y comprobar cual es el total que llevo gastado
    Given un gestor de gastos vacío
    When añado un gasto de 5 euros llamado Café
    Then el total de dinero gastado debe ser 5 euros

  Scenario: Eliminar un gasto y comprobar cual es el total que llevo gastado
    Given un gestor con un gasto de 5 euros
    When elimino el gasto con id 1
    Then debe haber 0 gastos registrados

  Scenario: Crear y eliminar un gasto y comprobar que no he gastado dinero
    Given un gestor de gastos vacío
    When añado un gasto de 5 euros llamado Café
    And elimino el gasto con id 1
    Then debe haber 0 gastos registrados

  Scenario: Crear dos gastos diferentes y comprobar que el total que llevo gastado es la suma de ambos
    Given un gestor de gastos vacío
    When añado un gasto de 5 euros llamado Café
    And añado un gasto de 10 euros llamado Comida
    Then el total de dinero gastado debe ser 15 euros

  Scenario: Crear tres gastos diferentes que sumen 30 euros hace que el total sean 30 euros
    Given un gestor de gastos vacío
    When añado un gasto de 5 euros llamado Helado
    And añado un gasto de 20 euros llamado Perfume
    And añado un gasto de 5 euros llamado Lotería
    Then el total de dinero gastado debe ser 30 euros

  Scenario: Crear tres gastos de 10, 30, 30 euros y elimino el ultimo gasto la suma son 40 euros
    Given un gestor de gastos vacío
    When añado un gasto de 10 euros llamado Gasolina
    And añado un gasto de 30 euros llamado Ropa
    And añado un gasto de 30 euros llamado Cena
    And elimino el gasto con id 3
    Then el total de dinero gastado debe ser 40 euros


  Scenario: Consultar el gasto acumulado de un mes específico
    Given un gestor con un gasto de 50 euros en 2025-03-01
    When añado un gasto de 20 euros llamado Fiesta en 2025-03-15
    And consulto los totales por mes
    Then "2025-03" debe sumar 70 euros


  Scenario: Control de presupuesto mensual
    Given un presupuesto de 100 euros
    When añado un gasto de 120 euros llamado Matricula
    Then el total gastado debe ser mayor que el presupuesto
    

  Scenario: Eliminar un gasto actualiza el balance total 
    Given un gestor con un gasto de 30 euros en 2025-03-01
    And un gestor con un gasto de 10 euros en 2026-03-02
    When elimino el gasto con id 1
    Then el total de dinero gastado debe ser 10 euros


