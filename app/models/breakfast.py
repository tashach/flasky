from app import db

class Breakfast(db.Model):
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    name = db.Column(db.String)
    rating = db.Column(db.Float)
    prep_time = db.Column(db.Integer)
    menu_id = db.Column(db.Integer, db.ForeignKey("menu.id"))
    menu = db.relationship("Menu", back_populates="breakfast_items")

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "rating": self.rating,
            "prep_time": self.prep_time,
            "menu_id": self.menu_id
        }

    @classmethod
    def from_dict(cls, cls_dict):
        return cls(
            name = cls_dict["name"],
            rating = cls_dict["rating"],
            prep_time = cls_dict["prep_time"],
            menu_id = cls_dict["menu_id"]
        )