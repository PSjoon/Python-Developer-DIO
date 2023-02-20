from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Session
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey
from sqlalchemy import create_engine
from sqlalchemy import select

# Base: estrutura db pre-definida
# interliga a programacao com o orm
Base = declarative_base()


class User(Base):
    __tablename__ = "user_account"
    # atributos
    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)

    # criacao de relacionamento
    # cascade: mudanca em cascata
    address = relationship(
        "Address", back_populates="user", cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"User(id={self.id},name={self.name},fullname={self.fullname})"


class Address(Base):
    __tablename__ = "address"

    id = Column(Integer, primary_key=True, autoincrement=True)
    email_address = Column(String(30), nullable=False)
    user_id = Column(Integer, ForeignKey(
        "user_account.id"), nullable=False)

    user = relationship("User", back_populates="address")

    def __repr__(self):
        return f"Address(id={self.id}, email_address={self.email_address}, user_id)"


# print(User.__tablename__)
# print(Address.__tablename__)

# conexao com DB
engine = create_engine("sqlite://")

# criando classes como tabelas no DB
Base.metadata.create_all(engine)

# inspecionar dados
# # insp = inspect(engine)
# # print(insp.get_columns('user_account'))

with Session(engine) as session:
    pedro = User(
        name="Pedro",
        fullname="Santos",
        address=[Address(email_address='pedro@gmail.com')]
    )
    sandy = User(
        name="Sandy",
        fullname="Ferreira",
        address=[Address(email_address='sandy@gmail.com')],
    )

    # persistindo dados no DB
    session.add_all([pedro, sandy])

stmt = select(User).where(User.name.in_(['Pedro', 'Sandy']))
print('filtrando user')
for user in session.scalars(stmt):
    print(User)
