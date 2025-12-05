from app import create_app, db
from app.models.user import User
from app.models.message import Message
from app.models.comment import Comment
from werkzeug.security import generate_password_hash

def run():
    app = create_app()
    with app.app_context():
        db.drop_all()
        db.create_all()

        u1 = User(nome='Alice', email='alice@example.com', senha=generate_password_hash('123456'))
        u2 = User(nome='Bob', email='bob@example.com', senha=generate_password_hash('123456'))
        db.session.add_all([u1, u2])
        db.session.commit()

        m1 = Message(titulo='Olá', conteudo='Primeira mensagem', user_id=u1.id)
        m2 = Message(titulo='Assunto', conteudo='Segunda mensagem', user_id=u2.id)
        db.session.add_all([m1, m2])
        db.session.commit()

        c1 = Comment(conteudo='Comentário 1', mensagens_id=m1.id, user_id=u2.id)
        c2 = Comment(conteudo='Comentário 2', mensagens_id=m2.id, user_id=u1.id)
        db.session.add_all([c1, c2])
        db.session.commit()

        print('Seed concluído: usuários, mensagens e comentários criados.')

if __name__ == '__main__':
    run()
