from sqlmodel import Session, SQLModel, select

def create(entity: SQLModel, session: Session, _type):
    session.add(entity)
    session.commit()
    session.refresh(entity)
    return entity


def get(_type, session: Session, id: int=None):
    if id == None:
        entity = session.get(entity, id)
        return entity
    
    else:
        statement = select(_type)
        results = session.exec(statement).all()
        return results


def update(entity: SQLModel, _type, id: int, session: Session):
    entity = session.get(_type, id)
    if not entity:
        pass

    entity.title = entity.title
    entity.description = entity.description
    entity.is_completed = entity.is_completed

    session.add(entity)
    session.commit()
    session.refresh(entity)

    return entity 


def delete(_type, id: int, session: Session):
    entity = session.get(_type, id)
    if not entity:
        pass
    session.delete(entity)
    session.commit() 
    pass
    
