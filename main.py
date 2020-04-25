from flask import Flask, render_template, redirect, request
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from flask_restful import abort
from data import db_session
from data.add_site import AddSiteForm
from data.topic_form import AddTopicForm
from data.login_form import LoginForm
from data.users import User
from data.sites import Site
from data.topics import Topic
from data.register import RegisterForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'U74anllYYrxWwqcwImKh8LaGFdb8uM'

login_manager = LoginManager()
login_manager.init_app(app)


def main():
    db_session.global_init("db/best_links.sqlite")

    @login_manager.user_loader
    def load_user(user_id):
        session = db_session.create_session()
        return session.query(User).get(user_id)

    @app.route('/login', methods=['GET', 'POST'])
    def login():
        form = LoginForm()
        if form.validate_on_submit():
            session = db_session.create_session()
            user = session.query(User).filter(User.email == form.email.data).first()
            if user and user.check_password(form.password.data):
                login_user(user, remember=form.remember_me.data)
                return redirect(f'/{0}/{0}')
            return render_template('login.html', message="Неверный логин или пароль", form=form)
        return render_template('login.html', title='Авторизация', form=form)

    @app.route("/<int:id_topic>/<int:id_all>")
    @app.route("/index/<int:id_topic>/<int:id_all>")
    def index(id_topic, id_all):
        id_list_users = [1]
        if current_user.is_authenticated:
            if current_user.id != 1:
                if id_all:
                    id_list_users = [current_user.id]
                else:
                    id_list_users.append(current_user.id)
        session = db_session.create_session()
        sites = session.query(Site).filter(Site.id_user.in_(id_list_users))
        if id_all:
            id_list_users = [1, current_user.id]
        topics = session.query(Topic).filter(Topic.user_id.in_(id_list_users))
        list_topics = sorted([p for p in topics], key=lambda q: q.topic_title)
        name_topics = {}
        name_topics[0] = 'Все темы сайтов'
        for topic in list_topics:
            if topic.id not in name_topics:
                name_topics[topic.id] = topic.topic_title
            elif topic.id == current_user.id:
                name_topics[topic.id] = topic.topic_title
        dict_site = {}
        list_sites = sorted([p for p in sites], key=lambda q: name_topics[q.id_topic])
        count_sites = {}
        count_sites[0] = len(list_sites)
        for p in list_sites:
            dict_site[p.id_topic] = dict_site.get(p.id_topic, []) + [p]
        for p in dict_site:
            count_sites[p] = len(dict_site[p])
        count_sites[-1] = len(dict_site)
        return render_template("index.html", dict_site=dict_site, name_topics=name_topics,
                               title='Лучшие сайты, отобранные вручную!', id_topic=id_topic,
                               id_all=id_all, count_sites=count_sites)
    
    @app.route("/")
    @app.route("/index")
    @app.route("/start")
    def start():
        id_topic, id_all = 0, 0
        id_list_users = [1]
        if current_user.is_authenticated:
            if current_user.id != 1:
                if id_all:
                    id_list_users = [current_user.id]
                else:
                    id_list_users.append(current_user.id)
        session = db_session.create_session()
        sites = session.query(Site).filter(Site.id_user.in_(id_list_users))
        if id_all:
            id_list_users = [1, current_user.id]
        topics = session.query(Topic).filter(Topic.user_id.in_(id_list_users))
        list_topics = sorted([p for p in topics], key=lambda q: q.topic_title)
        name_topics = {}
        name_topics[0] = 'Все темы сайтов'
        for topic in list_topics:
            if topic.id not in name_topics:
                name_topics[topic.id] = topic.topic_title
            elif topic.id == current_user.id:
                name_topics[topic.id] = topic.topic_title
        dict_site = {}
        list_sites = sorted([p for p in sites], key=lambda q: name_topics[q.id_topic])
        count_sites = {}
        count_sites[0] = len(list_sites)
        for p in list_sites:
            dict_site[p.id_topic] = dict_site.get(p.id_topic, []) + [p]
        for p in dict_site:
            count_sites[p] = len(dict_site[p])
        count_sites[-1] = len(dict_site)
        return render_template("index.html", dict_site=dict_site, name_topics=name_topics,
                               title='Лучшие сайты, отобранные вручную!', id_topic=id_topic,
                               id_all=id_all, count_sites=count_sites)

    @app.route('/logout')
    @login_required
    def logout():
        logout_user()
        return redirect(f'/{0}/{0}')

    @app.route('/register', methods=['GET', 'POST'])
    def reqister():
        form = RegisterForm()
        if form.validate_on_submit():
            if form.password.data != form.password_again.data:
                return render_template('register.html', title='Регистрация', form=form,
                                       message="Пароли не совпадают")
            session = db_session.create_session()
            if session.query(User).filter(User.email == form.email.data).first():
                return render_template('register.html', title='Регистрация', form=form,
                                       message="Этот пользователь уже существует")
            user = User(
                user_login=form.login.data,
                email=form.email.data,
                age=form.age.data
            )
            user.set_password(form.password.data)
            session.add(user)
            session.commit()
            return redirect('/login')
        return render_template('register.html', title='Регистрация', form=form)

    @app.route('/0/add_site', methods=['GET', 'POST'])
    def add_site():
        add_form = AddSiteForm()
        if add_form.validate_on_submit():
            session = db_session.create_session()
            site = Site(
                id_user=current_user.id,
                site_address=add_form.site_address.data.lower(),
                site_name=add_form.site_name.data,
                id_topic=add_form.id_topic.data,
                site_description=add_form.site_description.data
            )
            session.add(site)
            session.commit()
            return redirect(f'/{0}/{0}')
        session = db_session.create_session()
        if current_user.is_authenticated:
            topics = session.query(Topic).filter(Topic.user_id.in_([1, current_user.id]))
        else:
            topics = session.query(Topic).filter(Topic.user_id == 1)
        list_topics = sorted([p for p in topics], key=lambda q: q.topic_title)
        return render_template('add_site.html', title='Добавление сайта', form=add_form, list_topics=list_topics, nid=0)

    @app.route('/site/<int:id>', methods=['GET', 'POST'])
    @login_required
    def site_edit(id):
        form = AddSiteForm()
        if request.method == "GET":
            session = db_session.create_session()
            sites = session.query(Site).filter((Site.id == id)).first()
            if sites:
                form.site_address.data = sites.site_address
                form.site_name.data = sites.site_name
                form.id_topic.data = sites.id_topic
                form.site_description.data = sites.site_description
            else:
                abort(404)
        if form.validate_on_submit():
            session = db_session.create_session()
            sites = session.query(Site).filter((Site.id == id)).first()
            if sites:
                sites.site_address = form.site_address.data
                sites.site_name = form.site_name.data
                sites.id_topic = form.id_topic.data
                sites.site_description = form.site_description.data
                session.commit()
                return redirect(f'/{0}/{0}')
            else:
                abort(404)
        session = db_session.create_session()
        if current_user.is_authenticated:
            topics = session.query(Topic).filter(Topic.user_id.in_([1, current_user.id]))
        else:
            topics = session.query(Topic).filter(Topic.user_id == 1)
        list_topics = sorted([p for p in topics], key=lambda q: q.topic_title)
        return render_template('add_site.html', title='Редактирование сайта', form=form, list_topics=list_topics,
                               nid=sites.id_topic)

    @app.route('/site_delete/<int:id>', methods=['GET', 'POST'])
    @login_required
    def site_delete(id):
        session = db_session.create_session()
        site = session.query(Site).filter((Site.id == id)).first()
        if site:
            session.delete(site)
            session.commit()
        else:
            abort(404)
        return redirect(f'/{0}/{0}')

    @app.route('/0/add_topic', methods=['GET', 'POST'])
    def add_topic():
        add_form = AddTopicForm()
        if add_form.validate_on_submit():
            session = db_session.create_session()
            topic = Topic(
                topic_title=add_form.topic_title.data,
                user_id=current_user.id
            )
            session.add(topic)
            session.commit()
            return redirect(f'/{0}/{0}')
        return render_template('add_topic.html', title='Добавление темы', form=add_form)

    @app.route("/0/topics")
    def topics():
        session = db_session.create_session()
        if current_user.is_authenticated:
            topics = session.query(Topic).filter(Topic.user_id.in_([1, current_user.id]))
        else:
            topics = session.query(Topic).filter(Topic.user_id == 1)
        list_topics = sorted([p for p in topics], key=lambda q: q.topic_title)
        return render_template("topics.html", list_topics=list_topics, title='Список тем')

    @app.route('/topics/<int:id>', methods=['GET', 'POST'])
    @login_required
    def topic_edit(id):
        form = AddTopicForm()
        if request.method == "GET":
            session = db_session.create_session()
            topic = session.query(Topic).filter(Topic.id == id, Topic.user_id == current_user.id).first()
            if topic:
                form.topic_title.data = topic.topic_title
            else:
                abort(404)
        if form.validate_on_submit():
            session = db_session.create_session()
            topic = session.query(Topic).filter(Topic.id == id, Topic.user_id == current_user.id).first()
            if topic:
                topic.topic_title = form.topic_title.data
                session.commit()
                return redirect(f'/{0}/{0}')
            else:
                abort(404)
        return render_template('add_topic.html', title='Редактирование темы', form=form)

    @app.route('/topic_delete/<int:id>', methods=['GET', 'POST'])
    @login_required
    def topic_delete(id):
        session = db_session.create_session()
        topic = session.query(Topic).filter(Topic.id == id, Topic.user_id == current_user.id).first()
        site = session.query(Site).filter(Site.id_topic == topic.id).first()
        if site:
            return redirect(f'/{0}/{0}')
        if topic:
            session.delete(topic)
            session.commit()
        else:
            abort(404)
        return redirect(f'/{0}/{0}')


if __name__ == '__main__':
    app.run('127.0.0.1', 8000, True)
    main()
