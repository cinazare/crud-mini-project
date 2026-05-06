from sqlmodel import Session, SQLModel, select

def create(entity: SQLModel, session: Session):
    session.add(entity)
    session.commit()
    session.refresh(entity)
    return entity


def get(_type, session: Session, id: int | None = None):
    if id is not None:
        return session.get(_type, id)

    statement = select(_type)
    return session.exec(statement).all()


def update(entity: SQLModel, _type, id: int, session: Session):
    db_entity = session.get(_type, id)

    if not db_entity:
        return None
    
    entity_dict = entity.model_dump().items()

    for key, value in entity_dict:
        if value != None:
            setattr(db_entity, key, value)

    session.add(db_entity)
    session.commit()
    session.refresh(db_entity)

    return db_entity


def delete(_type, id: int, session: Session):
    entity = session.get(_type, id)

    if not entity:
        return None

    session.delete(entity)
    session.commit()

    return entity

    
