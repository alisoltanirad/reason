import nox

LINT_FILES = ["reason", "tests", "noxfile.py", "setup.py"]


@nox.session(python=["3.7", "3.8", "3.9", "3.10", "3.11"])
def test(session):
    session.install("-r", "requirements.txt")
    session.install("pytest")
    session.run("pytest", "-v", "tests")


@nox.session
def isort(session):
    session.install("isort")
    session.run("isort", *LINT_FILES)


@nox.session
def black(session):
    session.install("black")
    session.run("black", *LINT_FILES)


@nox.session
def lint(session):
    session.notify("isort")
    session.notify("black")
