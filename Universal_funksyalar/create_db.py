def New_Item_Db(db, a):
    db.add(a)
    db.commit()
    db.refresh(a)
