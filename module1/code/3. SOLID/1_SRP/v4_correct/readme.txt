This version demonstrates the complete SRP decoupling:
Instead of coupling Employee to jsonlibrary, we introduce a dedicated JsonEmployee adapter/DTO.
Employee remains pure domain logic, while EmployeeStorage converts Employee to JsonEmployee
and uses jsonlibrary to save the data. 