import random
import string
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))
from shared.student import GROUP_NAME, STUDENT_NAME, VARIANT_NUMBER  # noqa: E402

passwords = [
    "Compli4nc3@Check",
    "weak",
    "Risk@Ass3ssment",
    "guest",
    "Vulner4bility@Scan",
    "temp",
    "P3netration@Test",
    "demo",
    "S3curity@Audit",
    "trial",
]

criteria = {
    "min_length": 8,
    "require_digits": True,
    "require_upper": True,
    "require_special": True,
}

forbidden_passwords = {"weak", "guest", "temp", "demo", "trial", "password"}

def evaluate_password(pwd: str, all_passwords: list[str]) -> str:
    min_len = criteria["min_length"]

    if pwd in forbidden_passwords or len(pwd) < min_len:
        return "Заборонений"

    has_digit = any(ch.isdigit() for ch in pwd)
    has_upper = any(ch.isupper() for ch in pwd)
    has_lower = any(ch.islower() for ch in pwd)
    has_special = any(ch in string.punctuation for ch in pwd)

    crit_list = [has_digit, has_upper, has_lower, has_special]
    meets_all = all(crit_list)
    is_unique = all_passwords.count(pwd) == 1

    if meets_all and len(pwd) >= (min_len + 4) and is_unique:
        return "Дуже сильний"

    if meets_all and len(pwd) < (min_len + 4):
        return "Сильний"

    if any(crit_list) and not meets_all:
        return "Середній"

    if any(crit_list):
        return "Слабкий"

    return "Заборонений"


def run_task1() -> None:
    print(f"ЗАВДАННЯ 1 | Студент: {STUDENT_NAME} | Група: {GROUP_NAME} | Варіант: {VARIANT_NUMBER}\n")

    working_passwords = passwords.copy()
    random_indices = random.sample(range(len(working_passwords)), 3)
    duplicates = [working_passwords[i] for i in random_indices]
    working_passwords.extend(duplicates)

    for idx, pwd in enumerate(working_passwords, start=1):
        status = evaluate_password(pwd, working_passwords)
        print(f"{idx:<3} {pwd:<25} {status}")


if __name__ == "__main__":
    run_task1()