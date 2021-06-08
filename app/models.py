from app import db

class Book(db.Model):
    __tablename__ = 'book'

    id = db.Column(
        db.Integer, 
        primary_key=True
    )
    title = db.Column(
        db.String(100), 
        index=True, 
        unique=True, 
        nullable=False
    )

    def __repr__(self):
        return '<BookInfo - {}>'.format(self.title)