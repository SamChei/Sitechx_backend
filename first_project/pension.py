"""
Pension Scheme Calculator
--------------------------
Determines which pension scheme an employee qualifies for based on:
    - Age
    - Years of work experience
    - Monthly salary
    - Employment type (Government or Private)

"""

RETIREMENT_AGE = 60
MIN_EXPERIENCE_FULL_PENSION = 30
MIN_EXPERIENCE_PARTIAL_PENSION = 20
HIGH_SALARY_THRESHOLD = 100_000

def determine_scheme(age, experience, salary, is_government):
    # --- Government employees ---
    if is_government:
        if age >= RETIREMENT_AGE and experience >= MIN_EXPERIENCE_FULL_PENSION:
            return (
                "Government Full Pension Scheme",
                f"Meets retirement age ({RETIREMENT_AGE}+) and has "
                f"{experience} years of service (>= {MIN_EXPERIENCE_FULL_PENSION})."
            )
        elif age >= RETIREMENT_AGE and experience >= MIN_EXPERIENCE_PARTIAL_PENSION:
            return (
                "Government Partial Pension Scheme",
                f"Meets retirement age but has only {experience} years of "
                f"service (< {MIN_EXPERIENCE_FULL_PENSION})."
            )
        elif experience >= MIN_EXPERIENCE_PARTIAL_PENSION:
            return (
                "Government Deferred Pension Scheme",
                f"Has {experience}+ years of service but has not yet reached "
                f"retirement age ({RETIREMENT_AGE})."
            )
        else:
            return (
                "Government Provident Fund (GPF) Only",
                f"Insufficient service ({experience} yrs) for a pension scheme; "
                "eligible only for provident fund benefits."
            )

    # --- Private employees ---
    else:
        if age >= RETIREMENT_AGE and experience >= MIN_EXPERIENCE_FULL_PENSION:
            return (
                "Private Sector Superannuation Pension",
                f"Meets retirement age and has {experience}+ years of service."
            )
        elif salary >= HIGH_SALARY_THRESHOLD and experience >= MIN_EXPERIENCE_PARTIAL_PENSION:
            return (
                "National Pension Scheme (NPS) - Voluntary High-Tier",
                f"High salary (>= {HIGH_SALARY_THRESHOLD}) and "
                f"{experience}+ years of experience qualify for an "
                "enhanced voluntary contribution tier."
            )
        elif experience >= MIN_EXPERIENCE_PARTIAL_PENSION:
            return (
                "Employee Provident Fund (EPF) with Pension Component",
                f"Has {experience}+ years of service; qualifies for the "
                "standard EPF pension component."
            )
        else:
            return (
                "Employee Provident Fund (EPF) Only",
                f"Insufficient service ({experience} yrs) for pension "
                "component; eligible only for provident fund savings."
            )


def get_positive_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value < 0:
                print("Please enter a non-negative number.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a whole number.")


def get_positive_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("Please enter a non-negative number.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a numeric value.")


def get_yes_no(prompt):
    while True:
        answer = input(prompt).strip().lower()
        if answer in ("y", "yes"):
            return True
        elif answer in ("n", "no"):
            return False
        print("Please answer 'y' or 'n'.")


def main():
    print("=== Pension Scheme Eligibility Calculator ===\n")

    name = input("Employee name: ").strip()
    age = get_positive_int("Age (years): ")
    experience = get_positive_int("Work experience (years): ")
    salary = get_positive_float("Monthly salary: ")
    is_government = get_yes_no("Is this a government employee? (y/n): ")

    scheme, explanation = determine_scheme(age, experience, salary, is_government)

    print("\n--- Result ---")
    print(f"Employee   : {name if name else 'N/A'}")
    print(f"Age        : {age}")
    print(f"Experience : {experience} years")
    print(f"Salary     : {salary:,.2f}")
    print(f"Sector     : {'Government' if is_government else 'Private'}")
    print(f"\nQualified Pension Scheme: {scheme}")
    print(f"Reason: {explanation}")


if __name__ == "__main__":
    main()