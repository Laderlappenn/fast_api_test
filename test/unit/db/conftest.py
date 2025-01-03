# import pytest
#
# from models import (
#     Car,
#     engine,
# )
#
#
# @pytest.fixture(scope="function")
# def session():
#     if not engine.url.get_backend_name() == "sqlite":
#         raise RuntimeError('Use SQLite backend to run tests')
#
#     Base.metadata.create_all(engine)
#     try:
#         with Session() as session:
#             yield session
#     finally:
#         Base.metadata.drop_all(engine)
#
# @pytest.fixture(scope="function")
# def seed(session):
#     session.add_all(
#         [
#             User(id=1, fullname="John Doe"),
#             User(id=2, fullname="Katarine Alex"),
#         ]
#     )
#     session.commit()