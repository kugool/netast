from flask_script import Manager, Server
from main import app, db, User, Post, Comment, Tag
	

manager = Manager(app)

manager.add_command('server', Server())


@manager.command
def Setupdb():
    db.create_all()
    
    import random
    import datetime

    user = User.query.get(1)
    tag_one = Tag('python')
    tag_two = Tag('flask')
    tag_three = Tag('sqlalechemy')
    tag_four = Tag('jinja')
    tag_list = [tag_one, tag_two, tag_three, tag_four]
    
    s = 'example text'
    
    for i in range(100):
        new_post = Post('Post ' + str(i))
        new_post.user = user
        new_post.publish_date = datetime.datetime.now()
        new_post.text = s
        new_post.tags = random.sample(tag_list, random.randint(1,3))
        db.session.add(new_post)
        
    db.session.commit()


#manager.add_command('setup_db', Setupdb())

@manager.shell
def make_shell_context():
    return dict(app=app, db=db, User=User, Post=Post, Comment=Comment, Tag=Tag)


if __name__ == '__main__':
    manager.run()

