from server import db, Puppy, Owner, Toy

rufus = Puppy('Rufus', 2, 'Breed1')
fido  = Puppy('Fido',  3, 'Breed2')

# db.session.add_all([rufus, fido])
# db.session.commit()


print(Puppy.query.all())

# db.session.delete(Puppy.query.get(8))
# db.session.commit()

rufus = Puppy.query.filter_by(name = 'Rufus').first()
print(rufus)

# Create Owner object
jose = Owner('Jose', rufus.id)

# Give Rufus some toys
toy1 = Toy('Chew Toy', rufus.id)
toy2 = Toy('Ball', rufus.id)

db.session.add_all([jose, toy1, toy2]) # takes care of everthing
db.session.commit()

# Grab rufus after those additions!
rufus = Puppy.query.filter_by(name = 'Rufus').first()
print(rufus)

rufus.report_toys()



 
