import nox

@nox.session
def test(session):
    session.run("pytest", "-v", "tests")

@nox.session
def isort(session):
    session.install('isort')
    session.run('isort', 'reason', 'tests')

@nox.session
def black(session):
    session.install('black')
    session.run('black', 'reason', 'tests')

@nox.session
def lint(session):
    session.notify("isort")
    session.notify("black")
