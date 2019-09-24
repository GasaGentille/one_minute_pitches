from flask import render_template,request,redirect,url_for,abort
from . import main
# from ..request import get_movies,get_movie,search_movie
from ..models import User,Pitch,Comment
from .forms import UpdateProfile,PitchForm,CommentForm
from flask_login import login_required,current_user
from .. import db,photos
import markdown2 
import datetime

# Review = reviews.Review
# Views
@main.route('/')
def index():
   '''
   View root page function that returns the index page and its data
   '''
   # Getting pitch categories
 
   title = 'Home - Welcome to one minute pitch website'
   competitor_pitches = Pitch.get_pitches('competitor')
   employee_pitches = Pitch.get_pitches('employee')
   sport_pitches = Pitch.get_pitches('sport')


   return render_template('index.html', title = title, competitor = competitor_pitches, employee = employee_pitches,sport = sport_pitches )

@main.route('/user/<uname>') 
def profile(uname):
    user = User.query.filter_by(username = uname).first()
    pitches_count = Pitch.count_pitches(uname)
    user_joined = user.date_joined.strftime('%b %d,%Y')

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user,pitches = pitches_count ,date = user_joined)

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)

@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
        return redirect(url_for('main.profile',uname=uname))

    return render_template('review.html',review = review,format_review=format_review)

@main.route('/pitch/new', methods = ['GET','POST'])
@login_required
def new_pitch():
    pitch_form = PitchForm()
    
    if pitch_form.validate_on_submit():
        title = pitch_form.title.data
        pitch = pitch_form.text.data
        category = pitch_form.category.data
        #pitch instance
        new_pitch = Pitch(pitch_title=title,pitch_content=pitch,category=category,user=current_user,likes=0,dislikes=0)
        #save ptch
        print(new_pitch.pitch_title)
        new_pitch.save_pitch()
        return redirect(url_for('.index'))

    title = 'New pitch'
    return render_template('new_pitch.html',title = title,pitch_form = pitch_form)

@main.route('/pitches/competitor_pitches')

def competitor_pitches():
    pitches = Pitch.get_pitches('competitor')
    return render_template("competitor_pitches.html", pitches = pitches)

@main.route('/pitches/employee_pitches')
def  employee_pitches():
    pitches = Pitch.get_pitches('employee')
    return render_template("employee_pitches.html", pitches = pitches)

@main.route('/pitches/sport_pitches')
def  sport_pitches():
    pitches = Pitch.get_pitches('sport')
    return render_template("sport_pitches.html", pitches = pitches)

@main.route('/pitch/<int:id>', methods = ['GET','POST'])
def pitch(id):
    pitch = Pitch.get_pitch(id)
    # posted_date = pitch.posted_date.strftime('%b %d,%Y')

    if request.args.get("like"):
        pitch.likes = pitch.likes + 1

        db.session.add(pitch)
        db.session.commit()

        return redirect("/pitch/{pitch_id}".format(pitch_id=pitch.id))
        
    elif request.args.get("dislike"):
        pitch.dislikes = pitch.dislikes +1

        db.session.add(pitch)
        db.session.commit()

        return redirect("pitch/{pitch_id}".format(pitch_id = pitch.id))

    comment_form =  CommentForm()
    if comment_form.validate_on_submit():
        comment = comment_form.text.data

        new_comment = Comment(comment = comment,user = current_user,pitch_id=pitch)
        new_comment.save_comment()

    comments = Comment.get_comments(pitch)
    return render_template("pitch.html", pitch = pitch, comment_form = comment_form, comments = comments)

@main.route('/user/<uname>/pitches')
def user_pitches(uname):
    user = User.query.filter_by(username=uname).first()
    pitches = Pitch.query.filter_by(user_id=user.id).all()
    pitches_count = Pitch.count_pitches(uname)
    user_joined = user.date_joined.strftime('%b %d, %Y')

    return render_template("profile/pitches.html", user=user,pitches=pitches,pitches_count=pitches_count,date=user_joined)   
    


