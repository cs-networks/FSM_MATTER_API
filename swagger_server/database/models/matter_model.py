from swagger_server.database import db
from swagger_server.models.matter_properties import MatterProperties


class matter_model(db.Model):
    __tablename__ = "matter"
    # Database fields
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=True)
    state = db.Column(db.String)
    temperatur = db.Column(db.Float)

    def __getitem__(self, field):
        return self.__dict__[field]

    def to_obj(self) -> MatterProperties:
        return MatterProperties(id=self.id, state=self.state, temperatur=self.temperatur)

    def copy(self, other):
        other.id = self.id
        other.state = self.state
        other.temperatur = self.temperatur

    def __eq__(self, other):
        """Overrides the default implementation"""
        if isinstance(other, matter_model):
            return (self.id == other.id  # noqa: W503
                    and self.state == other.state  # noqa: W503
                    and self.temperatur == other.temperatur)  # noqa: W503
        return False

    @classmethod
    def get_all(cls):
        objects = cls.query.first()
        return objects

    @classmethod
    def get_by_id(cls, id=""):
        objects = cls.query.filter(cls.id.like(id)).first()
        return objects

    @classmethod
    def get_all_key_dict(cls):
        orders_entries = {}
        model_objects = cls.query.all()
        for item in model_objects:
            orders_entries[f'{item["id"]}-'] = item
        return orders_entries
