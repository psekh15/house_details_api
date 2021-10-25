from flask import Flask, jsonify
from flask_restful import Resource, Api, abort, reqparse
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///housedb.db'
db = SQLAlchemy(app)  # SQLAlchemy object created
api = Api(app)


class HouseModel(db.Model):
    """ Database model where class fields are database columns """
    id = db.Column(db.Integer, primary_key=True)
    street_address = db.Column(db.String(100), nullable=False)
    zipcode = db.Column(db.Integer, nullable=False)
    sewage = db.Column(db.String(100), nullable=True)

    def serialize(self):
        """  serialize data from Object to return it as a Json"""
        return {
            'id': self.id,
            'street_address': self.street_address,
            'zipcode': self.zipcode,
            'sewage': self.sewage
        }


parser = reqparse.RequestParser(bundle_errors=True)
parser.add_argument('street_address', type=str, required=True, help="Street address is a required parameter")
parser.add_argument('zipcode', type=int, required=True, help="Zipcode is a required parameter")
parser.add_argument('sewage', type=str, help="Sewage system type for the house")

update_parser = reqparse.RequestParser(bundle_errors=True)
update_parser.add_argument('street_address', type=str, help="Street address for the house")
update_parser.add_argument('zipcode', type=str, help="Zipcode for the house")
update_parser.add_argument('sewage', type=str, help="Sewage system type for the house")


class HouseList(Resource):
    """ get method: retrieve list of all houses
        post method: To record/add a new house
    """

    def get(self):
        house_list = HouseModel.query.all()
        return jsonify([HouseModel.serialize(house) for house in house_list])

    def post(self):
        args = parser.parse_args()
        house_record = HouseModel(street_address=args['street_address'], zipcode=args['zipcode'], sewage=args['sewage'])
        db.session.add(house_record)
        db.session.commit()
        return HouseModel.serialize(house_record), 201


class HouseById(Resource):
    """ get method: To retrieve a house with a specific id
        delete method: To delete a house with a specific id
        put method: To update house data for a house with a specific id
    """

    def get(self, house_id):
        return HouseModel.serialize(
            HouseModel.query.filter_by(id=house_id).first_or_404(
                description=f'House with id={house_id} is not available.'))

    def delete(self, house_id):
        house_record = HouseModel.query.filter_by(id=house_id).first_or_404(
            description=f'House with id={house_id} is not available.')
        db.session.delete(house_record)
        db.session.commit()
        return '', 204

    def put(self, house_id):
        args = update_parser.parse_args()
        house_record = HouseModel.query.filter_by(id=house_id).first_or_404(
            description=f'House with id={house_id} is not available.')
        if args['street_address']:
            house_record.street_address = args['street_address']
        if args['zipcode']:
            house_record.zipcode = args['zipcode']
        if args['sewage']:
            house_record.sewage = args['sewage']

        db.session.commit()
        return HouseModel.serialize(house_record), 201


class HouseByAddress(Resource):
    """
    get method: retrieve a specific house with specified address and zipcode
    delete method: delete a specific house with specified address and zipcode
    """

    def __init__(self):
        self.__street_address = update_parser.parse_args().get('street_address', None)
        self.__zipcode = update_parser.parse_args().get('zipcode', None)

    def get(self):
        return HouseModel.serialize(
            HouseModel.query.filter_by(street_address=self.__street_address, zipcode=self.__zipcode).first_or_404(
                description=f'Record with address={self.__street_address} and zipcode={self.__zipcode} is not available')
        )

    def delete(self):
        house_record = HouseModel.query.filter_by(street_address=self.__street_address,
                                                  zipcode=self.__zipcode).first_or_404(
            description=f'Record with address={self.__street_address} and zipcode={self.__zipcode} is not available')
        db.session.delete(house_record)
        db.session.commit()
        return '', 204


api.add_resource(HouseList, '/houseList',
                 '/')
api.add_resource(HouseById, '/houseList/house/<int:house_id>')
api.add_resource(HouseByAddress, '/houseList/house/')

if __name__ == '__main__':
    app.run(debug=True)
