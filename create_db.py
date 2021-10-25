from app import db
from app import HouseModel
""" Create a database and insert sample data"""

# db.session.query(HouseRecord).delete()
# db.session.commit()
# db.create_all()

# example records municipal, none, storm, septic, yes

sample_house_one = HouseModel(street_address="123 Main St", zipcode=95392, sewage="municipal")
sample_house_two = HouseModel(street_address="124 Market St", zipcode=13492, sewage="septic")
sample_house_three = HouseModel(street_address="223 17th St", zipcode=99223, sewage="septic")
sample_house_four = HouseModel(street_address="224 Harvey St", zipcode=39243, sewage="yes")

db.session.add(sample_house_one)
db.session.add(sample_house_two)
db.session.add(sample_house_three)
db.session.add(sample_house_four)
db.session.commit()

#check if data is stored in db
print(HouseModel.query.all())


